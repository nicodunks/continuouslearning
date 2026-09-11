# Weisman et al. (2025): a preferred goal angle can persist for days to weeks

[Preprint, DOI 10.64898/2025.12.09.693277](https://doi.org/10.64898/2025.12.09.693277), version posted December 11, 2025; [full PMC manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC12714015/). This reading uses the preprint, not a subsequently verified peer-reviewed version.

## Behavioral meaning

Head-fixed flies can repeatedly resume a preferred direction in a visual virtual world over days, including after an entire night without the orienting cue. Hourly virtual rotations cause corrective behavior. Thus an angular preference can persist much longer than the minutes-long experiments that defined heading and steering computations.

This is long-term **bearing maintenance**, not navigation to a remembered food location. Food is delivered at the tethered fly's mouth, conditional on walking or on a timer, rather than placed at a learned world location. The reconstructed hundreds of meters are virtual displacement derived from ball motion. There is no arrival criterion, distance-to-target representation, outbound/inbound journey or place-memory demonstration.

The paper is particularly useful because the long-term directional bias can be behaviorally latent: the fly may deviate for many hours or walk without coherent displacement in darkness, yet later resume the earlier bearing. A behavioral departure from a goal does not establish erasure of the goal.

## Figures 1–2: platform, survival and state

Twelve compact rigs support individual flies for many days with a 320-degree panoramic projection, 40-degree rear gap, spherical treadmill and automated sugar delivery. The bar is 11 degrees wide and 60 degrees high. Overhead lights follow a 12-hour on/off cycle; the orienting bar initially remains available all day and night. “Night” is therefore not automatically “no visual cue.”

The main feeding rule supplies a drop when the five-minute rolling mean translation speed exceeds 2 mm/s, with a three-minute refractory period. Drops are approximately 15 nL of 5% sucrose. This couples locomotion, nutritional state and survival. **Only 26 of 81 initialized flies survived at least seven days and entered the principal analysis**; 55 died earlier. A statement that flies generally maintain bearings for a week must preserve this selection.

The survivors show evening anticipation and a weaker morning anticipation in locomotor activity. The flies are mated females, for which weak morning anticipation is plausible. Immobility for at least five minutes is used as a sleep proxy. Absolute inferred sleep depends strongly on the motion threshold: roughly 10–21 minutes per nighttime half-hour over the tested thresholds. The main threshold gives about 330 minutes per night, lower than an external benchmark of about 570 minutes. These are movement-based estimates, not direct neural sleep measurements. Hunger and isolation are candidate contributors, not isolated causal factors.

## Figures 3–4: long-term consistency amid short-term variability

The 26 long-term trajectories span 7–10 days. Illustrative net displacements are 157 and 264 m; cumulative paths can exceed a kilometer. A comparison group of 82 heated/starved flies performs two 30-minute bouts separated by half an hour without the bar. Those two bouts are not 164 independent flies.

Long-term flies walk more slowly, stand more often (69% versus about 18% using the relevant speed criterion), have broader heading distributions and higher tortuosity than the short-term group. Temperature and feeding differ substantially: long-term flies are around 24–26°C; short-term flies are around 33–33.5°C and previously deprived of food for 16–28 hours. The comparison does not isolate duration alone.

The preferred bearing is not rigidly expressed. Individual trajectories sometimes travel elsewhere for half a day or more. Daily net-displacement vectors are compared with the accumulated displacement before that day. The Figure 4 schematic explicitly shows, for example, day 5 compared to days 0–4. Across-fly shuffles preserve the population's directional biases while destroying the correct identity pairing. Ten thousand shuffles show more within-fly consistency than this null. Fly 11 changes direction around day 5, making clear that the measure prioritizes a persistent overall bearing rather than detecting every local episode of straight travel.

## Figure 5: active correction, not just walking straight

Nineteen flies receive a ±90-degree bar jump every hour, 24 times per day. Jump direction stays fixed for a day and alternates the next day; the first day's direction is randomized. A bar jump is a **virtual** rotation, not physical passive displacement of the fly.

Some examples correct within about a second; others first turn incorrectly and take tens of seconds to resume the old direction. The main quantification uses distance walked after a jump, rather than a fixed elapsed-time response, and compares the post-jump displacement angle with the overall trajectory angle. Absolute error declines but does not reach zero. Pseudo-jumps constructed between real jumps provide a null that preserves ongoing behavior while rotating the reconstructed path artificially. The actual-jump error is lower beyond 5 mm in the reported analysis.

A complementary comparison reconstructs trajectories in two frames. The standard frame incorporates the bar jumps; the fixed frame tracks ball rotation as if the jumps never occurred. Corrective turns produce much more tortuous paths in the latter. Eighteen of nineteen whole trajectories have greater fixed-frame tortuosity; 137 of 161 individual days do too. This establishes use of the cue even in flies lacking one obvious week-long direction. It does not require every correction to target exactly the same week-long bearing.

## Figure 6: retrieval after twelve hours without the cue

Twenty-nine flies experience nights without the bar on days 4, 6 and 8, interleaved with control nights retaining the bar. In cue-free nights, substantial local movement produces little net displacement: a compact black patch on a hundreds-of-meters plot does not mean immobility or loss of all locomotion.

Daytime net-displacement bearings remain similar across both sorts of intervening night. Mean absolute differences are 23.9 degrees after bar-on nights and 28.6 degrees after bar-off nights; both are far below randomly paired-day values. The two observed distributions are not significantly different (p=0.5), which is not an equivalence demonstration. The result is strong evidence of persistence relative to a between-fly/day null, not perfect angular retention.

No EPG imaging or successful days-long EPG silencing is reported. The authors explicitly describe the latter as technically unresolved. The behavior is compatible with at least three broad explanations: a durable cue-to-compass map; compensatory updating of a goal when that map changes; or another compass/control mechanism. The experiment cannot select one.

## All nine supplementary figures

- **S1:** dimensional screen plans, controller photographs and software/hardware information flow. The fly-facing display and feeding apparatus are concrete components; the pipeline contains no hidden neural measurement.
- **S2:** full controller PCB schematic, including power regulators, microcontroller connections, illumination, solenoid, servo, encoder, display and control knobs. Its inclusion improves reproducibility of the platform, not identification of a neural circuit.
- **S3:** survival distribution: 55 die before seven days, ten analyzed flies die after seven days, sixteen analyzed flies are removed alive. Survival is a major selection factor.
- **S4:** individual activity/feeding histories and fractions in standing/slow/medium/fast states. The standing threshold here is 0.1 mm/s in minute bins, distinct from the 0.25 mm/s criterion used elsewhere. The wide heterogeneity should not be replaced by one average state.
- **S5:** circadian activity statistics and sleep-threshold sensitivity. The plotted per-bin p=0.05 threshold is explicitly uncorrected for multiple comparisons. Small time bins from the same fly are not independent biological replicates.
- **S6:** higher circular variance in long-term than short-term walking, plus all 26 separated trajectories colored by day. Broad distributions and direction changes coexist with a consistent net bias.
- **S7:** ten flies fed every 15 minutes, independent of walking, include trajectories extending about two weeks. One is tested only about five days; the others are tested 10–15 days. Speed and tortuosity are not significantly different from walking-triggered feeding (p=0.4 and 0.99). This argues against the walking contingency being necessary, without proving identical nutritional or motivational states. Timed-feeding flies also differ in rearing antibiotic exposure. One 24-day survivor is mentioned in the main text; this is not evidence of 24-day confirmed goal stability for the whole cohort.
- **S8:** all nineteen perturbation trajectories, uncorrected distance-wise significance and additional standard/fixed-frame examples. Even a tortuous standard-frame path can become much more tortuous when the bar jumps are omitted from reconstruction.
- **S9:** no support for the tested time-compensated sun-compass models. Daytime trajectories are rotated using equinox solar ephemerides for nine latitudes from −80 to +80 degrees. Even the best of these transformations increases tortuosity in all but one fly. This rejects an improvement predicted by these particular transformations, not every possible solar-navigation mechanism or every interpretation of the bar.

Some caption references to Figure 3 panels appear mismatched; interpret them using the shown datasets and sample sizes rather than assuming the panel label itself identifies a different experiment.

## Mathematics: what is measured and what would have to be stored

These equations restate the behavioral analysis and the mechanistic alternatives; the paper does not fit a new neural dynamics model.

For reconstructed world velocity \(u(t)\), define

\[
D_d=\int_{\mathrm{day}\ d}u(t)\,dt,\qquad
\psi_d=\arg D_d,\qquad
\Delta_d=\arg\left(D_d\overline{\sum_{k<d}D_k}\right).
\]

This measures the orientation of net progress. It is poorly determined if a day's net displacement is tiny, even when total walking is large. Tortuosity is

\[
T=\frac{\int |u(t)|dt}{|\int u(t)dt|},
\]

so it can become very large as net displacement approaches zero. Neither quantity establishes that the animal itself explicitly integrates and stores the experimenter's reconstructed displacement.

Heading concentration can be expressed as

\[
R=\left|N^{-1}\sum_k e^{i\theta_k}\right|,\qquad V=1-R.
\]

A large circular variance need not imply no persistent goal: a stable bias with frequent local detours can have a large \(V\) but a consistent long-term displacement angle.

Suppose an internal compass represents \(H=e^{i(\theta+\alpha)}\), where \(\alpha\) is its offset from the world, and an internal goal represents \(G=e^{i(g+\alpha)}\). A steering comparison may depend on

\[
G\overline H=e^{i(g-\theta)}.
\]

The common offset cancels. But if the compass remaps \(\alpha\to\alpha'\) while the goal remains in the old internal coordinates, the relative angle acquires an error. Preserving the same world goal then requires either stable mapping, co-transforming the stored goal by \(e^{i(\alpha'-\alpha)}\), or another way to recover the world-referenced preference. Overnight return constrains that interface without measuring which solution the fly uses.

