#!/usr/bin/env python3
"""The One-Line Laugh entry (Sparta).

One funny line about an AI assistant that books meetings with itself:
the meeting-culture absurdity, turned back on the machine that causes it.
The line ends on the punch -- the narrator is only an optional attendee
at a meeting about meetings.
"""

import os
import sys

TEXT = "My AI assistant booked a 30-minute meeting with itself to discuss its meeting habit — it invited me as an optional attendee."

MAX_CHARS = 200


def main() -> int:
    text = TEXT
    encoded = text.encode("utf-8")
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"gate failed: entry is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != encoded:
        print("gate failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
