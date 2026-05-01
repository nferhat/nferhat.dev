+++
title = "Low-Level-Bytes: The power (and safety) of Send and Sync"
description = "How Rust's approach to thread-safety and synchronization is amazing"
tags = ["rust", "low-level"]
release-date = "2026-04-30"
draft = true
+++

> Hello, this is the first installement of my blog series, *"Low-level Bytes"*, where I try
> to simplify and make concepts of low-level programming approachable to people with
> different contexts. (for example, web developers)
>
> This is to force myself to write technical stuff while trying to simplify as much as I
> can, while preserving the core idea, and conveying information.

Multi-threaded logic is at the core of highly complex systems that need high levels of concurrency and throughput, for example web servers, queue systems, banking infrastructure, high-frequency trading...

However, it is well known and established that writing *correct* and *safe* concurrent programs is much more complicated than writing single threaded programs. While not the topic of today's writing, before considering MT, you should think about trying to use an event-loop on a single thread, you don't know how far this can get you!

## A cautionary tale

Let's take the following C program.

```c
#include <pthread.h> // <1>
#include <stdio.h>

// <2> Some static data shared between threads
static int x = 0;

static void* func(void* _) {
    (void)_;
    for (int i = 0; i < 1000000; i++) x++;  // <3>
    return 0;
}

int main(void) {
    pthread_t a, b;
    pthread_create(&a, NULL, func, NULL);
    pthread_create(&b, NULL, func, NULL);
    // <3> Wait for both to finish
    pthread_join(a, NULL);
    pthread_join(b, NULL);

    printf("x = %d\n", x);
    return 0;
}
```

1. `pthreads` stands for **P**OSIX **threads**, and it's the standard threads implementations for Linux (on which I'm writing this article)
2. The `x` variable lives in *static memory*, IE. memory that is shared by the whole program (including the threads it spawns!)
3. This for loop is the actual "work" or effort, simulated here with an increment operation. We'll see down below how this instruction causes us problems...

But before anything, let's try to compile this program:

```bash
# Or cc/clang (or MSCV if you're crazy)
gcc -lpthread example.c -o example
```

And now run it...

```
$ ./example
x = 1115757

$ ./example
x = 987999

...
```

... *what?* Aren't we expecting it `x` to be equal to `2000000` exactly? Why it is far off our target, and more worryingly, why does it have a different value each time?

Congratulations! We successfully introduced a *data race* --- when two threads or processes try to read and write to a shared resource at the same time. In our case, both threads are reading *and* writing into static memory `x`.

If we disassemble our function with `objdump`, we'd get the following assembly code of <kw type=function>func</kw>

```asm
; <1> Setup the stack by saving the previous stack pointer
push   rbp
mov    rbp,rsp
mov    QWORD PTR [rbp-0x18],rdi ; saves the argument passed into the function
mov    DWORD PTR [rbp-0x4],0x0  ; initializes the loop counter
jmp    118d <t+0x24>

; Loop body
; <2> Here is our problem!
mov    eax,DWORD PTR [rip+0x2e94]
add    eax,0x1
mov    DWORD PTR [rip+0x2e8b],eax
add    DWORD PTR [rbp-0x4],0x1
; <3> exit condition
cmp    DWORD PTR [rbp-0x4],0xf423f
jle    117a <t+0x11>

; Restore the stack
; <4> Sets the return value.
mov    eax,0x0
pop    rbp
xor    edi,edi
ret ; the end
```

1. My machine is running NixOS (a *Linux* distribution) on a x86_64/AMD64 processor, which means it will be using the [System-V AMD64 ABI][sysv-amd64-abi]. This is standard stack setup for it.
2. We'll talk about it down below
3. The exit condition, `0xf423f` is equivalent to `999999`. It compares the value of the counter variable (stored in `[rbp-0x4]`) to that. On the instruction later, if the value is less than that, it jumps back to the beginning of the loop
4. Sets the return value to `0` which is what `NULL` is equal to in C. Nothing special, this is mandated by the ABI of the platform saying that `rax` (or `eax` for 32-bit integers) should be used for the return values.

