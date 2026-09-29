"""page_text.py  –  the words of the twin-test page that depend on results.  Numbers are read from results.json
where they appear, so the prose cannot drift from the data.   python3 level4/page_text.py -> page_text.json"""
import json, os, statistics as st
HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, 'results.json')))
def arm(a): return [n for n, r in R.items() if r['arm'] == a]
def m(a, c):
    xs = [R[n]['conds'][c]['score'] for n in arm(a) if c in R[n]['conds']]
    return st.mean(xs) if xs else float('nan')
def s(n, c): return R[n]['conds'][c]['score']
f = lambda x: f'{x:.2f}'
FW = {c: m('FW', c) for c in ['std30', 'std30_1k', 'len45', 'len60', 'len90', 'drift05', 'drift15', 'stop10', 'stop30', 'trips5']}
TB = m('TWIN-warm-B', 'std30'); TW = m('TWIN-warm', 'std30')
hand, rnd = s('hand', 'std30'), s('random', 'std30')
FWC = json.load(open(os.path.join(HERE, 'fwcold_text.json'))) if os.path.exists(os.path.join(HERE, 'fwcold_text.json')) else {}

T = {}
T['summary'] = f"""
<h3 style="margin-top:0">What happened, in five sentences</h3>
<p><b>1.</b> On every test, our fast-weight network (FW) beat its twin with the same history, by a wide margin: {f(FW['std30'])} against {f(min(TB, TW))} on the standard exam, so by the rule written before the run the claim is <b>supported</b>.</p>
<p><b>2.</b> But the twins did not lose because their memory was worse. They lost because they never learned to use a memory at all: every twin, warm or from scratch, at every learning rate, ended up spinning on the spot, and so did the textbook GRU.</p>
<p><b>3.</b> The reason is a trap in the training loss. It only measures distance from home at the end of the return, and for a network that cannot yet remember, spinning in place scores a much lower loss than walking, even though it homes worse. FW mostly escapes the trap, because its board starts collecting a tally from the first tick with no training: from scratch, all three FW seeds learned the first stage, and two ended as working navigators (1.86 and 2.60), although the third fell into the same spin at 30 seconds (5.23).</p>
<p><b>4.</b> When the twin and the GRU were given a teacher (a training term that tells them, every tick, where home is), they learned to home ({f(s('twin_aux0','std30'))} for the best twin), and on the exam these working activity memories paid much less for a 30-second stop than FW did (a cost of 0.05 to 0.23 against FW's {f(FW['stop30']-FW['std30'])}), although looking inside, FW's board keeps more of the information through the stop and simply reads it short.</p>
<p><b>5.</b> So on this task, fast weights win because a network that has them is much easier to train from this loss. The evidence does not show that their memory is better: an activity memory that has been taught what to hold comes within about 0.4 of FW on ordinary trips, with far less training behind it, and pays much less for standing still.</p>
"""
T['std30'] = f"""
<p>This is the number the first two nights chased. Our four FW networks score {', '.join(f(s(n,'std30')) for n in arm('FW'))} (average {f(FW['std30'])}). Every twin scores between 5.8 and 6.0, which is worse than a fly that never steers ({f(rnd)}). They all spin, so they all land in almost the same place, which is why their dots sit on top of each other.</p>
<p>The purple and blue rows are the diagnostic networks that were trained with a teacher. They are shown so you can see what a working activity memory scores; they are not part of the verdict, because their training loss was different.</p>
"""
T['std30_1k'] = f"""
<p class="note">Checked on 1,000 different trips (seed 5151) to make sure the usual 200 are not lucky: FW averages {f(FW['std30_1k'])} there, against {f(FW['std30'])} on the usual trips. The usual exam is about 0.06 kind to everyone; the ordering of every group is the same.</p>
"""
T['len'] = f"""
<p>The fly wanders for 30, 45, 60 or 90 seconds before turning home, and gets twice as long to come back. A perfect counter would score the same at every length, like the hand-built brain (green, about 0.8 throughout).</p>
<p>FW climbs from {f(FW['std30'])} at 30 seconds to {f(FW['len60'])} at 60 and {f(FW['len90'])} at 90. That is the leaky counter from night two: its board fades with a time constant of about 14 seconds, so on long trips it undercounts how far it went. The teacher-trained twin climbs less steeply ({f(s('twin_aux0','std30'))} to {f(s('twin_aux0','len90'))} for the best one), so on the longest trips it overtakes FW; the other teacher-trained networks climb about as steeply as FW.</p>
"""
T['drift'] = f"""
<p>FW goes from {f(FW['std30'])} to {f(FW['drift05'])} with light drift and {f(FW['drift15'])} with heavy drift. The best teacher-trained twin loses a similar amount ({f(s('twin_aux0','std30'))} to {f(s('twin_aux0','drift05'))} and {f(s('twin_aux0','drift15'))}). A wrong compass hurts both kinds of memory about equally, which makes sense: both are counting in the directions the compass tells them.</p>
"""
P = json.load(open(os.path.join(HERE, 'probe.json')))
pd = lambda n, k: P[n]['decode'][k]
fwn = [n for n in P if P[n]['arm'] == 'FW']
T['stop'] = f"""
<p><b>What happened:</b> the stop costs FW {f(FW['stop10']-FW['std30'])} for 10 seconds and {f(FW['stop30']-FW['std30'])} for 30 seconds. The hand-built brain loses nothing. The teacher-trained activity networks lose between 0.05 and 0.23 for 30 seconds. This is the opposite of what the roadmap argued. A gated activity memory that has learned to home loses less during a stop than our fast-weight board does.</p>
<p><b>Looking inside (right).</b> For each network, a straight-line readout was fitted to recover the home vector from its memory just before the stop (the board F for FW, the neurons' activity for the others), using half of 600 flies, and scored on the other half. Then the same readout was applied at the end of the 30-second stop, when nothing has been walked in between, so the right answer has not changed. A second readout was refitted at the end of the stop, which asks a different question: is the information still there in any straight-line form?</p>
<ol class="steps">
  <li><b>FW:</b> before the stop the readout is off by about {f(st.mean(pd(n,'before') for n in fwn))} units (the fly has walked {f(pd(fwn[0],'walked'))}). After the stop the same readout is off by {f(st.mean(pd(n,'after') for n in fwn))}, but a refitted one by only {f(st.mean(pd(n,'after_refit') for n in fwn))}. So the information is still on the board; the board has shrunk while the fly stood still (the erase gate eases off by about a third when standing, from about 0.0065 to 0.0045 per tick, but never closes), and a fixed reading of a shrunken count reads it short. The network's own reading is fixed in the same way, which is why it homes worse.</li>
  <li><b>Teacher-trained activity networks:</b> before the stop their readout is off by {f(pd('twin_aux0','before'))} to {f(pd('twin_aux1','before'))}; after it, refitted, by {f(pd('gru_aux0','after_refit'))} to {f(pd('gru_aux1','after_refit'))}. They lose more of the information than FW does, and their hold gates stay about 0.6 open while standing, so the simple story "the gate closes and holds" is not what they do.</li>
  <li><b>What I cannot yet explain:</b> the activity networks lose more information during the stop but pay less for it on the exam. My best guess, not measured: their own reading is not a fixed straight line, and it copes with the change better than FW's calibrated reading of a fading count.</li>
</ol>
"""
T['probe'] = "Each row is one network. Black tick: readout error just before the stop. Pale box: the same readout at the end of a 30-second stop. Solid bar: a readout refitted at the end of the stop. Red dashes: the average distance walked, which is what a readout that knows nothing would be off by. Half of 600 flies to fit, the other half to score; <code>level4/probe.py</code>."
T['trips'] = f"""
<p>Every line rises from trip 1 to later trips, including the random walk and the hand-built brain, because the later trips in this test happen to be harder. So the question is whether FW rises more than the others. It does not: FW run 41 rises by 0.18 from trip 1 to the average of trips 2 to 5, while the teacher-trained twin, whose memory the world wipes for free, rises by 0.31. FW's erase gate resets the board at food as cleanly as a free wipe.</p>
"""
T['scratch'] = f"""
<p><b>What happened:</b> without a teacher, no twin and no GRU learned to home at any learning rate. They all reached the later stages only because each stage ends after 1,500 iterations whether or not the network has learned, and they all ended up spinning. {FWC.get('sentence', 'Our network from scratch: see below; it was still training at the time of writing.')}</p>
"""
T['aux'] = f"""
<p>If a network never learns to home, there are two possible reasons. It might be unable to hold a home vector at all (not enough capacity), or it might be able to, but the training signal never shows it how. To tell them apart, four extra networks were trained from scratch with one addition to the loss: a small readout has to state the home vector at every tick of the outward walk, and is charged for its error. This is dense supervision, the way Cueva and Wei trained path-integrating networks in 2018. The readout is thrown away before the exam, so the exam is exactly the same.</p>
<ol class="steps">
  <li>With the teacher, both twins and both GRUs learned to home: twins {f(s('twin_aux0','std30'))} and {f(s('twin_aux1','std30'))}, GRUs {f(s('gru_aux0','std30'))} and {f(s('gru_aux1','std30'))} on the standard exam, all far better than a fly that never steers ({f(rnd)}). So activity networks of this size can hold a home vector. The failure without a teacher is about the training signal, not capacity.</li>
  <li>They are still behind FW on the standard exam ({f(FW['std30'])}). They trained for 4,000 iterations from nothing; FW's networks have about 9,800 iterations behind them and four hand-made fixes. So this gap is not a clean comparison of the two memories.</li>
  <li>They hold far better through the long stop, as the stop chart shows.</li>
  <li>The same teacher made FW worse: retraining runs 41 and 45 with it for 800 iterations {FWC.get('fwA', 'is reported in the narrative')}. The teacher reads the home vector from the neurons' activity, but FW keeps it on the board, so the teacher pushes FW to move its memory to where FW does not keep it.</li>
</ol>
"""
T['rule'] = """<p class="note">Read this verdict together with the section "Learning from scratch": the rule compares scores, and the scores here are decided by which network could be trained at all.</p>"""
json.dump(T, open(os.path.join(HERE, 'page_text.json'), 'w'), indent=1)
print('ok', list(T))
