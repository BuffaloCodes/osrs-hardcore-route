# Step 0: Hardening Block (v0.02)

**Purpose:** Raise HP, Magic, Attack and Strength before the efficient part of the route begins, on a mode where one death means a reset or a permanent transfer.

**Insert point:** First thing done on the account after a Death/Reset, to harden it against dangerous overworld events. Tutorial Island and Death's Delegate come first.

**Method:** Multiquesting. Each visit to an area advances every relevant quest, and no quest is finished before the next one is started unless that is the cheaper path.

**Status:** Working draft. Quest data comes from the OSRS Wiki as of 5 November 2026. Mudfoot's Big Adventure was released 2 days ago and its wiki page is flagged as possibly incomplete, so it was checked in-game on 5 November 2026.

---

## Conventions

| Rule | Standard |
|------|----------|
| Step IDs | Every action carries a fixed ID in code formatting: `visit.number`, for example `1.07`. IDs are never renumbered. New steps take the next free number in their visit. |
| Actions | Every action is a checkbox item. |
| Quest verbs | Start, Continue, Complete. |
| Quest references | Every mention of a quest in an action links its Quick Guide, inside brackets: `[[Quest name](Quick Guide URL)]`. |
| Items for later quests | The action ends with the quest tag, for example `Grab 6x logs [[Tree Gnome Village](...)]`. |
| Completion rewards | A `Rewards` block follows every Complete action. Any lamp or XP choice carries a `**Decision:**` line with a recommendation. |
| Danger | Any action where you can die starts with `[RISK: enemy name]`, and the enemy appears in that visit's combat table. |
| Carry-forward | Each visit ends with the items you must still hold for later quests. |
| Numbers | `gp` in lowercase, thousands separators (`1,833`), quantities as `6x`, `XP` in capitals, times as `1h 23m`. |

---

## Decisions locked in

| Topic | Decision |
|-------|----------|
| Mudfoot lamps (4 x 500 XP) | Magic until level 13. Any lamps left over go on Hitpoints. |
| Ides of Milk lamp (1,000 XP) | Hitpoints |
| Lamps on Hitpoints | Confirmed possible (tested in-game) |
| Wind Strike damage | Only the unlock matters. At Magic 13+ Wind Strike's base max hit is 8 (2 at levels 1-4, 4 at 5-8, 6 at 9-12). Cost is 1 air rune and 1 mind rune. |
| Food | Gathered first, on your own route (Visit 0) |
| Minimum HP / combat level gates | Deferred for now |
| Witch's House | All four experiment forms can be safespotted |
| Brutus (Ides of Milk) | Safespot between the feed troughs to the south (from your notes) |

**Lamp arithmetic:** Magic level 13 needs 1,833 XP in total and each lamp is 500, so you need ceil((1,833 - your current Magic XP) / 500) lamps. With no prior Magic XP that is all four.

---

## Itinerary by visit

| Visit | Area | Quests progressed | Result |
|-------|------|-------------------|--------|
| 0 | Ardougne, the Monastery, Witchaven and Brimhaven, then home teleport | Wilderness lever, Hazeel Cult, Sheep Herder, Monk's Friend, Clock Tower, Sea Slug and Tribal Totem, plus shopping and food and silk thieving | Six quests complete, food and supplies stocked, back in Lumbridge |
| 1 | Lumbridge | Mudfoot's Big Adventure and The Ides of Milk, interleaved | Both complete, lamps applied |
| 2 | Taverley | Witch's House | Complete |
| 3 | Baxtorian Falls | Waterfall Quest, Part 1 | Book read |
| 4 | Gnome Maze and Ardougne | Fight Arena and Tree Gnome Village, plus Glarial's pebble | Both complete, pebble in hand |
| 5 | Baxtorian Falls | Waterfall Quest, Parts 3 and 4 | Complete |

Visit 3 comes before the maze because the wiki's Quick Guide lists the pebble after Part 1 and the main route also does Waterfall up to the pebble first. Glarial's pebble is only given at that specific point in Waterfall Quest (confirmed), so Visits 3 and 5 cannot merge into one trip.

---

## Visit 0: Ardougne run (food, XP and supplies)

