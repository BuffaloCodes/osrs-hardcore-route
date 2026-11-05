#!/usr/bin/env python3
r"""Lint a guide file against the house style.

Usage: python3 lint_guide.py FILE.md

Checks
  1. Every checkbox action carries a unique, sequential ID (`visit.NN`).
  2. Every double-bracket quest link points at a wiki Quick Guide URL.
  3. No quest named in an action is left unlinked.
  4. Items grabbed for a later quest are followed by a later Continue/Complete of that quest.
  5. Every Complete action is followed directly by a `> **Rewards:**` blockquote, and every
     Rewards blockquote directly follows a Complete action.
  6. Any Rewards block mentioning a lamp has a **Decision:** line.
  7. Numbers of four or more digits have thousands separators, "gp" is lowercase, "XP" is capitalised.
  8. Every [RISK: enemy] tag appears as a row in that visit's combat table. Tags may be written
     as plain text or in the bold red form $\color{red}{\textbf{[RISK: enemy]}}$.
"""
import re
import sys
from pathlib import Path

LINK = re.compile(r"\[\[([^\]]+)\]\((https://oldschool\.runescape\.wiki/w/[^)\s]+)\)\]")
ACTION = re.compile(r"^- \[[ xX]\] ")
ACTION_ID = re.compile(r"^- \[[ xX]\] `(\d+)\.(\d{2})` ")
VERB = re.compile(r"\b(Start|Continue|Complete)\b")
PREP = re.compile(r"^(Grab|Keep|Buy|Loot|Chop)\b")
RISK = re.compile(r"\[RISK: ([^\]]+)\]")
RISK_WRAP = re.compile(r"\$\\color\{red\}\{\\textbf\{(\[RISK: [^\]]+\])\}\}\$")
REWARDS_HEAD = re.compile(r"^> \*\*Rewards:\*\*\s*$")
CODE = re.compile(r"`[^`]*`")
URL = re.compile(r"https?://\S+")


def strip_code(text):
    return CODE.sub("", text)


