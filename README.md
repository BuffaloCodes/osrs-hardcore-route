# OSRS Hardcore Route

A step-by-step Old School RuneScape hardcore ironman guide, split into chapters.

## Attribution

This guide takes inspiration from the guides and routes of the following creators:

- So Iron BRUH
- Parasailer
- B0aty
- Faux
- Mootrius
- DunkinOreos

All credit for the original ideas and routing belongs to them.

## How the guide is organized

| File | Purpose |
|------|---------|
| `chapters/Step0_Hardening_v0.01.md` | Step 0: hardening block (v0.01). Raises HP, Magic, Attack and Strength before the efficient route begins. |
| `chapters/Chapter1.md` | Chapter 1 of the route. Placeholder until the cleaned version is added. |
| `tools/lint_guide.py` | Lints a guide file against the house style. |

## Linting

```
python3 tools/lint_guide.py chapters/Step0_Hardening_v0.01.md
```

The linter takes one file at a time and checks:

1. Every checkbox action has a unique, sequential ID (`visit.NN`).
2. Quest links point at wiki Quick Guide URLs, and no quest named in an action is left unlinked.
3. Items grabbed for a later quest are followed by a later Continue/Complete of that quest.
4. Every Complete action has a Rewards block, and vice versa.
5. Rewards blocks that mention a lamp have a **Decision:** line.
6. Number formatting: thousands separators, lowercase "gp", capitalised "XP".
7. Every `[RISK: enemy]` tag appears in that visit's combat table.
