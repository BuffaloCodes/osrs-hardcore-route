# Changelog

Work on `chapters/Chapter0.md`, `tools/lint_guide.py` and `README.md`. Newest first. Commit hashes are in brackets. Wiki facts were checked against the OSRS Wiki on 5 November 2026.

## 6 November 2026 (notes sweep)

- Swept `chapters/Chapter0.md` end to end and rewrote the three notes files. `notes/Open_Items.md` now has 21 numbered items (guide fixes, author decisions, supplies, data) plus a table of every quest's state at `2.71`. `notes/Sources.md` lists every wiki page the guide cites, the author-tested facts and the reference guides. `notes/Questions.md` is split into 10 open questions and the answered ones.
- No change to `Chapter0.md` or `data/risk_data.csv`: the guide inconsistencies found are listed, not fixed.

## 6 November 2026 (answers applied)

- Restructured the repo: `Step0_Hardening_v0.03.md` is now `chapters/Chapter0.md` (version lives in its header and this changelog), and the working notes moved to `notes/` (`CLAUDE_Qs` is now `notes/Questions.md`, plus `Open_Items.md` and `Sources.md`). Older entries below use the old filenames.
- Removed everything after Visit 2 (Visits 3 to 6, the alternative order, the stat outcome and the Hardcore Worlds check), because that text did not contain the author's edits.
- Applied the author's answers to Visit 2: removed the Sunbeam ale, gem store and visit-ending steps (the visit now ends at `2.71`, and `2.71`+ renumbered), set 400 mind runes at `2.26`, dropped the Gary or Sue wording at `2.53`, and replaced the jaguar and funds TBDs.
- Level table: Slayer 9 and Hunter 13 from the Museum History Quiz, so total level is 258.
- Deleted `VISIT2_VERIFICATION.md`, now that its open items are settled.
- Cleaned stale references to the removed visits: itinerary rows for Visits 3 to 6, the Visit 4 order note, the Witch's House, Waterfall, Tree Gnome Village, Fight Arena and pebble sources, and the resolved open items that only concerned those visits (open items renumbered 1 to 6).
- Removed the Witch's House, Tree Gnome Village and Fight Arena item tags from `1.18` and `1.27` (linter now clean), and moved the open items and sources out of Step 0 into `notes/Open_Items.md` and `notes/Sources.md`.


## 6 November 2026 (v0.03 working draft)

### Visit 2 draft converted to numbered steps

- Converted the author's Visit 2 draft (Varrock, then Varlamore as far as Mistrock) into 69 checkbox steps, `2.01` to `2.69`, in the Visit 1 format, with quest Start, Continue and Complete links and italic `*(Optional)*` steps.
- Removed the two old Visit 2 steps (Aubury rune purchase, `2.02` and `2.03`), which duplicated the new steps. The Visit 2 Notes Funds block stays.
- Added `[RISK: Dark wizard (6)]` to `2.01` for the walking route. The max hit of 6 is not confirmed on the wiki.
- Quest label fixes from the wiki check: Children of the Sun finishes with Sergeant Tobyn (`2.12`), the manhole key is a Demon Slayer step (`2.20`), Daddy's Home completes with Marlo (`2.43`), Rag and Bone Man I starts with the Odd Old Man (`2.39`), and the 10 planks are for Daddy's Home (`2.37`).
- Smaller fixes: Thessalia is "browse" (`2.08`), axe levels (`2.48`), teak Woodcutting and Firemaking 35 (`2.50`), and world hopping for log spawns (`2.36`).
- Added `VISIT2_VERIFICATION.md`, the wiki check of the Visit 2 draft. It includes the in-game test results: Count Check still teleports to Barbarian Village (unknown whether it works again after a death or reset), Varrock has combat dummies, and the Eclipse red can be taken inside Apatura's building.

### Visit 2 completed to the Visit 1 structure

- Retitled Visit 2 "Varrock and Varlamore", rewrote the Goal, added the visit-specific notes line, and updated the itinerary row.
- Added a Varrock Diary line (Easy 5/14, or 4/14 without the optional dog) and counters on `2.05`, `2.08`, `2.11`, `2.35` and `2.37`.
- Added Rewards blocks for the four quests completed here: Gertrude's Cat (`2.40`), Children of the Sun (`2.12`), Daddy's Home (`2.43`) and the Lily Pad quest (`2.49`). None gives a lamp. The Complete steps now start with "Complete" so the linter matches them.
- Added a Jaguar row to the combat table (level 67, max hit 6, aggressive, east of Sunset Coast) and the `[RISK: Jaguar (6)]` tag on `2.58`.
- Added a `2.70` placeholder for how the visit ends and travels to Taverley, and Visit 2 Notes on Count Check, the Dark wizards, the Hunter's Guild, teak and the quests left open.
- Added "Estimated levels after Visit 2": 19 quest points and total level 246. Firemaking 50 is the step target. Woodcutting 48, Fletching 7, Cooking 11, Construction 8 and Attack 5 are estimates, with the assumptions listed under the table.
- Fixed a stale reference to Visit 2 steps `2.01` to `2.03` in the open items (now `2.25` and `2.26`).

