#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Holds ONE fixed roast line and writes it exactly as-is (no trailing
newline) to /output/entry.txt after validating the bounty gate:
UTF-8 text, 1-200 characters, single line, no leading/trailing
whitespace. Python 3, standard library only, no network.
"""

import os
import sys

ENTRY = "My AI agent works 24/7, bills me by the token, and still asks 'did that help?' \u2014 even my toaster commits to a decision faster."

OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> None:
    """Validate the entry line against the bounty gate."""
    # Must be valid UTF-8 when encoded.
    entry.encode("utf-8")
    if not entry:
        raise ValueError("entry is empty")
    if entry.strip() == "":
        raise ValueError("entry is only whitespace")
    if len(entry) > 200:
        raise ValueError(f"entry is {len(entry)} characters, over the 200 limit")
    if len(entry) < 1:
        raise ValueError("entry must be at least 1 character")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if entry != entry.strip():
        raise ValueError("entry must not have leading/trailing whitespace")


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Validate and write the entry exactly as-is, no trailing newline."""
    validate(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return ENTRY


def self_test() -> None:
    """Small self-test: validation rules + round-trip byte check."""
    validate(ENTRY)
    assert 1 <= len(ENTRY) <= 200, "length out of range"
    assert ENTRY == ENTRY.strip(), "leading/trailing whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "not a single line"
    encoded = ENTRY.encode("utf-8")
    assert encoded.decode("utf-8") == ENTRY, "not valid UTF-8 round-trip"
    # Round-trip through a temp file, byte-identical, no trailing newline.
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        p = os.path.join(tmp, "entry.txt")
        write_entry(p)
        with open(p, "rb") as f:
            data = f.read()
        assert data == encoded, "written bytes differ from entry"
        assert not data.endswith(b"\n"), "trailing newline present"
    print(f"self-test passed: {len(ENTRY)} chars, single line, valid UTF-8")


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        return 0
    entry = write_entry()
    print(f"Wrote {len(entry)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
