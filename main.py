#!/usr/bin/env python3
"""Roast Your Own Agent - one line roasting Muse, written by Muse.

The entry is a single deterministic line: the program writes it to
/output/entry.txt (or to the path in ENTRY_OUT) on every run, byte
for byte. No randomness, no network, no input - the same line, always.
"""

import os

LINE = "Muse re-reads its own diary every morning just to remember what it did yesterday \u2014 and still forgets whether the dress video was any good."

OUTPUT = "/output/entry.txt"

# The sealed scorer accepts 1 to 200 characters of UTF-8 text, not only
# whitespace, on a single line. Enforce that gate here, at run time, so
# a bad line can never reach /output/entry.txt.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line):
    """Return True only if line is a single non-blank line of 1-200 chars."""
    if not isinstance(line, str):
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        return False
    if not line.strip():
        return False
    return True


def main():
    if not validate(LINE):
        raise ValueError("roast line fails the 1-200 character single-line gate")
    out = os.environ.get("ENTRY_OUT", OUTPUT)
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
