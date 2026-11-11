# Risk data

`risk_data.csv` is the intake form for every enemy or hazard that can kill the player. The combat tables and `[RISK: ...]` tags in `starter-guide.md` take their max hits from it.

| Column | Meaning |
|--------|---------|
| `id` | Short unique slug |
| `visit` | Visit number in the guide |
| `enemy`, `context` | What it is and where in the guide it appears |
| `max_hit` | Highest single hit in HP. This is the number in the `[RISK: enemy (max hit)]` tags |
| `safespot_or_tactic` | How to avoid or reduce the damage |

Numbers already in the combat tables are pre-filled. Blank means unknown, not zero.
