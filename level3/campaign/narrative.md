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
