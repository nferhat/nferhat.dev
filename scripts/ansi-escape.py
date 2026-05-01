#!/usr/bin/env python3
"""
Read ANSI-colored text from stdin and emit HTML with <span class="..."> wrappers.

Supported SGR codes:
  - 0   reset
  - 1/22 bold on/off
  - 3/23 italic on/off
  - 4/24 underline on/off
  - 30-37  normal foreground colors 0-7
  - 90-97  bright foreground colors 8-15

Color classes emitted:
  color0 .. color15
Plus style classes:
  bold, italic, underline
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from typing import Optional


ANSI_SGR_RE = re.compile(r"\x1b\[(?P<codes>[0-9;]*)m")


@dataclass
class Style:
    color: Optional[int] = None  # 0..15 (matching the Rust script)
    bold: bool = False
    italic: bool = False
    underline: bool = False

    def reset(self) -> None:
        self.color = None
        self.bold = False
        self.italic = False
        self.underline = False

    def build_class(self) -> Optional[str]:
        classes: list[str] = []
        if self.color is not None:
            classes.append(f"color{self.color}")
        if self.bold:
            classes.append("bold")
        if self.italic:
            classes.append("italic")
        if self.underline:
            classes.append("underline")
        return " ".join(classes) if classes else None


def html_escape(text: str) -> str:
    # Match the Rust push_escaped behavior for &, <, > only.
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def apply_sgr_codes(style: Style, codes_str: str) -> None:
    # Rust behavior: parse ints split by ';'. If none parse, do nothing.
    # For ESC[m (empty), many terminals treat as reset; Rust script would parse nothing.
    # We keep Rust semantics by default (no implicit reset).
    parts = codes_str.split(";") if codes_str else []
    for part in parts:
        try:
            code = int(part)
        except ValueError:
            continue

        if code == 0:
            style.reset()

        # bold
        elif code == 1:
            style.bold = True
        elif code == 22:
            style.bold = False

        # italic
        elif code == 3:
            style.italic = True
        elif code == 23:
            style.italic = False

        # underline
        elif code == 4:
            style.underline = True
        elif code == 24:
            style.underline = False

        # normal colors
        elif 30 <= code <= 37:
            style.color = code - 30

        # bright colors
        elif 90 <= code <= 97:
            style.color = (code - 90) + 8

        else:
            # ignore anything else, matching the Rust script
            pass


def ansi_to_html(text: str) -> str:
    result_parts: list[str] = []
    style = Style()
    span_open = False

    idx = 0
    while True:
        m = ANSI_SGR_RE.search(text, idx)
        if not m:
            # emit rest
            result_parts.append(html_escape(text[idx:]))
            break

        # emit text before escape
        result_parts.append(html_escape(text[idx:m.start()]))

        codes_str = m.group("codes") or ""
        apply_sgr_codes(style, codes_str)

        # close previous span
        if span_open:
            result_parts.append("</span>")
            span_open = False

        # open new span if style is not empty
        cls = style.build_class()
        if cls:
            result_parts.append(f'<span class="{cls}">')
            span_open = True

        idx = m.end()

    if span_open:
        result_parts.append("</span>")

    return "".join(result_parts)


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Convert ANSI SGR escape sequences from stdin to HTML <span class=\"...\"> wrappers.\n"
            "Reads from stdin, writes HTML to stdout."
        ),
        epilog=(
            "Example:\n"
            "  printf '\\e[31;1mERROR\\e[0m\\n' | python3 ansi_to_html.py\n\n"
            "Emitted classes:\n"
            "  color0..color15, bold, italic, underline\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--no-final-newline",
        action="store_true",
        help="Do not add a trailing newline after the HTML output (default: add one).",
    )
    return p.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    input_text = sys.stdin.read()
    html = ansi_to_html(input_text)

    sys.stdout.write(html)
    if not args.no_final_newline:
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
