# What we learned about training

_This file is written by the supervisor as the night goes on and rendered into the report. Every claim names the run it comes from._

## The curriculum was necessary, and it is where the swings live
Runs 1 and 2 never earned their promotion to 20-second trips; they hit the 1,500-iteration cap. Run 3 earned it at iteration 804. Every run's cost per iteration doubled at the switch, because an episode is twice as long and training walks through every tick twice, forward and backward.

## The bad swings were the optimiser overshooting near the ceiling
Run 1 at iteration 800 and run 3 at iteration 1900 both lost most of their score in about thirty iterations. In run 3 the write gate nearly doubled (0.39 to 0.71) and the tallies saturated; a saturated tally does not just forget, it points the wrong way, so the loss went above a random walk. Adam's momentum carried a step that a few batches had asked for. Both recovered within a hundred iterations. Checkpoints every hundred iterations are what make this survivable.

## A fade is the easy solution, and it is not the fly's
Every run so far erases at about one percent per tick and never fires at food. The signal to fire at food is tiny (a few ticks per trip) and its payoff is delayed to the next trip. The reset is the one fly ingredient no run has found. Run 4 tests whether making leftovers hurt more (five trips per episode) changes that.

## Speed-weighted writing appeared once the write gate had room
Run 3's write gate follows speed with correlation +0.94; runs 1 and 2 were flat. The difference was not a knob about speed. It was that the two-second food stand lowered the overall write level and left the tallies off the ceiling, and in that regime speed-weighting pays.

## Making leftovers hurt more did not teach the reset (run 4)
Five trips per episode instead of two, warm from run 3. The first hundred iterations were a shock (score 3.06, up from 1.72) as the fade struggled with a board dirtied by three or four earlier trips, then the network settled back to about 1.7 by fading a little harder. The erase gate at food did not move: 0.0045, lower than away from food. The prediction failed, and the score at 20 s ended worse than the parent (2.30 vs 1.90). Lesson: the reset is not going to be forced by punishing a dirty board; the gate simply cannot see the five or twenty food ticks against the hundreds of others. The one useful thing run 4 gave is the first 30-second score, 2.37 at its best checkpoint, on trips longer than anything it trained on.

## Why the ceiling is not a clean lever (a decision, not a run)
Lowering the tally ceiling looked like the other way to force a reset. But the write strength and the A table are both trained, so the network can halve what it writes and double how loudly F counts, and a lower ceiling changes nothing. Skipped, and the reason is recorded here so it is not re-tried by accident.

## Run 5: the penalty again, but from a warm start
Run 2 raised the erase penalty from a cold start and got a dead network: with nothing yet learned, the penalty just closed the gate. Run 3's best checkpoint already homes, already has compass cells and a speed-following write gate, and a fade of about one percent per tick. Charging that fade ten times more, now that there is a working memory to protect, may push the erasing that remains into the one place it is free: the food ticks. Same parent as run 4, two trips, penalty 0.5. Prediction: erase at food rises above 0.1 while erase away from food falls below 0.003; score at 20 s stays near 1.9. Failure looks like run 2: the gate closes everywhere and the tallies saturate.
