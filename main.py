#!/usr/bin/env python3
"""Out-of-office auto-reply, written from the houseplant's point of view.

The program drops one short reply into /output/entry.txt: a single
line of plain UTF-8 text, no more than 120 characters long, and the
file ends right after the final full stop — no trailing newline.

Why this line works: it treats the phrase "on leave" as a botanical
fact rather than a HR formality. A leaf came off this morning, so the
plant is, strictly speaking, on leave. The rest of the sentence is
the plant's three demands — water, silence, and a cover story agreed
with the fern in the corner — which is where the second laugh sits.
"""

import os

# The reply itself, word for word as it belongs in the entry file.
LINE = (
    "I'm on leave \u2014 literally, one fell off this morning. "
    "Water me, don't email me, and tell the fern I said nothing."
)


def main() -> None:
    """Send the reply to the harness output path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # The strip keeps the file to exactly the line — nothing after it.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE.strip())


if __name__ == "__main__":
    main()
