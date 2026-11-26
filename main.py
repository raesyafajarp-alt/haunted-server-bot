#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Generates a single funny sign line for a haunted server room door
and writes it to /output/entry.txt (program/v1).

The sign text is fixed: every run produces the exact same bytes,
so the output is fully deterministic and reproducible.
"""

from pathlib import Path

ENTRY = "DO NOT REBOOT THE GHOST. He is the only one who remembers the root password."

MAX_LENGTH = 120
OUTPUT_FILENAME = "entry.txt"


def get_entry() -> str:
    """Return the sign text, enforcing the length gate (1-120 chars)."""
    return validate_entry(ENTRY)


def validate_entry(text: str) -> str:
    """Check one entry against the competition gates and return it unchanged.

    Gates: 1-120 characters, not only whitespace, single line.
    Raises ValueError on any violation so a bad entry can never be written.
    """
    if not 1 <= len(text) <= MAX_LENGTH:
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_LENGTH}")
    if not text.strip():
        raise ValueError("entry is blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def _write_entry(out_dir: Path, text: str) -> Path:
    """Write the validated entry to <out_dir>/entry.txt (UTF-8, LF)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / OUTPUT_FILENAME
    out_path.write_text(text, encoding="utf-8", newline="\n")
    return out_path


def main() -> None:
    import os

    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    _write_entry(out_dir, get_entry())


if __name__ == "__main__":
    main()
