# Open items

Running list for `chapters/Chapter0.md`. Last swept on 11 November 2026, after the cleanup that cut the guide down to the Hardcore Worlds starter route (Visits 0 to 10). Step IDs below are current.

## Decisions waiting on the author

1. **Gold ledger.** Add up expected gp across all ten visits, then adjust how much to steal and sell at the steps already in the guide.
   - Income: Hazeel Cult 2,000 gp, Sheep Herder 3,100 gp, the silk sale (`0.15`), Mudfoot 500 gp, X Marks the Spot 200 gp, Fight Arena 1,000 gp, The Feud 500 gp, and the Eclipse reds (`2.27`, 700 gp each).
   - Spending: the plague suit (100 gp), the Chronicle and teleport cards (`1.20`), 400 mind runes (`2.11`), wine (`1.17`), Brimhaven arena entries (200 gp each), the Feud (501 gp), the magic carpet (200 gp), the Aldarin boat (20 gp), and anything bought on the GE.
   - The Visit 2 Gold note says the rune purchase and later steps need gp the ledger has not confirmed. The old 3,704 gp floor and the 5,000 gp target are gone with the cut shopping.
2. **Eclipse reds.** Keep the Hunters' Guild trip in Visit 2 (`2.14` to `2.30`), or move the sale to Aldarin in Visit 8, or cut it. Decide after the ledger.
3. **The Grand Tree.** Kept for now. It gives 18,400 Attack XP, 7,900 Agility XP, 2,150 Magic XP and 5 quest points, but costs about 8 steps, the Jogres at the glider and a Black demon fight. The author said it may be cut for travel reasons.
4. **Demon Slayer.** Kept for now for its two 1,000 XP lamps (about 5 Hitpoints levels at the current estimate). The cost is a Delrith fight, 25 bones and the Wizards' Tower stop.
5. **Count Check and the Stronghold of Security fallback** (`2.01` and the Visit 2 Funds note). Count Check works as of 6 November 2026 (author test), but not known after a death or reset, and the wiki calls it one-time. The Stronghold has enemies and no combat table or risk data. Keep, add risk data, or drop.
6. **Dark wizard max hit.** The table uses 6, the highest among Dark wizards. The wiki gives 2 for the level 7 variant and no figure for level 20.
7. **Rune supply.** Mudfoot gives 80 air and 80 mind runes. The final outlaw (`1.13`) and Brutus (`1.31`, up to 80 casts) both draw on them, before the 400 mind runes bought at `2.11`. Check that 80 is enough for both, or move Brutus after a restock. Visits 5 and 6 need more runes still.
8. **Cake count.** `0.10` banks "as many cakes as you get up to level 20 Thieving" but `0.15` keeps exactly 28. Check the real yield, or reword `0.10` to "28 cakes".
9. **How the guide ends.** Visit 10 stops at the Rogue outfit. There is no closing note about handing off to a free route or another route. Add one, or leave it out.

## Numbers to fill in

10. **Level tables.** Visits 2 and 3 are marked stale, and Visits 4 to 10 have none. Visits 0 and 1 were recalculated during the cleanup (Visit 1: Agility 25, total level 106, 10 quest points). Recalculate all of them once the route is final. The recalculation also needs: the Agility target at `5.07`, the Magic target at `6.04` and your Thieving XP at `4.04`.
11. **Max hits.** Every max hit is `TBD` in the combat tables for Visits 3, 4, 7, 8 and 9, except those already known. Fill them in from the wiki and add matching rows to `data/risk_data.csv`.
12. **XP and drops.** Magic and Prayer XP per Brutus kill (Visit 6), and what Bull Sharks drop and how much gp they bring in (Visit 5).
13. **Bull shark spot.** Visit 5 says the shore north of the Karamja volcano, tested by the author. The exact spot is `[missing]` in `5.06`.

## Route and wording checks (markers in the guide)

| Step | Check |
|------|-------|
| `2.14` | Route from the quetzal drop-off to the Hunters' Guild. The step used to follow a walk to Auburnvale |
| `3.05` | How to reach Ardougne. The step used to follow a Rimmington house build |
| `3.06` | Where the 6 logs for Tree Gnome Village come from. Visit 0 woodcutting no longer supplies them |
| `4.01` | Veos's trip to Port Piscarilius is free (the author recalls it) |
| `4.02` | Route from Port Piscarilius to Hosidius |
| `5.02` | Route to Brimhaven |
| `8.01` | Route from the quetzal to Sunset Coast |
| `9.04` | Route from Al Kharid to Shantay Pass (the wiki does not give it) |
| `10.02` | Which bank to use in Burthorpe |

The links for Witch's House, Death on the Isle and The Feud follow the `/Quick_guide` pattern but have not been confirmed to exist. The linter checks the format only.

## Resolved in the cleanup

- **Scope:** The guide is now a Hardcore Worlds starter guide that ends at the Rogue outfit, not a multiquesting efficiency route.
- **Cut quests:** Monk's Friend, Sea Slug, Misthalin Mystery, Restless Ghost, Sheep Shearer, Rune Mysteries, Witch's Potion, Gertrude's Cat, Daddy's Home, the Lily Pad quest, Plague City, Biohazard, Black Knights' Fortress, and every quest that was only started. See the changelog.
- **Cut steps:** Construction, Firemaking to 50 on teak, all diary-only steps, the museum quiz and the shopping for cut quests. Quest items can be bought on the GE, since the account is not an ironman.
- **Title and header:** Still to do, in the housekeeping step.
