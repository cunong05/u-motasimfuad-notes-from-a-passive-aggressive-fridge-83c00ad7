#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun bounty entry.

Writes one funny passive-aggressive note from a smart fridge
to its owner, to /output/entry.txt.
"""

NOTE = "You opened me 14 times today, ate nothing, then told your friends I'm always empty. The yogurt heard you. So did I."

OUT_DIR = "/output"


def main():
    import os
    # Guard: the bounty requires one line, 1-200 characters, valid UTF-8.
    assert "\n" not in NOTE and 1 <= len(NOTE) <= 200, "note must be one line, 1-200 chars"
    NOTE.encode("utf-8")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(NOTE + "\n")


if __name__ == "__main__":
    main()
