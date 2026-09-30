# Round 6 charter: the fly's task as a test bed for frontier memories (29 Sept 2026, 16:08 PT; stop 18:45)

## Why
The essay's closing point is that a fast-weight memory (a table rewritten every step) is easy to learn because the
rule builds the memory and training only switches it on. The frontier of sequence models (gated linear attention,
Mamba, DeltaNet, Titans) is a family of such memories that differ in their rewrite rule. This round puts small,
faithful versions of their MEMORY RULES into FW's own skeleton and asks three questions on our task, under identical
conditions. All are single-layer, ~9,000-parameter versions (level4/frontier.py); they are "X-style rules", not X.

| design | memory form | rule | params | state numbers |
|---|---|---|---|---|
| fw_hebb (FW) | board, tied key/value | add | 8,708 | 4,160 |
| fw_blend | board, tied | per-tick beta between add and add-the-surprise, starts at exactly add | 8,773 | 4,160 |
| fw_delta | board, tied | add the surprise (delta) + eraser | 8,708 | 4,160 |
| kvq_hebb | 16x16 table, learned key/value/query | add + forget (gated linear attention, Mamba-2) | 8,707 | 320 |
| kvq_gdelta | same | surprise + forget (Gated DeltaNet) | 8,707 | 320 |
| kvq_delta | same | surprise, no forget (DeltaNet) | 8,707 | 320 |
| kvq_titans | same | surprise with momentum + forget (Titans-style) | 8,708 | 320 |
| mamba | 64 x 16 decaying numbers | selective state space (Mamba-1 style) | 8,227 | 1,088 |
| transformer | every past step | one layer of causal softmax attention, fixed sine positions | 8,737 | grows with the trip |
| twin, gru | activity | hold gate / GRU | 9,027 / 9,101 | 64 / 52 |

Build fixes before launch: blend starts at exactly beta = 0 (even beta 0.05 breaks run 41: 1.49 -> 5.50); transformer
uses fixed sine positions (a learned table made it 95k parameters); Mamba's selection sees input and activity;
Titans' momentum is an average (plain momentum exploded: effective step ~6). FWRule('hebb') reproduces run 41 (1.491).

## E1 - which designs can be discovered from our grade? (learnability)
10 s stage, cold, 1,200 iterations, step 1e-3 cosine, round-5 recipe, 4 starts. Baselines reused: FW 3/5, twin 0/5.
"Learned" = frozen 10 s exam below 2.39.
**Forecast from the round-5 rule** ("learns iff a working memory is present or one knob away"), using each untrained
design's memory at the turn (R^2, r6_untrained.json): fw_blend 0.99, fw_delta 0.76, kvq_gdelta 0.80, kvq_delta 0.75,
transformer 0.76 -> predicted to learn on at least 1 of 4 each; mamba 0.56 and kvq_titans 0.55 -> uncertain;
kvq_hebb 0.14 -> predicted 0 of 4 unless its write switches on like FW's (one knob). Rule counts as a success if designs
above 0.7 learn at a clearly higher rate than designs below 0.3.

## E2 - which memory is better once learning is easy? (memory benchmark)
bench.py: each design + readout trained to report the home vector every tick of 30 s walks (no steering, no trap),
1,500 iterations, 3 starts; frozen tests on 500 walks: 30/60/90 s, a 30 s stop, drift 0.15. Predictions: delta-rule
tables beat add-rule ones on the stop and at 90 s (55%); the transformer is best at 30 s but degrades beyond its training
length (60%); FW-hebb degrades with length because of its fade (70%).

## E3 - can a rule change improve our best score? (score push)
Warm from runs 28, 40, 41, 45, 800 iterations at 30 s with their own recipe, full exam. Arms: fw_blend; per-neuron forget
(erase_rows); a direct read path to the turn (direct_read); and a CONTROL that just continues training (fw_hebb), so
any gain is measured against more training, not against the old networks. Success: an arm beats the control by >= 0.2
with no overlap. Prediction: at most one arm succeeds (70%); beta stays near 0 (70%).

## Rules
One queue, 13 runs at a time. Everything reported, failures included. Pre-registered versus exploratory marked in the
write-up. If behind at 17:30: stop E1 at 3 starts, drop the weakest E3 arm.