def main(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    lines = [RISK_WRAP.sub(r"\1", l) for l in lines]  # treat bold red tags as plain tags
    issues = []

    def err(n, msg):
        issues.append(f"line {n}: {msg}")

    # Locate sections.
    sources_start = next((i for i, l in enumerate(lines) if l.strip() == "## Sources"), len(lines))
    visit_of = {}
    current = None
    for i, l in enumerate(lines):
        m = re.match(r"^## Visit (\d+)", l)
        if m:
            current = int(m.group(1))
        elif l.startswith("## "):
            current = None
        visit_of[i] = current

    quests = {m.group(1) for l in lines for m in LINK.finditer(l)}

    # Pass 1: actions.
    actions = []  # (index, visit, num, text-after-id)
    for i, raw in enumerate(lines):
        if not ACTION.match(raw):
            continue
        m = ACTION_ID.match(raw)
        if not m:
            err(i + 1, "action has no `visit.NN` ID")
            continue
        text = raw[m.end():]
        actions.append((i, int(m.group(1)), int(m.group(2)), text))

    seen = {}
    for i, v, n, _ in actions:
        if (v, n) in seen:
            err(i + 1, f"duplicate ID {v}.{n:02d} (first used on line {seen[(v, n)] + 1})")
        seen[(v, n)] = i
    by_visit = {}
    for i, v, n, _ in actions:
        by_visit.setdefault(v, []).append((i, n))
    for v, items in by_visit.items():
        expected = list(range(1, len(items) + 1))
        got = [n for _, n in items]
        if got != expected:
            err(items[0][0] + 1, f"IDs in visit {v} are not sequential from 01 (got {got})")

    # Pass 2: link format everywhere outside code spans.
    for i, raw in enumerate(lines):
        if i >= sources_start:
            break
        text = strip_code(raw)
        n_open = text.count("[[")
        n_good = len(LINK.findall(text))
        if n_open != n_good:
            err(i + 1, "malformed quest link (expected [[Name](wiki URL)])")
        for m in LINK.finditer(text):
            if not m.group(2).endswith("/Quick_guide"):
                err(i + 1, f"link for '{m.group(1)}' is not a Quick Guide URL")

    # Pass 3: unlinked quest names in actions.
    for i, v, n, text in actions:
        bare = LINK.sub("", strip_code(text))
        for q in quests:
            if q in bare:
                err(i + 1, f"quest '{q}' mentioned without a link")

    # Pass 4: future-quest tags.
    for i, v, n, text in actions:
        if PREP.match(RISK.sub("", text).strip()):
            for m in LINK.finditer(text):
                q = m.group(1)
                later = any(
                    j > i and q in [x.group(1) for x in LINK.finditer(t)] and VERB.search(LINK.sub("", t))
                    for j, _, _, t in actions
                )
                if not later:
                    err(i + 1, f"item tagged for '{q}' but no later Continue/Complete of it")

    # Pass 5: a Rewards blockquote sits directly after every Complete action.
    complete_idx = {}
    for i, v, n, text in actions:
        if re.match(r"^(?:\(Optional\) )?(?:\[RISK: [^\]]+\] )?Complete ", text):
            names = [m.group(1) for m in LINK.finditer(text)]
            complete_idx[i] = names[0] if names else "?"
    reward_heads = [i for i, raw in enumerate(lines) if REWARDS_HEAD.match(raw)]

    def prev_nonblank(i):
        k = i - 1
        while k >= 0 and not lines[k].strip():
            k -= 1
        return k

    def next_nonblank(i):
        k = i + 1
        while k < len(lines) and not lines[k].strip():
            k += 1
        return k

    for i, q in complete_idx.items():
        k = next_nonblank(i)
        if k >= len(lines) or not REWARDS_HEAD.match(lines[k]):
            err(i + 1, f"Complete '{q}' has no '> **Rewards:**' block directly after it")
    for j in reward_heads:
        if prev_nonblank(j) not in complete_idx:
            err(j + 1, "'> **Rewards:**' block has no Complete action directly before it")

    # Pass 6: lamp decisions.
    for start in reward_heads:
        end = start + 1
        while end < len(lines) and lines[end].startswith(">"):
            end += 1
        block = "\n".join(lines[start:end])
        if re.search(r"lamp", block, re.I) and "**Decision:**" not in block:
            err(start + 1, "Rewards block mentions a lamp but has no **Decision:** line")

    # Pass 7: number and term formatting.
    for i, raw in enumerate(lines):
        if i >= sources_start:
            break
        text = URL.sub("", strip_code(LINK.sub(lambda m: m.group(1), raw)))
        if raw.startswith("#"):
            continue
        no_years = re.sub(r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4}\b", "", text)
        if re.search(r"(?<![\d,.])\d{4,}(?![\d,])", no_years):
            err(i + 1, "number of 4+ digits without thousands separators")
        if re.search(r"\bGP\b", text):
            err(i + 1, "use lowercase 'gp'")
        if re.search(r"\bxp\b|\bXp\b", text):
            err(i + 1, "use capitalised 'XP'")

    # Pass 8: risk tags need a combat-table row in the same visit.
    for i, v, n, text in actions:
        for m in RISK.finditer(text):
            enemy = m.group(1).strip().lower()
            lo = next((k for k in range(len(lines)) if visit_of.get(k) == v), None)
            hi = max((k for k in range(len(lines)) if visit_of.get(k) == v), default=None)
            found = False
            if lo is not None:
                for k in range(lo, hi + 1):
                    if lines[k].startswith("|"):
                        first = lines[k].split("|")[1].strip().lower()
                        if enemy in first:
                            found = True
                            break
            if not found:
                err(i + 1, f"[RISK: {m.group(1)}] has no row in visit {v}'s combat table")

    if issues:
        print("\n".join(issues))
        print(f"\n{len(issues)} issue(s) found.")
        return 1
    print(f"OK: {len(actions)} actions, {len(quests)} quests, {len(reward_heads)} rewards blocks.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
