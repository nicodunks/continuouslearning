# Titova et al. (2023): returning to a remembered location after displacement

[Published article](https://doi.org/10.1242/jeb.245289) · [Main PDF](main.pdf) · [Scientific supplement](jexbio-226-245289-s1.pdf) · [Reading coverage](reading-log.md)

## Why this is central to the complete behavioral question

A fly revisiting a spot does not, by itself, demonstrate an internal location memory. It might recognize an external cue, follow a chemical trace, or remain near the location because reward changes its movement statistics. This paper both demonstrates a chemical-cue alternative and obtains stronger evidence for an internal navigation mechanism by separating the actual reward site from the location predicted by uncorrected path integration.

The behavioral result supports a short-range, reward-triggered return/search mechanism in freely walking flies. It does not establish long-term storage of several food sites, arbitrary relocalization after transport, or a neural implementation. Its strongest contribution is a **behavioral constraint on what the nervous system must be able to do**, together with a warning about the ambiguity of simpler assays.

## Figure 1: the environment can retain reward-associated information

Groups of 10–15 Gr43a>CsChrimson flies are confined to a 2-cm-diameter chamber on the floor of a 20-cm arena and optogenetically stimulated for 30 minutes. The chamber and flies are removed, and naïve groups explore the arena for another 30 minutes. A control receives the same illumination and handling but no emitter flies.

Naïve flies spend more time in the former emitter location: 22 emitter trials versus 24 no-emitter trials, P=0.04 by Welch's test. Each point is a **group**, not an independent individual fly. The heatmaps show a modest preference amid broader arena occupancy, not every fly homing directly to that spot.

Images show deposits on the floor after emitter flies were present. Their chemistry is not analyzed. Accordingly, the direct result is attraction associated with fly-deposited material; calling every deposit an identified pheromone would be too strong. There is also no nonrewarded-emitter condition, so the experiment does not establish that reward is necessary for depositing attractive cues.

Movie 1 documents emitter flies in the chamber. The downloaded rendition is 1,810 seconds long. Sampled frames across that interval and a late full-resolution frame were inspected; these support the setup but are not chemical identification or quantitative deposition measurements. The main figure's processed before/after images provide clearer evidence of deposits.

The first five minutes of naïve-fly observation are excluded because of long stops. The authors report similar qualitative results with those minutes included and when considering walking only, but those alternate plots are not supplied in the main figures.

## Figure 2: separate internal and external predictions

Individual hungry female flies walk freely in a dark, 60-cm-diameter arena. A 5.6-cm-diameter reward zone triggers red-light activation of Gr43a neurons. After cumulative illumination exceeds 60 seconds, reward is disabled on exit. When the fly walks onto a thin transparent sheet, the experimenter pulls it sideways without intentionally rotating it. Mean displacement is 92±27.8 mm; the manipulation lasts about three seconds and varies across trials.

The fly is then observed without further reward. The main test window is the first 100 seconds after displacement. The actual reward zone remains at its original physical location; the **fictive reward zone** is that location translated by the imposed displacement. This distinction makes two hypotheses predict different search locations.

Controls have the same genotype but receive no stimulation. Their corresponding nominal stimulation period is shortened to 0.5 seconds. Consequently the two groups do not have perfectly matched exposure histories or local trajectory histories; this is relevant to broad claims about reward-specific memory.

The study also selects trials strongly. Trials are aborted if the fly fails to find the zone within 20 minutes of activation, does not return for two minutes during stimulation, or flies during displacement. The methods report 19 of 65 rewarded trials and 20 of 42 controls finishing, then mention one rewarded trial discarded for hardware issues. Results and figure captions nevertheless use 19 rewarded flies and 20 controls. **The wording is inconsistent about whether the excluded fly precedes or follows that count.** Use the reported figure denominators when quoting results; resolve the underlying records before replication or meta-analysis. No power analysis was performed.

## Figure 3: what the displaced flies actually do

Rewarded flies concentrate search near the fictive reward zone, with the following reported results:

| Measure | Rewarded | No-reward control | Meaning |
|---|---|---|---|
| Visit fictive zone within 100 s | 13/19 | 1/20 | Reward history changes likelihood of reaching the internally predicted location |
| Visit actual zone within 100 s | 9/19 | 1/20 | Rewarded flies also revisit the physical site; behavior is not exclusive fictive-site selection |
| Time in fictive versus actual zone | Paired P=0.029 | Paired P=0.572 | Within rewarded flies, occupancy favors the fictive site |
| Initial five-second directions | Rayleigh P=0.018 | P=0.352 | Rewarded directions are nonuniform when expressed relative to fictive zone |

The mean initial direction differs from the fictive-zone direction by 28.9°. This is an approximate directional bias, not perfect vector steering. The Rayleigh test rejects circular uniformity; **it does not specifically test a mean of zero relative to the target**, nor does significance in one group and nonsignificance in another constitute a direct between-group test. The figure's direction and occupancy evidence should be interpreted jointly.

The fictive-zone heatmaps use a different translation for each trial, aligning its own fictive zone before pooling. The displayed actual zone is an average after these translations. This is appropriate for asking whether trajectories follow the internal prediction, but the coordinate choice must remain explicit.

The primary heatmaps are **walking-location histograms**, not time-occupancy histograms. Trajectories are first sampled every 0.1 s and then at 1-mm path-length intervals to remove long stops. Thus longer walks can contribute more points to a pooled heatmap. The paired zone-occupancy comparison separately uses time sampling and is a distinct piece of evidence.

## The displacement math in complex notation

This derivation expresses the paper's behavioral hypothesis; no neural vector state was recorded.

Write positions as complex numbers. Let the reward be at \(f\), and the fly just before displacement at \(x\). Its remembered return vector would be

\[
g=f-x.
\]

Passive displacement by \(d\) puts the real fly at

\[
x'=x+d.
\]

If the animal's internal position estimate misses the passive movement, it retains \(g\). Executing that vector from the new location leads to

\[
x'+g=(x+d)+(f-x)=f+d.
\]

That is the fictive reward location. A fully compensated position estimate instead gives

\[
g'=f-x'=g-d,
\]

which returns to the actual site. Therefore the displacement result is informative precisely because the navigation mechanism makes a predictable **error** when self-motion sensing misses externally imposed transport.

A candidate path-integrator update between reward encounters is

\[
g(t)=g(t_0)-\int_{t_0}^{t}s(\tau)e^{i\psi(\tau)}\,d\tau,
\]

where \(\psi\) is travel direction, not necessarily heading. Using body-relative velocity \(v_b\) and heading \(\theta\), the integrand would be \(e^{i\theta}v_b\), connecting to Lyu and Lu. The later steering error could depend on \(\arg g-\theta\), but neither this integrator nor that readout is identified here.

A remembered bearing \(e^{i\gamma}\) alone lacks distance and cannot generally define a finite search center after arbitrary movement. Nevertheless, the present geometry does not systematically vary outbound distances and paths to isolate every component of a metric vector memory. The authors appropriately present the result as evidence consistent with path integration, rather than complete identification of a unique algorithm.

## Supplement S1: a simpler algorithm can reproduce some apparent path-integration signatures

The paper constructs a chemical-cue agent in a one-dimensional circular channel, inspired by Behbahani et al. (2021). It is a counterexample to an inference from behavioral statistics, not a model claimed to be the fly's actual neural controller.

The agent walks, pauses to eat, reverses after a sampled run length, and deposits a chemical mark at reward. Marks decay linearly. Writing the intended expression without the apparent lower-bound typo in the printed equation:

\[
h(t)=\begin{cases}
1-(t-t_{\rm ph})/\tau,&t_{\rm ph}\le t\le t_{\rm ph}+\tau,\\
0,&\text{otherwise}.
\end{cases}
\]

After reward, a short run length is sampled; after spontaneous reversal, a much longer run length is sampled. Smelling a mark resets the run with

\[
\mu_{\rm ph}=\mu_{\rm rew}[1+k_\mu(1-h)],\qquad
\sigma_{\rm ph}=\sigma_{\rm rew}[1+k_\sigma(1-h)].
\]

Fresh marks promote short excursions; weakened marks allow longer ones. The nominal parameters are baseline mean/SD 80/20 body lengths, reward mean/SD 4.125/2.625, both gain factors 3, and lifetime 500 simulation steps. With the stated half-second step, that lifetime is 250 seconds.

S1A–C shows returns near the former reward after multiple circuits of the annulus, with run-midpoint peaks at integer revolutions. Alternating reward sides need not yield half-revolution peaks when old marks decay before the next experimental block. S1D–F shows similar midpoint distributions around a group of three rewards despite different final rewards. The simulations select trials visiting all three sites during the last two activation runs. Both designs use 1,000 simulations per stated condition.

The inference is narrow and important: those patterns are **not unique signatures** of a centrally stored reward position. It does not demonstrate that prior flies actually used only chemicals, nor that this agent explains every control in the earlier studies. The earlier papers must still be read in full and compared on their own conditions.

### Targeted code reading

Inspected public source at commit `0eb07940a9ffdedd97ada81f75e9d5f7bface579`: `pheromone_model.py`, `channels.py`, `generate_circling_trajs.py`, `config_circling.yaml`, and the relevant heatmap setup in `fig_displ_analysis.py`. No simulations or statistical reanalysis were run.

The model **does retain internal state**: walking/eating state, direction, local/global-search mode, and a run-distance counter. What it lacks is memory of a reward's spatial location. Calling it entirely memoryless would be inaccurate. The code resets the run counter after eating, smelling, or reversal; the persistent map of deposited cues is in the simulated environment.

Several details matter before using this code as a quantitative benchmark. The circling generator initializes food positions at 0 and π/2, whereas the main text describes opposite positions. `channels.py` treats these as angular coordinates directly. The YAML includes several parameter sets; `circling_simulations5.csv` matches the stated 80/20 baseline and other nominal parameters. Thus source inspection identifies a geometry discrepancy to resolve, not proof that the published figure was generated with that exact current driver. The decay code clips strength at zero and does not use the printed equation's malformed lower bound. These issues do not invalidate the conceptual counterexample, but preclude claiming exact reproduction from an unexamined script invocation.

## Supplements S2–S3: limits and controls

S2A shows a substantial thermal gradient created by the heated arena boundary: approximately low/mid-20s °C centrally and upper-30s °C near the edge. The task is visually dark, but the arena is not physically featureless. Both groups experience this layout; its interaction with search and displacement geometry remains a useful consideration. S2B measures reward illumination at five locations, approximately 0.37–0.49 mW/cm². S2C shows additional individual trajectories, including substantial variability in return and exploration.

S3A makes the difference between residence and distance-sampled walking histograms explicit. S3B–D supplies the original versus fictive coordinate frames and distributions of distances to the two zones. S3E replots initial directions relative to actual reward and displacement. These are alternative views of the same trials, not additional independent samples.

S3F–G tests whether flies simply retrace chemical trails on the sheet that moved with them. Trajectories immediately before and after displacement are aligned back into the same sheet frame; points within 2 cm of the displacement location are examined, with a 2.5-mm overlap tolerance. Only four of 39 trajectories have at least 1 cm of continuous overlap: two rewarded and two control. The group comparison is nonsignificant (Mann–Whitney P=0.230). This weakens exact local trail retracing as the explanation; it does not identify all chemistry or rule out every spatially diffuse cue strategy.

## What remains unresolved in the full behavioral account

1. **Which internal variable carries the return?** A home vector, remembered trajectory, or another reward-dependent search state can be constrained further by diverse paths, distances, rotations, and controlled sensory displacements. No neural encoding is measured here.
2. **Where and when is the origin written or reset?** Sixty cumulative seconds of reward can include repeated entries. That differs from writing one point after a single taste, and directly motivates reading the re-zeroing and spatial-learning literature.
3. **How are chemical cues and internal memory combined?** Both are available strategies. The result argues against an exclusively original-site chemical account after transport, not against chemical contributions under ordinary conditions.
4. **How far and how long does this memory operate?** The key assay is a local excursion followed by a 100-second test. It does not establish overnight revisits or long-distance commuting between multiple food sources.
5. **How does the fly recognize arrival and stop searching?** The reward is deliberately switched off; real ingestion, satiety, depletion, and a decision to leave are outside the demonstrated mechanism.
6. **Which circuit links travel estimation to this behavior?** PFNd necessity in Lu's assay is a relevant lead, not a circuit identification obtained by this study. Connectomics must connect candidate travel signals, integration/reset mechanisms, goal readouts, and locomotion without assuming the integrator's location.
7. **How general is the result across flies and preparations?** Strong trial selection, starvation, a single genotype, manual transport, and the mismatch with tethered physiology all limit immediate generalization.

## Connections to the reading program

Read Kim & Dickinson (2017), Corfas et al. (2019), Behbahani et al. (2021), Stern et al. (2019), Brockmann et al. (2018), and Lu et al. (2022) alongside these critiques. Add visual place learning (Foucaud 2010; Ofstad 2011), visual orientation memory (Neuser 2008), and learning in virtual landscapes (Haberkern 2019). These address different pieces of the user's question about remembering a thing and navigating back to it.

The eventual synthesis must allow **multiple ways of returning**. A chemical cue policy, an odor-associated bearing, a local path-integrated vector, and landmark-based place recognition can produce superficially similar trajectories while requiring different internal variables and circuits.
