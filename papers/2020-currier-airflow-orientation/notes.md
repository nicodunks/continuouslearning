# Currier, Matheson & Nagel (2020): airflow basis signals and corrective steering

[Published article](https://doi.org/10.7554/eLife.61510) · [Main PDF](main.pdf) · [Figures and supplements](elife-61510-figures-v2.pdf) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigation account

This paper identifies a plausible sensory input to navigation computations: two populations of fan-shaped-body neurons preferentially respond to airflow approximately 45° to either side of the fly. It also shows impaired stabilization of airflow-relative orientation when these populations are silenced. This supplies evidence about **airflow sensing and corrective action**, not a stored food location, accumulated displacement, or a learned destination.

The behavioral experiment is particularly important to interpret correctly. These are rigidly tethered flying flies controlling the direction of an airflow source through their wingbeat asymmetry. They orient **downwind in darkness without a food odor**. The physiology comes from awake, immobilized, non-flying flies. Neither experiment directly demonstrates walking upwind toward a remembered food source. Later work needs to explain how this sensory signal enters a different policy when odor, learning, locomotor state, and motivation change.

## Cell identities: avoid a misleading nomenclature shortcut

| Paper name | Hemibrain correspondence | Driver used here | Interpretation |
|---|---|---|---|
| P-F2N3 | PFNa | SS02255 | Ventral FB airflow population examined across columns |
| P-F1N3 | PFNm and PFNp | SS52244 | Another ventral population; driver does not separate the two hemibrain types |
| P-F3N2d | PFNd | SS00078 | Dorsal population in sensory survey |
| P-F3N2v | PFNv | SS52577 | Dorsal population in sensory survey |
| P-EN1 | P-EN1 | SS54295 | Compass-associated population |
| P-EN2 | P-EN2 | R12D09 | Compass-associated population |
| LNa | LAL–NO(a) | SS47432 | Candidate airflow input to PFNa through noduli |
| vFBN | Not confidently assigned in this paper | VT029515 | Antler-to-FB candidate input tested physiologically |

“Ventral P-FN” in this paper does **not** mean the named PFNv type. This distinction is essential when joining these results to Lyu, Lu, and the connectome. The methods explicitly identify PFNa and PFNm/PFNp by nodulus anatomy. Do not infer a confident modern vFBN identity from the broad name; the author response explicitly declines to provide one.

## Experiments and figures

### Figure 1: what reaches different central-complex populations?

Whole-cell recordings survey eight columnar types while presenting a stripe, airflow, airflow plus stripe, odorized airflow, and all three cues. Four stimulus directions are tested: front, rear, ipsilateral, and contralateral to the recorded cell. Simultaneous cues always come from the **same direction**. These are not cue-conflict experiments.

The ventral P-FNs respond especially strongly to airflow; adding odor has little effect on PFNa and a modest suppressive effect on P-F1N3. Strong airflow responses therefore cannot simply be relabeled attractive-odor responses. Other types show weaker or more diverse sensory responses. Responses are changes relative to baseline, and suppression contributes to the absolute response measure.

The supplementary baseline measurements show substantial differences between cell types in resting potential, input resistance, and rhythmic activity. P-ENs show prominent activity around 3 Hz; the ventral populations have different, less regular rhythms. These temporal rhythms are unrelated to the claim that a population profile across angular coordinates approximates a sinusoid.

Figure 1 supplement 2 shows individual-cell tuning and dynamic range, preventing the population mean from hiding heterogeneity. Supplement 3 supplies two example E-PG recordings: visual and airflow preferences can differ, and apparent lack of tuning under four-direction stimulation is not proof of absent sensory input.

### Figure 2: multisensory summation has a restricted meaning

At the population-average level, combined responses approximately follow sums of the constituent responses. Individual neurons vary substantially. P-EN2 responses are relatively consistent, whereas dorsal PFNs and extrinsic columnar cells use heterogeneous apparent combinations. Ventral PFNs remain airflow dominated.

The response-similarity analysis correlates concatenated time courses across stimulus directions, comparing airflow-plus-stripe with airflow alone and stripe alone. It includes both the stimulus and the post-stimulus period. A point near the diagonal means equal correlation with the two component traces. **This alone does not identify linear synaptic weights**: the component traces can already be correlated, and correlation ignores scale and offset. Figure 2A's direct comparison to a summed response is a separate, more direct population-level test.

Supplement 1 extends the similarity analysis to all eight types. PFNv includes negative stripe correlations, showing why a universal fixed additive rule would overstate the result. The study does not establish how inputs combine when wind and landmarks disagree, or after closed-loop learning establishes a stable compass offset.

### Figures 3–4: a pair of airflow preferences, not an angular map

PFNa and P-F1N3 show excitation for ipsilateral frontal airflow, suppression for contralateral/rear airflow, and in some cases rebound after airflow ends. Detailed PFNa sampling uses eight directions in 12 cells. Preferred directions cluster around 45° ipsilateral despite differing anatomical columns. One recorded cell is from the other hemisphere; the bilateral picture is not supported by equally large independent samples on both sides.

The tuning curves are not perfectly identical. Frontal responses and hyperpolarization differ somewhat across column groups; response dynamics range from transient to sustained. The authors treat these column-dependent differences cautiously. The preferred-angle summary is a response-weighted circular vector, not a demonstration that the entire response function contains only one Fourier harmonic.

What is established is shared open-loop airflow tuning across sampled columns. What is **not** established is that these cells never carry heading information. They receive PB input, and the open-loop preparation may fail to stabilize a compass-to-cue relationship. A conjunction of heading and body-relative airflow remains compatible with the results.

### Figure 5: where does airflow enter?

Two candidate input routes are examined. VT029515 vFBNs receive input in the antler and project to ventral FB. Trans-Tango labels regions characteristic of PFNs downstream, but these vFBNs are not strongly directionally tuned for airflow. They are consequently a poor explanation of the directional selectivity by themselves.

LNa calcium responses, measured in five flies, show directional tuning with the opposite sign to the PFNa population receiving their nodular output. The hemibrain provides anatomical support for the connection; an example body examined was 1508956088. Contralateral LNa input to a PFNa could generate PFNa's opposite preference through inhibition. **The inhibitory functional connection is a hypothesis here**, supported by connectivity and opposing tuning, not demonstrated by a selective perturbation of that synapse.

Figure 5 supplement 1 is a projection image: Trans-Tango signal appears in PB, FB layers 1–3, and NO layers 2–3. It supports a candidate relationship but is not a resolved synapse-by-synapse identity or proof that this is the directional-input source.

### Figure 6: a behavioral need for the targeted populations

Kir2.1 silencing of either restricted ventral-PFN driver impairs downwind stabilization. The broader R44B10 driver produces the most conspicuous phenotype on several measures. E-PG silencing does not produce the same deficit in this assay. Typical group sizes are 11–12 flies.

The important comparison is **behavior-specific necessity**. E-PG independence for this particular downwind task does not make the compass unnecessary for all navigation. Nor does a phenotype from PFN-targeting drivers demonstrate a full path from sensory input to motor output.

Figure 6 supplement 1 explicitly shows weak off-target R44B10 expression in mushroom bodies, ventrolateral protocerebrum, and subesophageal zone. Reviewers additionally questioned other PFN labeling. Three alternative broad lines proved lethal with constitutive Kir2.1. Thus the strongest phenotype cannot be assigned exclusively to the two desired PFN classes. Restricted-driver effects support their involvement, but do not erase broad-driver and developmental confounds.

### Figure 7: selecting an appropriate turn versus being able to turn

The experiment interrupts airflow or imposes brief rotations of its direction. Control flies turn to correct imposed directional slips; R44B10-silenced flies have an approximately zero average corrective response. Controls correct roughly 45% of large slips and 90% of small slips. Effects for individual restricted drivers are weaker than the broad-driver effect.

Responses to airflow cessation remain, as do broad distributions of wingbeat asymmetry and integrated slip responses. This argues for a deficit in coupling the sensory situation to the correct turn direction rather than simple paralysis. However, nonsignificant distribution comparisons do not prove every elementary sensory and motor process is intact.

The quantitative response is integrated for five seconds after a slip. Pooling left and right slips can preserve a broad distribution even when the association between slip direction and turn sign is lost. That is exactly why the signed corrective fraction adds information beyond the pooled distribution.

### Figure 8: two routes into the central complex

The proposed organization branches airflow information from antennal pathways through AMMC, wedge, and LAL. One route through ring neurons can anchor the E-PG compass, drawing on Okubo et al. (2020). Another through LNa reaches ventral PFNs with bilateral basis-like tuning. The schematic combines evidence from multiple papers; this paper does not independently establish every arrow.

A useful synthesis is that the same physical cue can serve two computations: a reference for heading, and a body-relative directional input. That does not yet say which downstream circuit chooses downwind, upwind, or a remembered goal.

## The math, using complex exponentials

The following reconstruction is an explanatory idealization, **not a model fitted by this paper**. Let body-relative airflow be

\[
w=s e^{i\delta},\qquad u_+=e^{i\pi/4},\quad u_-=e^{-i\pi/4}.
\]

The two real Cartesian projections onto these orthogonal axes are

\[
a_+=\operatorname{Re}(w\overline{u_+}),\qquad
 a_-=\operatorname{Re}(w\overline{u_-}).
\]

Because the axes differ by 90°,

\[
w=a_+u_+ + a_-u_-.
\]

There is no factor of one-half in this two-axis reconstruction. But it depends on **signed, calibrated projections**. Biological firing rates would require a baseline and gain, for example

\[
r_\pm=b_\pm+g_\pm a_\pm+\epsilon_\pm.
\]

The decoder must compensate for baselines, gains, and non-projective tuning. Firing-rate suppression can carry a negative baseline-subtracted quantity even though spikes themselves cannot have negative rates. If a model instead uses only two nonnegative front-facing channels with no baseline compensation, their positive weighted sum spans a cone; it cannot automatically represent every direction in the plane. This matters when comparing these recordings with Matheson's later model.

With heading \(\theta\), the coordinate transformation would be

\[
w_{\rm world}=e^{i\theta}w.
\]

Currier identifies candidate ingredients; it does not measure this complete transformation in the behaving fly. It certainly does not establish

\[
x(t)=x(0)+\int_0^t v_{\rm world}(\tau)\,d\tau
\]

or storage of a food position \(x_f\), followed by computation of \(x_f-x(t)\). Airflow is not automatically translational velocity.

### Does this require perfect sinusoids?

No biological evidence here establishes perfect sinusoidal tuning. Any periodic response can be expanded as

\[
f(\delta)=\sum_{k\in\mathbb Z} c_k e^{ik\delta}.
\]

The simple projection story assumes a constant term and the first harmonic dominate, with suitable symmetry and gain calibration. Higher harmonics, rectification, and asymmetric tuning can bias a naive decoder. For a densely and evenly sampled population, a first-harmonic readout can reject many higher harmonics through orthogonality; **two scalar channels alone do not guarantee that protection**. Whether downstream circuitry effectively extracts the useful component is a separate mechanistic question.

The preferred direction in Figure 4 is approximately

\[
\widehat\delta=\arg\left(\sum_j \Delta r(\delta_j)e^{i\delta_j}\right).
\]

A stable preferred phase of this vector does not imply absence of higher harmonics. Eight tested directions also limit which distortions can be resolved.

### Behavioral circular statistics

For virtual headings \(\theta_t\),

\[
m=\frac1T\sum_t e^{i\theta_t},\quad
\text{mean orientation}=\arg m,\quad
\text{fixation strength}=|m|.
\]

This is a directional resultant, unlike the principal-axis orientation index used in parts of Matheson (2022). A fly spending equal time in opposite directions can have a strong axis but a small resultant.

The slip correction fraction is

\[
C=-\frac{\Delta\theta_{\rm response}}{\Delta\theta_{\rm slip}}.
\]

A value of one means complete correction; zero means no average compensatory turn. It does not measure knowledge of a target location.

## Methods and supplementary qualifications that affect interpretation

All experimental flies are female. Patch recordings use 1–3-day-old flies; behavioral animals are 3–5 days old; imaging uses older flies starved 18–24 hours. These are different preparations and physiological states. Main sensory trials last 12 seconds: four baseline, four stimulus, four post-stimulus, with a nine-second interval. The survey has 20 direction/condition combinations and four repeats. Detailed PFNa tuning uses eight directions and five repeats.

Recordings are sampled at 10 kHz; cell identity requires two of three anatomical/fluorescent checks. Input resistance is monitored using a −2 pA pulse. Mean response analysis compares a one-second baseline ending 500 ms before onset with the interval 0.5–1.5 seconds after onset. Correlation analyses use smoothed PSTHs and include offset responses, so transient dynamics can influence apparent multisensory similarity.

Imaging uses 5 Hz GCaMP6f recordings with tdTomato-based motion correction, manually adjusted ROIs, and red-channel subtraction. One nonresponsive fly is excluded. These calcium responses are not instantaneous spike rates and cannot determine a fast synaptic transfer function by themselves.

The closed-loop behavior uses wingbeat asymmetry multiplied by a gain of 0.04, with feedback at 50 Hz. There are 60 twenty-second trials, ten repeats of each of six perturbations. Statistical comparisons are nonparametric with Bonferroni correction as described in the methods.

Several reporting inconsistencies should remain visible if reproducing the work:

- The short airflow pause is 150 ms in the Figure 7 legend, but “two samples (100 ms)” in the methods; two samples at the stated 50 Hz would be 40 ms. Resolve from acquisition code/data before implementing that timing.
- Figure 1 gives illumination in mW/cm², whereas the methods use µW/cm². Do not silently pick one for replication.
- The methods report 52 survey neurons, whereas the eight population Ns listed in Table 1 sum to 54. Keep per-experiment Ns rather than merging them into a falsely precise total.
- The transparent reporting form refers to sample-size estimation and a p-value table in the statistical section, neither of which is apparent in the final main PDF's short statistical section. The form appears to retain submission-stage wording. It also says data will be released upon acceptance; the final article supplies a Dryad DOI instead.

## What peer review changed

The published review history is unusually useful for structure/function reasoning. The original model proposed an output route from PFNs through LN neurons toward LAL. Reviewers used the **direction and compartmental distribution of connectomic synapses** to challenge it: the dominant arrangement makes LNa an input through noduli, not a plausible principal motor-output route. The authors revised the model and added the candidate-input experiments. This is a concrete example of anatomy ruling out an attractive but poorly grounded circuit story.

Review also repeatedly emphasized that weak visual responses in open loop do not exclude conjunctive heading tuning. E-PGs and P-ENs cannot simply be assigned unrelated functions because one dataset appears less tuned; a coupled compass network must be considered. The final account leaves the conjunction of airflow and heading to future closed-loop experiments.

The author response confirms that liquid-junction potential was not subtracted. It also records a corrected calculation of resting-potential SEM, after an initial explanation in terms of SD proved insufficient; the original erroneous computation was not retained. Therefore the high raw resting potentials should not be imported directly into a biophysical model without checking recording conventions. A proposed behavioral panel with too few upwind observations was removed rather than treated as firm evidence.

## Remaining questions and neighboring papers to resolve them

1. **How is heading combined with airflow in individual PFNa/PFNm/PFNp cells?** The present open-loop recordings cannot distinguish a pure airflow response from a conjunction whose heading component averaged out. Compare later closed-loop physiology and coordinate-transform papers.
2. **What exactly is the signed input from LNa?** Opposing tuning and synaptic anatomy constrain a hypothesis but do not determine transmitter action, gain, membrane compartment, or causal necessity.
3. **How does the same input support different policies?** Downwind flight here must be reconciled with odor-evoked upwind walking in Matheson and later hΔ circuits. Locomotor state, descending outputs, reward, and odor context may all matter.
4. **What does the antenna measure during natural movement?** Relative airflow depends on self-motion and ambient wind. In free flight, steady wind can advect the animal while optic flow supplies essential information. Neither an antenna signal nor an airflow-responsive PFN is automatically a ground-velocity vector.
5. **Where do wind memory and target memory enter?** Persistent upwind bearing in Kathman/Siliciano is a different variable from a remembered food position. This paper identifies neither storage mechanism.
6. **How robust is the basis computation to imperfect tuning?** Shared phase, signed deviations, heterogeneous gain, saturation, and dynamics need separate treatment. An anatomical shift alone does not calibrate them.
7. **Which output pathway actually controls flight correction?** The final paper deliberately leaves this unresolved. Later PFL/descending work must be joined with attention to flight versus walking and driver specificity.

Priority neighbors include [Okubo et al. 2020](https://doi.org/10.1016/j.neuron.2020.06.022), [Suver et al. 2019](https://doi.org/10.1016/j.neuron.2019.03.012), [Currier & Nagel 2018](https://doi.org/10.1016/j.cub.2018.09.020), [Álvarez-Salvado et al. 2018](https://doi.org/10.7554/eLife.37815), [van Breugel & Dickinson 2014](https://doi.org/10.1016/j.cub.2013.12.023), [Franconville et al. 2018](https://doi.org/10.7554/eLife.37017), and [Namiki et al. 2018](https://doi.org/10.7554/eLife.34272). These are reading leads, not claims that those papers have already received a full review.

## Implications for later connectome work

Start with correctly matched PFNa/PFNm/PFNp populations and compartment-aware upstream/downstream relations. Distinguish a sparse feedback edge from a dominant information route; the peer-review correction demonstrates the stakes. Compare LNa convergence, bilateral symmetry, and candidate FB-to-output routes, while retaining species, sex, and dataset differences. A connectome can constrain routes and rule out incompatible architectures. It cannot alone establish the encoded variable, natural behavioral policy, or memory dynamics.
