# [nferhat.dev](https://nferhat.dev)

This repository contains the content files used to generate my personal [website](https://nferhat.dev).

I made my own static website generator in order to turn these markdown files into the nice final result. Since I am not planning on creating templates for that website tool, you should probably use this repository as reference (or use Hugo or Zola, which are intended to be used by other people!)

If you are curious, the tool is [here](https://github.com/nferhat/website)

## Actual website features

These are mostly related to what's inside the `templates` and `style` directories. They define the skeleton and look of the website.

- Blogging with classification by tags
- Sleek layout and theme (who doesn't say that about their website, duh)
- Includes tree-sitter highlighting for: Rust, Gleam, C, Bash, Lua, GLSL, wgsl, and more to come!
  - Credits to the [Helix Editor](https://helix-editor.org) for the parsers and queries!
