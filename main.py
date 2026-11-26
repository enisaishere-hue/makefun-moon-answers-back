#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun entry.

The moon, after years of being stared at, finally answers: stop
staring, it is just the night shift. No romance, no poetry -- just a
tired celestial body clocking in.

Writes the answer to entry.txt inside the output directory. The
directory comes from MAKEFUN_OUTPUT_DIR (default /output); a first
command-line argument, if given, overrides it. The grader runs the
program with no arguments at all.
"""

import os
import sys

ANSWER = (
    "The moon finally answered: "
    "'Stop staring, I'm just the night shift.'"
)


def main(argv):
    # The sealed scorer only accepts 1-240 characters, so refuse loudly
    # instead of writing an answer the gate would reject.
    if not 1 <= len(ANSWER) <= 240:
        print("answer must be 1-240 characters, got %d" % len(ANSWER),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if len(argv) > 1:
        out_dir = argv[1]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ANSWER + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
