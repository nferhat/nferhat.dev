+++
title = "Various"
tags  = []
draft = false
+++

# Various

![thingy](/rice.webp "A pretty cool rice")

[tree-sitter]

```
Hello, world
```

Highlighted codeblock! With the power of [tree-sitter][tree-sitter]

[tree-sitter]: https://tree-sitter.github.io

```rust
fn main(a: usize) {
    let mut a = 12;
    unsafe { *(0x727) = nikmokkar; }
    
    info!(?whatever, "this is a log message")
}

struct Thingy<'a, D> {
    whatever: std::marker::PhantomData<'a>,
}
```

## Markdown Features Showcase

| Feature | Syntax | Rendered | Usage |
|---------|--------|----------|-------|
| **Bold Text** | `**bold**` | **bold** | Emphasize important content |
| *Italic Text* | `*italic*` | *italic* | Slight emphasis |
| ***Bold & Italic*** | `***both***` | ***both*** | Maximum emphasis |
| ~~Strikethrough~~ | `~~strike~~` | ~~strike~~ | Mark deleted text |
| `Inline Code` | `` `code` `` | `code` | Highlight code snippets |
| **`Bold Code`** | `**\`code\`**` | **`code`** | Important code reference |
| ***`All Combined`*** | `***\`code\`***` | ***`code`*** | Maximum styling |
| [Link Text](https://example.com) | `[text](url)` | [Link](https://example.com) | Add hyperlinks |
| **[Bold Link](https://example.com)** | `**[text](url)**` | **[Link](https://example.com)** | Emphasized link |
| ***[All Link](https://example.com)*** | `***[text](url)***` | ***[Link](https://example.com)*** | Fully styled link |
| [`Code Link`](https://example.com) | `` [`code`](url) `` | [`Link`](https://example.com) | Linked code |
| **[`Bold Code Link`](url)** | `**[\`code\`](url)**` | **[`Link`](url)** | Styled code link |
| Escaped \*Asterisk\* | `\*Asterisk\*` | Escaped \*Asterisk\* | Literal special chars |
| Escaped \[Bracket\] | `\[Bracket\]` | Escaped \[Bracket\] | Literal brackets |
| Escaped \!Exclamation\! | `\!Exclamation\!` | Escaped \!Exclamation\! | Literal exclamation |
| `var_name` | `` `var_name` `` | `var_name` | Variable names |
| `function()` | `` `function()` `` | `function()` | Function calls |
| `ClassName::method` | `` `ClassName::method` `` | `ClassName::method` | Class methods |
| `path/to/file.ext` | `` `path/to/file.ext` `` | `path/to/file.ext` | File paths |
| `$variable` | `` `$variable` `` | `$variable` | Shell variables |
| **`const VALUE`** | `**\`const VALUE\`**` | **`const VALUE`** | Constants |
| *`iterator.map()`* | `*\`iterator.map()\`*` | *`iterator.map()`* | Methods |
| **Very *Nested* Text** | `**Very *Nested* Text**` | **Very *Nested* Text** | Text nesting |
| ***Mix `code` and***** | Complex nesting | ***Mix `code`*** | Advanced styling |
| [**Bold** in link](url) | `[**Bold** in link](url)` | [**Bold** in link](https://x) | Link content styling |
| [*Italic* in link](url) | `[*Italic* in link](url)` | [*Italic* in link](https://x) | Link emphasis |
| [~~Struck~~ link](url) | `[~~Struck~~ link](url)` | [~~Struck~~ link](https://x) | Struck in link |
| Reference [link][ref] | `[link][ref]` + `[ref]: url` | Reference link | Link references |
| **`Complex::Type<T>`** | `**\`Complex::Type<T>\`**` | **`Complex::Type<T>`** | Generic types |
| `impl Trait for Type` | `` `impl Trait for Type` `` | `impl Trait for Type` | Trait impl |
| **`&mut self`** | `**\`&mut self\`**` | **`&mut self`** | Method receivers |
| *`Option<Result<T>>`* | `*\`Option<Result<T>>\`*` | *`Option<Result<T>>`* | Nested generics |
| `#[derive(Debug)]` | `` `#[derive(Debug)]` `` | `#[derive(Debug)]` | Attributes |
| **`fn main() {}`** | `**\`fn main() {}\`**` | **`fn main() {}`** | Function definition |
| ***`pub async fn()`*** | `***\`pub async fn()\`***` | ***`pub async fn()`*** | Async functions |
| `Error: Type Mismatch` | `` `Error: Type Mismatch` `` | `Error: Type Mismatch` | Error messages |
| **`CONSTANT_VALUE`** | `**\`CONSTANT_VALUE\`**` | **`CONSTANT_VALUE`** | Constant names |
| *`some_identifier`* | `*\`some_identifier\`*` | *`some_identifier`* | Identifiers |
| ~~`deprecated()`~~ | `~~\`deprecated()\`~~` | ~~`deprecated()`~~ | Deprecated items |
| `unsafe { ... }` | `` `unsafe { ... }` `` | `unsafe { ... }` | Unsafe blocks |
| **Bold *Italic* Mix** | `**Bold *Italic* Mix**` | **Bold *Italic* Mix** | Multi-level nesting |
| [**`Ultimate`** combo](url) | `[**\`Ultimate\`** combo](url)` | [**`Ultimate`** combo](url) | Full combination |
| `let x: &str = ""` | `` `let x: &str = ""` `` | `let x: &str = ""` | Variable declaration |
| **`match pattern {}`** | `**\`match pattern {}\`**` | **`match pattern {}`** | Match expressions |
| *`for item in iter`* | `*\`for item in iter\`*` | *`for item in iter`* | Loop syntax |
| `struct Point { x, y }` | `` `struct Point { x, y }` `` | `struct Point { x, y }` | Struct definition |
| **`impl Default`** | `**\`impl Default\`**` | **`impl Default`** | Trait implementations |
| ***`#![no_std]`*** | `***\`#![no_std]\`***` | ***`#![no_std]`*** | Crate attributes |
|  ![thingy](/rice.webp) | whatever | whatever | Images! |

[ref]: https://example.com
