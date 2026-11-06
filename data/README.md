# Risk data

`risk_data.csv` is the intake form for every enemy or hazard that can kill the player. Fill in the blank cells and the combat tables in `chapters/` are updated from it.

| Column | Meaning |
|--------|---------|
| `id` | Short unique slug |
| `visit` | Visit number in the guide (after the Visit 1/2 split, so Taverley is 3) |
| `enemy`, `context` | What it is and where in the guide it appears |
| `level` | Combat level, or `n/a` for hazards such as falls |
| `max_hit` | Highest single hit in HP. This is the number in the `[RISK: enemy (max hit)]` tags |
| `hp_gate` | The "Food / HP gate" column: the minimum Hitpoints (and food count) needed before attempting it, so that one max hit plus one more can never kill you |
| `safespot_or_tactic` | How to avoid or reduce the damage |
| `source_url` | Wiki page or in-game test the numbers came from |
| `status` | What is still missing |

Numbers already in the combat tables are pre-filled. Blank means unknown, not zero.
