# Fisher et al. (2019): Sensorimotor experience remaps visual input to a heading-direction network

[Article](https://doi.org/10.1038/s41586-019-1772-4) · [Complete author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC7753972/) · [Saved HTML](main-fulltext.html) · [Reporting summary](41586_2019_1772_MOESM1_ESM.pdf) · [Reading coverage](reading-log.md)

## Contribution to the navigation account

Visual input to the compass is selective and plastic, even though the input neurons' axons broadly overlap the compass ensemble. This paper measures visually evoked E-PG membrane potentials, identifies inhibitory ring-neuron contributions, and shows that experience in an ambiguous two-cue environment changes both visual responses and the compass reference frame.

Read alongside Kim et al. (2019), it supplies physiology for the learned visual calibration mechanism. But it does not directly measure learning at a single identified R→E-PG synapse, and it does not demonstrate a stored destination or return to food. The authors' comparison to simultaneous localization and mapping concerns a mechanistic principle; the experiments use cues that cannot be approached and do not demonstrate a complete positional map.

## What is measured, and why the protocol matters

A compass cell's activity during ordinary turning mixes visual input, angular-velocity input and recurrent network activity. To separate cue-position responses, the authors flash a seven-degree-wide vertical bar for 500 ms, followed by 500 ms of darkness, at pseudorandom positions. Flash-triggered membrane-potential changes remain reproducible while the fly's yaw varies. Randomization of positions also prevents steady fixation of the stimulus.

The visual receptive field is the mean voltage in the final 250 ms of the flash minus the 250-ms pre-flash baseline. The cell's closed-loop heading tuning is a different measurement: spike-filtered membrane potential averaged in 35 heading bins as the animal turns. Correlation between the two asks whether visual inputs are aligned with the cell's overall heading representation. It does not simply correlate two copies of the same measurement.

Electrophysiology uses a 270° panorama spanning approximately −127° to +143°, onto which the full 360° virtual world is compressed. A twenty-degree virtual right turn moves the cue fifteen physical degrees left; the cue jumps across the missing ninety degrees at the edge. Two virtual opposing cues are therefore 135° apart on the physical screen. Calcium imaging instead uses a full 360° panorama. The difference is material when comparing behavior, apparent angular gain and cue ambiguity across papers.

The flies are newly eclosed virgin females, collected roughly 3–10 hours before electrophysiology or 12–26 hours before imaging. Some cohorts are food deprived for several hours and studied near subjective evening to encourage walking; Figure 5 also uses warmed saline, about 25–32°C. The animal walks on a nine-millimeter foam ball, tracked around 60–70 Hz. PB calcium imaging samples volumes at 6–9 Hz; electrophysiological signals are sampled at 20 kHz after a 5-kHz low-pass filter. This is neither freely moving foraging nor a uniform behavioral state across all experiments.

## Main figures: observations and inference

**Figure 1 — visual inhibition is selective.** Across 73 E-PG neurons in 68 flies, some cue positions produce hyperpolarization and others little or none. Roughly half also have depolarizing positions, plausibly reflecting disinhibition through the recurrent network. A neuron's visual receptive field is not simply predicted by its anatomical wedge across animals: among 21 filled cells, peak inhibition versus wedge position has circular correlation 0.097, P = 0.66. That supports individual-specific calibration, not a claim that there is no ordered map within a fly.

The flash controls are important. Population yaw does not systematically depend on cue position or jump distance; individual-fly tests also do not reach significance after correction. Thus a position-selective voltage response is not readily explained by a stereotyped turn evoked by each flash. These are controls on a specific confound, not a general assertion that visual cues never influence locomotion.

**Figure 2 — visual input usually aligns with heading tuning.** Interleaved open-loop flash mapping and closed-loop walking show positive correspondence in most of forty cells from 39 flies. Extended Data displays every pair, including weak and negative correlations. This is a tendency with substantial heterogeneity, consistent with imperfect alignment between sensory input and the full compass state.

**Figure 3 — ring neurons contribute inhibitory visual drive.** Some R2/R4d neurons respond selectively to a bar; others respond to full-field illumination or fail to show spatial bar tuning. The small recording sample contains spatially tuned responses in three of seven R2 and one of three R4d cells. Five-millisecond optogenetic activation of R2 or R4d neurons hyperpolarizes E-PGs (seven and four E-PG recordings, versus five controls). Kir2.1 expression driven by two independent lines reduces visually evoked E-PG hyperpolarization relative to genetic controls. This combination supports the proposed pathway more strongly than anatomical overlap alone.

The silencing is not a selective deletion of every visually responsive ring neuron. Both drivers label multiple R types and other neurons, and coverage is incomplete. Remaining responses can reflect residual ring input. Convergent results from two drivers strengthen attribution because ring neurons appear to be their shared labeled class, but neither experiment resolves every individual synaptic connection.

**Figure 4 — ambiguous experience can leave a changed reference frame.** Imaging experiments use at least ten minutes of one-cue pre-training, twenty minutes of two-cue training, and at least four minutes back in one cue. During two-cue experience, the offset can alternate between values about a half-turn apart; the bump often traverses half the ensemble twice during a full behavioral turn. The visual ambiguity can dominate the self-motion signal.

After the second cue disappears, some flies return to the original offset, others retain a shifted offset, and others continue switching. Persistent changes occur in about half of experiments. The analysis of nineteen flies finds significantly more probability in the opposing half of the offset distribution during training and afterward. Five of the original 24 flies were excluded for weak fluorescence or an unstable starting offset. The result is retained remapping over minutes, with heterogeneous outcomes; it is not a measured days-long memory.

**Figure 5 — visual receptive fields themselves change.** Whole-cell recordings compare receptive fields before and after twelve minutes of two-cue training. Some responses become less inhibitory at one position and more inhibitory elsewhere. The absolute mean change across cue positions is larger for 22 trained cells than seventeen one-cue controls (P = 0.043). Four trained cells show changes more than two control standard deviations above the control mean; these dramatic examples should not stand in for the entire distribution.

Change magnitude correlates with both receptive-field shape change (R² = 0.44) and the extent of heading modulation during training (R² = 0.52). Cells weakly modulated during training generally change little, consistent with the bump skipping their sector. This supports an activity-dependent association. However, training activity was not independently clamped in this experiment, and a correlation with modulation is not itself a direct demonstration of a molecular postsynaptic gate.

The proposed interpretation is depression of inhibitory R→E-PG input when presynaptic visual activity and postsynaptic compass activity coincide, balanced by potentiation elsewhere. The readout is a net visually evoked synaptic potential in an intact recurrent circuit. Specific synapse identity, the biochemical update law and the division between LTD and LTP remain inferred.

## Extended Data: details that change the interpretation

**ED1** documents the apparatus, the absence of a consistent flash-evoked turn, and a receptive field measured repeatedly over forty minutes. Stable control responses make experience-linked changes more interpretable.

**ED2** separates voltage responses during and after flashes. Hyperpolarization declines after cue removal, whereas depolarization tends to persist. That is consistent with direct inhibitory input plus a longer-lasting disinhibitory network state. It does not directly identify each intervening synapse. Population inhibition is stronger for lateral cues, with minima near ±100°, plausibly inherited from ring-neuron receptive fields. The lack of a between-fly anatomical map is also checked for maximum depolarization, not only peak inhibition.

**ED3** shows two sequentially recorded cell pairs in two brains. By chance, their dendrites occupy adjacent wedges; their visual and heading tuning are similar. This small within-animal observation complements the absence of a common across-animal offset. **ED4** shows all forty visual/heading tuning pairs, including the poorly aligned cells.

**ED5** provides multi-color anatomical characterization: 78 single-neuron clones for R20A02 and 61 for R54E12, spanning several ring-neuron types. **ED6** shows that the silencing conclusion also holds for mean negative visual responses, not just the peak. Its caption contains a duplicated driver name when describing two different coverage estimates: both sentences say R20A02. The second apparently concerns R54E12, but that is an interpretation, so precise percentages should not be copied without qualification. The images show roughly greater total labeling in R20A02, but total cell counts and subtype proportions are distinct measurements.

**ED7** displays offset distributions for all nineteen imaging experiments, making the variable post-training outcome visible. **ED8** displays the seventeen training cells beyond the five main-figure examples. **ED9** distinguishes matched twelve-minute one-cue controls from longer interleaved one-cue controls. Some control cells show spontaneous changes in both receptive field and heading tuning, though none as large as the largest trained examples. Training increases remapping; it does not create the only possible source of change.

The sole publisher supplementary download is the three-page reporting summary. All nine scientific Extended Data figures are in the main manuscript rather than an additional scientific PDF. The report specifies partial blinding for one silencing line, no blinding for the other, and no general random assignment beyond choosing the protocol before starting an experiment. Raw data are available on request; no request was sent.

## Mathematics and what a phasor leaves out

For a simplified account of sensory input, let g_m(ψ) be ring-neuron responses to a cue at angle ψ and W_nm ≥ 0 the inhibitory efficacy onto E-PG n:

\[
I_n(\psi)=-\sum_m W_{nm}g_m(\psi).
\]

A strong anatomical overlap need not imply equal W values. If all rows were identical, visual input alone would provide no preference among E-PG phases. Learning a pattern of relatively weak inhibition creates preferred phases for a cue. This is a conceptual expression of the proposed mechanism, not a fit to recorded single-synapse weights.

For the PB decoder, let F_j be ΔF/F in the sixteen glomeruli. Since the PB has two repeats of the circular E-PG representation, the relevant Fourier coefficient is

\[
Q_2=\sum_{j=0}^{15}F_j e^{-i2\pi(2j)/16}.
\]

The released analysis uses the negative of its phase, −arg(Q_2), with the sign chosen to match the anatomical convention. Treating this as the first Fourier coefficient over all sixteen glomeruli would be wrong: it is the second harmonic over the full PB, corresponding to one turn per eight glomeruli. Left/right averaging is used for some displays; the stated phase analysis uses the sixteen-glomerulus signal.

The offset comparison asks whether neural and visual phases retain a constant difference. A two-cue scene has the symmetry e^{i2(ψ+π)} = e^{i2ψ}, so visual appearance alone cannot distinguish two headings separated by π. A single-bump network can jump between them without maintaining two simultaneous activity bumps. The retained shift on return to one cue is what motivates a plasticity explanation beyond instantaneous sensory ambiguity.

For the receptive-field analysis, define

\[
A=\frac1N\sum_k |r_{\rm after}(\psi_k)-r_{\rm before}(\psi_k)|,
\quad S=1-\operatorname{corr}(r_{\rm before},r_{\rm after})^2,
\quad M=\max h_{\rm training}-\min h_{\rm training}.
\]

These correspond to absolute change, shape change and training modulation. The Methods' wording can be mistaken for a correlation optimized across angular shifts; the released code uses an ordinary correlation coefficient between the two curves at corresponding positions. Also, S is not a fully general shape distance: perfectly inverted curves have correlation −1 and hence S = 0, just like identical curves. The separate absolute-change metric and actual curves are therefore essential.

No perfect sinusoid is required for these operations. Fourier phase summarizes an imperfect population pattern, and sensory receptive fields can be irregular. The larger unresolved issue is which visual inputs change the compass phase and how their effective influence is learned.

## Analysis and scope limits

The Methods impose health, tuning and locomotor criteria. For the remapping experiment, ten cells are excluded for insufficient turning during training and six for nearly flat pre-training visual or heading tuning (range ≤2 mV). Large stereotyped inhibitory events are excluded or clipped, affecting about 5% of open-loop and 10% of closed-loop epochs in Figure 5. Imaging also omits weak Fourier-power periods. These choices make the comparisons meaningful for a usable heading signal but limit extrapolation to inactive or poorly tuned states.

The analysis-code archive was acquired using the working `wilson-lab` GitHub organization; the PMC manuscript's `wilsonlab` link does not work. The README, ROI-analysis function and targeted phase/shape calculation sections were inspected. No raw-data reproduction or model simulation was performed. The main publisher PDF remains an acquisition gap; the complete author-manuscript HTML, all fourteen scientific figure images and reporting PDF are saved locally.

## Remaining questions and role of the connectome

- Which ring-to-compass synapses change, and can changes in recurrent state or upstream responses contribute to the measured potential? The hypothesized locus is well motivated, not directly isolated at single-synapse resolution here.
- What maintains a learned mapping through sleep, new scenes, variable illumination and behavioral state? Minute-scale remapping does not establish lifetime stability or capacity.
- How does the system decide whether a conflict means the compass is wrong, the landmark moved, or the environment changed? An ambiguous pair of bars does not distinguish these explanations.
- What keeps stored goal vectors aligned with a changing compass frame? The two-cue training does not measure goal representations or navigation to a remembered target.
- How do local, approachable landmarks support positional memory? R2/R4d responses to sparse isolated objects motivate a celestial-cue hypothesis, but this experiment cannot identify every natural role of those classes.
- A connectome can constrain candidate input pathways and convergence. It cannot turn synapse count into the learned W matrix, identify a plasticity rule, or establish that a visual association is a food-place memory. Structure/function analysis should retain these alternatives explicitly.