## Amendment 16:35 (exploratory, after the first E2 results)
The gated-linear-attention table (kvq_hebb) learned nothing even with a teacher. Probe: its table overflows (mean |S| 4.1 by 30 s; its read is ~4x the network's own recurrent input), while the delta table stays small (0.07): the add rule needs a limit and the delta rule brings its own. Added kvq_hebbl = kvq_hebb with FW's two safeguards (write strength 0.1, lid +-1), 3 starts in E2 and 4 in E1. Marked exploratory.

## Amendment 16:40 (exploratory): making FW-delta work from first principles
Nico: "I don't think FW-delta can't work." Two first-principles repairs, each testing one reason it might fail:
1. Stability. A delta write is stable only if step x |key|^2 < 2 (DeltaNet normalises keys for this). FW's tied key is the whole activity (|x|^2 ~ 32), so ws x write x |x|^2 ~ 0.1 x 0.73 x 32 = 2.3: every write overshoots (the benchmark error of fw_delta grew from 38 to 50). fw_deltan scales the key to length 1.
2. Counting. Delta writes (value - read) x key. If the value already carries the board's read plus the new step, the surprise written is exactly the step, and delta counts like Hebb. FW's value (the new activity) contains the read weighted by the table A; fw_deltanA starts A at 1 so the read flows fully into the value ("one knob away" again).
Prediction: fw_deltan learns some (stable) but still under-counts on long walks; fw_deltanA counts and approaches FW-Hebb in the benchmark (50%).

## Amendment 16:48 (exploratory, follows the E2 result): E4, does the best memory also home better?
E2 (so far): kvq_hebbl (add rule, learned key/value/query, FW's write strength and lid) is the best path integrator at every test (30 s 0.72 vs FW 1.78; 90 s 6.57 vs 9.10; stop 2.13 vs 3.70), with 320 state numbers against FW's 4,160. E4 trains it on homing through the full curriculum from scratch (10 -> 20 -> 30 s, up to 1,500 per stage, 4,000 in all; step 1e-3 cosine; round-3 cold recipe): 4 starts on the normal grade, 2 with the teacher (x0.1). Compared with FW-cold (1.86, 2.60, 5.23) and FW's best warm networks (1.56) on the full level-4 exam. Prediction: it learns 30 s on at least 2 of 4 starts (55%) and at least one start beats 1.56 (35%).
E1 trimmed to 3 starts per design at 16:49 to protect the write-up time.

17:25 kvq_hebbli (exploratory): hebbl born as a 16x16 FW board (identity key/value/query/read). Question: does the best memory become learnable when a working memory is one knob away at birth? E1 seeds 0-3 + bench s0, launched directly (outside the queue).
17:28 kvq_hebbli withdrawn before training. Born as a 16 x 16 FW board (key, value, query = the first 16 neurons, read back
into them) its board ran away at birth: 100% of cells at the lid, home vector R^2 ~0. With the read starting at zero the
lid fraction fell to 7-17% but it still held nothing (R^2 -0.1 to 0.02, 2,000 flies). Not run; too late to find the
right birth wiring. Probe note: for 256-cell boards the untrained R^2 depends on the ridge strength (kvq_gdelta 0.80 at
lambda 0.01 vs 0.01-0.04 at lambda 1-10), so the untrained-R^2 forecast for the key-value designs is not trustworthy.
17:19 E4 stopped to free cores for E1 (graded from each run's iteration-1,400 checkpoint, the end of its 10 s stage):
plain 0 of 4 learned (2.92-2.94, spinning; all four left the 10 s stage by the 1,500-iteration limit, not by passing);
with the teacher 1 of 2 (1.91, passed at iteration 1,430; the other 2.66).
17:40 (exploratory, while E1 ran): the transformer is learning at 10 s from the score alone (s0 running 1.21, s1 1.66).
Check of why: untrained, its ACTIVITY at 10 s already carries the home vector (R^2 0.79-0.82) and the home direction
(0.83-0.84), as FW's does (0.77-0.78) and the twin's does not (0.38-0.39). Likely mechanism (not isolated): attention with
small random weights is close to an even average over the whole trip's list, and the average of the steps taken is the
direction of travel, i.e. minus the way home. A working memory present at birth, as the round-5 rule requires.

## Results (18:10) - details in narrative.md, numbers in r6_results.json
E1: transformer 3/3; fw_blend 1/3; all key-value tables, delta forms, Titans-style, Mamba 0/3 (hybrid 0/4); kvq_hebb overflowed.
Forecast (store R^2 > 0.7 learns at >= 1 of 4): right for fw_blend and transformer, wrong for fw_delta, kvq_gdelta, kvq_delta.
E2 predictions: delta beats add on stop and 90 s - wrong; transformer best at 30 s, degrades beyond - second best, degrades (half);
FW degrades with length - right. E3: no arm beat control (prediction "at most one" right; beta ~0 right). E4: 0/4 plain,
1/2 with teacher (prediction "learns 30 s on >= 2 of 4" wrong).

## After round 6: the dial (Path 1), written 20:14, before any training
Question: does the birth signal CAUSE learnability? Set it on purpose inside one design and count who learns (10 s stage,
1,200 iterations, round-5/6 recipe, 4 starts each; learned = exam10 < 2.39). Birth signals measured first (dial_probe.json):
transformer with query/key weights x3 at birth: 0.70-0.79; x12: 0.54-0.65 (normal x1: 0.82-0.84, learned 3/3).
twin with 2 hand-wired counters: 0.58-0.61; with 4: 0.83 (0 counters: 0.36-0.40, learned 0/5; 16: 0.83, learned 2/5).
Predictions from the 0.7 rule: transformer x3 learns on >= 2 of 4; transformer x12 learns on <= 1 of 4 (unless training
undoes the sharpening early, which the within-reach measure at iterations 100-200 would show); twin k=2 learns 0 of 4;
twin k=4 learns about as often as k=16 (1-3 of 4). Confirmation = the two within-design contrasts go the predicted way.

## Path 4, the running-sum birth for the lid hybrid (written 20:17, before training)
kvq_hebblc3: kvq_hebbl whose key and query layers get a bias, set at birth to 3 on one shared coordinate (32 extra numbers,
8,740 in all). Every key then starts nearly the same, so a read returns roughly the sum of all values written: a running
total from birth, the trick that makes the untrained transformer point home. Birth signal 0.80-0.81 (plain hybrid 0.51-0.59;
c=1 0.75-0.81, c=10 0.79-0.80). Predictions: it learns 10 s homing on >= 3 of 8 starts (plain hybrid 0 of 4); on the memory
test it stays within 0.3 of the plain hybrid's 0.73 at 30 s (keys are still free to learn). Both true = the best memory made
findable by changing only its start.
Wave 2 (20:23): transformer x6 (birth 0.58-0.69), 4 starts; transformer x1 (normal) 2 more starts (s3, s4); control
kvq_hebblc0 = the same 32 extra numbers started at zero (birth signal as the plain hybrid), 4 starts. Prediction: control
learns 0-1 of 4, so any rescue by hebblc3 is due to the running-sum start, not the extra numbers. Path 2 (race.py) early
result: turning share and a turn-vs-ideal alignment at iterations 0-200 do not separate learners from failures among the
24 within-reach runs (spin 0.04 vs 0.03 at birth, 0.50 vs 0.44 at 100); they separate only late (0.50 vs 0.67 at 600).
20:28 dial, twin results: k=2 (birth 0.60-0.64) 0 of 4 learned (predicted 0: right); k=4 (birth 0.82-0.83, as high as
k=16) 0 of 4 (predicted 1-3: WRONG). Same birth signal, different outcome: the direction readout does not capture what the
16-counter twin has. Added (exploratory): k=8 x 4 starts and k=16 x 4 more starts (s5-s8) to see whether counter number
matters and to firm up k=16's 2 of 5.

## After round 6: results (21:00)
Dial, transformer (att_sharp): x1 5/5 (s0-s4; 1.36-1.79, mean 1.65), x3 4/4 (mean 1.91), x6 2/4 (2.31), x12 2/4 (2.53);
birth signal 0.83 / 0.71 / 0.60 / 0.57. Predictions: x3 >= 2 of 4 RIGHT; x12 <= 1 of 4 WRONG (2 of 4, weak scores).
Dial, twin counters: k=2 0/4, k=4 0/4, k=8 0/4 (birth 0.62 / 0.83 / 0.83), k=16 1/4 new (3/9 with round 5). k=4 prediction WRONG.
Pooled (96 graded runs, best early pointing-home R^2 at it 0/100/200): <0.4 0/20, 0.4-0.6 1/11, 0.6-0.7 4/11, 0.7-0.8 12/25,
>=0.8 9/29. The 0.7 line is not sharp; the chance rises then levels near 40%.
Path 4: kvq_hebblc3 2/8 learned (2.37, 1.76); memory test 0.94 / 6.64 / stop 2.45 (kept the lead: prediction RIGHT);
learnability prediction (>= 3 of 8) WRONG. Control kvq_hebblc0 1/4 (1.56): training built the shared key part itself
(0.55 -> 0.76 by it 100). Not separable from the start with 12 tries.
Landscape at birth (slope.py): spin direction identical for all designs (loss ~5.3 -> 2.72); steer direction depth varies
(twin16 2.13, twin4 2.49, FW 2.79, transformer 3.01, hybrid 2.74, Mamba 3.34); does not predict learning.
Race (race.py): turn share 0.04 at birth -> ~0.5 by it 100 for learners and failures alike; learners 0.50 at it 600,
failures 0.67. Nothing at birth separates them.
21:03 wave 3 (firming the counts, same recipe, written before running): kvq_hebblc3 s8-s15, kvq_hebblc0 s4-s11,
transformer x6 s4-s7, x12 s4-s7, twin k16 s9-s12. Question: with ~16 tries each, is the running-sum start better than the
same knob started at zero? Prediction: no clear difference (both 15-30%), i.e. the knob, not its starting value, matters.
Wave 3 results (21:45): kvq_hebblc3 0 of 8 new (2 of 16 in all); kvq_hebblc0 1 of 8 new (2 of 12); prediction "no clear
difference" RIGHT: the start value does not matter; the extra key/query bias lifts the plain hybrid from 0/4 to ~1 in 7.
Transformer x6 5/8 (mean 2.25), x12 4/8 (2.49). Twin k16 5/13 in all. Pooled 124 runs: <0.4 0/20, 0.4-0.6 2/15,
0.6-0.7 8/20, 0.7-0.8 13/28, >=0.8 11/41.
