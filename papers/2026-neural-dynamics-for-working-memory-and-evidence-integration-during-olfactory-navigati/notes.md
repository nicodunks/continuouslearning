# Kathman et al. (2026): maintaining a navigational intention through odor gaps

[Paper](https://doi.org/10.1038/s41467-026-75945-2), Nature Communications 17:9082. Nicholas D. Kathman, Aaron J. Lanz, Jacob D. Freed and Katherine I. Nagel. Main article, all figures, scientific supplement and peer review read; exact coverage in [reading log](reading-log.md).

## Contribution to a complete behavior

An odor encounter does not continuously specify what to do. The fly must sometimes keep walking in a useful direction after odor disappears, and sometimes abandon that direction to search. This paper identifies persistent, spatially localized activity in fan-shaped-body local neurons associated with the first behavior. Repeated odor encounters also contribute to activity over a longer window than immediate locomotor changes. Silencing reduces persistent upwind behavior.

This supplies a short-term intention-maintenance component. It does not establish a remembered food location, a distance-to-food variable, or a procedure for returning to a previously visited place from a new position. It also does not establish the recurrent mechanism of persistence: that is the subject of the Lanz follow-up cited in the discussion.

**Identity matters:** most recordings use broad VT062617-Gal4, predominantly labeling hΔK. Do not propagate the older hΔC attribution from Matheson without its addendum. The specific hΔK split is VT062617AD; VT037223DB (SS63158). The peer response also mentions hΔF in the broad line and negative imaging results not shown here; these are not a substitute for the follow-up's cell-specific measurements.

## Experimental chain and figures

### Figure 1: odor recruits activity that can outlast the stimulus

Head-fixed, hungry female flies walk on a ball. A rotating nozzle supplies wind with direction coupled to turning, while odor can be controlled separately. VT062617 dorsal FB projections show a localized activity bump during odor; individual bouts can persist after odor offset. Persistence durations across 82 qualifying bumps from 14 flies are fit with an exponential time constant of 5.59 ± 0.55 s. This is a distribution of termination times, not a demonstration that each bump amplitude decays exponentially with that constant.

Bump presence is associated with less variable heading and lower angular speed. Around bump termination, heading departs from the odor-period goal. These observations support maintenance of a directional state, but do not alone determine whether the bump causes straight walking, is maintained by straight walking, or participates in a reciprocal loop. The later silencing experiment supplies causal evidence for a contribution.

### Figure 2: activity position is not a straightforward heading readout

The bump is relatively stable while heading changes. Pooled heading/bump correlation is 0.043 (p=0.22); per-fly means show a small positive correlation, 0.095 (p=0.03). Thus “no heading relationship whatsoever” would overstate the result.

During a ±90° wind rotation, eight selected responding trials in four flies show a mean heading displacement of 25.41° (p=0.006), versus 9.87° for bump position (p=0.072). This supports a goal interpretation over a directly tracking compass interpretation. It does not show a full 90° compensation, and a nonsignificant bump displacement does not prove perfect invariance.

The proposed explanation is that wind rotates the compass reference frame while the goal bump stays fixed within neural coordinates, producing a steering error. EPG movement was not simultaneously measured here. Distinguish this inferred mechanism from the measured wind/behavior/VT062617 relationship.

### Figure 3: history dependence in a virtual turbulent plume

The fly's fictive position indexes a movie of an actual near-surface plume. Concentration is adaptively compressed and converted into binary odor delivery. Individual encounters can have little immediate effect, while repeated exposure accompanies a rising bump amplitude. Activity can continue across gaps. During bump-off periods the fly deviates more from its prior goal; the angular-speed comparison in this plume assay is not significant (p=0.12), whereas goal deviation is (p=0.01, eight flies).

A multivariate linear-filter analysis separates first-order correlations with odor, forward velocity and absolute angular velocity. The odor filter is positive and broad over preceding seconds; forward velocity has a narrower positive association; turning is negatively associated. This is evidence of history-dependent odor contributions after accounting for those measured covariates. It is not identification of a unique neural evidence accumulator or proof that activity literally encodes odor encounter frequency. The authors explicitly removed their frequency-encoding claim after additional analysis during review failed to support it.

### Figure 4: another local population has different fast dynamics

Broad 52G12 ventral local neurons have transient rather than strongly accumulating responses. Their mean odor-filter peak half-width is 5.29 s versus 8.1 s for VT062617 (five versus six flies, p=0.03). Their angular-speed association is positive rather than negative. The same apparatus and behavioral correlations do not inevitably produce the persistent pattern.

Both populations also show slower trial-to-trial relationships between activity and upwind behavior. This leaves room for engagement/internal state to modulate both circuits. It does not mean both populations implement the same memory.

### Figure 5: silencing affects persistence more clearly than initial orientation

Free-walking flies receive 500-ms odor pulses at 1 Hz in approximately 12 cm/s wind. Wild-type upwind-orientation probability grows with pulse count and persists after the train. Broad VT062617 silencing reduces post-odor upwind orientation after 1, 5 and 10 pulses. Initial upwind behavior is relatively preserved.

Specific hΔK split-line silencing requires higher light intensity and produces a significant post-odor reduction only after 10 pulses (p=0.0079; one pulse p=0.5399, five p=0.065; Bonferroni threshold 0.017). Supplementary Table 2 gives experimental N=23/24/24 and controls N=26/28/29. The main caption's sample-size wording is less clear and must not be treated as interchangeable with this table. Broad-line time courses and paired summary panels also have differing reported counts.

The specific result supports an hΔK contribution; it does not establish that hΔK explains the entire broad-driver phenotype. Incomplete inhibition and additional cells are both possible. Upwind orientation is a heading-within-90°-cone metric, not distance traveled to a source.

### Figure 6: persistence can help a specified search controller

A three-state model alternates baseline walking, goal-directed upwind walking, and local search. Odor initiates/reinitiates the goal state; after odor loss the controller leaves it stochastically. Too-short persistence causes premature search in ordinary within-plume gaps; too-long persistence can carry agents past the source. In this particular plume/controller/objective, 6.4 s is best among the tested values, close to the measured 5.59 s.

Crucially, success is **fraction of time within 15 mm of the source**, not probability of first arrival or time to first arrival. A model that lacks source recognition can be penalized for overshooting even after it has found the source. The paper therefore demonstrates a useful persistence scale under its assumptions, not a universal optimum for flies. The locomotor distributions are only approximately matched; overlap of mean confidence intervals does not establish equality of full distributions.

## Computation and math, using exponentials

### A directional intention plus its persistence are different variables

For interpretation, write a goal as q(t)=R(t)e^{iφ(t)} and heading as h(t)=e^{iθ(t)}. A steering comparator can use

    Im[q conjugate(h)] = R Im[e^{i(φ−θ)}].

This is our compact connection to the PFL steering literature, not an equation fitted to these recordings. The paper primarily measures bump amplitude/presence and peak-column position. It does not derive the comparator or prove that fluorescence amplitude R represents confidence, accumulated probability, or distance.

Persistence could preserve φ while R stays appreciable, then terminate the intention. Maintaining φ is not integrating displacement. Remembered position would require an additional quantity such as p(t)=∫v_world(t)dt and a target p*, with the desired direction obtained from p*−p(t). No such positional memory is demonstrated here.

### Exponential bout durations versus leaky analog memory

If the goal state has a constant post-odor escape hazard 1/τ, its survival is

    Pr(T > t) = e^{−t/τ}.

A population of abrupt on/off bouts can therefore have an exponential duration distribution even if an individual bout has roughly constant amplitude before switching off. This is distinct from assuming R(t)=R(0)e^{−t/τ} for each bout.

The model uses discrete p_leave=1/(τ_p f_s), f_s=15 Hz. Thus after n eligible steps the survival is (1−p_leave)^n, approximately e^{−n/(τ_p f_s)} for small p. Fresh odor prevents the post-odor escape. Search returns to baseline with probability 0.01 per frame, giving mean 6.67 s. These phenomenological switching rules are imposed; they are not emergent dynamics of an hΔK/PFG circuit in this paper.

### The stimulus already has temporal processing

At 100 Hz, measured plume concentration C_i is converted using

    x_i = C_i/(C_i + A_i + β),     β=0.025
    A_{i+1} = A_i + (C_i−A_i)/500
    odor_i = 1[x_i > 0.5].

A has a five-second adaptation scale. At 15 Hz the model uses 75 samples for the same nominal time. This processing defines what the animal experiences and matters when interpreting neural history dependence; the delivered stimulus is not the original continuous concentration movie. The movie represents a plume measured 6 mm above a surface in 10 cm/s flow.

### Locomotor controller

Five DN-like units have a saturating nonlinearity

    a(x) = 20/(1+e^{−x/4}) − 10.

Their recurrent matrix has diagonal 0.8, stop-unit couplings −0.03, and cross-side couplings 0 in baseline/goal versus −0.035 in search. In the goal state the imposed directional input can be written

    u_next = a(Mu + [1,1,0,−1,−1]^T Im[e^{i(θ−ψ)}]
                  + [0,0,−0.1,0,0]^T + noise).

The upwind target ψ is supplied to the model. It has not learned a food site or derived the wind bearing from modeled sensory neurons. The public wrapper additionally gives baseline a weak directional bias of the opposite sign. Positive stop-unit activity suppresses both forward and angular movement.

### Equations checked against public code

Read-only inspection of [author repository](https://github.com/nagellab/Kathmanetal2025), commit `371dc9de7a26edb0de4ee79b077a09283ac3a2eb`; no simulations run.

- Printed Eq. 11 uses sums for angular output, despite the text saying differences. `run_nav_simulation.m` uses `diff(U([1 5]))` and `diff(U([2 4]))`: angular output is 0.1(U5−U1)+0.2(U4−U2). Forward output is 0.7 max(0,U1+U5)+0.3 max(0,U2+U4). The printed coefficient table also assigns units inconsistent with the definitions. The wrapper integrates angular output as radians/s, while positions are updated in plume pixel coordinates; its variable comments should not be accepted as a complete unit audit.
- Printed Eq. 7 places λ outside the reciprocal. `computebumpfilters copy.m` actually also uses `1./diag(s) + lambda`. This is not ordinary ridge regularization 1/(s+λ), and does not suppress divergence at small singular values. Do not silently repair the equation in a reproduction or claim a robustness audit has been done.
- The Methods' wording about absolute heading is ambiguous. `Fig1ij-bumptrig_offonly_pulse_cntrlcomp.m` defines `goalhead = abs(heading - mean(heading(odor interval)))`, not abs(abs(heading)−goal). This remains a difference from an arithmetic mean, not explicitly a wrapped circular error in that line.
- The figure-six driver currently has `ntrials = 5` and calls `FSCnavmodel_altplumes`; the paper reports 500 trials per τ. The public wrapper is useful for interpreting operations but is not by itself a frozen, fully verified recreation of the published run.

## What the supplements add

**Supplementary Figure 1:** straight-run durations are longer post odor than at baseline (fit scales 8.8±6.7 versus 2.5±0.3 s); these are behavioral duration fits, separate from neural persistence. No-air motor controls argue against nozzle movement alone causing the bump. Two stained brains contain 38 and 39 labeled cell bodies. Across-fly bump-duration variation is substantial. Bumps beginning post odor do not show a significant pre-versus-during heading-variability reduction, unlike those beginning before/during odor. The aligned bump profiles are narrow, peaked and variable across flies.

**Supplementary Figure 2:** individual odor filters show broad but heterogeneous histories. Forward speed rises around bump onset (2.13 to 3.60; p=0.046), and during odor it is higher with a bump (p=0.032). This cautions against describing bump amplitude as purely sensory.

**Supplementary Figure 3:** 52G12 labels many more cells (179 and 212 in two brains), with transient responses and no corresponding increase in straightness during bump periods. It is a broad population comparison, not a perfectly matched single-type negative control.

**Supplementary Figure 4:** specific hΔK silencing's modest high-light effect is visible mainly after 10 pulses. Constant anemometer traces across odor on/off argue against a wind-speed transient explaining the response. The wind-speed plot uses 8/16/33 cm/s, whereas Methods says 8/25/33; retain this discrepancy. Pooled correlations with wind speed are significant but the reported ANOVA comparisons are not.

**Tables/reporting:** exact lines, software and per-condition statistics are supplied. Stimuli were randomized within blocks; analyses were automated without genotype blinding. Reporting form is dated October 2025 and is not fully synchronized with the final paper's details (including antibody inventory).

**Peer review:** the persistence estimate changed from 7.8 to 5.59 s with stricter bump selection; odor-frequency encoding was withdrawn; wind-frame and goal-direction-versus-location interpretations were explicitly debated. Reviewers also challenged the model's overshoot penalty and incomplete locomotor match. Author statements about unpublished hΔF measurements and prolonged wind-tunnel running should remain attributed statements rather than independently evaluated datasets.

## Methods that constrain interpretation

Imaging uses 7–12-day-old females starved approximately 24 h; free behavior uses 3–7-day-old females starved 18–24 h. Imaging samples dorsal projections at 4–8 volumes/s with GCaMP7f. Eight hand-drawn putative columns, max-Z projection, motion correction and a lowest-three-percent fluorescence baseline are used. Peak position is an argmax after one-second temporal and two-column spatial smoothing, not a first-harmonic phase fit.

Bumps must exceed mean+0.5 SD, last at least three seconds, and gaps shorter than three seconds are merged. Post-odor persistence includes only bumps beginning during odor and ending after it. These choices and inclusion of only flies with sufficient walking/bump trials condition the measured duration distribution. Wind speed is selected per fly for useful upwind behavior and sometimes adjusted later. The motor clips fast rotations and can accumulate heading errors of up to roughly 90° within a trial. These do not erase the within-assay findings but matter for quantitative generalization.

Some statistics pool multiple bumps from each fly; others use per-fly means. They do not all have the same independent experimental unit. The paper's small wind-shift subset, broad drivers, calcium filtering and incomplete silencing all constrain the precision of circuit claims.

## Remaining questions and neighboring circuits

1. **Storage mechanism:** is persistence recurrent hΔK↔PFG activity, intrinsic cellular dynamics, slow synapses, or combinations? Follow Lanz's mechanistic paper rather than treating the present behavioral model as the answer.
2. **Writing and resetting:** what selects which direction enters memory, and why does turning erase or disengage it? Is turning a cause of reset, a consequence, or both?
3. **Readout:** which paths from hΔK/PFG to PFL steering carry goal phase, amplitude and state? How does this coexist with FC2's odor-boundary return representation in Siliciano?
4. **Reference frames:** when wind and landmarks disagree, which anchors heading and which anchors the remembered intention? Read Okubo and Basnak rather than equating all stable FB bumps.
5. **Evidence content:** what exactly is accumulated—recent odor occupancy, reliability of a heading, locomotor engagement, or another latent quantity? The withdrawn frequency result makes this distinction especially important.
6. **Perfect sinusoids:** this dataset does not show perfect sinusoids and does not require them for persistence. The narrow profile in Supplementary Figure 1g contains higher spatial harmonics. A downstream first-harmonic projection can still provide a useful phase; whether actual wiring performs that projection is a separate question. Amplitude, concentration and higher harmonics must not be conflated.
7. **Place memory:** neither short-term direction maintenance nor the model's upwind target supplies an updateable remembered location. Path integration and landmark-conditioned spatial learning remain separate reading branches.
8. **Arrival and revisits:** where does the system switch from approach to stopping/feeding, store a useful site, then return after departing? The model's failure to recognize arrival is a concrete missing link in the behavioral chain.

Connectomics can constrain recurrence, the separation of writing/gating/readout inputs, and neighboring memory circuits. It cannot determine the slow effective synaptic dynamics or task-dependent gating from synapse counts alone. Later simulations should target those unresolved alternatives after reading the relevant physiology and behavior.