[sysv-amd64-abi]: https://wiki.osdev.org/System_V_ABI

Coming back to the hot path of the loop (IE the `x++`), this happens in three instructions:

1. Since `x` is in shared/static memory, we have to load it from it's address (which the compiler decided to be `rip+0x2e94`) into a local register, `eax`
2. It increments the value copied into the *local register* of the thread by `0x1`, essentially this is our `x = x+1`
3. It saves back to global memory

The whole issue is since we copy the value into a local register *before* incrementing. Since each thread has a different local `eax` register (which the CPU will context-switch from/to depending on order of execution), we can cause the case where for example:

- `x = 102`
- thread one copies `x` into `eax`
- at the *same time*, thread two copies `x` into `eax`
- both increment their local copies
- both write `x = 103`, essentially skipping a "step"

While this example is trivial to explain, actual code won't likely be just a simple for loop incrementing. Imagine if instead of `x`, you have some nested struct with shared pointers (for example data vectors), it would be a nightmare to figure out what's happening!

Sure. Now let's see the equivalent code in rust.

```rust
use std::thread::spawn;
static mut x: i32 = 0;

fn main() {
    spawn(|| {
        for _ in 0..1_000_000 {
            x += 1;
        }
    });
    spawn(|| {
        for _ in 0..1_000_000 {
            x += 1;
        }
    });
}
```

However, the Rust compiler, `rustc`, quickly stops us in our tracks...

<div class=codeblock><pre><code><span class="bold"></span><span class="color9 bold">error[E0133]</span><span class="bold">: use of mutable static is unsafe and requires unsafe function or block</span>
 <span class="bold"></span><span class="color12 bold">--&gt; </span>sync.rs:7:13
  <span class="bold"></span><span class="color12 bold">|</span>
<span class="bold"></span><span class="color12 bold">7</span> <span class="bold"></span><span class="color12 bold">|</span>             x += 1;
  <span class="bold"></span><span class="color12 bold">|</span>             <span class="bold"></span><span class="color9 bold">^</span> <span class="bold"></span><span class="color9 bold">use of mutable static</span>
  <span class="bold"></span><span class="color12 bold">|</span>
  <span class="bold"></span><span class="color12 bold">= </span><span class="bold">note</span>: mutable statics can be mutated by multiple threads: aliasing violations or data races will cause undefined behavior

<span class="bold"></span><span class="color9 bold">error[E0133]</span><span class="bold">: use of mutable static is unsafe and requires unsafe function or block</span>
  <span class="bold"></span><span class="color12 bold">--&gt; </span>sync.rs:12:13
   <span class="bold"></span><span class="color12 bold">|</span>
<span class="bold"></span><span class="color12 bold">12</span> <span class="bold"></span><span class="color12 bold">|</span>             x += 1;
   <span class="bold"></span><span class="color12 bold">|</span>             <span class="bold"></span><span class="color9 bold">^</span> <span class="bold"></span><span class="color9 bold">use of mutable static</span>
   <span class="bold"></span><span class="color12 bold">|</span>
   <span class="bold"></span><span class="color12 bold">= </span><span class="bold">note</span>: mutable statics can be mutated by multiple threads: aliasing violations or data races will cause undefined behavior

<span class="bold"></span><span class="color9 bold">error</span><span class="bold">: aborting due to 2 previous errors</span>
<span class="bold">For more information about this error, try `rustc --explain E0133`.</span>
</pre></code></div>

Indeed! Using mutable statics is **not** allowed! The compiler is even nice enough to tell us that this might cause data races, which leads to undefined behaviour (scary!)

The initial solution is to achieve shared data in another way, using a shared pointer: <kw type=type>Rc</kw> (which is analogus to C++'s <code class=inline-code><span class=module>std::</span><span class=type>shared_ptr</span></code>). Essentially, it does the following:
