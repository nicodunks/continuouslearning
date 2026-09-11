# Kim, Rouault, Druckmann & Jayaraman (2017): Ring attractor dynamics in the Drosophila central brain

[Paper](https://doi.org/10.1126/science.aal4835) · [Combined article and supplement PDF](main.pdf) · [Reading coverage](reading-log.md) · [Authors' model and inference code](https://github.com/hrouault/RingAttractor)

## Contribution to the behavioral account

This paper tests the mechanism that maintains an angular state. It goes beyond observing a heading-related bump: localized optogenetic excitation writes a new EPG population state, suppresses the previous state, and leaves an activity bump that persists or drifts after the imposed excitation ends. The experiments support a recurrent attractor in which EPG neurons participate, with effective local excitation and long-range competition favored by the tested perturbations and models.

That is a mechanism for maintaining a current heading representation. It is not a mechanism for storing multiple food locations, computing displacement to one of them, or deciding which target to pursue. A heading attractor and a goal-memory attractor can share dynamical ideas while encoding different variables and having different inputs and outputs.

## Preparation: a useful dissociation, with limits

Four-to-six-day-old female flies express GCaMP6f, with or without CsChrimson, using split-GAL4 SS00096. Their head and body are tethered for flight; front legs are removed and the proboscis is immobilized. A 330° azimuth by 60° elevation display is controlled by left-minus-right wingbeat amplitude. The display's azimuth is mapped to 360° for analysis. In darkness, the accumulated wingbeat-amplitude difference generates a virtual scene trajectory, not a measurement of actual body rotation.

The important contrast with Seelig & Jayaraman's walking preparation is that tethered flight in darkness produces persistent EPG activity that is largely uncoupled from the motor-derived virtual heading. The authors suggest missing normal haltere feedback as one explanation. They do not directly test that explanation. It would be incorrect to conclude that freely flying flies cannot integrate angular motion in darkness.

This relative uncoupling makes the experiment useful: the investigators can manipulate and observe the internal state with reduced interference from self-motion-driven updating. It also means that successful persistence in this assay is not a demonstration of a complete functioning flight compass under natural conditions.

## Figures and causal logic

### Figure 1: persistence and visual tracking during flight

The activity is generally a single localized bump in single-bar, complex-scene and dark conditions. Its position tracks visual orientation in closed loop, with fly-specific offsets. In darkness it persists but has little average correlation with the accumulated motor-derived heading. The estimated bump width is roughly a quarter of the ring, with inter-fly variability. Ten flies contribute to the visual comparisons.

The separation of persistence from motor updating is the main experimental opportunity, not a minor negative control. It allows the subsequent tests to ask what the recurrent network does when its state is overwritten.

### Figure 2: overwrite the state and suppress its competitor

The same two-photon beam alternates low-power imaging scan lines and high-power localized stimulation lines. Exciting a small EB region increases activity there and reduces activity at the original bump, including remote positions. Once stimulation stops, the new bump can remain. The main single-spot analysis includes 405 trials from 13 flies; these are repeated observations within flies.

The suppression is a functional interaction. The experiment does not identify a direct inhibitory EPG-to-EPG synapse. Other cells and multi-synaptic loops can implement the effective competition.

A critical supplemental test drives two EB locations directly, holding one stimulation power constant and increasing the other. The stronger second stimulus suppresses the reference response. Because both populations are directly stimulated, this is more informative than merely showing that a sensory-evoked bump disappears: suppression cannot be explained solely by turning down the old visual input.

### Figure 3: why persistence alone is insufficient, and drift helps

A simple winner-take-all network could preserve one active state, but its winners have no privileged relationship to neighboring angular positions. The paper instead observes predominantly small, continuous changes in bump position after optogenetic release. Artificially induced states acquire dynamics resembling spontaneous states.

The first approximately 0.5 s after stimulation is special: CsChrimson off-kinetics hold the state closer to the stimulated location. Later drift is compared separately. Drift distributions with and without CsChrimson are not significantly different in the reported later-window comparison; the early post-stimulus distribution differs. The statistical statement is consistency, not proven identity.

The inference is that EPG activity participates in the recurrent state. It does not establish that EPG cells alone form the complete attractor or that intrinsic cellular mechanisms make no contribution. Purely cell-autonomous persistence or a passive echo of slowly decaying visual input cannot readily explain the full combination of overwriting, competition and spatially organized drift.

### Figure 4: distinguish effective connectivity by response to displaced input

A small visual displacement often makes the existing bump flow toward the new position. A larger displacement more often creates a new bump while the old one disappears—a jump. Both tested local and global connectivity models can show both outcomes. Merely observing jumps does not distinguish them.

The more discriminating experiment stimulates narrow 22.5° wedges sequentially. It asks how much input is required for a jump when initial and target states are 90° versus 180° apart. The laser-power threshold is not significantly different between these distances (paired P = 0.102; 14 comparisons from ten flies). The effective input is also estimated from the ratio of stimulated to post-stimulation bump amplitude, mostly near the natural amplitude and well below the strong-input requirement of the illustrated global model. An additional supplemental protocol includes 135°.

The local model has an approximately flat inhibitory background far from the old bump; a remote target therefore faces a similar threshold at different distances. In the global model, inhibition varies with angular distance, producing stronger distance dependence. These results favor narrow effective excitation with broad inhibition within the analyzed model family and calibration assumptions. A nonsignificant threshold difference is not an equivalence test, and several amplitude estimates are sparse or variable.

## What the supplementary figures add

| Figure | Details needed for interpretation |
|---|---|
| S1 | Alternative bump-count and width analyses, single-bar example, and visual/dark amplitude comparison. The mean visual/dark peak-amplitude ratio is about 1.6 ± 0.105 SEM across ten flies. This supplies an indirect constraint on input strength, not a measured synaptic current. |
| S2A–B | Scanner dwell time and dose response. Illumination is spatially nonuniform, and dose response is calibrated in non-flying trials at a superficial EB location. Laser power cannot be translated into equal neural drive everywhere without controls. |
| S2C–D | No-CsChrimson controls. Some fluorescence drop when the bar disappears comes from visual-display light leaking into the detector; it is not all neural suppression. |
| S2E | In a dedicated assay retaining the closed-loop stripe, optogenetic shifts increase absolute turning. The analysis includes 47 stimulated and 98 control trials from ten flies and reports P ≈ 0.00018 for 1–2.5 s. The relation between signed bump displacement and signed turning is variable, not a deterministic compensatory-turn law. |
| S2F | The bump's peak activity persists after stimulation, allowing its position to drift. Selecting the most active ROIs at each time measures persistence of a bump somewhere, not persistence in the same cells. |
| S2G | Two-site direct stimulation establishes functional competition more specifically than sensory-to-opto replacement alone. |
| S3 | Makes the competing model assumptions explicit: arbitrary winners, broad angular interactions, or local interactions with global inhibition. Cartoon edges are effective interactions, not reconstructed synapses. |
| S4A–B | Explores input width/strength, jump probabilities and assumed trial-to-trial variability. The result is conditional on input statistics. |
| S4C–E | Documents manual near-threshold stimulation and pairing across initial positions; adds 90°/135°/180° comparisons. |
| S4F–G | Local models themselves have parameter regimes requiring much stronger input. Weak input can coexist with the original bump as a second, externally driven bump; uniqueness refers to the autonomous persistent state, not every forced configuration. |
| S4H–I | Expands the connectivity family to differences of two von Mises profiles plus a constant. This is a broader parameter exploration, not an exhaustive test of every biophysical circuit. |

The main text says behavior is not significantly perturbed and points to S2E as a qualification. The notes should retain the actual distinction: the targeted stripe-fixation assay does find increased turning. It selects stable fixation before stimulation, continuing flight, and successful neural shifts. Controls are later stable periods from the same flies. This establishes a behavioral effect under those selections, not universal navigation necessity or a fully characterized goal comparator.

## The dynamical mathematics in exponential notation

### General recurrent model

For activities \(r_n\) on a ring with periodic indices, the model takes the form

\[
\tau\dot r_n=-r_n+\left[\sum_m K_m r_{n-m}+1+I_n\right]_+,
\qquad [x]_+=\max(x,0).
\]

The rotationally invariant convolution \(K\) is an assumption about effective interactions. It is not derived from a connectome here. Mirror symmetry is also assumed in the autonomous model; this paper is primarily about retention and input-driven replacement rather than the asymmetric velocity drive needed for path integration.

On a linear, fully active background, the angular modes are complex exponentials,

\[
v_n^{(k)}=e^{2\pi i kn/N},\qquad
\widehat K_k=\sum_m K_m e^{-2\pi i km/N}.
\]

Convolution multiplies each mode by \(\widehat K_k\). For a perturbation within that linear regime, growth rates are \((\widehat K_k-1)/\tau\). This is the spectral reason regular spatial patterns can arise from regular connectivity. Rectification changes the active set, so this linear statement is not a complete solution of the localized nonlinear bump.

### Local excitation, global inhibition

The local discrete model is

\[
\tau\dot r_n=-r_n+
[\alpha r_n+D(r_{n-1}+r_{n+1}-2r_n)-\beta S+1+I_n]_+,
\qquad S=\sum_m r_m.
\]

For nonzero angular mode \(q=2\pi k/N\), the local interaction contributes

\[
\alpha+D(e^{iq}+e^{-iq}-2).
\]

Uniform inhibition acts on the zero mode. Local positive feedback can destabilize a uniform representation while the inhibitory pool limits total activity. Thresholding then supports a spatially bounded bump. This is a proposed generative mechanism for a smooth activity profile; the sensory input need not arrive as a perfect sinusoid.

In the continuum model, inside an active region the stationary equation becomes

\[
D r''+(\alpha-1)r=\beta S-1.
\]

With \(\omega=\sqrt{(\alpha-1)/D}\), one single-bump solution centered at \(\theta_0\) is

\[
r(\theta)=A\left[1+\frac{e^{i\omega x}+e^{-i\omega x}}{2}\right],
\quad x=\theta-\theta_0,\quad |x|\leq\pi/\omega,
\]

and zero outside that support, using the appropriate circular coordinate around the center. Its total activity is \(S=2\pi A/\omega\), giving

\[
A^{-1}=1-\alpha+2\pi\beta/\omega.
\]

The supplement gives existence conditions \(\alpha>1+D\) and positive \(A^{-1}\). The first places the bump within the ring; the second prevents an unbounded positive-feedback solution in this threshold-linear model. Width, gain and inhibition are linked, not freely interchangeable parameters.

This function is a localized branch of exponentials plus a constant, cut off outside its support. It is not a pure first harmonic over the entire ring. Its phase can be decoded as discussed in the Seelig notes, but that does not imply all higher spatial harmonics disappear.

### Attractor geometry versus storage accuracy

If the equations are exactly translation invariant, every shifted stationary bump is also a stationary solution. The family \(r_0(\theta-\theta_0)\) forms an angular manifold. Perturbations changing shape can decay, while the phase direction is neutral. Noise projected along that direction produces drift; external landmarks can anchor it.

Thus, persistence and drift are compatible. A persistent bump is not a perfectly accurate memory. Discrete neurons, heterogeneous weights and modulation can introduce preferred positions or errors. Demonstrating an approximately continuous family in the biological circuit does not prove exact mathematical rotational symmetry.

### Why displaced inputs flow or jump

A broad displaced input overlaps the existing active population and creates a spatial gradient that shifts it. A narrow weak remote input may fail to displace it; a stronger remote input creates a competitor that wins through inhibition. The local model can temporarily sustain the original bump and a weaker input-supported bump. At the loss of that two-bump solution, the old bump disappears.

The supplementary derivation integrates across the localized input to relate its strength to a slope discontinuity. It then determines the largest drive that permits coexistence. Close to a particular local-model phase boundary, the required stimulated/natural peak ratio approaches six. Consequently, not every local model matches the observed low threshold: the experiments constrain its parameter regime as well as its broad architecture.

The global example instead uses

\[
K(\theta)=J_0+\frac{J_1}{2}(e^{i\theta}+e^{-i\theta}).
\]

This convenient first-harmonic kernel produces bumps after rectification but imposes an angular dependence on the suppressed population. The experiment tests consequences of that particular effective interaction, not the general utility of Fourier representations.

## Supplementary theory and inference: assumptions to keep visible

The visual jump-probability comparison uses a Gaussian distribution over input widths and strengths and accepts modeled probabilities within 0.1 of the measurements. The authors explicitly report that **other assumptions—including different input statistics, slower input dynamics, or relaxed fit criteria—allow the global model to reproduce that probability curve too**. The optogenetic comparisons provide additional constraints; the visual probability curve alone is not a unique identification.

To classify multiple simultaneous bumps, the analysis fits mixtures of von Mises profiles. A one-angle PVA would be inadequate: two antipodal bumps can cancel or create an intermediate apparent angle. The likelihood penalizes squared fluorescence error, with a prior penalizing extra bumps and a temporal-coupling prior favoring nearby positions in adjacent frames. Those priors directly influence bump counts and continuity.

The supplement calls the method Bayesian sampling but also acknowledges that transition probabilities do not exactly obey detailed balance and uses inverse temperature five to concentrate near high-score states. Its output should not be treated as an exact calibrated posterior over neural configurations. The existence of priors does not invalidate the result, but independent activity images and threshold-based checks remain important.

Jump/flow classification uses a 45° continuity threshold over four consecutive time points. Trials with stopped flight or noisy configurations are excluded. The drift analysis excludes failed/noisy initial states, including early multiple-bump configurations and zero-bump epochs. Reported drift proportions therefore describe the retained cases.

Laser jump thresholds are the average of the two lowest successful powers after manual adjustment, with a minimum number of successful trials. They are not independently fit 50%-success psychometric thresholds. For amplitude normalization, the same ROI is measured 1–1.5 s after stimulation; cases drifting more than 30° are excluded. These are sensible controls for expression variability but also define the subset supporting the model comparison.

## Targeted equation-to-code checks

The authors' repository was read at commit `2b7b3dc08e0ca191d05796424087497264ceec26`; it was not executed. This is a targeted check of the dynamics, parameter conventions and inference implementation, not a reproduction of the published results.

- `deriv_fft` implements convolution, adds baseline one and external input, rectifies, then subtracts the current rate. It therefore clarifies the threshold-linear dynamics where the printed theoretical notation is inconsistent.
- The local implementation weights global inhibition by angular spacing and the discrete Laplacian by inverse spacing squared. Raw discrete weights and continuum parameters should not be equated without that normalization.
- The public parameter driver uses 256 discretization points. Its cosine coefficients are −0.2 and 0.15, whereas the methods print −8 and 6. Both ratios agree, but their absolute mapping requires attention to discretization/normalization and the version used; this reading does not certify that the public defaults reproduce Fig. 4.
- The simulation helper named `vonmises` uses a peak-scaled profile and, for lower concentration, an affine-shifted version. The bump-fitting code instead uses a properly normalized von Mises density. The same name does not mean the same amplitude convention.
- The inference code's temporal coupling greedily matches nearby bumps one to one across adjacent frames using circular distance. The printed equation sums all cross-time pairs. The code uses coupling width \(2\pi/16\), one ROI, whereas the text describes 0.5 as half an ROI without a consistent angular convention. These differences matter for reproducing jump/flow classifications.
- The code allows at most four bumps and updates their widths within a concentration range of two to six. The textual move list does not describe width updates. The authors' observation of at most two inferred bumps is not simply a hard two-bump software cap.

There are also visible mathematical reporting issues. The printed global stationary profile uses a Heaviside symbol alone where a rectified amplitude is needed for a graded bump. One localized-input expression mixes its variable phase with the threshold phase in the denominator. These should be checked algebraically before reuse rather than copied into a new simulator.

A more substantive convention issue is width: experimental Fig. 1 uses FWHM, while the simulation methods state a 90° zero-to-zero width. For the local branch above, support width is \(2\pi/\omega\) and FWHM is \(\pi/\omega\). They differ by two. This reading flags the mismatch and does not claim a resolved quantitative match of those definitions.

## Remaining questions and connections

1. **Which cells implement effective excitation and inhibition?** The perturbation infers a functional kernel. The angular-integration and ultrastructure/connectome literature is needed to identify its multi-cell implementation.
2. **How is the state moved by real self-motion?** This tethered-flight assay largely removes that coupling. A maintained angle without a calibrated velocity input will not support navigation through darkness.
3. **How robust is the phase to anatomical heterogeneity?** Exact ring symmetry is assumed mathematically. Finite, irregular biological connectivity must still support sufficiently accurate states and updates.
4. **How is state-dependent amplitude controlled?** Amplitude fluctuates during flight and changes with flight state. It is not solely a scalar readout of visual input power or directional certainty.
5. **How is a remembered goal compared with the compass?** S2E indicates behavioral consequences, but does not identify the selected goal or downstream signed-error computation.
6. **How do multiple memories coexist?** Global competition is useful for one current heading. It would erase multiple simultaneous targets if naively reused without separate storage, context or gating.
7. **How do visual reference changes preserve old goals?** Replacing the current heading state does not automatically transform stored goal bearings or integrated displacement.

The productive role of later connectomics is to turn the effective interactions into cell-specific candidate mechanisms, then ask which structural alternatives remain consistent with the perturbations. The graph should constrain that inference alongside physiology, rather than be treated as an independently sufficient decoder of navigational function.

## Supplementary assets still requiring follow-up

All 42 pages of the combined PDF—including every scientific figure, Methods, full theoretical supplement, references and all eleven movie captions—were read and inspected visually. Movies S1–S11 themselves remain unavailable locally: the attempted publisher movie endpoint returned HTTP 403, the legacy Janelia download site timed out, and a targeted web search did not locate a mirror. Their captions are evidence about the authors' intended demonstrations, not a substitute for viewing the movies. This access gap remains open in the reading log.
