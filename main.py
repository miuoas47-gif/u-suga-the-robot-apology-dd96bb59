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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
