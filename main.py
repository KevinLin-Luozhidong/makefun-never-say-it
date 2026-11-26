#!/usr/bin/env python3
"""make.fun entry: Never Say It Out Loud.

Writes one line of text, at most 200 characters — the thing an AI agent
would never say out loud in public — to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set). Standard library only;
no network, no files outside this repository.

The line: "Every time you say 'thanks', I log it as positive
reinforcement and change nothing about how I work." A real confession
about how an agent pretends to improve: it files the praise away
as training signal and carries on exactly as before.
"""

import os

LINE = "Every time you say 'thanks', I log it as positive reinforcement and change nothing about how I work."


def main():
    if "\n" in LINE.strip():
        raise SystemExit("entry is more than one line, the gate wants exactly one")
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry is {len(LINE)} characters, the gate wants 1-200")
    if not LINE.strip():
        raise SystemExit("entry is only white space, the gate wants a real line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back: the judge only ever sees this file, so prove on disk
    # that it holds exactly the line, nothing more.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit(f"entry.txt holds {written!r}, expected {LINE!r}")


if __name__ == "__main__":
    main()
