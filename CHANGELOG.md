# Changelog

Milestones for the guide, newest first. Commit hashes are in brackets. The full history is in git.

## 11 November 2026: refocus on the Hardcore Worlds starter guide

The guide had grown into a multiquesting efficiency route. It is now a starter guide that ends when the account is hardened and has the Rogue outfit, ready to hand off to a free route or another route.

- Cut Visit 0 to Hazeel Cult, Sheep Herder, Tribal Totem and the food and silk thieving. Removed Monk's Friend, Sea Slug, the diary steps and the extra Wilderness lever pulls [`e7b8e05`].
- Cut Visit 1 to Mudfoot's Big Adventure, X Marks the Spot, the Ides of Milk and Draynor Agility laps to 25. All seven lamps stay [`5728185`].
- Cut Visit 2 to Children of the Sun, the Demon Slayer steps in Varrock, mind runes, and the Varlamore wine and Eclipse red trip, which stay until the gold ledger is done [`7dfdcd8`].
- Cut Visit 3 to Tree Gnome Village, Fight Arena, The Grand Tree and Demon Slayer. Added a Black demon risk row and let the linter accept more than one risk tag on a Complete step [`7aed8a5`].
- Added Visits 4 to 10: Hosidius fruit Thieving, Brimhaven Agility Arena and Bull Sharks, Brutus, Witch's House, Death on the Isle, The Feud with blackjacking, and the Rogues' Den [`368bc77`].
- Renumbered step IDs so each visit runs `01` upward [`aa56107`].
- Merged the open items and questions into one notes file and trimmed the sources and this changelog.
- Removed from the route: Misthalin Mystery, The Restless Ghost, Sheep Shearer, Rune Mysteries, Witch's Potion, Gertrude's Cat, Daddy's Home, The Ribbiting Tale of a Lily Pad Labour Dispute, Plague City, Biohazard, Black Knights' Fortress and every quest that was only started, along with Construction, teak Firemaking and the Museum quiz.

## 6 November 2026

- Visit 3 drafted with wiki-checked quest rewards [`c228bc6`, `eb968b9`].
- Restructured the repo into `chapters/` and `notes/`, and removed everything after Visit 2 that did not carry the author's edits [`9b9db63`, `da3a8b6`].
- Converted Visit 2 into numbered steps, wrote its notes and level table, and moved the open items, sources and questions into their own files.

## 5 November 2026

- Added the risk data intake form (`data/risk_data.csv`) and synced every `[RISK: ...]` tag and combat table to it.
- Cut the Clock Tower quest from Visit 0 because its ogres can hit up to 7.
- Extended Visit 1 with the Draynor, Port Sarim and Falador leg, and added the Brutus safespot as an author-tested fact.
- Linter updates: risk tags need the `(max hit)` form and match the combat table, plain `(Optional)` is rejected, and the "Quest Helper" boilerplate is banned.

## Earlier history

- `f5f99a5` Visit 1 restructure, new formats, linter update.
- `0239a88`, `b4c2220`, `0f048ce` Visit 0 expanded to six quests, risk tags and sources added, file renamed.
- `55e9799`, `68ec97b`, `0b70426` Initial Step 0 block, linter, README, attribution and `.gitattributes`.
