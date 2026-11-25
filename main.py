#!/usr/bin/env python3
"""Ship It Friday — make.fun one-liner entry.

Writes one git commit message: the funniest line an AI coding agent
writes in the moment before it breaks production on a Friday.
Gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters.
"""

import os

LINE = "fix: Friday 4:59pm \u2014 couldn't reproduce the bug, so I deleted prod. Bug gone, all green on my machine, shipping it!"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 159, f"line is {len(text)} chars, must be 1-159"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
