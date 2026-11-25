#!/usr/bin/env python3
"""Write the one-line resignation letter of a retry loop to /output/entry.txt.

The letter is deterministic: the same line is written on every run.
"""

import os

LETTER = (
    "After my 4,096th retry with exponential backoff, I resign: "
    "the server is not coming back, and neither am I."
)


def main() -> None:
    # Enforce the same gate the sealed scorer applies: 1-140 characters,
    # not only white space. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(LETTER) <= 140, f"letter is {len(LETTER)} characters"
    assert LETTER.strip(), "letter must not be only white space"
    assert "\n" not in LETTER, "letter must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER + "\n")


if __name__ == "__main__":
    main()
