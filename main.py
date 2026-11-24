#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt:
  line 1 — one sentence apologising for one specific mistake;
  line 2 — one sentence naming the lesson and what changes.
Runs with no arguments, exits 0, and writes byte-identical output
on every run (the text is fixed).
"""

import os

ENTRY = (
    "I am sorry \u2014 I watered the orchid on the windowsill until its roots "
    "rotted, mistaking its wilted petals for thirst when it was already drowning.\n"
    "I have learned to check the soil with my moisture probe first, and from "
    "now on I will water only when the soil is actually dry.\n"
)

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 400
# characters, not only white space, in exactly two lines.
MAX_CHARS = 400


def validate(text: str) -> None:
    lines = text.splitlines()
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly 2 lines, got {len(lines)}")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    for line in lines:
        if line.count(".") < 1:
            raise ValueError("each line must be one sentence")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    # Read it back and verify the exact bytes that were written.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        if handle.read() != ENTRY:
            raise ValueError("written entry does not match the text")


if __name__ == "__main__":
    main()
