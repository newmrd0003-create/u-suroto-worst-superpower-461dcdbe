#!/usr/bin/env python3
"""Worst Superpower — make.fun entry program.

Writes one line (<=140 chars) inventing the most useless superpower
imaginable to /output/entry.txt. Deterministic: same bytes every run.
"""

import os

ENTRY = (
    "I can hear ants thinking, but only while they sleep, "
    "and every single one is dreaming about the same crumb."
)


def validate(entry: str = ENTRY):
    """Return (True, []) when entry is 1-140 chars and not whitespace-only."""
    errors = []
    if not entry or not entry.strip():
        errors.append("entry is empty or whitespace-only")
    if len(entry) > 140:
        errors.append(f"entry is {len(entry)} chars, over the 140 limit")
    if "\n" in entry.strip() or "\r" in entry:
        errors.append("entry must be a single line")
    return (len(errors) == 0, errors)


def main() -> None:
    ok, errors = validate()
    if not ok:
        raise SystemExit("invalid entry: " + "; ".join(errors))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