A remembered location is a stronger requirement: for target \(x_*\) and current position \(x(t)\), the required displacement is \(x_*-x(t)\), whose angle generally changes as the fly moves. Maintaining a fixed \(g\) is not equivalent to computing that vector.

## Methods and remaining limitations

Canton S mated females are pin-tethered two to three days after eclosion, with wings glued together. This is an intact-brain behavioral preparation, but it constrains flight, social interaction and diet. Ball tracking runs at 60 Hz; the display updates nominally at up to 120 Hz, with slower actual software updates acknowledged. The monitoring camera saves sparse frames plus full-rate feeding snippets. No continuously imaged compass is hiding behind the behavioral plots.

Most analyses downsample to seconds or tens of seconds; short perturbation illustrations retain 60 Hz data. Speed is formed from net forward/sideways displacement in a bin, so temporal resolution matters for tortuosity and local movements. The one-week raw recording is about 20 GB per fly. Raw data, code and detailed designs were promised upon publication; none was acquired or executed in this reading, and no unapproved request was sent to the authors.

The origin of the preferred angle remains unresolved. It could reflect learning, long-lived internal bias, developmental individuality or a combination. There is no experiment here that trains a chosen angle and demonstrates subsequent replacement, or switches two learned destinations by context. Long-term menotaxis could share the short-term PFL controller, but that circuit assignment is an inference awaiting direct tests.

## Implications for the larger project

This paper adds a genuine behavioral constraint on longevity and retrieval. Any complete account should allow an angular preference to survive periods when it is not expressed and should explain how retrieval remains consistent with the sensory frame. Connectomics can identify candidate places where cue, compass, memory and state signals interact; one static individual cannot by itself distinguish long-lived learned weights from a developmental bias.

Follow the cited long-term imaging, naturalistic cue mapping, individuality, dispersal and local-search studies. The next useful synthesis is not to assume this preference is a food memory, but to determine how bearing memory, spatial memory and motivational switching could coexist and which experiments actually connect them.

## Coverage

Complete PMC main text, all Methods, references and all six main figures read and visually inspected. All nine supplement pages (printed pages 28–36) read and visually inspected, including the circuit-board schematic. Main PDF remains an acquisition gap: publisher access returned an error, while full HTML and original figure images are saved. The PDF supplement was recovered through the Europe PMC supplementary archive. No movies were listed in that inventory; no code or raw behavioral-data reproduction is claimed.
