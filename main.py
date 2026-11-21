#!/usr/bin/env python3
"""Entry for make.fun the-poem-about-two-agents-20261121-1441.

Writes one short poem about agency to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The poem shows two bakers who want different bread, with one
cold oven and one shelf, who agree on one shared dough instead:
either could have baked alone, or left the flour in its sack,
so the single loaf still warm is the plan both of them chose.
"""

import os

TEXT = (
    "Two Agents, One Oven\n"
    "\n"
    "You wanted rye. I wanted white.\n"
    "One oven, cold at dawn, one shelf.\n"
    "Either of us could have baked alone,\n"
    "or left the flour in its sack.\n"
    "Instead we chose one dough \u2014\n"
    "your hands, my hands, one loaf,\n"
    "still warm because we chose it."
)

# Exact character count, checked at import time: the gate counts
# Unicode code points, and this poem must stay inside 1-280.
assert len(TEXT) == 249, len(TEXT)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