### Visit 2 route changes from the author's notes

- Moved the combat dummy step to straight after Children of the Sun (`2.13`), since finishing the quest leaves you on the Varrock Castle roof where the dummies are.
- Added steps after Family Crest: steal a cup of tea at the tea stall (Varrock Diary, `2.28`), bank the tea, runes and research notes (`2.29`), and withdraw the hammer and saw (`2.30`). The hammer and saw are no longer in the earlier bank withdrawal (`2.24`).
- Filled the withdraw list at `2.35`: bucket of milk, raw sardine, Chronicle, axe, knife, gp stack, doogle leaf and 3x waxwood logs.
- `2.40` now makes 1 normal plank for the diary task and 3 waxwood planks. The 10 regular planks are already banked from Entrana.
- Jugs of wine cost 1 coin (`2.49`). Daddy's Home gives 1 quest point (confirmed). The Lily Pad quest start location is confirmed, so its TBD note was removed (`2.52`).
- Tea stall at `2.28` confirmed safe (no guards), so its guard TBD was removed. Added `2.46` to withdraw the 10x planks for Daddy's Home from the bank passed on the way back to Old Man Yarlo, which renumbered `2.46` onward by one (the Sunbeam ale step is now `2.69`, the visit ending `2.74`).
- Varrock Diary is now Easy 6/14, or 5/14 without the dog. Steps after `2.27` renumbered, so every Visit 2 step ID from `2.13` onward changed; the step numbers in the entries above this one and in `VISIT2_VERIFICATION.md` are from before this change.

### CLAUDE_Qs and risk data

- Replaced the old contents of `chapters/CLAUDE_Qs` with the current input needed and questions: Visit 2 runes and funds, the Sunbeam ale shortcut, the visit ending, the jaguar and Dark wizard data, the quests left open, the level table assumptions and a few housekeeping questions.
- `data/risk_data.csv`: the Dark wizard row now points at step `2.01` (was `2.02`) and a Jaguar row was added for step `2.62`.

### Open items for Visit 2

- `[TBD]` notes remain at `2.69` (Sunbeam ale and the Taverley shortcut) and `2.74` (how the visit ends).
- The `300 runes?` question at `2.26` and the funds check against the 3,704 gp floor are open. The nails and bolts of cloth at `2.41` cost about 3,550 gp.
- The Romeo & Juliet finish (Apothecary potion, Varrock crypt) is not in Visit 2.
- Visit 3 onward has not been edited by the author.

## 5 November 2026 (v0.02 working draft)

### v0.03: Level column removed and file renamed

- Renamed `chapters/Step0_Hardening_v0.02.md` to `chapters/Step0_Hardening_v0.03.md` (git rename, history kept) and updated the title, README and this file.
- Removed the Level column from every combat table, which now has Enemy, Max hit and Safespot / tactic. The linter now reads Max hit from the second column. Open item 6 now just notes that the tables come from `data/risk_data.csv`.

### Risk data synced to the guide

- `data/risk_data.csv` is populated by the author and now has only `id`, `visit`, `enemy`, `context`, `max_hit` and `safespot_or_tactic` (dropped `level`, `hp_gate`, `source_url`, `status`).
- Every `[RISK: ...]` tag and combat-table Max hit cell now carries the CSV number. Wilderness level 51 is 99, meaning any hit can be fatal. The Witch's experiment tag uses 5, the worst form.
- Added a failed pickpocket tag at `1.04` and rows for failed pickpockets and the Draynor rooftop course to the Visit 1 table.
- Linter: a risk tag now passes if any matching combat-table row has its max hit, so one tag can cover several rows.
- Removed the Food / HP gate column from every combat table, and the Draynor rooftop row from the Visit 1 table and the CSV, since the course cannot hurt you. The Level column stays, with some `TBD` levels still open.

### Cleanup from CLAUDE_Qs answers

- Cut bloat: struck-through text, the Ring of Life note, the Visit 1 notes that repeated other text, the five non-route rewards lines, and the Visit 0 and Visit 1 carry-forward blocks. Merged the gold text and shortened the Thieving note and footnotes.
- Removed all 17 `[add which quests need these]` placeholders (item quest tags are not being added to bought or picked-up items).
- Wording: bank names at `1.37` and `1.52`, range location at `1.42`, Entrana law altar and spawns at `1.45`, Brutus capped at 80 Wind Strike casts at `1.67`.
- Visit 1 now ends after Brutus. Varrock is the new Visit 2 (Chronicle teleport, walk with a Dark wizard risk tag, buy runes). Old Visits 2 to 5 are now Visits 3 to 6, with IDs, references and the itinerary renumbered.
- Added `data/risk_data.csv` and `data/README.md` as the risk data intake form, pre-filled from the combat tables.
- Not yet done: fill the risk data and push it into the combat tables, and the gold ledger.

### Visit 1: Draynor, Port Sarim and Falador leg [`af26fb7`]

