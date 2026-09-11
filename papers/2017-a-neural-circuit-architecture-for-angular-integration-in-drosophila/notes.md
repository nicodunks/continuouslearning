# Green et al. (2017): a circuit architecture for angular integration

Source: [Nature, DOI 10.1038/nature22343](https://doi.org/10.1038/nature22343); [complete author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC6320684/). The manuscript title uses “neuronal” where the publication uses “neural.”

## What this contributes to a complete navigation account

This paper identifies anatomically shifted pathways that can update an internal estimate of facing direction when a fly turns. It separates two P-EN subtypes whose similar projections conceal different activity phases and timing. Silencing impairs compass tracking in darkness; local activation moves the heading representation in the anatomically predicted direction.

That is a component of navigation, not a destination memory. The task contains no learned food site, displacement vector, route choice or return journey. Its value for our larger question is to constrain how the current-heading input to a navigation controller gets updated. It also exposes a concrete failure of anatomy-only reasoning: projecting bridge activity through the known arbors does not reproduce the measured ellipsoid-body activity.

## Preparation and measurement

Young female flies walk on a 6.35-mm, approximately 42–46-mg ball while tethered for two-photon imaging. FicTrac measures spherical rotation at 50 Hz. A closed-loop bright bar supplies a distant landmark, or the display is dark. The cylindrical display covers 270 degrees, retaining a 90-degree gap in the virtual world. This differs from experiments that rescale the visible arena to a full circle; angles should not be pooled without checking conventions.

EPGs are targeted with R60D05. VT032906 is called P-EN1; VT020739 and R12D09 target P-EN2. These are historical driver-based distinctions, not a guarantee that every labeled neuron belongs to one modern connectomic type. Multicolor tracing and double labeling support the distinction but show off-target cells and some overlap. The manuscript's anatomical figures look from posterior, placing the left bridge on the left. Movie orientation is separately qualified in the manuscript, so it must not silently set the sign of circuit diagrams.

GCaMP measures compartment-dependent calcium, not spikes or released transmitter. Volumes are averaged across planes; most recordings are translation-registered, while simultaneous EB recordings are not. ROI baseline is the bottom 5% of fluorescence values. Independent z-scoring facilitates comparisons but removes information about absolute amplitudes.

## Figure-by-figure evidence

### Figure 1: all three populations track heading

EPG, P-EN1 and P-EN2 activity has two or three periodic peaks across the bridge. A Fourier component with an eight-glomerulus period gives a phase that follows virtual heading. Closed-loop offsets can stay stable for minutes but vary across flies. Example trajectories illustrate tracking; across-fly correlations quantify it.

This is not evidence that all three populations encode the same variable in all compartments. A phase decoder can track heading despite different spatial profiles and gain. The number of peaks reflects duplicated angular organization of the bridge, not multiple remembered destinations.

### Figure 2: shifted anatomy meets turn-related asymmetry

With the revised column numbering, EPGs project without a column shift while left-bridge P-ENs shift +1 and right-bridge P-ENs shift −1 on the EB representation. A right turn preferentially activates right-bridge P-ENs, appropriately positioned to move EPG activity counterclockwise in the figure's coordinate convention. Left turns give the opposite imbalance. EPG bridge activity is much less lateralized by turning.

The crucial ingredient is a direction-dependent imbalance between oppositely shifted pathways. Anatomical overlap alone does not specify the synaptic sign, efficacy, recurrent stability or speed of the resulting phase motion.

### Figure 3: subtype and compartment matter

Simultaneous EPG/P-EN imaging shows P-EN1 roughly in phase with EPG in the bridge, but P-EN2 approximately in antiphase. Mapping those bridge profiles through the anatomical projections predicts a broadened P-EN1 peak and a P-EN2 valley at the EPG peak in the EB. The measured EB profiles instead have sharp activity peaks for both subtypes.

During turns, P-EN1 is biased toward the leading edge of the EPG bump and P-EN2 toward the trailing edge. Straight-walking profiles differ from turning profiles. This supports different contributions to bump dynamics but leaves local transformation of signals between compartments unexplained.

Weak red signals led to explicit exclusions: eight of 22 P-EN1 EB flies were excluded, leaving 14; the P-EN2 EB comparison has 11 flies. Bridge comparisons include 20 P-EN1 recordings and 12 P-EN2 recordings with one weak recording excluded. These are selected measurable calcium populations, not equally observable samples of every neuron.

### Figure 4: temporal ordering and necessity

P-EN1 asymmetry precedes movement of the **neural heading phase**; P-EN2 asymmetry follows it. Both can follow the fly's physical turning by hundreds of milliseconds. “P-EN1 leads” must not be translated into “P-EN1 commands the behavioral turn.”

Temperature-sensitive shibire in three P-EN driver lines reduces heading tracking in the dark at 32°C relative to 22°C and parental controls. At 34°C activity becomes too dim/diffuse for reliable decoding; 32°C deliberately gives a partial impairment. Thus the result is neither a clean frozen compass nor proof that these are the only updating pathways. Some neural movement remains.

### Figure 5: stimulation tests the projection direction

Local ATP application activates P2X2-expressing P-ENs in one or two bridge glomeruli. EPG activity changes at the corresponding shifted location. Both P-EN subtypes produce the same anatomically medial response for a given stimulation location. This does not contradict their proposed opposing contributions during natural turns: their normally active bridge locations differ in phase.

ATP was titrated differently for P-EN1 and P-EN2 (0.5 versus 0.1 mM). Five flies per subtype contribute. No-ATP and no-Gal4 controls constrain nonspecific application effects. Phase-aligned averages include trials beyond the selected illustrative examples. This establishes a functional route with predictable spatial displacement, not its complete natural operating dynamics or monosynaptic implementation.

## Extended Data 1–10

1. Periodic bridge profiles, angular offsets and phase/behavior comparisons establish the basic heading measurement. Empirical spatial profiles need not be exact sinusoids just because a Fourier component decodes them.
2. Additional examples support heading tracking in the different cell populations and conditions; they are not separate goal-memory tests.
3. Driver expression and anatomical context constrain which labeled cells can contribute to the measured signal; driver names cannot replace tracing.
4. Original versus revised numbering clarifies the +1/−1 projection rule. Synaptotagmin supports presynaptic specializations in EB and noduli. Multicolor flip-outs provide single-cell tracing, with unresolved or color-assigned branches marked rather than silently treated as definitive.
5. Turn-related bridge asymmetry persists in darkness. This establishes a nonvisual contribution but does not identify proprioception versus efference copy.
6. Open-loop short-lived random-dot optic flow evokes asymmetry even during epochs with little turning. Turning along with the dots reduces the response, consistent with visual and nonvisual contributions opposing one another under this manipulation. Seven flies per subtype are shown. The dots are designed to separate visual motion from a stable positional landmark.
7. Double labeling distinguishes the P-EN1 and P-EN2 populations while showing imperfect genetic separation. R12D09 strongly overlaps VT020739; its overlap with VT032906 is smaller.
8. Imaging bridge and EB in the same P-EN populations confirms the discrepancy between anatomical projection and measured terminal profile. It is not merely a two-color comparison across unrelated flies. Simultaneous red and green EPG recordings control for a simple indicator-induced spatial displacement.
9. EB recordings reproduce subtype-dependent leading/trailing asymmetry relative to EPG phase movement. Cross-correlations to behavior must be distinguished from cross-correlations to the neural phase. Individual-fly traces reveal variability hidden by the average.
10. Visual tracking under shibire is less consistently affected than dark tracking, but VT020739 does show impairment; the correct claim is not universally intact visual tracking. ATP and genetic controls accompany the local stimulation experiments.

## Supplementary discussion: qualifications central to the mechanism

The proposed sequence is a behavioral turn, arrival of asymmetric signals, shifted excitation, and movement of the EPG peak. Additional inhibition is explicitly needed to keep excitation from spreading the peak indefinitely. Its implementation is not established here.

P-EN1 GCaMP6m phase can lag behavior by about 600 ms, versus about 300 ms for P-EN2 and EPG. The authors suggest calcium buffering from multiple indicator copies may slow the circuit itself. This is a plausible explanation, not an independently measured correction. Simultaneous measurements with different indicators support the relative P-EN1-before/ P-EN2-after ordering.

The proposed P-EN2 “brake” is explicitly speculative. It requires something to stop, potentially continued bump motion, rather than following automatically from the wiring. Other proposed roles include task-dependent modulation and a heading-to-travel transformation. The observation of a more sinusoidal P-EN2 bridge signal motivates the latter possibility but does not demonstrate it. The later PFN/hΔC travel-vector circuit must not be retroactively attributed to this P-EN2 speculation.

The bridge has nine glomeruli per side: EPGs primarily occupy the inner eight, P-ENs the outer eight. A perfectly closed, translation-invariant ring is therefore not directly the measured anatomy. The discussion proposes additional EPG-like cells for the outer-glomerulus gap and Δ7 neurons for indirect antiphase coupling, potentially also helping close that gap. These are anatomically motivated candidates, not causal results from this paper.

The authors distinguish an internally constructed heading estimate from an explicit steering-wheel command. Long behavioral-to-calcium lags favor that distinction here, although later downstream effects on behavior remain possible. Their occasional stimulation-associated turns are not a quantified complete steering account.

## Supplementary Table 1: all three pages

VT032906: 45 traced cells, 41 classified consistent with P-EN and 37 unambiguous. Two cells instead have PFN-like FB/NO2V anatomy; other rows are unresolved or anomalous. VT020739: 43/43 consistent and 32 unambiguous. R12D09: 38/41 consistent and 36 unambiguous. Rows 5 and 29 have Δ7-like bridge-local anatomy, while row 37 lists another bridge-local morphology. The caption's statement about 2/41 local neurons should not erase that third row; it appears to refer to the two matching local examples rather than fully summarize every non-P-EN entry.

“NI” means not identifiable, not anatomical absence. Asterisks mark EB tiles assigned by color when the axon could not be traced. There are minor apparent transcription anomalies, including VT032907 in one otherwise VT032906 row and an unusual tile assignment in the R12D09 table. They should not be converted into new circuit rules without checking original tracing data.

## Mathematics in complex form

The following is an explanatory reduction, not a quantitative model fitted in this paper. Let the first harmonic of a ring population be

\[
Z=\sum_j r_j e^{i\phi_j}=A e^{i\theta}.
\]

If \(A>0\), then

\[
\dot\theta=\operatorname{Im}(\dot Z/Z),\qquad
\dot Z=i\omega Z
\]

for ideal constant-amplitude heading integration. Anatomical shifts of ±δ applied to the represented bump yield feedback terms

\[
\dot Z\supset (a_+e^{i\delta}+a_-e^{-i\delta})Z.
\]

The phase-moving component is

\[
\dot\theta\supset (a_+-a_-)\operatorname{Im}(e^{i\delta}).
\]

The common component instead changes amplitude and must be balanced by the rest of the network. A sign-convention change reverses which anatomical side is called positive; it does not change the need for opposite shifts and a turn-dependent imbalance.

If the source harmonic is antiphase, it is multiplied by \(e^{i\pi}=-1\). The same anatomical shift can then exert the opposite phase tendency. This illustrates why equal axonal projections need not imply equal natural computational effects. It is **not** a complete account of P-EN2: its measured EB profile is reshaped relative to its bridge profile, so literal propagation of the bridge harmonic is contradicted by the data.

More generally write a bump as \(r(\phi)=\sum_n c_n e^{in(\phi-\theta)}\). Extracting the first harmonic estimates phase without requiring every higher harmonic to vanish. A localized sharp bump naturally includes higher harmonics. For Lyu-style vector arithmetic, the important additional question is which harmonics survive the biological projections, nonlinearities and readout. Decoding an angle with a Fourier transform is not proof that the circuit performs a mathematically exact first-harmonic computation.

## Analysis choices that limit interpretation

Phase is obtained by an eight-glomerulus Fourier component, with missing middle positions filled using the periodic organization; phase traces are smoothed. Correlations use selected lags: approximately 0.6 s for P-EN1 and 0.3 s for EPG/P-EN2, and 0.2 s in the fast-indicator shibire experiments. For some asymmetry plots a lag is chosen to maximize the relationship. These analyses describe delayed tracking, not zero-lag sensory estimates.

Only sufficiently active walking epochs enter some quantitative analyses: forward speed at least 1 mm/s and a threshold on the strongest ROI fluorescence. Weak or stopped states therefore cannot be assumed to have the reported tracking quality. Turning events use smoothed velocity and minimum size, duration and separation criteria.

Several plotted signal gains are rescaled for illustration, including hand-chosen or fitted factors. Apparent overlap is not proof of unit integration gain. No complete mechanistic simulation or archived source-code reproduction was performed in this reading.

## Remaining questions and links to neighboring circuits

- Which neurons generate the nonvisual angular-velocity signal, and how is its gain calibrated across walking, flight, speed and load?
- What transforms P-EN calcium profiles between bridge and EB, particularly the apparent phase inversion/reshaping of P-EN2? Compartment-specific synapses, inhibition and intrinsic conductances are candidates, not interchangeable explanations.
- Which loops stabilize a stationary heading versus translate it, and how do they close the real bridge's anatomical boundary?
- How do visual landmarks reset the estimate without invalidating a stored goal or displacement vector in the previous frame?
- Which downstream comparison uses heading, and how is that comparison gated by odor, hunger, search and remembered reward?
- Is a given returning behavior driven by remembered place, an accumulated displacement, a preferred bearing or external marks? Nothing in this task discriminates those possibilities.

Read alongside Turner-Evans et al. (2017) for electrophysiology and a quantitative rate model, Kim et al. (2017) for attractor perturbations, and later functional/connectomic ring studies for actual recurrent pathways. Preserve their different preparations, genetic access, compartment measurements and sign conventions. The shared shifted-loop idea is strong; a complete set of identical experimental claims is not.

## Coverage

Complete author-manuscript main text, Methods, captions and reference list read. All five main and ten Extended Data images visually inspected. All six supplementary PDF pages read and visually inspected, including all three table pages. All seven publisher movie descriptions read; 24 evenly spaced frames from each movie inspected. Movies 2/3, 4/5 and 6/7 are normal/half-speed presentations of the same respective examples, not six independent experiments. Movie 1 uses fast EPG calcium imaging; the others show EPG, P-EN1 and P-EN2 GCaMP6m examples.

The main PDF remains an acquisition gap; complete HTML and original figure images are saved instead. The seven movies are locally downloaded but ignored by Git. Sampled inspection is not continuous frame-by-frame viewing. No public peer-review file was acquired.
