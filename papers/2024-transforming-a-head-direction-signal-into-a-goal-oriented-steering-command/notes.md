# Westeinde et al. (2024): steering direction and error-dependent gain

Elena A. Westeinde, Emily Kellogg, Paul M. Dawson, Jenny Lu, Lydia Hamburg, Benjamin Midler, Shaul Druckmann and Rachel I. Wilson. **Transforming a head direction signal into a goal-oriented steering command.** Nature 626, 819–826. [Paper](https://doi.org/10.1038/s41586-024-07039-2). [2025 author correction](https://doi.org/10.1038/s41586-024-08245-8).

Full 33-page PDF, all five main and ten Extended Data figures, Methods, four-page reporting summary and one-page correction read and visually inspected. Coverage is logged separately. These notes distinguish experimental findings from the proposed downstream mechanism; no simulations have been rerun.

## Role in a complete behavior

A fly pursuing a bearing must correct small deviations accurately and turn out of large errors quickly. This study asks how the same heading/goal system can handle both regimes. PFL3 supplies the bilateral steering bias, while PFL2 is recruited near the opposite-to-goal heading and can increase rotational speed. The proposed DNa03 pathway lets a symmetric PFL2 input amplify an existing asymmetric PFL3 signal.

The behavior is spontaneous directional walking in a visual virtual environment, with cue jumps that disturb orientation. There is no food-location learning, remembered two-dimensional destination, displacement test or direct measurement of goal-memory storage. The goal is generally inferred from behavior. Common goal input to the three PFL populations is a model assumption motivated by anatomy, not a complete functional identification of its source.

## Variables and circuit organization

| Object | Representation or role |
|---|---|
| θ | Current heading relative to the visual cue; positive is clockwise/rightward |
| θg | Desired bearing, inferred from directional walking in most analyses |
| θ0 | Flexible offset between internal heading coordinates and the cue |
| PFL3R/L | Cells named for right/left **axon output**, not PB dendrite side |
| PFL2 | Bilateral-output population; heading map shifted approximately 180° |
| S | Model scale of total heading-plus-goal input; proposed relation to steering commitment |
| A | Model amplitude of goal input relative to heading input; distinct from S |
| ρ | Length of the mean heading unit vector; consistency of direction, not direct memory strength |

The PFL3 heading maps are shifted ±67.5°, not ±90°. Together with PFL2's 180° shift, the three axes approximately cover three sectors; “approximately 120° apart” is not exact equilateral geometry. Anatomy is hemibrain v1.2.1, not our MaleCNS reconstruction.

## Math in complex-exponential form

Let \(h=e^{i(\theta-\theta_0)}\) and \(q=Ae^{i(\theta_g-\theta_0)}\). At neural coordinate φ, define

\[
z_\delta=e^{i\delta}h+q,\qquad
u_\delta(\phi)=\operatorname{Re}[z_\delta e^{-i\phi}]
=\frac{z_\delta e^{-i\phi}+\overline{z_\delta}e^{i\phi}}2.
\]

The model assigns δ = +67.5° to PFL3R, −67.5° to PFL3L and 180° to PFL2, then computes

\[
r_\delta(\phi)=f(Su_\delta(\phi)).
\]

The amplitude of the summed input pattern obeys

\[
|z_\delta|^2=1+A^2+
A\left[e^{i(\theta-\theta_g+\delta)}+e^{-i(\theta-\theta_g+\delta)}\right].
\]

Thus each population detects alignment between a differently rotated heading phasor and the same goal phasor. For PFL2, δ = π, so the input amplitude is smallest at the goal and largest opposite it. PFL3R and PFL3L peak at oppositely offset errors. A nonlinear transformation followed by summation across neural coordinates turns this amplitude difference into a difference in total population output. A linear f would simply cancel the zero-mean spatial inputs; it cannot perform this goal-dependent comparison.

The ideal directional component has the familiar form

\[
\dot\theta\propto\operatorname{Im}(e^{i\theta_g}e^{-i\theta})
=\frac{e^{i(\theta_g-\theta)}-e^{-i(\theta_g-\theta)}}{2i}.
\]

But this paper focuses on the **gain and dynamics around that computation**, not merely this formula.

### Why symmetric PFL2 output can change directional steering

Write xR and xL for summed PFL3 activity and b for common PFL2 input. The indirect branch is schematically

\[
y_R=f(wx_R+vb),\qquad y_L=f(wx_L+vb).
\]

For a small difference Δx = xR − xL around mean x,

\[
y_R-y_L\approx w f'(wx+vb)\Delta x.
\]

This is an explanatory local expansion of the proposed mechanism. Common excitation increases the sensitivity to the left–right difference if it moves the receiving cells into a region with greater slope. With linear f, b cancels exactly; symmetric excitation has no effect on the difference. Nonlinearity at DNa03 is therefore a substantive requirement, not a cosmetic implementation detail.

In the full model,

\[
D3_{R/L}=f\left(\sum_j P3_{R/L,j}+4\sum_j P2_j\right),
\]
\[
D2_{R/L}=f\left(\sum_j P3_{R/L,j}+12D3_{R/L}\right),
\qquad \dot\theta\propto D2_R-D2_L+\epsilon.
\]

The weights 1, 4 and 12 are approximate relative values motivated by synapse counts, not measured unitary conductances. Within a connection type the weights are equalized. PFL3 reaches DNa02 directly and through DNa03; PFL2 contributes to the latter branch bilaterally.

### Model implementation details that should not disappear in a cartoon

The model uses 1,000 units per PFL population and 1,000 goal units for a quasi-continuous representation. The authors report that discretizing to twelve units per PFL population preserves their conclusions, but this is not the individually reconstructed 24-PFL3-cell model used by Pires.

All model cells use the same effective activation function: inputs are rescaled over the modeled range to [−1,1], passed through ELU (M for M ≥ 0, e^M − 1 otherwise), and outputs rescaled to [0,1]. These normalizations and the common transfer function are modeling choices, not identified homeostatic mechanisms. The authors report qualitative robustness to sigmoid/ReLU substitutions.

Closed-loop simulations update at 10 Hz. They include Gaussian steering noise filtered at 2 Hz and rescaled; the same frozen noise is used for different S values in Figure 5d. The Methods describe the rescaled noise using angular units, so exact units and time-step conversion should be checked against the public code before reproduction. The discrete update and its effective delay matter when interpreting oscillations at high gain.

A deterministic symmetric model still has zero bilateral difference exactly at the anti-goal. PFL2 increases gain around this unstable point; noise or another asymmetry initiates escape. It does not magically specify a left/right choice at exact opposition. Similarly, an instantaneous continuous-time first-order proportional controller does not itself overshoot: the oscillatory behavior is a property of the implemented feedback dynamics. The model illustrates the benefit of error-dependent gain, not a uniquely established dynamical law of the animal.

## Main figures and evidential weight

### Figure 1: the behavioral reason to include PFL2

Flies on a ball keep different bearings relative to a bright bar. Cue jumps of ±90° and 180° occur every minute. Rotational **speed** remains high near the anti-goal, whereas a bare sinusoidal signed error signal approaches zero there. This motivates another mechanism. Distinguish speed |dθ/dt| from mean signed velocity: frequent turns in either direction can give high speed and near-zero mean velocity.

The model diagrams introduce common goal input and rotated heading maps; they are not recordings of identified goal cells. Figure 1g shows 56 fly epochs and Figure 1h reports 46 flies. The main text's phrase “map of space” refers here to angular coordinates.

### Figure 2: a direct PFL2 perturbation plus activity measurements

P2X2 expression and local ATP iontophoresis activate PFL2, verified with a simultaneous whole-cell recording. Twelve experimental and eleven control flies show increased rotational speed; flies walking forward tend to slow or step backward. Turn direction varies, consistent with bilateral output rather than a fixed directional command. Extended Data 4 provides all four pulse durations and sideways-speed measurements.

Calcium imaging in the PFL2-specific line (33 flies) shows a moving spatial activity pattern and amplitude that is higher around the anti-goal, associated with faster rotation and slower forward walking. Bump phase follows heading with the expected reversed neural-space convention. A sinusoid is fitted to extract amplitude and phase; that procedure does not independently prove an exact sinusoidal biological signal.

### Figure 3: PFL3 population steering bias, with mixed-driver limitations

The mixed driver labels PFL2 and PFL3. Its LAL signal peaks near the goal, unlike the PFL2-specific line; the authors therefore interpret it as dominated by PFL3. Right-minus-left activity varies with heading error and turning (23 flies), matching the opponent comparison model.

This is a supported attribution, not perfect genetic isolation. Extended Data 5 is central: the qualitative differences in bilateral sums and differences help justify the attribution, but do not give an exact numerical contamination fraction. Pires's independent PFL3 work provides useful convergence without making this experiment more cell-specific than it is.

### Figure 4: inhibitory heading input and nonlinear goal modulation

Whole-cell recordings show heading tuning and changes in inhibitory postsynaptic potential frequency after cue jumps while the fly is stationary. This supports the proposed largely inhibitory Delta7 contribution, consistent with Delta7 supplying roughly 80% of heading input. It does not directly identify every observed IPSP as a Delta7 event through paired recording or selective Delta7 perturbation.

Goal-related modulation of heading tuning is stronger at the spike-rate level than the amplitude of somatic voltage tuning. PFL2 tuning is strongest for preferences near the anti-goal; PFL3 shows the opposite offset structure. This supports nonlinear input-to-spike conversion. Unlike Pires's emphasis on electrotonically separated input compartments, the presentation here emphasizes a goal-dependent voltage bias followed by a common nonlinearity. These accounts are related, but their detailed compartmental interpretation should not be collapsed into one directly measured mechanism.

Cell identities were checked with fills: 12 PFL2 and 15 PFL3 among 30 recordings; three were other types. Figure 4f uses 11 PFL2 cells and 4g 15 PFL3. There is an IPSP sample-count inconsistency: the Figure 4d caption lists 22 cells, while the Methods say 20 of 27 qualified. Retain that discrepancy rather than invent a reconciliation.

### Figure 5: downstream model and behavioral-state dependence

DNa03 receives PFL3 and bilateral PFL2 input; DNa02 receives direct PFL3 and DNa03 input. The model's indirect branch increases steering gain most strongly at large error, permitting vigorous correction without the same high-gain oscillations near the goal. The PFL2-silenced comparison in Extended Data 1 is a **model ablation**, not an animal silencing experiment.

In recordings, corrected/high-consistency jumps show larger voltage changes than uncorrected/low-consistency jumps. Voltage changes precede turning by roughly 150–200 ms in the lag analysis. This is consistent with a premotor role, not proof that one recorded cell caused a particular turn. Corrected/high-ρ and uncorrected/low-ρ also differ in behavioral state, and the comparison does not independently manipulate S.

PFL2 amplitude modulation correlates with directional consistency (reported r ≈ 0.371). In this specific long-epoch analysis, the goal is inferred from the PFL2 amplitude minimum rather than from behavior. That model-based inference is useful for low-consistency epochs but must not be described as an independent FC2 goal measurement.

## Extended Data audit

| Figure | Why it matters |
|---|---|
| ED1 | Resolver geometry; shifting modeled goal shifts equilibrium; PFL2 removal is simulated, not experimental |
| ED2 | Mixed-line expression and cell fills; corrected PFL2-specific driver identity; specificity is regional, with other expression outside CX |
| ED3 | Cue-jump imaging averages, differing baseline state, and signed response to ±90° jumps |
| ED4 | All ATP pulse lengths, voltage verification, controls, forward/rotational/sideways effects |
| ED5 | Evidence for PFL3 dominance in the mixed LAL signal; PFL2's approximately symmetric activity |
| ED6 | Unsubtracted voltage/rate curves retain offsets hidden by normalization in main Figure 4 |
| ED7 | Jump-response timing and control for differences in distance to preferred heading; supports state modulation but does not identify its source |
| ED8 | Reducing overall input scale S versus reducing goal amplitude A can produce different low-consistency patterns |
| ED9 | Raw and normalized fluorescence: normalization changes amplitude differences but does not create all observed modulation |
| ED10 | Behavioral segmentation and inferred switches of goal; the algorithm is not a direct readout of an internal decision |

## Preparation and analysis assumptions

Female flies, head and body fixed, wings removed, on a 9-mm ball. Imaging animals are 20–72 h posteclosion; patching animals 16–30 h. Bar width is 7.5°, closed-loop yaw gain 0.7. The rear region has reduced bar height rather than the same full rear visual gap used in Pires. Jumps alternate +90°, 180°, −90° in a fixed sequence after at least 15 minutes of acclimation.

FicTrac runs at 60 Hz; volumetric imaging at 6–8 Hz. Patch data are acquired at 20 kHz, low-pass filtered at 5 kHz, junction-corrected by −13 mV, then downsampled for analysis. One region is imaged per ten-minute epoch, not simultaneous PB/FB/LAL. PB and FB bump amplitudes are pooled in several analyses. Nine FB ROIs and ten PB ROIs are used for PFL2, which should not be mistaken for twelve functionally proven identical columns.

Fluorescence uses a low-decile baseline, then median/MAD normalization rather than ordinary mean/standard-deviation z-scoring. Goal and consistency use heading unit vectors within a 30-second window, excluding near-stationary time and the five seconds after jumps. Segmentation uses ρ = 0.88, with robustness checked over 0.70–0.98. Single-cell goal-binned tuning lowers the threshold to 0.7. A corrected jump means return within 30° for ±90° jumps or 60° for 180° jumps within ten seconds; latency analysis uses a different, faster-response selection.

No experimenter blinding or formal prospective power calculation. Samples, cells, jumps and time points are distinct units. Raw experimental data are available on reasonable request according to the paper; analysis/model code is public at [Wilson lab repository](https://github.com/wilson-lab/WesteindeWilson_AnalysisCode). Reading is complete without claiming raw-data reproduction.

## Correction and document inconsistencies

The 11 March 2025 correction identifies the PFL2-specific line as **VT007338AD;VT044709DBD**, replacing the erroneous VT033284AD;VT007338DBD label. The local main PDF already has the corrected ED2c and stock-origin paragraph, but the old label persists in its reporting summary and part of the Figure 1 genotype list. Use the correction and validated expression description, not an arbitrary copied string. The correction changes driver documentation, not the computational conclusion.

## What remains unanswered for navigation to something remembered?

1. Where is the goal written, stored and recalled? The common goal population is abstract in this model; FC2 is supplied by the companion paper, with its own storage caveats.
2. What changes S or A? Tangential inhibition, goal amplitude, motivation and exploration are proposals. Low ρ can also reflect switching among goals, not weak commitment to one goal.
3. Does DNa03 actually implement the required gain modulation? Wiring supports convergence, but the needed transfer function and state-dependent amplification require further functional evidence.
4. How are anti-goal escapes selected? Symmetric gain needs asymmetry/noise to pick a direction; unilateral sensory inputs and other steering systems may contribute.
5. How are speed, backward steps and turning coordinated in natural locomotion? Activation affects several kinematic variables, and the current model chiefly predicts rotation.
6. How are stored locations converted into a changing goal bearing after translation? This paper does not perform that transformation.
7. How are heading and goal codes kept aligned during cue remapping? The model shifts both together with θ0. A mechanism protecting remembered goals from drift is proposed, not shown.

## Consequence for the synthesis and later connectomics

Add an error-dependent gain branch to the heading/goal comparator. Preserve DNa02/DNa03, output laterality, input compartments, transmitter evidence and individual connections when examining MaleCNS. Do not infer the proposed nonlinearity simply from a high synapse count. Read upstream goal-learning/odor-persistence work and the descending-neuron studies before interpreting this as a complete food-seeking controller.
