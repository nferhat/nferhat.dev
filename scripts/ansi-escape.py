#!/usr/bin/env python3
"""
Read ANSI-colored text from stdin and emit djot with [text]{.class} span wrappers.

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

# Characters that would otherwise be parsed as djot syntax (or trigger smart
# punctuation, for runs of '-' and '.') inside the emitted text.
DJOT_SPECIAL_RE = re.compile(r"""[\\`*_{}\[\]<>~^$!"'|#]|-(?=-)|\.(?=\.)""")


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

    def build_classes(self) -> list[str]:
        classes: list[str] = []
        if self.color is not None:
            classes.append(f"color{self.color}")
        if self.bold:
            classes.append("bold")
        if self.italic:
            classes.append("italic")
        if self.underline:
            classes.append("underline")
        return classes


def djot_escape(text: str) -> str:
    return DJOT_SPECIAL_RE.sub(lambda m: "\\" + m.group(0), text)


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


def wrap_span(text: str, classes: list[str]) -> str:
    escaped = djot_escape(text)
    if not text or not classes:
        return escaped
    attrs = " ".join(f".{c}" for c in classes)
    return f"[{escaped}]{{{attrs}}}"


def ansi_to_djot(text: str) -> str:
    result_parts: list[str] = []
    style = Style()

    idx = 0
    while True:
        m = ANSI_SGR_RE.search(text, idx)
        end = m.start() if m else len(text)

        # emit text before the escape (or the rest), wrapped in the current style
        result_parts.append(wrap_span(text[idx:end], style.build_classes()))

        if not m:
            break

        apply_sgr_codes(style, m.group("codes") or "")
        idx = m.end()

    return "".join(result_parts)


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Convert ANSI SGR escape sequences from stdin to djot [text]{.class} spans.\n"
            "Reads from stdin, writes djot to stdout."
        ),
        epilog=(
            "Example:\n"
            "  printf '\\e[31;1mERROR\\e[0m\\n' | python3 ansi-escape.py\n\n"
            "Emitted classes:\n"
            "  color0..color15, bold, italic, underline\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--no-final-newline",
        action="store_true",
        help="Do not add a trailing newline after the djot output (default: add one).",
    )
    return p.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    input_text = sys.stdin.read()
    djot = ansi_to_djot(input_text)

    sys.stdout.write(djot)
    if not args.no_final_newline:
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
