# Round 3 charter: the twin with our network's head start (written 11:10 PT, 29 Sept 2026, before any run; hard stop 12:10)

## The one change
Our network (FW) starts every run with its erase gate almost shut (bias −5: it fades 0.67% per tick), so its board **holds by default** from the first tick. That setting was chosen by hand on night one. The twin in rounds 1 and 2 started with its hold gate half open (bias 0: it throws away half its value every tick), so it had to learn to hold before it could learn anything else. Round 3 gives the twin the same head start: hold-gate bias −5 (it keeps 99.24% per tick at the start, measured). Nothing else changes: same grading (last-10 s distance plus the erase charge), same exam, same curriculum (10 → 20 → 30 s, promotion under 1.5 or 1,500 iterations per stage, 4,000 in all), same batch, same world, same cosine decay, seeds 0 to 2. FW is not retrained: its three cold runs from this morning (fw_c0 to fw_c2: 1.86, 5.23, 2.60) used exactly this recipe at rate 1e-3, so they are the matched opponent.

Why this is fair and not a thumb on the scale: it removes an asymmetry in starting settings that favoured FW, and it is standard practice for gated networks (LSTM forget gates are started at "remember" for this reason, Jozefowicz et al. 2015).

## Runs (12, all cold, 4,000 iterations)
- **TWIN-hold** (primary): bias −5, rates 1e-3 and 3e-4, seeds 0 to 2.
- **TWIN-hold3** (secondary): bias −3 (keeps 95.3% per tick at the start), rate 1e-3, seeds 0 to 2. Run because −5 leaves the gate on the flat end of its sigmoid, the "deaf gate" FW itself suffered from on night one.
- **GRU-hold** (reference): update gate started at "keep" (+5), rate 1e-3, seeds 0 to 2.
The twin is judged at its best of the three settings (lowest mean standard-exam score), which favours the rival, as every amendment today did.

## Verdict (same rule as the charter)
Cold pair, FW-cold against the best TWIN-hold setting, on the standard exam, longer trips, drift and the long stop: means differ by at least 0.2 with no overlap = better; at least 0.2 with overlap = leans; else tie. Trainability: how many seeds pass each stage by learning (promotion before the cap).

## Predictions
- The head start helps: at least one twin setting passes the 10 s stage by learning on at least 2 of 3 seeds. 55%.
- If it learns, the twin ties FW-cold on the standard exam (FW-cold's three seeds span 1.86 to 5.23, so ties are easy to get). 50%.
- If it learns, the twin pays less than FW for the 30 s stop. 65%.
- GRU-hold learns on at least 1 of 3 seeds. 50%.

## Timeline
11:10 launch · ~11:40 training done · 11:40 to 11:50 exam and probe · 11:50 to 12:05 page section, narrative, commit, republish.

## Amendment 11:15 · the split twin
Looked inside at iteration 700: all twelve runs were at chance, and training had pulled the twin's hold gate open (from 0.0076 to 0.23 on average) while the network turned hard (mean |turn| 5.8 on the return): the head start was undone. The reason is structural. FW has two kinds of parts: 64 fast neurons that update fully every tick (they follow the heading) and a slow board that holds the count. The twin has one population that must do both; started all-slow it cannot follow the heading, so training opens the gates, and the store with them. Added **TWIN-split**: the same twin, same size (9,027 trained numbers), with 32 neurons starting fast (hold-gate bias +5, updating 99.3% per tick, like FW's neurons) and 32 starting slow (bias −5, keeping 99.3% per tick, like FW's board). Rates 1e-3 and 3e-4, seeds 0 to 2, same recipe. This is the closest structural twin of FW that holds its memory in activity. The twin arm is judged at its best setting across TWIN-hold, TWIN-hold3 and TWIN-split. Prediction: TWIN-split passes the 10 s stage by learning on at least 2 of 3 seeds at one rate. 50%.

## Result (11:55)
0 of 18 rival runs learned to home (best standard-exam score 4.86, worse than a fly that never steers at 4.38); 1 of 18 clearly learned the 10 s stage (running score 1.69 against 2.31 for chance) without meeting the 1.5 promotion bar. FW from scratch, same recipe: 1.86, 5.23, 2.60. Cold-pair verdict by rule: FW better on every level (see the page). Predictions: head start helps, wrong; GRU learns, wrong; stop and tie, untestable.
