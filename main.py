"""Alien Field Notes: The Two Day Earth Review — entry program.

Writes one original one-line review of planet Earth by an alien tourist
to /output/entry.txt (max 200 characters).
"""

import os

LINE = "The shower had two knobs, three settings, and no labels. I navigate wormholes for a living. 3/5 stars."


def main() -> None:
    # Self-check: the gate requires 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line out of gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
