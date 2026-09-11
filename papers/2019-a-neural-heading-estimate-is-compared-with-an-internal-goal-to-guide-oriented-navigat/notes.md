# Green et al. (2019): A neural heading estimate is compared with an internal goal to guide oriented navigation

[Article](https://doi.org/10.1038/s41593-019-0444-x) · [Author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC7688015/) · [Saved HTML](main-fulltext.html) · [Scientific supplement](41593_2019_444_MOESM1_ESM.pdf) · [Reading coverage](reading-log.md)

## The behavioral computation established here

A walking fly can select a bearing, keep it relative to a distant visual cue, and correct disturbances. This paper supplies causal evidence that the internal compass participates in that correction: displacing the E-PG heading estimate in darkness elicits turns that would restore its previous value, together with reduced forward speed.

The target in this task is an angular bearing. The flies receive no training to reach a virtual two- or three-dimensional destination, and there is no remembered food site. The authors explicitly state that the physical goal representation is not identified. Their “goal” is inferred from persistent behavior and perturbation responses. This makes the paper a bridge from heading estimation to steering, rather than a complete account of navigational memory.

## Preparation and operational definitions

The principal experiments use 1–3-day-old females, food deprived for 8–16 hours, with heated water or saline over the head and upper thorax. Main experiments use approximately 34°C; the Methods describe at least 30°C, with 26°C controls for temperature-sensitive silencing. These conditions encourage sustained walking and plausibly dispersal from an unfavorable location. The paper does not show that the same motivational state or bearing-selection process governs return to a rewarding site.

A head-fixed fly walks on an air-supported ball while an 11.25° bright bar moves in rotational closed loop with gain one. The display spans 270° horizontally, leaving a ninety-degree rear gap in which the bar disappears. The gap is retained, unlike the compressed angular coordinates in Fisher's electrophysiology. Head pitch, plate and ball occlusion leave roughly 45–50° of the nominally 81°-high bar visible, likely in the dorsal visual field. Calling it a potential celestial cue is an interpretation, not a measured natural identity.

The mean heading vector is computed from unit vectors over sliding windows, usually sixty seconds, shifted in one-second increments. Samples with forward velocity below 0.5 mm/s are omitted for this stability measure so standing still does not count as purposeful orientation. This is a time-weighted heading concentration, not net displacement divided by path length and not a distance-to-target measure.

For perturbations, the “goal” is approximated by the circular mean heading or E-PG phase over the ten seconds before the manipulation. Trials must have circular standard deviation below 45° in this interval: approximately 90% of bar-jump trials and 77% of neural-stimulation trials qualify. No forward-speed requirement is applied to the principal perturbation plots. A stable pre-perturbation bearing is evidence of a current preference, but may not equal the latent goal on every trial.

## Main figures and causal logic

**Figure 1 — sustained arbitrary-angle fixation.** Fourteen wild-type flies walk for meters in virtual trajectories while maintaining different bearings relative to a bright bar. Individual flies can change their preferred direction slowly or abruptly. Across sixty-second windows, heading vectors concentrate near the edge of the unit circle. In darkness, long-window stability declines even though short-timescale turning and forward-speed distributions look similar. The cue improves persistent orientation rather than merely making all walking faster or less variable at every timescale.

**Figure 2 — the fly corrects position errors, not just visual motion.** Abrupt ±90° bar rotations are followed by turns that tend to return the bar to its former angular position. A 180° jump and reappearance after thirty seconds of darkness also evoke correction. These manipulations go beyond a reflex that cancels only instantaneous bar velocity. Forward speed declines after perturbation, especially when the deviation is large.

The return is not universal. Supplementary Figure 3 separates 129 trials that return within thirty degrees in the ten-to-thirty-second window from 165 that do not, across the combined jump dataset. Failed or incomplete corrections can reflect low engagement, the cue landing in the blind gap, a changing goal, or a mismatch between pre-jump heading and the true internal goal. The illustrative movie should not be mistaken for a near-perfect success rate.

**Figure 3 — turning and speed vary with angular error.** The authors pool behavior before and through correction to estimate motor responses across error angles. Signed turning changes direction across the goal; forward speed is highest near alignment and lower farther away. Each heatmap column is normalized separately because occupancy is concentrated near zero error. A bright column is thus a conditional velocity distribution, not evidence that all error angles are equally sampled.

**Figure 4 — E-PG phase represents current heading in this behavior.** During bar jumps, the E-PG phase follows the cue, while behavior indicates that the chosen bearing remains approximately unchanged. The E-PG-to-landmark offset therefore stays near its original value across 78 rotations in 22 flies. A goal signal would instead remain fixed while the cue moved. Supplementary Figure 5 extends the dissociation: when flies spontaneously choose a different maintained bearing, the E-PG-to-cue calibration remains similar. This argues against identifying E-PG phase with either the desired heading or current-heading-minus-goal.

**Figure 5 — normal E-PG output is needed for arbitrary bearings.** Temperature-sensitive shibire expression in three E-PG driver lines degrades E-PG phase tracking and sustained arbitrary-angle fixation. The population still has calcium activity, and some visually driven phase-velocity correlations remain, but accumulated angular tracking is poor. Behavior retains a bias to keep the cue in front, suggesting that simpler fixation can be supported by additional pathways.

The evidence should not be summarized as every comparison being independently significant: one comparison with the 77E05 driver-only control has P = 0.08. The overall convergence across lines, physiology and behavior is the relevant pattern. General slowing also complicates interpretation of reduced turning; the supplement addresses this explicitly.

**Figure 6 — coherent neural displacement tests the sign of the controller.** In complete darkness, the authors express the ATP-gated channel P2X2 in P-ENs and puff 0.5 mM ATP onto one or two PB glomeruli for 20–50 ms, about two minutes apart. This shifts E-PG activity bilaterally to a position medial to stimulation. Seventeen experimental flies and fifteen controls are studied.

The fly tends to turn in the direction that would restore the previous neural phase. This distinguishes a negative-feedback controller from the idea that rotating the neural heading representation directly commands a corresponding physical rotation like a steering wheel. Stimulation side alone does not predict turn direction; the displaced phase relative to its starting phase does. Forward speed decreases too, with larger effects for larger phase displacement.

This is P-EN stimulation with an E-PG readout, not selective direct E-PG perturbation. The authors could not obtain physiological bilateral repositioning by stimulating E-PGs at one PB location. They also avoided optogenetic light because it could change behavior in control flies. P-EN and E-PG phases are coupled, so these experiments do not uniquely identify the precise population read by every downstream controller.

**Figure 7 — a common error-dependent response.** Motor responses plotted against displacement from the prior E-PG phase resemble responses to visual-scene rotations. Together with the silencing results, this favors a compass-dependent comparison in both light and darkness. Calcium and behavioral measurements are smoothed, and lags are selected to maximize the response: approximately 350 ms from visual error versus 100 ms from neural phase error. These are approximate analysis optima, not clean measurements of individual synaptic delays.

**Figure 8 — hypotheses, not a reconstructed circuit.** Pure retinal template matching could explain visible-cue behavior but cannot by itself explain responses to a neural displacement in darkness. A comparison between estimated heading and an internal goal can explain both, possibly aided by visual matching. The authors also leave open that a two-dimensional position/vector comparison could produce the observed angular behavior. No downstream goal-storage cell class is established in this paper.

## Supplementary figures and tables

**S1** derives the heading-concentration analysis and compares bar and darkness over many window lengths. Stable local walking statistics do not ensure long-term orientation. **S2** shows that stimulus contrast and airflow can change behavioral mode. Tall dark bars promote front- or anti-fixation; bright bars support arbitrary-angle fixation. High ventral airflow, enough to flutter wings, increases front fixation of dark bars. Pin-tethered flies use a different 330° arena, fifteen-second analysis windows and unmeasured laser heating. These conditions should not be treated as interchangeable with the main preparation.

**S3** includes half-turn jumps, success/failure distributions and cue return after thirty seconds of darkness (167 traces from twelve flies). Successful trials begin with faster forward walking than failures, despite similar preceding angular variability. **S4** selects trials with less than 20°/s change in turning around a half-turn jump; forward slowing remains. This supports separable speed regulation rather than slowing being entirely a mechanical consequence of turning.

**S5** analyzes thirty goal-switching events in eleven flies and supports the interpretation of E-PGs as current heading. **S6** verifies the physiological effects of shibire at 26 versus 34°C. Visually driven phase velocity can remain correlated with cue velocity while phase position drifts badly; velocity correlation is therefore an insufficient measure of compass integrity. The displayed pairwise P values are not multiplicity-corrected.

**S7** shows reduced virtual dispersal and heading stability over multiple windows. **S8** shows residual correction when the goal cue is in front, with much worse correction for side bearings. This is an important neighboring behavior: visually directed fixation need not require the same circuit operation as arbitrary-angle menotaxis.

**S9** is essential for interpreting motor effects. After matching pre-jump forward speed, reduced turning in E-PG-impaired flies is no longer distinguishable from controls (P = 0.87 and 0.34 for the two jump directions). Matching excludes about 78% of control and 18% of impaired trials. The difference in slowing persists for half-turn jumps (P = 0.01), but the ninety-degree comparison is P = 0.065. The conclusion is therefore not that every motor-response difference survives speed matching.

**S10 and Table 1** characterize the three E-PG drivers. There is an internal count discrepancy: the S10 caption says 46 of 48 labeled cells are unambiguous E-PGs, but Table 1 lists 26, 15 and 17 cells, totaling 58, with 24 + 15 + 17 = 56 unambiguous. Two 27F02 cells have unusual cross-side wedge/glomerulus assignments. The table and caption are both preserved; the precise total should not be silently reconciled. Some cells innervate demi-wedges, relevant to assumptions about uniform angular tiling.

**S11** shows relatively stable neural phase despite behavioral drift in darkness. That is consistent with a fly trying to hold an internally estimated bearing while the estimator drifts relative to the world. Stability alone would not establish active correction, which is why the perturbation experiment matters. A labeling discrepancy remains: panel c says a thirty-second window, whereas its caption describes sixty seconds.

**S12** controls for stimulation side and genotype. ATP stimulation raises mean E-PG fluorescence by about 23% in experimental flies; it is not a mathematically pure phase rotation at fixed amplitude. Controls initially have weaker co-injected dye signals, but selecting control puffs with comparable dye intensity still shows no measurable E-PG increase. The angular dependence of turning and slowing supports the phase-based interpretation while amplitude and the stimulated P-EN pathway remain possible contributors.

**Tables 2–3** list all experimental timing, fly counts, drivers and stock origins. The P-EN driver is VT032906. The reporting summary describes no exclusions except unhealthy flies; the article and supplement additionally specify trial-selection criteria and exclusions in speed-matching analyses. Reading “no exclusions” as “every recorded trial appears in every plot” would be wrong.

All four movies were inspected through their complete captions and 24 evenly spaced frames each. Movies 1 and 2 show the same fly maintaining different bearings 24 minutes apart. Movies 3 and 4 show the same neural-stimulation example at normal and double speed. They view the fly from the front, reversing the displayed left/right PB relative to the paper's posterior convention; the two-second red stimulation marker is longer than the actual ATP pulse. This is sampled inspection, not frame-complete viewing.

## Mathematics in complex notation

Let the internal heading estimate and goal be

\[
H=e^{i\hat\theta},\qquad G=e^{ig},\qquad E=G\overline H=e^{i(g-\hat\theta)}.
\]

A simple controller consistent with the *qualitative* findings is

\[
\omega=k\operatorname{Im}E,\qquad
v_{\rm forward}=v_{\min}+k_v\frac{1+\operatorname{Re}E}{2}.
\]

These are explanatory equations, not a fit reported by Green et al. The data show sign- and magnitude-dependent responses; they do not establish these exact functions or prove that neurons literally multiply phasors. Anatomical and displayed angular conventions must be accounted for before assigning a sign to a measured turn.

If the internal estimate is experimentally shifted while G is unchanged, E rotates by the opposite amount and the controller initially turns to cancel the perturbation. At exactly opposite headings, this sine-like controller has no preferred turning direction. Noise, asymmetry or a nonlinear steering process must resolve the left/right choice. The half-turn experiments show eventual correction without proving an exact deterministic sine law at the antipode.

The behavioral concentration statistic is

\[
\bar Z_T=\frac1{N_T}\sum_{t\in T,\,v_f(t)\ge0.5\,\mathrm{mm/s}} e^{i\theta(t)},\qquad R_T=|\bar Z_T|.
\]

It measures stability over a window. A large R_T does not tell us where the fly is, how far away a goal lies, or whether the chosen bearing is rewarding.

For a remembered place x* and current position x(t), the relevant desired bearing would instead be

\[
G(t)=\frac{x^*-x(t)}{|x^*-x(t)|},
\]

with complex coordinates for positions in the plane. The paper does not measure x*, x(t), or the transformation that updates G(t) during travel. Its behavioral goal can remain constant without any place computation.

## Remaining questions and links to later work

Where is the goal stored, what selects it, why does it change, and how is its strength regulated? These questions lead to the later FC2/PFL studies and goal-memory work, rather than being answered by an E-PG activity bump alone. The thirty-second cue-removal result establishes short retention; days-to-weeks preferences require separate evidence.

A complete return-to-food behavior additionally needs a destination representation, displacement estimation, goal retrieval in a compatible reference frame and arrival detection. Even a perfect bearing controller cannot by itself supply those variables. The connectome can constrain candidate pathways carrying heading and goal signals to steering outputs, while the present perturbations constrain the required sign of feedback. It cannot identify the remembered place or the goal-selection rule from connectivity alone.

The main PDF remains missing after publisher and PMC attempts; the full author manuscript and all eight main figures are saved. The twenty-page publisher scientific supplement and three-page reporting summary are present and fully read. PMC lists an alternative DOC supplementary file that could not be retrieved; its publisher counterpart's twelve figures and three tables are all covered in the saved PDF. Code and raw data are available on request, and no request or independent reproduction was performed.