**Goal:** Reach Ardougne and clear the Wilderness lever first, then earn Thieving XP and gold from [[Hazeel Cult](https://oldschool.runescape.wiki/w/Hazeel_Cult/Quick_guide)] and [[Sheep Herder](https://oldschool.runescape.wiki/w/Sheep_Herder/Quick_guide)], steal food and silk, and complete [[Monk's Friend](https://oldschool.runescape.wiki/w/Monk%27s_Friend/Quick_guide)], [[Clock Tower](https://oldschool.runescape.wiki/w/Clock_Tower/Quick_guide)], [[Sea Slug](https://oldschool.runescape.wiki/w/Sea_Slug/Quick_guide)] and [[Tribal Totem](https://oldschool.runescape.wiki/w/Tribal_Totem/Quick_guide)] on the way. Shop for the later visits, then home teleport to Lumbridge.

**Gold:** Do not count on the 25 gp that may be on the account at spawn. [[Hazeel Cult](https://oldschool.runescape.wiki/w/Hazeel_Cult/Quick_guide)] pays 2,000 gp first, which covers the 100 gp plague suit for [[Sheep Herder](https://oldschool.runescape.wiki/w/Sheep_Herder/Quick_guide)], and [[Sheep Herder](https://oldschool.runescape.wiki/w/Sheep_Herder/Quick_guide)] pays 3,100 gp. Expect a 5,000 gp stack before shopping. Selling 73x silk later returns 4,380 gp.

**Ardougne Easy Diary tasks completed in this visit:** lever (task 8), church altar (task 4), Probita (task 10), cake (task 2) and silk (task 3), so 5/10. The fishing task after [[Sea Slug](https://oldschool.runescape.wiki/w/Sea_Slug/Quick_guide)] is a Medium task (Catch any fish on the Fishing Platform).

- [ ] `0.01` Spawn in Death's Office (in Lumbridge if post-Reset), activate your Escape Crystal to function as a Ring of Life, and equip it in your ring slot
- [ ] `0.02` Bank all items, withdraw the bronze axe, grab 1x log, then go downstairs [[Monk's Friend](https://oldschool.runescape.wiki/w/Monk%27s_Friend/Quick_guide)]
- [ ] `0.03` Take the empty jug from the kitchen and fill it with water [[Monk's Friend](https://oldschool.runescape.wiki/w/Monk%27s_Friend/Quick_guide)]
- [ ] `0.04` Minigame teleport to Soul Wars and leave through the Edgeville portal
- [ ] `0.05` [RISK: Wilderness level 51] Use the Edgeville Wilderness lever to be transported to the Deserted Keep (level 51 Wilderness). This is the riskiest step in the visit, so it goes first, before more time is invested in the account
- [ ] `0.06` [RISK: Wilderness level 51] Pull the Deserted Keep lever straight away and choose Ardougne
- [ ] `0.07` [RISK: Wilderness level 51] Use the Ardougne lever to teleport back to the Deserted Keep (Ardougne Easy Diary, 1/10 tasks completed)
- [ ] `0.08` [RISK: Wilderness level 51] Pull the Deserted Keep lever again and choose Ardougne
- [ ] `0.09` Start [[Hazeel Cult](https://oldschool.runescape.wiki/w/Hazeel_Cult/Quick_guide)]: talk to Ceril Carnillean in East Ardougne, just north of the clock tower
- [ ] `0.10` Complete [[Hazeel Cult](https://oldschool.runescape.wiki/w/Hazeel_Cult/Quick_guide)] in full, siding with Hazeel (detailed steps to be added)

#### Rewards: [[Hazeel Cult](https://oldschool.runescape.wiki/w/Hazeel_Cult/Quick_guide)]
- 1 quest point and 1,500 Thieving XP
- 2,000 gp (plus 5 gp more if you sided with the Carnilleans)
- Hazeel's mark if you sided with Hazeel, or Carnillean armour if you sided with Ceril and obtained an extra piece
- 5 Kudos, claimable from Historian Minas in the Varrock Museum
- **Decision:** Side with Hazeel. This matches the main route (Step 5), the Thieving XP is the same either way, and it avoids the level 13 Alomone fight. Your call, since the choice only changes the item reward.

- [ ] `0.11` Take 4x purple dye from the spawn north of the clock tower, near the spirit tree [[Land of the Goblins](https://oldschool.runescape.wiki/w/Land_of_the_Goblins/Quick_guide)] [[Song of the Elves](https://oldschool.runescape.wiki/w/Song_of_the_Elves/Quick_guide)] [[Recipe for Disaster](https://oldschool.runescape.wiki/w/Recipe_for_Disaster/Quick_guide)] [[Ghosts Ahoy](https://oldschool.runescape.wiki/w/Ghosts_Ahoy/Quick_guide)]
- [ ] `0.12` Start [[Sheep Herder](https://oldschool.runescape.wiki/w/Sheep_Herder/Quick_guide)]: talk to Councillor Halgrive outside the East Ardougne church, then buy the plague suit (100 gp) from Doctor Orbon
- [ ] `0.13` Complete [[Sheep Herder](https://oldschool.runescape.wiki/w/Sheep_Herder/Quick_guide)] in full (detailed steps to be added)

#### Rewards: [[Sheep Herder](https://oldschool.runescape.wiki/w/Sheep_Herder/Quick_guide)]
- 4 quest points and 3,100 gp
- 1,000 Hunter XP
- Ability to hunt goats on Wyrmscraig

- [ ] `0.14` Visit the Ardougne general store and buy the supplies for the later visits (3x rope, 1x water-filled vial pack, 30x balls of wool, 7x papyrus)
- [ ] `0.15` Burn your Prayer point and restore it at the altar in the East Ardougne church (Ardougne Easy Diary, 2/10 tasks completed)
- [ ] `0.16` Check your insured pets with Probita (Ardougne Easy Diary, 3/10 tasks completed)
- [ ] `0.17` Buy 2x silver bar from the Silver Merchant [add which quests need them]
- [ ] `0.18` [RISK: Ardougne guard] [RISK: Hero] [RISK: Paladin] Steal cakes from the Bakery Stall in Ardougne, standing underneath the Baker to avoid detection (Ardougne Easy Diary, 4/10 tasks completed)
- [ ] `0.19` [RISK: Ardougne guard] [RISK: Hero] [RISK: Paladin] Keep stealing from the Bakery Stall until you have banked at least 14x bread [add which quests need these] and as many cakes as you get up to level 20 Thieving, then bank all the food
- [ ] `0.20` [RISK: Ardougne guard] [RISK: Hero] [RISK: Paladin] Steal 84x silk from the Silk Stall (leaves you at about level 23 Thieving, see the notes)
- [ ] `0.21` Run to the Ardougne Monastery and Start [[Monk's Friend](https://oldschool.runescape.wiki/w/Monk%27s_Friend/Quick_guide)]: talk to Brother Omad
- [ ] `0.22` Start [[Clock Tower](https://oldschool.runescape.wiki/w/Clock_Tower/Quick_guide)]: run to the clock tower and talk to Brother Kojo, then go down the ladder and start on the white cog (north-west direction), taking rat poison along the way
- [ ] `0.23` [RISK: Thieves] Continue [[Monk's Friend](https://oldschool.runescape.wiki/w/Monk%27s_Friend/Quick_guide)]: exit the dungeon ladder, head south-west to the stone circle, go down the ladder, run past the thieves and take the child's blanket
- [ ] `0.24` Continue [[Clock Tower](https://oldschool.runescape.wiki/w/Clock_Tower/Quick_guide)]: leave and place the white cog in the clock tower (top floor)
- [ ] `0.25` Continue [[Monk's Friend](https://oldschool.runescape.wiki/w/Monk%27s_Friend/Quick_guide)]: return the blanket to Brother Omad and proceed with the quest
- [ ] `0.26` Continue [[Monk's Friend](https://oldschool.runescape.wiki/w/Monk%27s_Friend/Quick_guide)]: head to Brother Cedric and give him the jug of water and the logs
- [ ] `0.27` [RISK: Dungeon rat] Continue [[Clock Tower](https://oldschool.runescape.wiki/w/Clock_Tower/Quick_guide)]: take the nearby bucket and fill it at the well, then head down the ladder to the north-east and follow the path to the blue cog
- [ ] `0.28` [RISK: Ogres] Continue [[Clock Tower](https://oldschool.runescape.wiki/w/Clock_Tower/Quick_guide)]: climb up the ladder and place the blue cog in the clock tower (second floor), then obtain the black cog (north-east direction, downstairs) and place it (basement), then obtain the red cog (south-east direction, downstairs) and place it on the correct spindle (first floor)
- [ ] `0.29` Complete [[Clock Tower](https://oldschool.runescape.wiki/w/Clock_Tower/Quick_guide)]: talk to Brother Kojo

#### Rewards: [[Clock Tower](https://oldschool.runescape.wiki/w/Clock_Tower/Quick_guide)]
- 1 quest point, 500 gp and 1,000 Firemaking XP

- [ ] `0.30` Complete [[Monk's Friend](https://oldschool.runescape.wiki/w/Monk%27s_Friend/Quick_guide)]: head to the Ardougne Monastery and talk to Brother Omad

#### Rewards: [[Monk's Friend](https://oldschool.runescape.wiki/w/Monk%27s_Friend/Quick_guide)]
- 1 quest point and 2,000 Woodcutting XP
- 8x law rune
- Brother Omad will throw parties for you by speaking to him

- [ ] `0.31` Bank to gain inventory space, then cut and burn logs to level 35 Woodcutting (Firemaking 30 is expected on the way, see the notes)
- [ ] `0.32` Take your gp and a small fishing net, then take the boat to Brimhaven
- [ ] `0.33` Buy 1x swamp paste from Trader Stan [[Sea Slug](https://oldschool.runescape.wiki/w/Sea_Slug/Quick_guide)]
- [ ] `0.34` Buy 7x soda ash, 7x bucket of sand, 1x cake tin and 1x glassblowing pipe from Trader Stan [add which quests need these]
- [ ] `0.35` Start [[Tribal Totem](https://oldschool.runescape.wiki/w/Tribal_Totem/Quick_guide)]: head to Kangai Mau in the Shrimp and Parrot
- [ ] `0.36` [RISK: Sea slug] Start [[Sea Slug](https://oldschool.runescape.wiki/w/Sea_Slug/Quick_guide)]: return to Witchaven and talk to Caroline, north of the town; do not pick up the sea slugs
- [ ] `0.37` [RISK: Sea slug] Complete [[Sea Slug](https://oldschool.runescape.wiki/w/Sea_Slug/Quick_guide)] in full (detailed steps to be added; do not pick up the sea slugs)

#### Rewards: [[Sea Slug](https://oldschool.runescape.wiki/w/Sea_Slug/Quick_guide)]
- 1 quest point and 7,175 Fishing XP
- Access to the Fishing Platform
- Oyster pearls

- [ ] `0.38` Fish an anchovy or shrimp on the Fishing Platform after the quest (Ardougne Medium Diary task, not part of the Easy total)
- [ ] `0.39` Buy 1x raw sardine, 2x fishing rod, 1x fly fishing rod, 1x harpoon, 10x fishing bait and 1x lobster pot from Lovecraft's Tackle in Witchaven [add which quests need these]
- [ ] `0.40` [RISK: Giant rats] [RISK: Zombies] Continue [[Tribal Totem](https://oldschool.runescape.wiki/w/Tribal_Totem/Quick_guide)]: carry on to the point where you collect the totem (investigate the stairs first, because triggering the trap drops you into the Ardougne Sewers)
- [ ] `0.41` Sell 73x silk back to the Silk trader (leave 11x in the bank) for 60 gp each, then sell your oyster pearls to the general store (Ardougne Easy Diary, 5/10 tasks completed)
- [ ] `0.42` [RISK: Jungle spiders] Complete [[Tribal Totem](https://oldschool.runescape.wiki/w/Tribal_Totem/Quick_guide)]: bring your coins, ghostspeak amulet, a spade, 20x balls of wool, the tribal totem and the treasure scroll, then head to Brimhaven

#### Rewards: [[Tribal Totem](https://oldschool.runescape.wiki/w/Tribal_Totem/Quick_guide)]
- 1 quest point and 1,775 Thieving XP
- 5x swordfish

- [ ] `0.43` Home teleport to Lumbridge (optional: minigame teleport to Clan Wars first to restore run energy)

> **Notes:**
> - **Purple dye:** The spawn gives one dye at a time, so 4x means waiting on respawns. Fit this around the quest steps rather than standing still.
> - **Ring of Life:** It does not work in the Wilderness. It is only the safety net for aggressive overworld monsters after the lever steps.
> - **Silk trader:** He refuses to speak to you after you steal from his stall. The Silk stall page says to wait 20 to 30 minutes since the last theft, and the Ardougne Diary page says 10 consecutive minutes outside Ardougne without logging off. Plan for the longer figure and stay logged in. To complete the diary task, first offer to sell your silk for 120 gp, then counter his bid with 60 gp.
> - **Woodcutting and Firemaking:** [[Sea Slug](https://oldschool.runescape.wiki/w/Sea_Slug/Quick_guide)] needs Firemaking 30, and the route does not train it directly. Cutting and burning logs up to Woodcutting 35 is expected to reach Firemaking 30 along the way. Confirm your Firemaking level before starting [[Sea Slug](https://oldschool.runescape.wiki/w/Sea_Slug/Quick_guide)].
> - **Thieving:** You start at 1,500 XP (level 11) after [[Hazeel Cult](https://oldschool.runescape.wiki/w/Hazeel_Cult/Quick_guide)]. Level 20 needs 4,470 XP, so about 2,970 XP of food is needed (186 steals at 16 XP each, counting the cake step). 84x silk at 24 XP each adds 2,016 XP, which ends at about 6,486 XP (level 23). [[Tribal Totem](https://oldschool.runescape.wiki/w/Tribal_Totem/Quick_guide)] needs level 21 and rewards 1,775 XP, taking you to about 8,261 XP (level 25).
> - **Floor numbers:** The [[Clock Tower](https://oldschool.runescape.wiki/w/Clock_Tower/Quick_guide)] steps use US floor numbering (the wiki's first floor is the second floor here).

**Combat table: Visit 0**

| Enemy | Level | Max hit | Safespot / tactic | Food / HP gate |
|-------|-------|---------|-------------------|----------------|
| Wilderness level 51 (Deserted Keep) | n/a | TBD | None. Pull the lever on arrival and do not move. The Ring of Life does not work here | TBD (deferred) |
| Ardougne guard | TBD | 3 | Stand underneath the Baker while stealing | TBD (deferred) |
| Hero | TBD | 9 | Same as the guard | TBD (deferred) |
| Paladin | TBD | 8 | Same as the guard | TBD (deferred) |
| Thieves (stone circle den) | 14 / 14 / 26 | TBD | Run past, do not fight | TBD (deferred) |
| Ogres (red cog room) | 53 | TBD | Run in, pick up the red cog and return to the ladder | TBD (deferred) |
| Dungeon rat (blue cog cell) | TBD | 2 | TBD | TBD (deferred) |
| Sea slug (Fishing Platform) | n/a | 3 (only when picked up) | Do not pick up the sea slugs | TBD (deferred) |
| Giant rats (Ardougne Sewers, 8x) | TBD | 1 | Only met if the staircase trap is triggered | TBD (deferred) |
| Zombies (Ardougne Sewers, 3x) | TBD | 3 | Only met if the staircase trap is triggered | TBD (deferred) |
| Jungle spiders (Brimhaven) | TBD | 6 | TBD | TBD (deferred) |

**Carry-forward after Visit 0:** Escape Crystal (equipped), bronze axe, 4x purple dye, banked bread and cakes, 11x silk (banked), 3x rope, 1x water-filled vial pack, balls of wool left after [[Tribal Totem](https://oldschool.runescape.wiki/w/Tribal_Totem/Quick_guide)], 7x papyrus, 2x silver bar, 7x soda ash, 7x bucket of sand, cake tin, glassblowing pipe, the fishing gear from Lovecraft's Tackle, and the gp left after shopping and sales.

---

## Visit 1: Lumbridge (Mudfoot + Ides of Milk)

- [ ] `1.01` Talk to Captain Harlan outside the Lumbridge General Store to Start [[Mudfoot's Big Adventure](https://oldschool.runescape.wiki/w/Mudfoot%27s_Big_Adventure/Quick_guide)]
- [ ] `1.02` (Optional) Claim the bronze shortsword and wooden shield from Captain Harlan
- [ ] `1.03` Continue [[Mudfoot's Big Adventure](https://oldschool.runescape.wiki/w/Mudfoot%27s_Big_Adventure/Quick_guide)]: cross the River Lum to the building just south of the cow field (first meeting with Mudfoot)
- [ ] `1.04` Continue [[Mudfoot's Big Adventure](https://oldschool.runescape.wiki/w/Mudfoot%27s_Big_Adventure/Quick_guide)]: return to the general store and confront the outlaw roaming outside (cutscene)
- [ ] `1.05` Continue [[Mudfoot's Big Adventure](https://oldschool.runescape.wiki/w/Mudfoot%27s_Big_Adventure/Quick_guide)]: walk north along the road to the chicken field (second meeting, Mudfoot is south of the windmill)
- [ ] `1.06` Talk to Cassius at the Lumbridge pond, just south of the windmill, to Start [[The Ides of Milk](https://oldschool.runescape.wiki/w/The_Ides_of_Milk/Quick_guide)]
- [ ] `1.07` [RISK: Ranger outlaw] Continue [[Mudfoot's Big Adventure](https://oldschool.runescape.wiki/w/Mudfoot%27s_Big_Adventure/Quick_guide)]: kill the ranger outlaw and loot the shortbow and bronze arrows
- [ ] `1.08` Continue [[The Ides of Milk](https://oldschool.runescape.wiki/w/The_Ides_of_Milk/Quick_guide)]: talk to Gillie Groats in the cow field, just north of the entrance (option 3)
- [ ] `1.09` Continue [[The Ides of Milk](https://oldschool.runescape.wiki/w/The_Ides_of_Milk/Quick_guide)]: talk to Seth Groats in the farmhouse by the chicken coop, north-west of the cow field, and search the shelves on the south wall for The groats principles
- [ ] `1.10` Continue [[The Ides of Milk](https://oldschool.runescape.wiki/w/The_Ides_of_Milk/Quick_guide)]: return the book to Cassius for a milk sample, drink it in front of him, then talk to him again for a second sample
- [ ] `1.11` Continue [[The Ides of Milk](https://oldschool.runescape.wiki/w/The_Ides_of_Milk/Quick_guide)]: talk to Duke Horacio upstairs in Lumbridge Castle about the permit

> **Hold:** Do not return to Gillie yet. Drinking her sample leads to the Brutus fight, which waits until Mudfoot's staff and runes are in hand.

- [ ] `1.12` [RISK: Mage outlaw] Continue [[Mudfoot's Big Adventure](https://oldschool.runescape.wiki/w/Mudfoot%27s_Big_Adventure/Quick_guide)]: kill the mage outlaw by the H.A.M. hideout and loot the staff and runes
- [ ] `1.13` Keep the staff and the 80x air runes and 80x mind runes (Wind Strike ammunition) [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)] [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)] [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]
- [ ] `1.14` [RISK: Final outlaw] Continue [[Mudfoot's Big Adventure](https://oldschool.runescape.wiki/w/Mudfoot%27s_Big_Adventure/Quick_guide)]: kill the final outlaw at the Lumbridge graveyard, south-east of the hideout, with Magic or Ranged gear (or poison)
- [ ] `1.15` Complete [[Mudfoot's Big Adventure](https://oldschool.runescape.wiki/w/Mudfoot%27s_Big_Adventure/Quick_guide)]: report to Captain Harlan at the general store

#### Rewards: [[Mudfoot's Big Adventure](https://oldschool.runescape.wiki/w/Mudfoot%27s_Big_Adventure/Quick_guide)]
- 1 quest point and 500 gp
- Shortbow and 80x bronze arrows, staff and 80x mind runes and 80x air runes, iron scimitar and iron kiteshield
- 4x antique lamps (500 XP each, any combat skill)
- **Decision:** Magic until level 13 (1,833 XP in total), any remaining lamps on Hitpoints. At Magic 13 Wind Strike hits for up to 8.

- [ ] `1.16` Use the Mudfoot antique lamps as decided above
- [ ] `1.17` Continue [[The Ides of Milk](https://oldschool.runescape.wiki/w/The_Ides_of_Milk/Quick_guide)]: return to Gillie Groats and drink the milk sample when prompted
- [ ] `1.18` [RISK: Brutus] Continue [[The Ides of Milk](https://oldschool.runescape.wiki/w/The_Ides_of_Milk/Quick_guide)]: open the gate north-east of Gillie and fight Brutus from the safespot between the feed troughs to the south
- [ ] `1.19` Continue [[The Ides of Milk](https://oldschool.runescape.wiki/w/The_Ides_of_Milk/Quick_guide)]: speak to Gillie about the bull, then confront Cassius at the pond
- [ ] `1.20` Complete [[The Ides of Milk](https://oldschool.runescape.wiki/w/The_Ides_of_Milk/Quick_guide)]: return to Gillie Groats for the additional rewards

#### Rewards: [[The Ides of Milk](https://oldschool.runescape.wiki/w/The_Ides_of_Milk/Quick_guide)]
- 1 quest point and access to Brutus (repeatable cow boss)
- Cowbell amulet: faster milking, a teleport to the Lumbridge cow field (1 air rune per charge, up to 1,000, not past level 20 Wilderness), and a Brutus respawn ring
- 1x magic lamp (1,000 XP, any combat skill)
- **Decision:** Put the lamp on Hitpoints. Recommendation for the amulet: charge it sparingly, because the same air runes are your Wind Strike ammunition.

- [ ] `1.21` Use the Ides of Milk magic lamp on Hitpoints
- [ ] `1.22` Grab 6x logs [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)] (chop them, or bring an axe instead)
- [ ] `1.23` Keep 5x coins [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)] for the Khali brew
- [ ] `1.24` Keep 1x rope [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)] (bought in Visit 0 from the Ardougne general store)
- [ ] `1.25` Buy 6x air runes, 6x earth runes and 6x water runes [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)] from Aubury's rune shop in Varrock (route placement to be decided)
- [ ] `1.26` Grab 1x leather gloves [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)] (the main route's Step 3 takes them from Father Urhney's house in Lumbridge Swamp)

**Combat table: Visit 1**

| Enemy | Level | Max hit | Safespot / tactic | Food / HP gate |
|-------|-------|---------|-------------------|----------------|
| Ranger outlaw | 6 | not listed | none listed | TBD (deferred) |
| Mage outlaw | 6 | not listed | none listed | TBD (deferred) |
| Final outlaw | 8 | not listed | Uses Protect from Melee after your first hit, so bring Magic or Ranged. Very low levels can run around the graveyard until it aggros Mudfoot instead. | TBD (deferred) |
| Brutus | not listed | specials up to 19, cannot be prayed against | Feed-trough safespot to the south (from your notes, unverified) | TBD (deferred) |

**Carry-forward after Visit 1:** staff, 80x air runes, 80x mind runes, 6x logs, 5x coins, 1x rope, 6x air runes, 6x earth runes, 6x water runes, 1x leather gloves, food from Visit 0.

**Overlap with main-route Steps 1 and 2:** Duke Horacio (Step 1, Rune Mysteries) and the general store (Step 2 purchases) are in the same places as this visit. Fold those errands in when the blocks are merged.

---

## Visit 2: Taverley (Witch's House)

- [ ] `2.01` Grab 2x cheese [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)] (one spare) from Aggie in Draynor Village, on the way west
- [ ] `2.02` Talk to the Boy south-east of the long garden in Taverley, next to the members gate, to Start [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]
- [ ] `2.03` Continue [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]: walk west, then north, to the Witch's house front door and search the potted plant closest to the door for the key
- [ ] `2.04` Continue [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]: enter, read the diary on the table, then climb down the ladder to the north
- [ ] `2.05` Continue [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]: equip the leather gloves and open the gate (search the boxes for gloves if you have none)
- [ ] `2.06` Continue [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]: search the cupboard for a magnet, climb the ladder and go to the small southern room
- [ ] `2.07` Continue [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]: drop cheese to lure out a mouse, then use the magnet on the mouse
- [ ] `2.08` Continue [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]: cross the garden to the fountain without being caught by the Witch (use the hedges, do not walk on the grass, keep full run energy)
- [ ] `2.09` Continue [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]: check the fountain, then use the key on the shed door on the east side. Do not take the ball yet
- [ ] `2.10` [RISK: Witch's experiment] Continue [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]: kill the experiment in all four forms (fleeing resets to form 1)
- [ ] `2.11` Continue [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]: take the ball and leave by teleport or through the garden and front door
- [ ] `2.12` Complete [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]: give the ball to the Boy

#### Rewards: [[Witch's House](https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide)]
- 4 quest points and 6,325 Hitpoints XP (fixed, no decision)
- Unlocks the Witch's experiment in the Nightmare Zone, which is an unsafe activity on Hardcore Worlds, so skip it
- Required later for Recipe for Disaster and Grim Tales

**Combat table: Visit 2** (combined experiment HP is 144)

| Enemy | Level | Max hit | Safespot / tactic | Food / HP gate |
|-------|-------|---------|-------------------|----------------|
| Witch's experiment, form 1 (Skavid) | 19 | not listed | Step under it from the north-eastern corner until it moves north, then Magic from one tile south-west | TBD (deferred) |
| Witch's experiment, form 2 (spider) | 30 | not listed | Same as form 1 | TBD (deferred) |
| Witch's experiment, form 3 (bear) | 42 | not listed | Safespot from the south of the shed, past the ball | TBD (deferred) |
| Witch's experiment, form 4 (wolf) | 53 | not listed | Same as form 3 | TBD (deferred) |

**Carry-forward after Visit 2:** staff, 80x air runes, 80x mind runes, 6x logs, 5x coins, 1x rope, 6x air runes, 6x earth runes, 6x water runes, food.

---

## Visit 3: Baxtorian Falls, Part 1

- [ ] `3.01` Talk to Almera in her house north-east of Baxtorian Falls (choose "How can I help?") to Start [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]
- [ ] `3.02` Continue [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: board the raft west of her house
- [ ] `3.03` Continue [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: talk to Hudon and go through all of his dialogue, or the book will not spawn
- [ ] `3.04` Continue [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: walk to the southern end of the island and swim in the water, then enter the large building to the north (Hadley)
- [ ] `3.05` Continue [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: go upstairs and search the southernmost bookcase on the eastern wall for the Book on Baxtorian, then read it and close it

**Carry-forward after Visit 3:** staff, 80x air runes, 80x mind runes, 6x logs, 5x coins, 1x rope, 6x air runes, 6x earth runes, 6x water runes, food.

---

## Visit 4: Gnome Maze and Ardougne

- [ ] `4.01` Make sure you have 2 empty inventory slots, then talk to Lady Servil just outside the north-east corner of the Gnome Maze (choose "Can I help you?") to Start [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]
- [ ] `4.02` Talk to King Bolren in the centre of the Gnome Maze (choose "I would be glad to help.") to Start [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)]. Starting it lets you follow Elkoy through the maze
- [ ] `4.03` Continue [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: enter the dungeon at the end of the maze, search the off-coloured crate in the east room for a key, unlock the gate in the west room, and talk to Golrie to receive Glarial's pebble
- [ ] `4.04` Keep Glarial's pebble [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)] (talk to Golrie again if you lose it)
- [ ] `4.05` Continue [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)]: talk to Commander Montai (red hat) at the south-west edge of the battlefield, south of the river (choose "Ok, I'll gather some wood.")
- [ ] `4.06` Continue [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)]: give Commander Montai the 6x logs, then talk to him a third time (choose "I'll try my best.")
- [ ] `4.07` Continue [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)]: talk to the three tracker gnomes (tracker 2 in a building on the east side of the Khazard Stronghold, tracker 1 north-west of it, tracker 3 in its south-west corner). Tracker 3 gives the ballista coordinates
- [ ] `4.08` Continue [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)]: fire the ballista in the south-west corner of the battlefield, past the bridge, and enter the coordinates
- [ ] `4.09` Continue [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)]: climb over the crumbled wall at the stronghold north of the village (ignore or kill the Khazard commanders), climb the ladder, search the chest, and take the first orb of protection
- [ ] `4.10` Continue [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)]: leave by the front door, talk to Elkoy, then to King Bolren (choose "I will find the warlord and bring back the orbs.")
- [ ] `4.11` [RISK: Khazard warlord] Continue [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)]: find the warlord north-west of the battlefield, below West Ardougne, and kill him for the remaining orbs
- [ ] `4.12` Complete [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)]: return the orbs to King Bolren

#### Rewards: [[Tree Gnome Village](https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide)]
- 2 quest points and 11,450 Attack XP (fixed, no decision)
- Spirit tree transport and the gnome amulet
- Unlocks the Khazard warlord in the Nightmare Zone, which is an unsafe activity on Hardcore Worlds, so skip it

- [ ] `4.13` Continue [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]: search the chest in the house in the far north-east of the area for the Khazard armour, equip it, and go south into the prison (keep it on inside)
- [ ] `4.14` Continue [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]: enter the south-east room with the jails and talk to the Head Guard in the southernmost jail room, near the staircase. Skipping this removes the Khali brew option later
- [ ] `4.15` Continue [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]: leave the arena, go to the western bar, and buy a Khali brew for 5 coins from the Khazard Barman
- [ ] `4.16` Continue [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]: return to the jail and talk to the guard for the keys, then use the keys on Sammy's cell door (the most north-eastern cell)
- [ ] `4.17` [RISK: Khazard ogre] Continue [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]: kill the Khazard ogre (talk to Justin if the fight does not start)
- [ ] `4.18` [RISK: Khazard scorpion] Continue [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]: talk to your cellmate Hengrad and kill the Khazard scorpion
- [ ] `4.19` [RISK: Bouncer] Continue [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]: kill the Bouncer
- [ ] `4.20` (Optional) [RISK: General Khazard] Continue [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]: kill General Khazard, or skip him by running through the south-east door of the arena or north until he stops being aggressive
- [ ] `4.21` Complete [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]: return to Lady Servil

#### Rewards: [[Fight Arena](https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide)]
- 2 quest points, 12,175 Attack XP and 2,175 Thieving XP (fixed, no decision)
- 1,000 gp and the Khazard armour set
- Unlocks the Bouncer in the Nightmare Zone, which is an unsafe activity on Hardcore Worlds, so skip it

**Combat table: Visit 4**

| Enemy | Level | Max hit | Safespot / tactic | Food / HP gate |
|-------|-------|---------|-------------------|----------------|
| Khazard warlord | 112 | not listed | Start the fight, walk west until he de-aggros near the large dead tree, step slightly south and attack from outside his aggro range. He gets caught between the West Ardougne wall and the northern dead tree. Melee: step in and out of his range beside the large skull to the south. | TBD (deferred) |
| Khazard ogre | 63 | not listed | Safespot behind a nearby skeleton with Magic, Ranged or a halberd | TBD (deferred) |
| Khazard scorpion | 44 | not listed | Run to the safespot or use Protect from Melee at once | TBD (deferred) |
| Bouncer | 137 | not listed | Same approach as the scorpion. Once the General Khazard fight starts you cannot re-enter the arena | TBD (deferred) |
| General Khazard | 142 | not listed | Magic safespot (wiki image caption), or skip him | TBD (deferred) |

**Carry-forward after Visit 4:** Glarial's pebble, 1x rope, 6x air runes, 6x earth runes, 6x water runes, staff, spare Wind Strike runes, food.

---

## Visit 5: Baxtorian Falls, Parts 3 and 4

- [ ] `5.01` Bank everything except Glarial's pebble, food and a transport method [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)] (2 free slots, no runes allowed in the tomb)
- [ ] `5.02` [RISK: Moss Guardians] Continue [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: use the pebble on Glarial's Tombstone, east of the waterfall, and start a fight with a skeleton inside to keep the guardians off you
- [ ] `5.03` Continue [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: go west and search the chest for Glarial's amulet (drop and pick it up again if you need extras), then go the other way and search the tomb for Glarial's urn
- [ ] `5.04` Bank, then withdraw the rope, the 6x air, 6x water and 6x earth runes, Glarial's amulet, Glarial's urn and food [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)] (weapons and armour are allowed in the dungeon)
- [ ] `5.05` Continue [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: board the raft, use the rope on the rock across the water to the south, then on the dead tree. Do not enter the barrel
- [ ] `5.06` [RISK: Fire Giants] Continue [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: with Glarial's amulet carried or equipped, enter the doorway, take the right path and search the northernmost crates for a key
- [ ] `5.07` Continue [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: return to the left side, avoid the fire giants, and use the key on the door
- [ ] `5.08` Continue [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: in the chalice room place 1x air rune, 1x water rune and 1x earth rune on each pillar, then put Glarial's amulet on her statue
- [ ] `5.09` Complete [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]: do not click "Take treasure" (it washes you out). Use Glarial's urn on the chalice with 5 free inventory slots

#### Rewards: [[Waterfall Quest](https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide)]
- 1 quest point, 13,750 Attack XP and 13,750 Strength XP (fixed, no decision)
- 2x diamonds, 2x gold bars and 40x mithril seeds

**Combat table: Visit 5**

| Enemy | Level | Max hit | Safespot / tactic | Food / HP gate |
|-------|-------|---------|-------------------|----------------|
| Moss Guardians | 84 | 14 | Glarial's Tomb is single-way combat, so start a fight with a skeleton first | TBD (deferred) |
| Fire Giants | 86 | not listed | Avoid the left side and slip past without engaging. Killing one counts toward a medium Kandarin diary task | TBD (deferred) |

---

## Alternative order (safety over space)

Do Waterfall's combat part before the harder Gnome Maze fights: Visit 3, then a short maze trip for the Tree Gnome Village start and the pebble only, then Visit 5, then back to the maze for the Tree Gnome Village finish and Fight Arena. Waterfall's recommended level (25) is lower than Tree Gnome Village (45) and Fight Arena (50). The cost is an extra round trip, and it breaks the single maze visit in Visit 4.

---

## Rough stat outcome (approximate)

- **Attack:** 11,450 + 12,175 + 13,750 = 37,375 XP, about level 40.
- **Strength:** 13,750 XP, about level 30.
- **Hitpoints:** 1,154 base + 1,000 (Ides lamp) + 6,325 (Witch's House) = 8,479 XP, about level 25, before any XP from fights.
- **Magic:** level 13 from the Mudfoot lamps (Wind Strike max hit 8).
- **Thieving:** 1,500 XP from Hazeel Cult plus 2,175 XP from Fight Arena, on top of the cake food run.

These figures come from the standard XP table and exclude anything else you earn on the way.

---

## Hardcore Worlds check

- None of these quests is on the wiki's unsafe-activity list, but a death during any quest is still a real death.
- Witch's House, Tree Gnome Village and Fight Arena each unlock a Nightmare Zone encounter. The Nightmare Zone is an unsafe activity, so skip those unlocks.
- The Hardcore Worlds page lists no quest changes. These quests are assumed to behave normally.

---

## Open items

1. **Food route:** Detailed steps and quantity (being drafted).
2. **Rune supply:** Wind Strike costs 1 air and 1 mind rune per cast. Mudfoot's package gives 80x of each. Killing the Witch's experiment (144 HP combined) takes at least 18 max-damage hits, and the warlord (170 HP) at least 22, so real fights will need more casts than that.
3. **Item sources:**
   - **Rope:** Resolved. Bought in Visit 0 at the Ardougne general store (step `1.24` now keeps it).
   - **Waterfall runes (6x air, 6x earth, 6x water):** Bought at Aubury's rune shop in Varrock, the only feasible source. Still to decide: where the Varrock stop sits in the route (step `1.25` is a placeholder, and the carry-forward lines for Visits 1 to 3 still list the runes), and the cash budget.
   - **Leather gloves:** Step `1.26` takes them from Father Urhney's house in Lumbridge Swamp (the Restless Ghost area), but Step `2.05` says Witch's House has gloves in its boxes. Still to check whether the gloves are needed at that point. If not, drop `1.26` and the glove entry in Visit 1's carry-forward.
4. **Pebble prerequisite:** Resolved. The pebble is only given at that specific point in Waterfall Quest, so the Visit 3, 4, 5 order stands.
5. **Trough safespot:** From your notes. It was not on the wiki pages I read, so confirm it works before relying on it at low HP.
6. **Combat gates:** Minimum HP and combat level per fight (deferred).
7. **Merge with the main route:** How Steps 1 and 2 combine with Visit 1, and how Visit 0 sits next to Step 1.

---

## Sources

- Mudfoot's Big Adventure quick guide: https://oldschool.runescape.wiki/w/Mudfoot%27s_Big_Adventure/Quick_guide
- The Ides of Milk quick guide: https://oldschool.runescape.wiki/w/The_Ides_of_Milk/Quick_guide
- Hazeel Cult quick guide: https://oldschool.runescape.wiki/w/Hazeel_Cult/Quick_guide
- Witch's House quick guide: https://oldschool.runescape.wiki/w/Witch%27s_House/Quick_guide
- Waterfall Quest quick guide: https://oldschool.runescape.wiki/w/Waterfall_Quest/Quick_guide
- Tree Gnome Village quick guide: https://oldschool.runescape.wiki/w/Tree_Gnome_Village/Quick_guide
- Fight Arena quick guide: https://oldschool.runescape.wiki/w/Fight_Arena/Quick_guide
- Cowbell amulet: https://oldschool.runescape.wiki/w/Cowbell_amulet
- Wind Strike: https://oldschool.runescape.wiki/w/Wind_Strike
- Glarial's pebble: https://oldschool.runescape.wiki/w/Glarial%27s_pebble
- Hardcore Worlds: https://oldschool.runescape.wiki/w/Hardcore_main
