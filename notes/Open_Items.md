# Open items

Running list for `chapters/Chapter0.md`. Last swept against the guide on 6 November 2026 (Visits 0 to 2, steps `0.01` to `2.71`). Items marked **Guide fix** are places where the guide text disagrees with itself and needs an edit. Items marked **Author** are waiting on a decision or test.

## Deferred by the author

1. **Gold ledger:** Add up expected gp across Visits 0 to 2: income (Hazeel Cult 2,000, Sheep Herder 3,100, silk sale 4,380, oyster pearls, Daddy's Home or Mudfoot rewards) against spending (the plague suit, general store, Trader Stan and Lovecraft's shopping, fares, Aubury's runes, bolts of cloth and nails). To be done once Chapter 0 is finished, then moneymaking is adjusted where needed. The numbers it has to reconcile:
   - `0.33` expects roughly 5,000 gp after Visit 0 shopping, still carrying the tag `[BUFFALODAD NEEDS TO CONFIRM THIS COVER IT]`.
   - The Visit 0 gold note says the route is about 500 gp short of the target without Clock Tower. The gold top-up (cakes or silk) is the player's choice, and the cake count needs the general store's buy price.
   - The Visit 2 floor is 3,704 gp after Aubury at `2.26`, but the nails and cloth at `2.41` alone cost about 3,550 gp (100 steel nails at 3 gp, 5 bolts of cloth at 650 gp).
2. **Visit 2 notes trim:** The author wants the Visit 2 notes block trimmed like Visits 0 and 1, later.
3. **Quests left open:** Finished when the later visits are written (see the quest table below). Shield of Arrav's partner is a non-issue for now.

## Guide fixes (the guide disagrees with itself)

4. **Visit 1 ending:** The Visit 1 goal and itinerary row say the visit ends with collecting the Chronicle and teleporting to Varrock, but no step does that. Visit 1 stops at `1.70`, and `2.01` handles getting to Varrock. Either add a step or trim the goal and itinerary.
5. **Visit 0 gold note, Visit number:** `0.33` says the cash covers "the rune purchases in Varrock later (Visit 1)". Varrock is Visit 2.
6. **Waterfall runes:** The Visit 2 goal and itinerary row say the runes for Waterfall Quest are bought, but `2.26` buys 400 mind, 100 air, 50 water, 50 earth and 20 fire runes. Nothing in Chapter 0 explains why the water, earth and fire counts are 50, 50 and 20. The old note about 6x of each rune no longer matches the step.
7. **Visit 2 goal omits Rune Mysteries:** `2.24`, `2.25` and `2.29` advance Rune Mysteries (research package to Aubury, research notes banked), but the Visit 2 goal and itinerary row do not list it.
8. **Title and header:** The title still reads "Step 0: Hardening the Account (v0.03)", while the file is now `Chapter0.md`. The Status line and the "Insert point" line also still use the "Step 0" and "Tutorial Island comes first" wording.
9. **Visit 0 food counts:** `0.19` banks "at least 14x bread and as many cakes as you get up to level 20 Thieving", but `0.33` keeps exactly 28 cakes. Check that the stall yield up to level 20 is at least 28 cakes, or reword `0.19`.
10. **Eleven silk kept:** `0.20` steals 84 silk and `0.33` sells 73, leaving 11 in the bank. No step in Chapter 0 uses the 11.
11. **Arrow shafts:** `2.39` fletches 2,100 arrow shafts and the level table counts the Fletching XP, but no step in Chapter 0 uses them.

## Author decisions and tests

12. **Count Check after a death or reset:** Works as of 6 November 2026 (author test). Whether it works again after a reset is unknown, and the wiki calls it one-time. Left as untested in the funds note.
13. **Stronghold of Security fallback:** If funds are short, `2.01` and the funds note fall back to Barbarian Village for the free 10,000 gp. The Stronghold has enemies, and there is no combat table or risk tag for it. The funds note only says low hit points are a worry. Decide whether to add risk data or drop the fallback.
14. **Firemaking and Thieving ranges:** Visit 0's Firemaking 36 is the low end of an estimated 36 to 39, and Thieving 25 is before the gold top-up. The later tables inherit these.
15. **Dark wizard max hit:** The table uses 6, which is the highest max hit among Dark wizards. The wiki gives 2 for the level 7 variant and no figure for level 20.
16. **Level tables:** Combat XP from the outlaws, Brutus and other fights is not counted in any table. The XP maths for Prayer, Crafting, Cooking, Construction, Hunter, Slayer, Fletching and Woodcutting was spot-checked on 6 November and matches the wiki XP table. Recheck Woodcutting and Firemaking after the first real run, since they depend on the log mix and teak count.

## Supplies

17. **Rune supply:** Wind Strike costs 1 air and 1 mind rune per cast. Mudfoot's package gives 80x of each, and Brutus (`1.67`) can take up to 80 casts, on top of the final outlaw (`1.19`). Check whether 80 each is enough for both fights, or whether Brutus waits until runes can be restocked. `2.26` then buys 400 mind runes, and 400 more air runes if no staff of air is bought.
18. **Food route:** Drafted as Visit 0. Remaining: the food quantity for the later fights. Quest tags for bought and picked-up items are deliberately not being added.
19. **Purchases with no consumer in Chapter 0:** These are bought or picked up for later visits that are not written yet, so check each against the later visits once they exist:
    - Visit 0: 4x purple dye (`0.11`), 3x rope, water-filled vial pack, 7x papyrus (`0.14`), 2x silver bar (`0.17`), 7x soda ash, 7x bucket of sand, cake tin and glassblowing pipe (`0.26`), and the fishing gear in `0.31` (2x fishing rod, fly fishing rod, harpoon, fishing bait, lobster pot).
    - Visit 1: the Entrana eggs (`1.45`), 7x onion (`1.65`), 2x woad leaf (`1.53`), eye of newt (`1.43`), 16x feather pack (`1.41`), the Falador farm tools and sacks (`1.50`), and the food from Wydin's (`1.40`).
    - Visit 2: sweetcorn, needle and bucket of water (`2.56` to `2.58`), pot of flour (`2.64`) and 6x onion (`2.65`).
    - Rope is resolved as a source: bought at the Ardougne general store, with no step in Visit 1.

## Data and structure

20. **Stale rows in `data/risk_data.csv`:** Rows for Visit 3 (Witch's experiment x4), Visit 5 (Khazard warlord, ogre, scorpion, bouncer, General Khazard) and Visit 6 (Moss Guardians, Fire Giants) belong to visits that were removed from the guide. Delete them, or keep them for when those visits come back.
21. **Merge with the main route:** How Chapter 0 hands over to Chapter 1 (currently a placeholder). Chapter 0 ends at the Mistrock bank at `2.71` with no step beyond it, by the author's instruction.

## Quests at the end of Chapter 0

| Quest | Started | Advanced | State at `2.71` | Finishes |
|-------|---------|----------|-----------------|----------|
| Hazeel Cult | `0.09` | | Complete | |
| Sheep Herder | `0.12` | | Complete | |
| Monk's Friend | `0.21` | | Complete | |
| Sea Slug | `0.28` | | Complete | |
| Tribal Totem | `0.27` | `0.32` | Complete | |
| Mudfoot's Big Adventure | `1.06` | `1.10` to `1.19` | Complete | |
| X Marks the Spot | `1.05` | `1.15`, `1.21`, `1.31` | Complete | |
| The Restless Ghost | `1.09` | `1.26`, `1.30`, `1.48` | Complete | |
| Misthalin Mystery | `1.24` | | Complete | |
| Sheep Shearer | `1.63` | | Complete | |
| The Ides of Milk | `1.13` | `1.58` to `1.68` | Complete | |
| Gertrude's Cat | `2.02` | `2.10`, `2.37` | Complete | |
| Children of the Sun | `2.12` | | Complete | |
| Daddy's Home | `2.22` | `2.31`, `2.46` | Complete | |
| Lily Pad Labour Dispute | `2.53` | | Complete | |
| Rune Mysteries | `1.02` | `1.47`, `2.24`, `2.25` | Open: research notes banked, return them to Sedridor | Later visit |
| A Porcine of Interest | `1.33` | `1.49` | Open | Later visit |
| Vampyre Slayer | `1.34` | `1.35`, `2.32` | Open: garlic and beer ready | Later visit |
| The Corsair Curse | `1.46` | | Open: started only | Later visit |
| The Knight's Sword | `1.54` | `2.16` | Open | Later visit |
| Black Knights' Fortress | `1.55` | | Open: started only | Later visit |
| Demon Slayer | `2.07` | `2.14`, `2.15`, `2.19`, `2.21` | Open: key collected | Later visit |
| Romeo & Juliet | `2.09` | `2.44`, `2.45` | Open: finishes in the Varrock crypt after the cadava potion | Later visit |
| Shield of Arrav | `2.16` | | Open: needs a partner | Later visit |
| Priest in Peril | `2.20` | | Open | Later visit |
| Family Crest | `2.27` | | Open | Later visit |
| Rag and Bone Man I | `2.42` | | Open: started only | Later visit |

Quest points at `2.71`: 19, including the 1 from Tutorial Island.

## Visit 3 (drafted 6 November 2026, steps `3.01` to `3.40`)

22. **Max hits:** Every max hit in the Visit 3 combat table and `[RISK: ...]` tag is `TBD`: Hobgoblin, Bear, maze monsters, Khazard commander, Khazard warlord, Fight Arena enemies, Spider, Jogre and Delrith. Fill them in from the wiki and add matching rows to `data/risk_data.csv`.
23. **Levels table:** Filled in (total level 356). It depends on Visit 2's estimated XP, which sits inside a level range for several skills. Strength 7 is 1 XP short of level 8, Thieving 28 could be 29, Magic 19 assumes exactly 1,833 XP after Visit 2, and Hitpoints 20 is close to the level 21 threshold. The gnome agility lap, the Biohazard dummies and spell casts are not counted. Recheck after the first real run.
24. **Diary tasks:** The diary line names the Gnome Agility Course lap (`3.18`) and the Hunter Emporium (`3.23`), but not the diary or the count. The gnomeball goal (`3.21`) may also be a diary task.
25. **Castle Wars direction:** `3.14` says head north towards the Tree Gnome Village. The author is verifying the direction.
26. **Maze risk:** The monsters in the Tree Gnome Village maze (`3.15`) are still to be analysed.
27. **Purchases with no consumer yet:** Feathers and arrow shafts (`3.02`), and the swamp toad (`3.20`) are not used in Visit 3. Check them against later visits.
28. **After `3.40`:** The next quest is not named, and the list of steps after it (Agility 50 and Bull Sharks, 36,512 Thieving XP, Death on the Isle, Brutus training, Black Knights' Fortress, Witch's House, The Feud, Thieving 50 and the Rogue outfit) is unordered. Death on the Isle and Brutus training have requirements to check first.
29. **Stale risk data:** The old Visit 3 rows in `data/risk_data.csv` (Witch's experiment) belong to the removed Visit 3, not this one. Item 20 covers them.

### Quests completed in Visit 3

| Quest | Started | Complete |
|-------|---------|----------|
| Rune Mysteries | `1.02` | `3.06` |
| Witch's Potion | `3.08` | `3.08` |
| Tree Gnome Village | `3.15` | `3.16` |
| Fight Arena | `3.24` | `3.24` |
| The Grand Tree | `3.22` | `3.38` |
| Plague City | `3.31` | `3.31` |
| Biohazard | `3.32` | `3.39` |
| Demon Slayer | `2.07` | `3.35` |

Quest points after Visit 3: 37. Quest rewards were checked against the wiki on 6 November 2026.

## Resolved

- **Combat tables:** Filled from `data/risk_data.csv` for Visits 0 to 2.
- **Rope:** Bought in Visit 0 at the Ardougne general store.
- **Item tags:** Witch's House, Tree Gnome Village and Fight Arena tags removed from `1.18` and `1.27` when Visits 3 to 6 were cut.
- **Jaguars:** Avoid them while walking, minor risk.
- **Sunbeam ale, gem store and visit-ending steps:** Deleted at the author's request.
- **Lily Pad quest:** Just finish the quest, no need to choose Gary or Sue.
- **Level table:** Slayer 9 and Hunter 13 from the Museum History Quiz, total level 258.
