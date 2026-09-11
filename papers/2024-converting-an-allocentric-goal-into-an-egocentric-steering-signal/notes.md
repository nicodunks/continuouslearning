# Mussells Pires et al. (2024): from a desired bearing to steering

Peter Mussells Pires, Lingwei Zhang, Victoria Parache, L. F. Abbott and Gaby Maimon. **Converting an allocentric goal into an egocentric steering signal.** Nature 626, 808–818. [Publisher](https://doi.org/10.1038/s41586-023-07006-3).

Read with the question: **how does a remembered navigational objective influence movement from the fly's current state?** Full main PDF, Methods, six main figures, twelve Extended Data figures, supplementary discussion and reporting summary read; see [reading log](reading-log.md). This is a reading and mathematical interpretation, not a reproduction of the experimental analyses.

## What part of a complete behavior does this explain?

This paper supplies a mechanism for comparing a current **heading** with a desired **bearing**, then issuing a turn. It also develops a behavior in which an experienced wind direction influences subsequent orientation after the wind disappears. That is a substantial sensory-history-to-action connection.

It does **not** demonstrate navigation to a remembered two-dimensional food location. Maintaining a previously learned bearing after a rotation differs from recomputing the direction of a destination after translation. It neither identifies the substrate storing the wind-associated bearing nor establishes that the FC2 activity observed during spontaneous menotaxis is the persistent storage mechanism in the wind-memory assay.

The strongest circuit account is:

- A heading signal reaches PFL3 in the protocerebral bridge (PB), predominantly through Delta7, with some direct EPG input.
- FC2 activity in the fan-shaped body (FB) can communicate and causally set a desired bearing.
- PFL3 neurons combine heading and goal-related inputs nonlinearly. Their anatomical offsets differ between populations projecting to the left and right lateral accessory lobes (LAL).
- Population imbalance predicts steering; unilateral PFL3 activation causes predominantly ipsilateral turning.
- Partial PFL3 silencing impairs performance in the wind-induced angular-memory task.

These are convergent experiments, not one simultaneous recording of every stage of the complete chain.

## Variables and reference frames

| Variable | Meaning | Evidence and important distinction |
|---|---|---|
| H | Current heading relative to external directional cues | EPG/Delta7 compass-related signal; a heading is not a position or necessarily the direction of translation |
| G | Desired allocentric bearing | FC2 bump phase behaves like a goal signal during menotaxis; focal activation changes the maintained bearing |
| G − H | Body-relative angular error | PFL3 population computation approximately extracts a signed function of this difference |
| R − L | Difference between right- and left-projecting PFL3 population outputs | Predicts turning; distinct from the side of a cell's PB arbor |
| Wind-associated bearing | Previously experienced upwind direction in the visual reference frame | Sequential angular-memory assay; no distance-to-target representation is established |

“Allocentric” here means relative to a cue-defined angular reference frame, not a globally calibrated map. Bump-to-world offsets vary between flies. The relevant issue is alignment of heading and goal codes within an animal.

## Mathematics using complex exponentials

### The desired operation

Represent heading and goal as unit phasors:

\[
h=e^{iH},\qquad q=e^{iG}.
\]

The relative direction is obtained by rotating the goal into the current body frame:

\[
q\bar h=e^{i(G-H)}.
\]

An ideal signed steering signal is

\[
F(H,G)=K\operatorname{Im}(q\bar h)
=\frac{K}{2i}\left[e^{i(G-H)}-e^{-i(G-H)}\right].
\]

With the convention that positive turning increases H, the ideal dynamics \(\dot H=F(H,G)\) stabilize H = G for K > 0. The opposite heading H = G + π is also a zero but is unstable: a small deviation selects a turn direction. Exact opposition does not select a unique direction in a perfectly symmetric deterministic model.

This output is an angular control error, not a displacement vector. It does not say how the goal phasor q was chosen or how it changes as the fly translates.

### What the neurons implement in the paper's model

For cell j, let its heading and goal preferences be \(h_j\) and \(g_j\). Write the two real-valued inputs without trigonometric notation:

\[
u_j=\tfrac12[e^{i(H-h_j)}+e^{-i(H-h_j)}],
\qquad
v_j=\tfrac d2[e^{i(G-g_j)}+e^{-i(G-g_j)}].
\]

Then

\[
r_j=f(u_j+v_j),\qquad
f(x)=a\log(1+e^{b(x+c)}),\qquad
F=\sum_{j\in R}r_j-\sum_{j\in L}r_j.
\]

The fitted parameters are a = 29.23 Hz, b = 2.17, c = −0.7 and d = 0.63. These describe an effective input-to-rate relation; they are not measured synaptic conductances. The full model uses 24 PFL3 neurons, twelve on each output side, with anatomical heading preferences and twelve goal columns.

The nonlinear step matters. A purely linear sum has no interaction between H and G; shared goal inputs cancel in the bilateral difference and cannot modulate the heading response appropriately. As an explanatory expansion, the quadratic term in f(u + v) contains a cross-term proportional to uv. Products of the exponentials produce both difference-angle and sum-angle components. Summation across the anatomically offset populations retains the useful difference component while canceling many other components. This expansion explains the mechanism; it is not a claim that the fitted softplus is exactly quadratic.

### Why near-sinusoidal steering need not require precise fine tuning

The **supplementary discussion**, not just the main figure, supplies the key argument. In the idealized population model, the anatomical angle assignments imply

\[
F(H,G)=-F(-H,-G),\qquad
F(H+\pi/2,G+\pi/2)=F(H,G).
\]

Expand in complex Fourier modes:

\[
F(H,G)=\sum_{m,n}C_{mn}e^{i(mH+nG)}.
\]

Reality requires \(C_{-m,-n}=\overline{C_{mn}}\), and the first symmetry additionally makes the coefficients antisymmetric under (m,n) → (−m,−n). The second symmetry requires

\[
C_{mn}\ne0\ \Longrightarrow\ e^{i(m+n)\pi/2}=1,
\quad\text{hence }m+n\in4\mathbb Z.
\]

The desired pair (m,n) = (−1,1) and (1,−1) is allowed. Terms depending on heading alone at first order, goal alone at first order, or their first-order sum are forbidden. But higher harmonics are not all forbidden: (−2,2) is allowed, as is (2,2). The supplement reports about 2% for the former and less than 1% for the latter in this model, attributing their small size to the smooth nonlinearity.

Thus wiring symmetry helps obtain a useful steering law without tuning one exact firing-rate curve. It does **not** enforce an exact sinusoid, exact rotational invariance at every angle, or robustness to arbitrary anatomical asymmetries. Fourfold symmetry is weaker than continuous rotational symmetry. The reported approximately 0.06° standard deviation of the model's equilibrium error is a property of its idealized construction, not measured behavioral precision.

### Relationship to Lyu

[Lyu's circuit](../2022-lyu-allocentric-travel-vector/notes.md) estimates a travel vector by rotating body-relative movement into the external frame: \(v_w=e^{iH}v_b\). Here, the conceptual control operation rotates a goal into the body frame: \(q_b=e^{-iH}q\), then extracts a signed lateral component. The computations are complementary, but that algebra does not establish a biological hDeltaB → FC2 connection or a complete feedback loop through a stored location.

## Main figures: what each establishes

### Figure 1 — separating heading from a candidate goal signal

Head-fixed flies walk on a ball with a closed-loop visual bar. Brief ±90° bar jumps perturb visually defined heading. EPG phase follows the changed heading; FC2 phase remains relatively stable during selected menotaxis episodes. The two populations were recorded in different animals. FC2 can also move rapidly at other times, arguing against its stability being merely slow calcium filtering.

Selection matters: the strict main analysis includes only about 7% of candidate trials, requiring clear directional walking and reliable neural signals. Extended Data 3 relaxes criteria to about 59% of trials and preserves the qualitative separation, with more FC2 drift. Methods and the Extended Data caption use different return-angle thresholds in their descriptions; any exact replication should resolve this against code rather than silently treating the wording as identical.

### Figure 2 — causally imposing a goal bearing

Focal two-photon activation at two separated FB locations changes the heading maintained by the fly. Sixteen experimental and ten control flies support a within-fly relationship between FC2 activation location and chosen bearing. Across flies, the absolute phase-to-world offset varies. Stimulation also suppresses more distant FC2 activity, consistent with competition through inhibition, but the intervening inhibitory circuit is not identified here.

The sites alternate for 30-second epochs with 60-second intervals; this is not randomized arbitrary goal selection. Imaging illumination can itself activate the opsin, affecting intertrial activity. Forward speed increases when the fly is aligned with the imposed goal, so the behavioral consequences extend beyond turning alone.

### Figure 3 — single-cell conjunction of heading and goal

Whole-cell recordings from 21 PFL3 neurons (15 left-projecting, six right-projecting) show heading tuning whose spike-rate amplitude depends on the inferred goal. Somatic membrane potential is more strongly dominated by heading than the spike rate is. Goal is estimated from the fly's mean heading during a straight-walking bout, rather than independently recorded at each moment.

Extended Data shows every cell and substantial unequal sampling: individual heading/goal bins contain roughly 40 ms to 14 minutes of data, with many missing bins. The result is stronger at the pooled tuning level than as a claim that every cell was exhaustively mapped over all combinations.

### Figure 4 — anatomy plus nonlinearity makes the comparison

The 24-cell population model combines common goal-column input with different left/right heading offsets. Subtracting summed outputs gives a steering function close to the imaginary part of the goal-to-heading phasor ratio. The fitted goal-versus-heading preference difference is approximately −48°, compared with a mean anatomical prediction near −67.5°; these are related but not identical estimates. The full population model uses the anatomical mapping.

The fit explains approximately 95% of variance in averaged tuning, versus roughly 30% in the unaveraged spike-rate samples. The authors analyze how Poisson variability can explain much of this difference. The 95% number must not be presented as prediction of every moment of spiking or behavior.

### Figure 5 — output imbalance influences turning

Bilateral PFL3 LAL calcium signals show transient asymmetries that precede turns by about 100 ms. Those signals lag deviations from the goal by about 200 ms. These are measurements involving calcium indicators, not direct synaptic transmission delays. Unilateral PFL3 stimulation predominantly causes ipsilateral turning, with controls including PFL1 stimulation.

About 8% of stimulation trials turn in the unexpected direction. A crucial Extended Data caveat is that the driver labels only part of PFL3, so the measured asymmetry need not equal the complete population asymmetry. Such trials do not, by themselves, demonstrate a downstream override or sign-switching policy.

### Figure 6 — sensory history can guide subsequent orientation

Flies experience 30 seconds of wind from one of six angles relative to the visual reference. At wind offset, the bar jumps by 180°, and the fly is tested without wind for 60 seconds. The principal measurement uses 5–35 seconds after offset. Three trials occur within each direction block; the second and third are analyzed because performance improves with experience. The six directions are tested sequentially, not stored simultaneously as six independent destinations.

EPG inactivation strongly impairs this wind-off orientation despite relatively preserved wind-on orientation. This establishes dependence on the compass pathway for the task, not the precise stage at which memory is stored, retrieved or converted into action.

Partial PFL3 silencing increases error and reduces the number of successfully followed directions in the main TNT experiments. Expression labels about ten of the 24 cells. Two experimental replicates support the main conclusion, but other driver/effector comparisons have weaker or nonsignificant outcomes. The population-removal model reproduces the scale of impairment after noise is calibrated to control behavior; it removes random cells, not an exact reconstruction of each driver's expression pattern. It supports consistency, not unique identification of the mechanism.

## Extended Data and supplements: details that change interpretation

| Item | Contribution to the argument |
|---|---|
| ED1 | Driver expression, off-target cells and incomplete population coverage; FC2 driver is not an isolated subtype |
| ED2 | Menotaxis classification, bar-jump behavior and walking-state dependence |
| ED3 | Relaxed trial selection, rapid FC2 changes and episodes where FC2 drifts but an older behavioral bearing returns; especially relevant to storage versus readout |
| ED4 | Spatial suppression during FC2 activation, individual phase offsets, variable response onset and alignment-dependent speed |
| ED5 | Actual connectivity matrices, Delta7 mapping, FC2 subtypes and the twelve-versus-nine-column issue |
| ED6 | Morphological/electrophysiological identification of PFL3 versus PEG; heading tuning of every recorded PFL3 |
| ED7 | Goal modulation stronger in spikes than somatic voltage; uneven and missing sampling is visible |
| ED8 | Goal modulation persists in near-standing periods, arguing against a simple walking-velocity confound |
| ED9 | Compartmental interpretation, softplus fit, ideal-model error and predictions using measured FC2 plus a **synthetic**, bar-derived heading signal |
| ED10 | Timing relative to heading error and the incomplete-labeling explanation for unexpected turns |
| ED11 | All silencing comparisons, expression counts, wind-on matching control and model ablations |
| ED12 | Conceptual comparison with Lyu's coordinate transformation; complementary arithmetic is not evidence for a connected memory circuit |
| Supplement pp. 2–3 | Irregular Delta7 mapping, tiny model residual without a goal, Fourier/symmetry argument |
| Reporting summary | Female flies, exclusion rules, sample-size decisions and lack of experimenter blinding |

## Anatomy: what to carry into later MaleCNS analysis

The source anatomy is the female hemibrain, described as v1.2 in figure text and v1.2.1 in the reporting summary. It is not our downloaded MaleCNS dataset.

In the PB, Delta7 supplies approximately 77% and EPG 14% of PFL3 input synapses. Treating every PFL3 heading preference as simply the heading angle of its anatomical glomerulus would miss the Delta7 sign and phase transformation. Two irregular cells require assignments based on their dominant Delta7 inputs, whose upstream EPG inputs determine the relevant angles. The supplement says correcting these assignments improves model accuracy.

In the FB, FC2A/B/C together supply about one third of **columnar-cell synapses** onto PFL3, not one third of all synapses. The hemibrain reconstruction contains 18 FC2A, 33 FC2B and 37 FC2C cells. The driver labels roughly 70–100 somata and appears to include B/C; pooled functional observations should not be assigned indiscriminately to every subtype. hDeltaA, hDeltaI and hDeltaM are other substantial columnar inputs worth understanding in their own literature. Tangential inputs may modulate the computation but their functional role is not established by cell shape alone.

The twelve-column account is supported by similarities between FC2 input vectors onto paired left/right PFL3 cells. A nine-group scheme would merge cells that need not receive functionally identical FC2 input. This is a concrete example of why cell labels and column counts must be reconciled rather than pasted between papers.

Later analysis should preserve individual cells, compartment-specific connections and angle assignments. A type-to-type edge count alone loses precisely the structure used by this computation.

## Methods and assumptions worth retaining

- Experiments use 1–4-day-old female flies, head fixed on an 8-mm ball, with wings/proboscis constrained. Most preparations involve approximately three hours of food deprivation; FC2 stimulation has a longer agarose protocol. Temperature and effector conditions differ across assays.
- The visual arena spans 270°, leaving a rear gap. FicTrac runs at 50 Hz. EPG/FC2 imaging is about 4.95 Hz and LAL imaging about 9.16 Hz. Neural indicator filtering and sampling matter for latency interpretation.
- Whole-cell recordings are sampled at 10 kHz, low-pass filtered at 4 kHz and corrected for a −13 mV junction potential. Identification uses morphology for an initial subset and electrophysiological criteria for additional cells; not every cell has the same anatomical verification.
- Straight bouts are segmented from ball-derived trajectories using Ramer–Douglas–Peucker simplification (25-mm tolerance; segments longer than 200 mm). Mean heading defines the behavioral goal. This is an operational definition, not an independently measured mental target.
- EPG phase extraction uses a Fourier period of 8.5 glomeruli; FC2 uses a 16-ROI population vector. Phase conventions and offsets should not be borrowed unmodified from Lyu.
- The FC2-to-model analysis rescales measured activity and combines it with a synthetic heading signal derived from the bar, with a 200-ms lag. This is useful model testing, but not simultaneous EPG/FC2/PFL3 measurement.
- The proposed electrotonic explanation puts soma/PB heading input closer together while FB goal input influences the spike-initiation zone more than the recorded soma. The drawing contains a question mark at the spike-initiation zone: direct compartmental recordings do not establish that mechanism here.
- Wind angles omit straight ahead and directly behind, and blocks proceed clockwise or counterclockwise following pilot-informed design. Interpretation should respect sequential training and the visual gap.
- Experimenters were not blinded. Sample sizes generally follow earlier work; the second main TNT replicate was increased following power analysis on the first. Multiple-comparison correction is not generally applied. Individual flies, cells, trials and time bins are different sampling units.

## Remaining questions, organized around a complete behavior

1. **What is remembered, and where?** Wind-history-dependent orientation supports angular memory. FC2 activity can communicate a selected bearing, but ED3 shows why a persistent behavioral objective need not equal uninterrupted persistent FC2 activity. Storage could involve other populations, synapses or intracellular state; these alternatives remain open here.
2. **How is sensory experience written into the goal?** The wind-memory assay and FC2 manipulation do not identify the complete wind → goal-writing pathway. The corresponding sensory and learning papers must supply it, if known.
3. **How are multiple objectives selected?** Hunger, learned value, competing odors and exploration may alter which goal is expressed. This paper does not identify the selection mechanism or establish multiple stored locations.
4. **What changes after translation?** A fixed G suffices for maintaining a bearing. Returning to a fixed point generally requires recomputing G from the current position or an equivalent homing representation. That computation is absent from this model.
5. **How does locomotion finish the behavior?** PFL3 activity influences turning, but descending pathways, speed control, stopping at a source, obstacle responses and sensory re-acquisition remain to be connected.
6. **How robust is the comparison in real anatomy?** The symmetric model is elegant; individual synaptic asymmetry, subtype differences, gain changes and reference-frame recalibration need independent constraints before transferring it to MaleCNS.
7. **Which neighboring inputs mean what?** hDeltaA/I/M and other PFL3 inputs are candidate contributors, not unnamed copies of FC2. Their signals could express other goals, context or dynamics. Their identities and physiology should guide hypotheses before simulations.

## Contribution to the running synthesis

This paper closes much of the **current heading + selected angular goal → corrective turn** link and provides a task linking directional experience to later action. It leaves the origin, storage and translation-dependent updating of a goal substantially unresolved. Read the companion Westeinde study for the output computation and neighboring PFL populations, and the wind/olfactory learning literature for the upstream goal formation and persistence mechanisms. Neither adjacency nor matching variable names is enough to join them into a demonstrated serial circuit.
