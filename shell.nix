{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell rec {
  packages = with pkgs; [
    shopify-cli # templates LSP
    marksman    # markdown LSP

    # Scripts
    python3     

    # Building grammars.
    gcc        
    tree-sitter
  ];
}
