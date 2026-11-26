#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign line to /output/entry.txt (program/v1).
The line is fixed and deterministic: the same bytes on every run.
"""

import os

ENTRY = "DO NOT REBOOT THE GHOST. He is the only one who remembers the root password."

# Gate: 1 to 120 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars"
assert ENTRY.strip(), "entry is blank"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
