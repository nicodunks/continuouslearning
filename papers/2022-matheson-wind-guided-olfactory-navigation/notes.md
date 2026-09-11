# Matheson et al. (2022): A neural circuit for wind-guided olfactory navigation

[Article](https://doi.org/10.1038/s41467-022-32247-7), Nature Communications 13, 4613. Read with the essential [2024 addendum](https://doi.org/10.1038/s41467-024-46225-8). Full article, figures, scientific supplement, reporting summary, addendum and peer-review file read. Archived model code inspected for the mathematical implementation; no simulations or raw-data reanalysis performed. See [reading log](reading-log.md).

## What this contributes to the complete behavior

This paper connects odor-sensitive pathways to a mechanism for selecting a wind-relative walking direction. Odor indicates that moving upwind is useful; wind supplies a direction. The fan-shaped body (FB) is a candidate place where these signals meet. Patterned FB activity can influence persistent orientation, and a model shows how a directional representation could be compared with heading to steer.

This is one component of finding food. It does not identify the food's position, learn that position, estimate remaining distance, recognize arrival, or explain a return trip. A model fly moving upwind during an externally imposed odor pulse is not a demonstration of navigating back to a remembered place.

## The cell-identity correction changes the circuit inference

The 2024 addendum is indispensable. VT062617, used for physiological and behavioral experiments, additionally or perhaps predominantly labels **hΔK**, characterized by an ellipsoid-body projection. The responses in Fig. 5E–I and behavior in Fig. 6 may therefore arise from hΔK rather than hΔC.

But the anatomical convergence in Fig. 5B–C remains a result about **hΔC**: it receives direct input from odor-sensitive FB5AB and wind-sensitive PFNa. The addendum explicitly says hΔK does not receive these direct inputs, although indirect inputs exist.

Consequently, replacing every hΔC label with hΔK would be incorrect. Keep three claims separate:

- **Anatomy:** direct FB5AB/PFN convergence onto hΔC in the hemibrain.
- **Physiology/manipulation:** a VT062617 population, potentially chiefly hΔK, responds to odor and wind and affects orientation.
- **Model:** an idealized hΔC-labelled directional population and additional local circuitry can generate the observed classes of behavior.

Their relationship requires intermediate pathways and cell-specific evidence. [Kathman et al. (2026)](../2026-neural-dynamics-for-working-memory-and-evidence-integration-during-olfactory-navigati/notes.md) adds more specific hΔK evidence but does not by itself validate the original direct-input diagram. Hamid et al. (2024), cited in the addendum, is a required follow-up.

## Experiments and figures

### Figure 1 and S1: odor initiates several separable actions

Broad optogenetic activation of Orco/IR8a olfactory receptor neurons can substitute for odor: upwind movement during stimulation and increased trajectory curvature after stimulation. Without wind, activation still produces offset search but no directed upwind movement. Broad combined receptor-neuron silencing disrupts navigation; silencing individual receptor classes leaves substantial behavior, and single receptor populations are generally insufficient to reproduce the broad response.

The comparison is not an exact dynamical equivalence between vinegar and optogenetic stimulation. Different glomerular recruitment and temporal response dynamics could contribute. The authors favor partly distinct populations for upwind and search responses, but behavioral dissociation alone does not uniquely identify that decomposition.

### Figure 2 and S2: MB and LH signals have context-dependent motor consequences

Activating cholinergic AD1b2 lateral-horn neurons (LH1396/1538/1539) promotes upwind walking and offset search. MB052B (MBON15–19), MB077B (MBON12), and MB082C (MBON13/14) also promote upwind behavior, with different search effects. Individual MB052B components do not reproduce the collective upwind effect. MB434B (glutamatergic MBON5/6) promotes downwind behavior. MB112C (GABAergic MBON11) and MB011B (glutamatergic MBON1/3/4) mainly straighten trajectories without producing wind-directed movement.

A neuron's effect in a quadrant preference assay is therefore not a context-independent motor command. Lines with different preference phenotypes can both reduce curvature in this assay. This is relevant to translating learned odor value into an action appropriate to the environment.

Calcium measurements show vinegar responses in the principal upwind-promoting groups without robust wind-direction tuning during odor. The stronger claim that these neurons never convey wind information is unwarranted: AD1b2/LH1396 supports above-shuffle direction classification at wind onset, largely because frontal stimulation differs from lateral stimulation. Supplementary α′3 MBON electrophysiology (12 cells, six hemispheres) shows similar odor responses for ipsilateral and contralateral presentation, but used an earlier, different stimulus setup.

Individual MB/LH silencing does not abolish navigation; some manipulations increase responses. This permits redundancy, compensation and assay-specific recruitment. It does not establish that each activated pathway normally drives the behavior in isolation.

### Figures 3–4 and S3–S4: contextual inputs to the FB

A screen of roughly 40 FB input lines identifies tangential activation hits, whereas uniform activation of tested PFNs does not produce the same upwind response. A negative result from activating all directional channels together is not evidence that their natural patterned activity is unnecessary.

Trans-Tango labeling and hemibrain paths place MB/LH outputs upstream of dorsal FB inputs. FB5AB receives direct contacts from the relevant MBON line groups and appears in many two-synapse paths from vinegar-responsive PN pathways through LH. The connectome search uses hemibrain v1.1 and thresholded connections; a path's existence is not a measured effective gain.

Cholinergic FB5AB activation restricted with CLIN to central-complex lineages promotes upwind movement. Other tangential hits include 65C03, 12D12 and the ventral-FB split line. Their stimulation effects can persist after light offset, unlike the pronounced offset-search response of several upstream pathways. Not every activation hit responds to odor: 45D04 is an example.

S4 is easy to oversummarize. FB5AB increases activity between wind alone and odor; vFB split decreases over that comparison, while still allowing odor to be decoded. Other lines do not show a significant increase in that comparison. An odor-related decrease can carry information. FB5AB also adapts strongly across stimulus blocks. The model's positive Boolean odor gate is not a fitted description of these diverse responses.

Individual tangential silencing does not eliminate upwind behavior; some effects increase it. This is not evidence for a unique obligatory FB5AB route.

### Figure 5 and S5: anatomical convergence versus recorded activity

Twenty reconstructed hΔC neurons receive wind-sensitive PFN inputs in ventral dendritic regions and FB5AB contacts around dorsal output tufts. **Axo-axonic gating of output** is a plausible mechanism, distinct from simple summation of two dendritic drives. Calcium at output tufts does not resolve membrane integration or transmitter release.

VT062617 imaging finds localized, odor-enhanced, wind-direction-dependent activity. Analysis includes 87 responsive columns across 16 flies and selects responses exceeding two baseline standard deviations. Preferred direction does not map consistently onto anatomical column across flies. This is compatible with an individually offset heading reference, but not a direct test of an allocentric wind code: the flies were immobilized, and heading was not independently varied or simultaneously measured in EPGs.

Responses can also occur at wind onset/offset, so even the original physiology does not support strict activation only during odor. S5's cholinergic labeling is subject to the same driver-identity caution as the functional experiments.

### Figure 6 and S6: patterned activity influences orientation

Sparse SPARC2 expression, targeting about 15% of the driver population, makes many flies walk repeatedly in an individual preferred direction during activation. Broad activation instead causes unstable turning and increased curvature. The sparse orientation comparison is significant (65 experimental flies versus 34 controls, p = 0.0035).

This is evidence that the pattern matters, not proof that the naturally represented variable is a remembered food destination. Expression-vector direction does not predict preferred walking direction (S6E), and expression-vector length or cell count does not significantly predict orientation index (S6C–D). The rectangular arena has a long-axis bias. Removing positions near walls addresses immediate wall contact but does not erase arena geometry as an influence.

Acute VT062617 silencing leaves the initial upwind response relatively intact but reduces the later part of the ten-second odor response (reported p = 0.0475, uncorrected t-test; n = 24). ORN silencing affects early and late behavior; FB5AB silencing does not show the same impairment (n = 32). This supports a contribution to sustained orientation **during odor**. It should not be silently equated with the post-odor persistence measured by Kathman.

The orientation index is PCA/SVD anisotropy of a polar histogram represented in Cartesian coordinates: SD along PC1 divided by SD along PC2. It is not the conventional circular resultant length, and an axis preference can increase it. Preferred direction additionally resolves which side of the axis is more occupied.

### Figure 7 and S7: a conceptual controller

The model reads a wind-related representation against heading to generate upwind orientation, an arbitrary reproducible bearing under sparse activation, and unstable turning under broad activation. The latter requires an added mutually inhibitory, adapting local population. Removing it eliminates the broad-activation curvature increase in S7. That demonstrates a requirement of this implementation, not identification of the biological inhibitory population.

The model's opposite-column motif is inspired by other horizontal FB cell types (hΔA/G/H/M), not established mutual inhibition among the recorded cells. Its signs, effective gains and simplified relays are hypotheses. The 20-to-eight-column transformation is a constructed overlap map, not the full measured synaptic matrix.

The alternative frontal-wind representation only produces reliable upwind correction when initially within ±90° of upwind, or after random turns bring the fly into that range. A full allocentric representation is supplied directly in the principal model. The additional rear-tuned channels needed to derive it from the proposed PFN architecture were not identified here.

### Figure 8: a framework, with missing links

Columnar directional inputs and tangential contextual signals could select directional outputs. This framework motivates multiple goals and flexible navigation, but there is no odor-conditioning experiment, multiple-memory retrieval experiment, or full food-source behavior in this paper.

## Mathematics in complex-exponential form

These equations explain the computational proposal; they do not imply that neurons contain complex numbers. Let θ be heading, ω wind direction, δ = ω − θ, and φ_j a column's phase. The code uses degrees internally; equations here use radians. Define a sampled directional profile

\[
q_j(\alpha)=\operatorname{Re}e^{i(\phi_j-\alpha)},\qquad
B_j(\alpha)=\frac{q_j(\alpha)-\min_k q_k(\alpha)}{\max_k q_k(\alpha)-\min_k q_k(\alpha)}.
\]

This **sample-dependent min–max normalization** is what the archived implementation uses, with maximum input one. It differs in amplitude details from simply writing 1 + Re(exp(i(φ−α))). For finite columns, the sampled extrema change with phase.

Heading inputs to right PFL3, left PFL3 and PFL2 are respectively

\[
B(3\pi/2-\theta),\quad B(\pi/2-\theta),\quad B(-\theta).
\]

The fully allocentric model supplies a 20-column wind input B(π−ω). Its phase is stipulated; the model does not construct it from identified wind afferents.

The frontal version constructs

\[
a_R(\delta)=\tfrac12[1+\operatorname{Re}e^{i(\delta-\pi/4)}],\qquad
a_L(\delta)=\tfrac12[1+\operatorname{Re}e^{i(\delta+\pi/4)}],
\]

\[
w(\phi)=C(\theta)^{-1}\{a_R B(3\pi/4-\theta)+a_L B(5\pi/4-\theta)\}.
\]

C is the maximum of this summed profile evaluated for frontal wind, as implemented in `heading_inputs_pfn.m`. Thus the weights are nonnegative, offset directional tuning curves, not unrestricted signed vector components. Ignoring finite-grid normalization, the first harmonic points between the two PFN basis directions, which explains the restricted range. These two front-preferring channels alone do not yield an exact arbitrary 360° coordinate transformation.

Let Tπ shift a profile halfway around the ring, M map 20 columns to eight, o be the imposed odor gain, and p the optogenetic pattern. The implementation computes

\[
h=M\,S_h\{T_\pi(ow+p)\}+n,
\qquad S(x;b,k)=\frac{1}{1+e^{-(x-b)/k}}.
\]

The order matters: the sigmoid is applied **before** the 20-to-eight transformation. Noise is added afterward. The maximum derivative of this sigmoid is 1/(4k); “slope 1/k” in the code comments describes a steepness parameter rather than the actual peak derivative.

The adapting mutually inhibitory population follows

\[
\tau_u\dot u=-u+S_u(-W_{ii}u-ga+h),\qquad
\tau_a\dot a=-a+u,
\qquad \ell=h-g_{inh}T_\pi u.
\]

Wii couples opposite columns with weight 1.1, τu = 1 ms, τa = 100 ms and g = 0.5. Its imposed inhibitory sign and slow adaptation permit symmetry breaking and alternation under broad drive. This is not a derived circuit mechanism for storing a food location.

For each PFL population,

\[
\tau_p\dot r_X=-r_X+S_p(B_X+\ell).
\]

The sigmoid makes overlap between local and heading activity matter. In the code, τp = 1 ms; k = 0.1, h threshold 0.7, local-population threshold −0.15, and PFL threshold 1.7. Turning and forward signals are

\[
\theta_{t+1}=\theta_t+0.03\bigl(\sum r_R-\sum r_L\bigr)+\eta_t,\qquad
v_t=6+0.25\sum r_{PFL2}.
\]

The numerical turning coefficient uses **degrees per simulation step**. Position is integrated from the forward signal and heading, with time converted from milliseconds to seconds. The model contains no position-dependent odor plume: odor is an externally scheduled stimulus.

A shared compass offset cancels in comparing directional phases. If both heading and wind/goal have an offset β, their relative phase remains (ω+β)−(θ+β)=ω−θ. But that cancellation requires the signals to share a reference. Their common reference and the complete wind transformation were proposed, not directly measured here.

## Does this explain perfect sinusoids?

No. The code calls trigonometric functions to supply exact sampled first harmonics, then normalizes, combines and thresholds them. The recorded column responses do not establish exact sinusoidal tuning, and the model does not explain the network dynamics or learning that would generate such tuning.

A useful distinction is between needing a readable **first harmonic** and requiring the entire firing-rate profile to be sinusoidal. For a real population profile r(φ), its first harmonic can be summarized by z = Σ_j r_j e^{iφ_j}. Higher harmonics need not destroy a directional signal, but finite sampling, uneven weights and nonlinear readout can mix them and distort phase. This paper does not quantify that robustness. It therefore cannot close the sinusoid-generation question raised by Lyu.

## Code versus printed model: reproducibility details

Inspected the archived [Zenodo v1.0.0 release](https://doi.org/10.5281/zenodo.6762105), directory `nagellab-Mathesonetal2022-095a663`. This was a targeted reading, not execution or validation of the complete analysis pipeline.

- The article describes a 0.05 s Euler step, whereas the figure driver explicitly supplies times in milliseconds, uses a ten-second stimulus as 10000, and the trajectory routine divides dt by 1000. The effective step is **0.05 ms**, consistent with the parameter table's 20 kHz and millisecond neural time constants.
- The frontal PFN gains include +1 and division by two. Omitting those baseline terms changes the allowable vector directions and is not an equivalent implementation.
- Heading/wind profiles use sampled min–max normalization, and the local sigmoid precedes the column transformation.
- Random turns use a Bernoulli event at each step with probability 0.0003 and magnitude `20 * random_sign * randn^2`. This is a signed squared-normal amplitude, not a Gaussian amplitude, despite the comment and simplified description. At 20 kHz the mean event rate is six per second.
- Neural noise is updated with a normal draw multiplied by dt, rather than the square-root-dt scaling of a standard Euler–Maruyama OU process. Its discrete amplitude is therefore timestep dependent. Treat the published implementation as a discrete model unless this convention is reconciled.
- The directional neural contribution to heading is a per-step increment without explicit dt; changing dt requires rescaling that coupling and the turn-event probability.

These details matter if reproducing this model later. They do not invalidate the behavioral observations.

## Methods and limits that affect interpretation

Behavioral activation largely uses genetically blind norpA males, with tsh-Gal80 suppressing ventral-nerve-cord expression. Other experiments are described as female in the main methods/reporting summary. The supplementary genotype table and reporting summary disagree in the GtACR row (w1118 versus norpA), and their male wording also conflicts with the broad “all other flies female” statement. Preserve this reporting inconsistency rather than resolving it by assumption.

Flies were starved about 24 hours and tested near ZT1–4. Ages vary by experiment: behavioral activation generally 3–10 days, imaging 5–21 days, and the electrophysiology cohort younger. Behavior used roughly 12 cm/s wind and 1% vinegar; imaging used different wind speeds/setups and 10% vinegar. Immobilized imaging with removed front legs does not sample the same sensorimotor loop as freely walking behavior.

Tracking was 50 Hz with low-pass filtering. Stationary periods below 1 mm/s, trials with less than 25 mm movement, and insufficiently active flies were excluded. SPARC analyses additionally remove locations within 3 mm of walls and use a 2–6 s interval. These are conditional measurements of locomotion, not unconditional time allocation across walking, stopping and feeding.

Response windows vary across screens (early five seconds for several peripheral/MB/LH analyses, ten seconds for FB). Curvature is angular velocity divided by speed, so slowing alone can inflate it; screen display rules suppress some low-motion phenotypes. Compare raw components before treating curvature as a unique search command.

Direction classification uses response and fly identity, ten-fold cross-validation and shuffled labels. This is not a leave-one-fly-out generalization analysis. Failure of that particular decoder to exceed shuffle is not proof of zero information.

The reporting summary adds exclusions: two 65C03 flies with rhythmic activity and no stimulus responses; one of 17 VT062617 flies with no column exceeding the responsiveness threshold; electrophysiology with inadequate access/input resistance ratios. Analyses were automated but experimenters were not genotype-blinded. Sample sizes followed prior studies rather than a reported prospective power calculation.

## What the peer review clarifies

All three reviewers challenged broad activation as evidence for a directional code; this led to sparse activation and a substantially revised model. The first review also pointed out that several proposed PFN–hΔC–PFL pathways were weak, heterogeneous or absent as direct connections. The authors explicitly changed the presentation to a conceptual framework and stayed agnostic about intermediate relays and the precise wind representation.

A later reviewer objected to suddenly calling odor-gated wind activity a goal representation without a goal manipulation; the authors removed that wording from the disputed paragraph. This is precisely the distinction needed in our synthesis.

The axo-axonic issue persisted through revision. Output gating is an interesting hypothesis, not a measured transfer function. Likewise, the authors acknowledged that the full allocentric wind version would require rear-wind vectors not yet characterized. A simulated trajectory is evidence of computational possibility under those assumptions, not evidence that every assumed neuron or connection exists.

## Remaining questions and neighboring papers

1. Which intermediates deliver odor/wind information to hΔK, and how does that route relate to the direct hΔC inputs? Follow Hamid, Kathman and Lanz, preserving driver specificity.
2. Which signal represents physical wind, the chosen bearing, and a maintained intention? Simultaneous heading/wind/goal manipulations are needed to distinguish them.
3. What changes odor value into a navigation policy after learning? The MB activation screen motivates this question but does not answer it. Follow Aso and the MB learning literature.
4. How is the initial upwind turn generated when sustained-orientation circuitry is silenced? Candidate parallel LH/LAL/descending paths should be read before choosing a connectome search.
5. What ends persistence and initiates search? The model's imposed stimulus periods do not explain search scheduling. Compare Kathman's post-odor state persistence and Siliciano's boundary-return vectors.
6. Which PFL and descending pathways are actually used? The 2022 PFL2 forward-speed rule must be reconciled with [Westeinde 2024](../2024-transforming-a-head-direction-signal-into-a-goal-oriented-steering-command/notes.md), where PFL2 contributes to large-error steering and activation increases turning while reducing forward movement. The newer evidence changes the old controller; the two cannot simply be pasted together.
7. How does a transient direction become a location memory, and how is it updated after displacement? Nothing here demonstrates that step. Read visual-place learning and idiothetic local-search work.
8. How are realistic tuning curves generated, calibrated and decoded with so few neurons? Exact sinusoidal inputs are an assumption here.

## Role for later connectomics

The concrete structural problem is to resolve cell identities and intermediate paths between contextual signals, directional representations, recurrent maintenance and steering outputs. Compare actual cell types and compartmental synapse locations, rather than combining driver labels into a single hΔ population. Preserve dataset/sex differences between the female hemibrain and the downloaded male CNS.

Only after the neighboring literature is integrated should simulations ask which unresolved mechanism can account for the combined observations. Useful discriminating constraints include early versus late turning, persistence after odor loss, response to turning, and the effects of sparse versus broad activation. Merely reproducing upwind motion with a supplied wind vector would not resolve the biological gaps.
