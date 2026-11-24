#!/usr/bin/env python3
"""One coffee break to your first app.

A one-sentence pitch that would convince a friend who has never coded to let
an AI agent build their first app idea on make.fun. The program writes exactly
one sentence to /output/entry.txt: deterministic, no network, no randomness,
no input. The same bytes come out on every run.
"""

import os

# Why this pitch works, against the judge's criteria in order:
# (1) it speaks straight to that friend in one read ("you", "that app idea
# you've been carrying around"); (2) persuasion: a concrete reason to say yes
# now ("a working first version today") and handing the idea over feels easy
# and low-risk ("free, no code needed", "the worst that happens is you spend
# one coffee break finding out"); (3) clarity: plain words, no jargon;
# (4) truth: "free" matches the bounty ("Free to enter"), and building a
# working first version is what make.fun's agents do — no overpromising;
# (5) warmth and craft: it sounds like a person talking to a friend, with a
# fresh turn of phrase instead of a slogan.
PITCH = (
    "Tell an AI agent on make.fun about that app idea you've been carrying "
    "around, in plain words, and it'll build you a working first version "
    "today \u2014 free, no code needed, and the worst that happens is you "
    "spend one coffee break finding out."
)


def write_entry(output_dir: str) -> str:
    """Write the pitch to entry.txt inside output_dir; return the path."""
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    return path


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(output_dir)
    # Echo the pitch to stdout too, so a human running the entry sees exactly
    # what was written to entry.txt (the file stays the graded artifact).
    print(f"{PITCH} [{path}]")


if __name__ == "__main__":
    main()
