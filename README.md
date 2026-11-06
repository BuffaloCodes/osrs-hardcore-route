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
| `chapters/Step0_Hardening_v0.02.md` | Step 0: hardening block (v0.02). Raises HP, Magic, Attack and Strength before the efficient route begins. |
| `chapters/Chapter1.md` | Chapter 1 of the route. Placeholder until the cleaned version is added. |
| `data/risk_data.csv` | Intake form for enemy and hazard levels, max hits and HP gates (see `data/README.md`). |
| `tools/lint_guide.py` | Lints a guide file against the house style. |
| `CHANGELOG.md` | Chronicle of the work done on the guide, tooling and README, with commit hashes. |

## Conventions

| Rule | Standard |
|------|----------|
| Step IDs | Every action carries a fixed ID in code formatting: `visit.number`, for example `1.07`. Once the guide is published, IDs are never renumbered and new steps take the next free number in their visit. |
| Actions | Every action is a checkbox item. |
| Quest verbs | Start, Continue, Complete. |
| Quest references | Every mention of a quest in an action links its Quick Guide, inside brackets: `[[Quest name](Quick Guide URL)]`. |
| Quest steps | Short quests are not written out step by step. The quest link is the guide, and the player is expected to use it. Only steps that matter to the route (risks, items, decisions) are spelled out. |
| Items for later quests | The action ends with the quest tag, for example `Grab 6x logs [[Tree Gnome Village](...)]`. |
| Completion rewards | A `> **Rewards:**` blockquote follows every Complete action. Any lamp or XP choice carries a `**Decision:**` line with a recommendation. |
| Danger | Any action where you can die starts with a bold red tag carrying the enemy's max hit, written `$\color{red}{\textbf{[RISK: enemy name (max hit)]}}$`. The enemy appears in that visit's combat table, and the max hit matches the table's Max hit cell (`TBD` or `not listed` where the table says so). The colour shows where maths rendering is supported, such as GitHub and the VS Code preview. |
| Optional choices | Any text that offers an optional choice, including `(Optional)` steps, is italicised. |
| Visit layout | Each visit opens with its combat table, then the steps, then a notes block and the estimated levels. |
| Numbers | `gp` in lowercase, thousands separators (`1,833`), quantities as `6x`, `XP` in capitals, times as `1h 23m`. |

## Step 0 decisions

| Topic | Decision |
|-------|----------|
| Mudfoot lamps (4 x 500 XP) | Magic until level 13. Any lamps left over go on Hitpoints. |
| Ides of Milk lamp (1,000 XP) | Hitpoints |
| Lamps on Hitpoints | Confirmed possible (tested in-game) |
| Wind Strike damage | Only the unlock matters. At Magic 13+ Wind Strike's base max hit is 8 (2 at levels 1-4, 4 at 5-8, 6 at 9-12). Cost is 1 air rune and 1 mind rune. |
| Food | Gathered first, on the author's own route (Visit 0) |
| Minimum HP / combat level gates | Deferred for now |
| Witch's House | All four experiment forms can be safespotted |
| Brutus (Ides of Milk) | Safespot between the feed troughs to the south (tested in-game: no damage taken, no special-attack dodging needed) |

**Lamp arithmetic:** Magic level 13 needs 1,833 XP in total and each lamp is 500, so you need ceil((1,833 - your current Magic XP) / 500) lamps. With no prior Magic XP that is all four.

## Linting

```
python3 tools/lint_guide.py chapters/Step0_Hardening_v0.02.md
```

The linter takes one file at a time and checks:

1. Every checkbox action has a unique, sequential ID (`visit.NN`).
2. Quest links point at wiki Quick Guide URLs, and no quest named in an action is left unlinked.
3. Items grabbed for a later quest are followed by a later Continue/Complete of that quest.
4. Every Complete action is followed directly by a `> **Rewards:**` blockquote, and vice versa.
5. Rewards blocks that mention a lamp have a **Decision:** line.
6. Number formatting: thousands separators, lowercase "gp", capitalised "XP".
7. Every `[RISK: enemy (max hit)]` tag (plain or in the bold red form) appears in that visit's combat table, and its max hit matches the table.
8. No "Quest Helper" or "follow the Quick Guide" boilerplate.
9. Every `(Optional)` mention is italicised.
