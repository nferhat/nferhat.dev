{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell rec {
  packages = with pkgs; [
    shopify-cli # templates LSP
    marksman    # markdown LSP
    prettier    # format

    # Scripts
    python3

    # Building grammars.
    gcc
    tree-sitter
  ];
}
