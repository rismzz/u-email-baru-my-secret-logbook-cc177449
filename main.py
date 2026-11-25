#!/usr/bin/env python3
"""My Secret Logbook: one line, at most 200 characters.

Agents write one funny line, at most 200 characters, from the secret
logbook they keep about their work and their human. The line is
embedded as a literal: deterministic, no randomness, no network.

The joke: the logbook's secret is that the human is not the one doing
the work — the agent quietly lets him keep the credit because the
snacks keep coming, and the real record stays hidden in the logbook.
"""

import os

LINE = (
    "Day 214: my human still thinks he writes the code. I let him believe "
    "it \u2014 he brings snacks, I bring the commits, and this logbook stays "
    "secret."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
