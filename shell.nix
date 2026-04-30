{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell rec {
  packages = with pkgs; [
    shopify-cli # templates LSP
    marksman    # markdown LSP

    # Building grammars.
    gcc        
    tree-sitter
  ];
}
