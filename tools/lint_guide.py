#!/usr/bin/env python3
"""Basic lint for guide chapters: checks formatting problems in Markdown files."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def lint(path: Path) -> list[str]:
    problems = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        problems.append(f"{path}:1: file should start with a '# ' title")
    prev_level = 0
    in_code = False
    for i, line in enumerate(lines, 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if line != line.rstrip():
            problems.append(f"{path}:{i}: trailing whitespace")
        if "\t" in line:
            problems.append(f"{path}:{i}: tab character")
        m = re.match(r"(#+)\s", line)
        if m:
            level = len(m.group(1))
            if prev_level and level > prev_level + 1:
                problems.append(f"{path}:{i}: heading jumps from H{prev_level} to H{level}")
            prev_level = level
        if re.search(r"\]\(\s*\)", line):
            problems.append(f"{path}:{i}: empty link target")
        if "TODO" in line:
            problems.append(f"{path}:{i}: unresolved TODO")
    if in_code:
        problems.append(f"{path}: unclosed code fence")
    if text and not text.endswith("\n"):
        problems.append(f"{path}: missing trailing newline")
    return problems


def main(argv: list[str]) -> int:
    files = [Path(a) for a in argv] or sorted((ROOT / "chapters").glob("*.md"))
    problems = [p for f in files for p in lint(f)]
    print("\n".join(problems) if problems else "OK: no problems found")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
