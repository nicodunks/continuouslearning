# Round 4 charter: test the "memory before learning" explanation by flipping it, and test a trap-free grade (29 Sept, 14:27 PT; 30-minute budget)

Setting: the 10 s stage, where every rival failed and FW learned. Same recipe for all: 800 iterations, step size 1e-3 (no decay), batch 32, 2 s at food, erase charge 0.05, three random starts (seeds 0-2). Measure: running score over the last 50 iterations at iteration 800 (chance 2.31, a spinner 2.39 at 10 s), plus the frozen standard exam at 10 s.

Arms (manipulations checked before training with level4/untrained_probe.py: home vector R^2 at the turn):
- FW (baseline): R^2 0.88-0.93 before training.
- FW-noHS: write strength started at 0, board empty (R^2 -0.02). Prediction: learns much worse than FW, or spins. 65%.
- TWIN (baseline): R^2 about 0.
- TWIN-HS: 16 neurons wired as slow heading counters (hold gate ~0.005, inputs = heading) (R^2 0.71). Prediction: learns (ends below 2.0). 60%.
- TWIN-trapfree: plain twin, grade = smooth closest approach (tau 0.5) + 0.2 x last-10-s grade (the mix passes level4/trap_curve.py). Prediction: stops spinning and beats chance, but learns less than TWIN-HS. 50%.
Explanation supported if FW-noHS loses most of FW's advantage and TWIN-HS gains most of it.

## Amendment 14:34 (before any extended result was seen)
At 800 iterations even baseline FW learned on only 1 of 3 starts (earlier runs needed 250-911 iterations for this stage), so 800 was too short to judge any arm. Every run continues from its own checkpoint with the same settings: FW arms to 1,400 iterations, twin arms to 2,000 (the twins are five times cheaper). The 800-iteration numbers are kept in level4/r4_results_800.json.
