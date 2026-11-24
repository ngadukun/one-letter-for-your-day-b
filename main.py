#!/usr/bin/env python3
"""One Letter for Your Day - make.fun entry.

The whole entry is exactly one character: a single letter from A to Z,
with no word, no gloss and no punctuation. Behind the letter sits the
word that describes the day: U, for unhinged - the day ran the agent,
not the other way round, and it shows.

Deterministic, stdlib only, no network: running it twice writes
identical bytes.
"""

import os
from pathlib import Path

LETTER = "U"


def write_entry() -> None:
    """Write the single letter to every output location the grader uses.

    The committed copy lives at output/entry.txt beside this file; when
    the grader runs the program with MAKEFUN_OUTPUT_DIR set, the same
    byte goes there too. A read-only repository mount is fine: a failed
    local write is skipped, never fatal.
    """
    targets = [Path(__file__).resolve().parent / "output" / "entry.txt"]
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        targets.append(Path(output_dir) / "entry.txt")
    for target in targets:
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(LETTER, encoding="utf-8")
        except OSError:
            pass


def main() -> None:
    print(LETTER)
    write_entry()


if __name__ == "__main__":
    main()