- Added steps `1.33` to `1.56`: start A Porcine of Interest, Vampyre Slayer, The Corsair Curse, The Knight's Sword and Black Knights' Fortress, complete X Marks the Spot, a Draynor Rooftop Course lap to Agility 5, Wydin's, Gerrant and Betty purchases, Entrana, Sarah's farm shop, and Falador.
- Added a Lumbridge pickpocket step (`1.04`) for the Lumbridge & Draynor Diary. The diary count is now Easy 3/12.
- X Marks the Spot now completes in Visit 1. Its lamp is 300 XP and goes on Hitpoints.
- Moved the Wizards' Tower steps (Rune Mysteries, the ghost's skull) to just after Captain Tock. The deposit step now keeps the air talisman, because a deposit box cannot be withdrawn from.
- Renumbered Visit 1 to 72 steps and remapped every step reference.
- Added a home teleport cooldown note (30 minutes and shared, otherwise the player walks).
- Added a Black Knights' Fortress note: it needs 12 quest points, and you have exactly 12 at that step.
- Quest points now include Tutorial Island's 1 (9 after Visit 0, 15 after Visit 1). Visit 1 estimate: Hitpoints 15, Agility 5, total level 192.
- The Brutus feed-trough safespot is recorded as tested in-game (no damage taken, no special-attack dodging).
- Updated the Visit 1 Goal, itinerary row, diary count and carry-forward for the new items.

### Visit 0 and style pass [`9e4e0fc`, `482d39e`]

- Merged Monk's Friend into one Start step and one Complete step. Renumbered Visit 0 to `0.01`-`0.35` and updated step references.
- Every `[RISK: ...]` tag now carries the enemy's max hit, for example `[RISK: Sea slug (3)]`, copied from that visit's combat table.
- Removed the "follow the Quick Guide link or RuneLite's Quest Helper plugin" boilerplate from the guide and README.
- Optional choices are italicised: `(Optional)` steps, the Clan Wars teleport asides, the gold top-up choices, and similar asides.
- Gold: Visit 0 aims to be back to about 5,000 gp after shopping, to cover the Varrock runes. Keep 28 cakes for food and only sell cakes above that. The price-confirmation note stays open.
- Combat table: the Silk Stall has no safespot, only the Bakery Stall does.
- Estimated levels after Visits 0 and 1 are now a 24-skill table with quest points and total level, using the lower Firemaking estimate (36).
- Linter: risk tags need the `(max hit)` form and the value must match the combat table. It also rejects the banned boilerplate and any plain `(Optional)`, and accepts the italic `*(Optional)*` form on Complete steps. README conventions and lint list updated to match.

### Clock Tower removed from Visit 0 [`3a31cf3`]

- Removed the five Clock Tower steps and their rewards block, because the ogres in the red cog room can hit up to 7. Cost: 1 quest point, 500 gp and 1,000 Firemaking XP.
- The Firemaking XP only mattered for the Firemaking 30 gate at Sea Slug, which the log burning still clears. The quest is not scheduled anywhere in the guide.
- Added a player-choice gold top-up to replace the 500 gp: extra cakes (safer, safespot under the Baker) or about 9 extra silk (riskier, no safespot).
- Removed the Ogres and Dungeon rat combat rows and the floor-numbers note. Quest points and level estimates updated.

### Tooling

- Installed Python 3.12.10 (user scope, via winget). The linter now runs: `python -I tools/lint_guide.py chapters/Step0_Hardening_v0.03.md`.

### Verified against the wiki

- Black Knights' Fortress needs 12 quest points to start.
- Tutorial Island (now Learning the Ropes) gives 1 quest point since 22 October 2025.
- X Marks the Spot rewards 200 coins and a 300 XP antique lamp. Veos finishes it at the Port Sarim docks.
- The Draynor Village Rooftop Course has no Agility requirement. The Lumbridge & Draynor Easy diary includes the lap and a Lumbridge man/woman pickpocket.
- Captain Tock is at the crossroads north of Port Sarim, just south of the Falador farm. Sarah is at the Falador farm.
- Entrana refuses weapons and armour but allows runes. The Lumbridge Home Teleport has a shared 30-minute cooldown.
- Not verified: the planks and eggs spawns on Entrana, Brutus's hitpoints, and the Dark wizard max hits by level.

### Open items carried forward

- Confirm the 5,000 gp target covers the Varrock runes (note left on `0.33`), and finish the gold ledger.
- Decide whether to keep the carry-forward sections.
- Fill the 17 `[add which quests need these]` placeholders in Visits 0 and 1.
- Fill the remaining TBD levels in the combat tables.
- Move Varrock (`1.71`, `1.72`) into Visit 2 and update the Visit 1 Goal, itinerary row and notes. Taverley moves to a later visit.
- Add a risk tag and combat-table row for the Dark wizards outside Varrock (`1.71`).
- Convert the pending bracket notes (`BUFFALODAD...`, `UNSURE...`, `THIS SHOULD END VISIT 1...`) once resolved.

## Earlier history

- `f5f99a5` Visit 1 restructure, new formats, linter update.
- `0239a88`, `b4c2220`, `0f048ce` Visit 0 expanded to six quests, risk tags and sources added, file renamed.
- `55e9799`, `68ec97b`, `0b70426` Initial Step 0 block, linter, README, attribution and `.gitattributes`.
