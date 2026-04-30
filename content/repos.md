+++
title = "My projects"
tags = []
+++

### fhtc

Also known as [`fht-compositor`](fhtc), it's by far my most "achieved" project (if you even care about that), and also the project in which I poured the most amount of time. I would say I am close to achieving all I want to do with it, however there are still missing "small stuff" that can add up really quickly.

Even if it was never intended to be, people have grown to call `fhtc` a "Hyprland" killer, or a "cooler & faster Hyprland alternative", and to be honest the feature set quite matches up nice. Distributions like [AxOS](https://axos-project.com) are considering switching to it, so if anything I'm glad about it!

Working on this project also led me to work on/with [Smithay](smithay), [Winit](winit), and more crates from the Rust x Wayland ecosystem! This allowed me to level up my knowledge in graphics programming (working directly with OpenGL, DRM, and more) and how we can turn simple TTYs into full-fledged graphical sessions.

If you are interested, here's the [Discord](https://discord.gg/H58C8AdU7x) link. Feel free to mention/tag me there!

[fhtc]: https://nferhat.github.io/fht-compositor
[smithay]: https://github.com/Smithay
[winit]: https://github.com/rust-windowing/winit

***

### website(-rs?)

This website is statically generated, IE all the assets/content are pre-built and you are only served the final HTML/CSS/whatever. This is thanks to a *custom* generator that I built with Rust (how suprising, I know).

Currently not public, I'd rather keep it private since it's not finalized, heavily opinionated, and may be lacking a lot of features right now, however you're seeing this website built by it, sooo, it's working, I guess.

Current feature-set includes:

- Rendering of (most) markdown features, with support for [Github-Flavoured Markdown](gfm).
- [Liquid](liquid)-based templating
- [SASS](sass) for styling (and only it!)
- A tiny (but useful!) CLI that includes a hot-reloading server

And that's really it! While minimal, I strive to keep it this way, I don't need much more out of a website generator. If I need custom stuff, I'll add it, or just use inline HTML, depends on how I feel about it.

[liquid]: https://shopify.github.io/liquid/
[gfm]: https://github.github.com/gfm/#what-is-github-flavored-markdown-
[sass]: https://sass-lang.com

***

### M-security

[M-security](m-sec) is a side-project I worked on with [IV](https://github.com/Adel-Ayoub) under [MicroClub](microclub)'s developement departement. It's a high-performance security SDK. The core concept is to move away all the sensitive processing into a Rust library, loaded through `flutter-rust-bridge`, and only communicate what's necessary from/to Dart.

The Rust library handles all the annoying "security stuff" (like making sure data doesn't hit swap, or the actual encryption algorithms), and also interfaces with hardware features for features like [Hardware Key Derivation](hkdf) and exposing them cleanly to Dart.

There's a lot of cool stuff going on there, if you are a mobile developer doing sensitive stuff or needing encryption/hashing/whatever algorithms, you should really check it out!

[m-sec]: https://github.com/MicroClub-USTHB/M-security
[microclub]: https://microclub.info
[hkdf]: https://en.wikipedia.org/wiki/HKDF
