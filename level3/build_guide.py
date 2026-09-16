import json
motif=json.load(open('motif_data.json')); runs=json.load(open('runs_seq.json')); sat=json.load(open('sat_data.json'))
data=json.dumps(dict(motif=motif,runs=runs,F=sat['F'],Ft=sat['t'],dist=sat['dist']),separators=(',',':'))
html=r'''<title>Before the Deep Dive</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Literata:opsz,wght@7..72,400;7..72,600;7..72,400i&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
:root{--bg:#F4F5F9;--panel:#FFFFFF;--ink:#1A2233;--mute:#66707F;--line:#D8DCE5;--soft:#EAEEF3;--blue:#2F5BEA;--teal:#0E8A7E;--coral:#D9482B;--amber:#C27A00;--green:#3F7D20;--rand:#9AA1AD;--chalk:#EEF2FF}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#0F141C;--panel:#171E29;--ink:#E8ECF3;--mute:#98A2B2;--line:#2A3342;--soft:#1F2833;--blue:#7C9CFF;--teal:#3FC2B3;--coral:#FF6E4F;--amber:#F0A83A;--green:#7BC257;--rand:#6B7382;--chalk:#1A2340}}
:root[data-theme="dark"]{--bg:#0F141C;--panel:#171E29;--ink:#E8ECF3;--mute:#98A2B2;--line:#2A3342;--soft:#1F2833;--blue:#7C9CFF;--teal:#3FC2B3;--coral:#FF6E4F;--amber:#F0A83A;--green:#7BC257;--rand:#6B7382;--chalk:#1A2340}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:Literata,Georgia,serif;font-size:17px;line-height:1.55;margin:0;padding:0 18px}
.wrap{max-width:1180px;margin:0 auto;padding-block:32px 90px;display:grid;grid-template-columns:230px minmax(0,1fr);gap:40px}
@media (max-width:900px){.wrap{grid-template-columns:1fr}nav.side{position:static!important}}
nav.side{position:sticky;top:20px;align-self:start;font-family:"Bricolage Grotesque",sans-serif;font-size:14px;line-height:1.35}
nav.side a{display:block;color:var(--mute);text-decoration:none;padding:5px 0 5px 12px;border-left:2px solid var(--line)}
nav.side a:hover,nav.side a:focus-visible{color:var(--ink);border-color:var(--blue);outline:none}
nav.side .q{color:var(--blue);font-family:"JetBrains Mono",monospace;font-size:11px;margin-right:6px}
h1,h2,h3,h4{font-family:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif;text-wrap:balance;line-height:1.1;margin:0}
h1{font-size:clamp(34px,4.5vw,52px);font-weight:700}
h2{font-size:30px;font-weight:700;margin-top:80px;padding-top:20px;border-top:3px solid var(--ink)}
h2 .q{font-family:"JetBrains Mono",monospace;font-size:13px;color:var(--blue);display:block;margin-bottom:8px;letter-spacing:.08em}
h3{font-size:20px;font-weight:600;margin-top:28px}
h4{font-size:16px;font-weight:600;margin-top:14px}
p{max-width:68ch;margin:14px 0}
.lede{font-size:20px;max-width:62ch}
.eyebrow{font-family:"JetBrains Mono",monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--mute)}
.term{border-bottom:2px dotted var(--teal);cursor:help}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:20px 22px;margin-top:18px}
.sketch{background:var(--chalk);border:1px dashed var(--blue);border-radius:10px;padding:18px 22px;margin-top:18px}
.sketch .eyebrow{color:var(--blue)}
.real .eyebrow{color:var(--teal)}
.how{background:var(--soft);border-radius:8px;padding:12px 16px;font-size:15px;margin-top:14px}
.how b,.idea b{font-family:"Bricolage Grotesque",sans-serif}
.controls{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px 22px;margin:8px 0 14px}
.ctl label{display:flex;justify-content:space-between;font-family:"JetBrains Mono",monospace;font-size:12.5px;color:var(--mute)}
.ctl output{color:var(--ink);font-weight:600;font-variant-numeric:tabular-nums}
.ctl input[type=range]{width:100%;accent-color:var(--blue);margin-top:4px}
.ctl small{display:block;color:var(--mute);font-size:12.5px;line-height:1.35;margin-top:3px}
canvas{width:100%;height:auto;display:block}
svg{max-width:100%;height:auto;display:block}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}.three{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
@media (max-width:760px){.two,.three{grid-template-columns:1fr}}
.btn{font-family:"Bricolage Grotesque",sans-serif;font-weight:600;font-size:14px;border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:6px;padding:7px 12px;cursor:pointer}
.btn[aria-pressed="true"],.btn.on{background:var(--blue);color:#fff;border-color:var(--blue)}
.btn:focus-visible{outline:2px solid var(--coral);outline-offset:2px}
.row{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:10px}
table{border-collapse:collapse;font-variant-numeric:tabular-nums;font-size:15px;margin-top:12px;width:100%}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}th{font-family:"JetBrains Mono",monospace;font-size:12px;color:var(--mute);font-weight:400;letter-spacing:.04em}
td.n,th.n{text-align:right}
.legend{display:flex;flex-wrap:wrap;gap:6px 18px;font-family:"JetBrains Mono",monospace;font-size:12px;color:var(--mute);margin-top:8px}
.legend i{display:inline-block;width:18px;height:3px;vertical-align:middle;margin-right:6px;border-radius:2px}
.knobs{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px;margin-top:12px}
.knob{border:1px solid var(--line);border-radius:8px;padding:10px 12px;background:var(--panel);cursor:pointer;font-size:14px}
.knob:hover,.knob.on{border-color:var(--blue);box-shadow:0 0 0 2px var(--chalk)}
.knob b{font-family:"Bricolage Grotesque",sans-serif;display:block;font-size:15px}
.knob .flag{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--mute)}
.knob .turned{color:var(--blue);font-family:"JetBrains Mono",monospace;font-size:11px;display:block;margin-top:4px}
.group{margin-top:22px}.group h4{color:var(--mute);letter-spacing:.06em;text-transform:uppercase;font-size:12px;font-family:"JetBrains Mono",monospace}
.detail{border-left:4px solid var(--blue);padding:10px 16px;margin-top:14px;background:var(--panel);font-size:15.5px;min-height:60px}
.pill{display:inline-block;font-family:"JetBrains Mono",monospace;font-size:11px;padding:2px 8px;border-radius:20px;border:1px solid var(--line);color:var(--mute);margin-right:4px}
.pill.ok{color:var(--green);border-color:var(--green)}.pill.bad{color:var(--coral);border-color:var(--coral)}.pill.part{color:var(--amber);border-color:var(--amber)}
.stepper{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.stepper button{font-family:"JetBrains Mono",monospace;font-size:12px;padding:5px 9px;border-radius:6px;border:1px solid var(--line);background:var(--panel);color:var(--ink);cursor:pointer}
.stepper button.on{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.card{margin-top:16px;display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media (max-width:760px){.card{grid-template-columns:1fr}}
.card .box{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:14px 16px;font-size:15px}
.card .box h4{margin-top:0;color:var(--mute);font-size:12px;letter-spacing:.06em;text-transform:uppercase;font-family:"JetBrains Mono",monospace}
.eq{font-family:"JetBrains Mono",monospace;font-size:14px;background:var(--soft);padding:12px 14px;border-radius:8px;overflow-x:auto;white-space:nowrap;margin-top:10px}
.eq .a{color:var(--teal)}.eq .b{color:var(--coral)}.eq .c{color:var(--amber)}.eq .d{color:var(--blue)}
.caveat{border-left:4px solid var(--coral);padding-left:14px;color:var(--mute);font-size:15px}
.big{font-family:"Bricolage Grotesque",sans-serif;font-size:26px;font-weight:700;font-variant-numeric:tabular-nums}
.grid16{display:grid;grid-template-columns:repeat(8,1fr);gap:4px;margin-top:10px}
@media (max-width:760px){.grid16{grid-template-columns:repeat(4,1fr)}}
.map{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:12px;font-size:14.5px}
@media (max-width:760px){.map{grid-template-columns:1fr}}
.map div{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:10px 12px}
.map b{font-family:"Bricolage Grotesque",sans-serif;display:block}
.status{font-family:"JetBrains Mono",monospace;font-size:11px}
.done{color:var(--green)}.part{color:var(--amber)}.todo{color:var(--coral)}
</style>
<div class="wrap">
<nav class="side" aria-label="questions">
 <a href="#q1"><span class="q">Q1</span>Inputs, outputs, and what a knob is</a>
 <a href="#q2"><span class="q">Q2</span>Why the erase shift was not a knob</a>
 <a href="#q3"><span class="q">Q3</span>A sigmoid parked at −5</a>
 <a href="#q4"><span class="q">Q4</span>Peter's delta rule</a>
 <a href="#q5"><span class="q">Q5</span>Is F versus no-F a fair test?</a>
 <a href="#q6"><span class="q">Q6</span>Reset: yes, fade, or never</a>
 <a href="#q7"><span class="q">Q7</span>Every run: reason, prediction, finding</a>
 <a href="#q8"><span class="q">Q8</span>The circuit motifs, in depth</a>
 <a href="#q9"><span class="q">Q9</span>Backpropamine</a>
 <a href="#q10"><span class="q">Q10</span>Peter's head-direction paper</a>
 <a href="#q11"><span class="q">Q11</span>Follow-ups on the lid</a>
</nav>
<main>
<div class="eyebrow">Level 3 · a study guide · eleven questions</div>
<h1>Before the deep dive</h1>
<p class="lede">Your questions, answered in order, each with a drawn sketch you can push on and the real numbers next to it. Read it top to bottom once, then keep it open beside the Night Report.</p>
<p>Two conventions throughout. Boxes with a <span style="color:var(--blue)">dashed blue border</span> are drawn analogies: simplified on purpose, so a shape is easy to see. Boxes with a <span style="color:var(--teal)">teal label</span> are the real thing, computed from run files. Dotted words are <span class="term" title="like this">terms explained where they first appear</span>.</p>

<!-- ============ Q1 ============ -->
<h2 id="q1"><span class="q">QUESTION 1</span>What goes in, what comes out, and what is a knob</h2>
<p>Start with the machine itself. The network is 64 <span class="term" title="A neuron here is one number that gets recomputed every tick from the numbers feeding into it, then squashed to lie between −1 and +1">neurons</span>. Every tick (a tenth of a second of fly time) it receives four numbers, updates all 64 neurons, and emits three numbers. Click any part of the drawing.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: the whole machine, with its four inputs on the left, the 64 neurons in the middle and the three outputs on the right. Click any part to read what it is.</div>
 <svg viewBox="0 0 900 340" id="machine" role="img" aria-label="inputs, network, outputs">
  <defs><marker id="ar" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="var(--mute)"/></marker></defs>
  <g class="node" data-k="in0"><rect x="20" y="40" width="170" height="44" rx="8" fill="var(--panel)" stroke="var(--blue)"/><text x="105" y="67" text-anchor="middle" font-family="Bricolage Grotesque" font-size="15" fill="var(--ink)">compass, east-west part</text></g>
  <g class="node" data-k="in1"><rect x="20" y="100" width="170" height="44" rx="8" fill="var(--panel)" stroke="var(--blue)"/><text x="105" y="127" text-anchor="middle" font-family="Bricolage Grotesque" font-size="15" fill="var(--ink)">compass, north-south part</text></g>
  <g class="node" data-k="in2"><rect x="20" y="160" width="170" height="44" rx="8" fill="var(--panel)" stroke="var(--blue)"/><text x="105" y="187" text-anchor="middle" font-family="Bricolage Grotesque" font-size="15" fill="var(--ink)">speed</text></g>
  <g class="node" data-k="in3"><rect x="20" y="220" width="170" height="44" rx="8" fill="var(--panel)" stroke="var(--blue)"/><text x="105" y="247" text-anchor="middle" font-family="Bricolage Grotesque" font-size="15" fill="var(--ink)">at food? (0 or 1)</text></g>
  <g class="node" data-k="win"><line x1="190" y1="152" x2="300" y2="152" stroke="var(--mute)" stroke-width="2" marker-end="url(#ar)"/><text x="245" y="140" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--mute)">W_in · 320 numbers</text></g>
  <g class="node" data-k="net"><rect x="305" y="30" width="290" height="250" rx="14" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="450" y="60" text-anchor="middle" font-family="Bricolage Grotesque" font-size="18" font-weight="700" fill="var(--ink)">64 neurons, all wired to all</text>
   <g id="dots"></g></g>
  <g class="node" data-k="W"><rect x="320" y="215" width="80" height="50" rx="6" fill="var(--soft)" stroke="var(--line)"/><text x="360" y="236" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--ink)">W</text><text x="360" y="254" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">slow, 4096</text></g>
  <g class="node" data-k="A"><rect x="410" y="215" width="80" height="50" rx="6" fill="var(--soft)" stroke="var(--line)"/><text x="450" y="236" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--ink)">A</text><text x="450" y="254" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">slow, 4096</text></g>
  <g class="node" data-k="F"><rect x="500" y="215" width="80" height="50" rx="6" fill="var(--chalk)" stroke="var(--teal)" stroke-width="2"/><text x="540" y="236" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--teal)">F</text><text x="540" y="254" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">fast, 4096</text></g>
  <g class="node" data-k="wout"><line x1="595" y1="152" x2="700" y2="152" stroke="var(--mute)" stroke-width="2" marker-end="url(#ar)"/><text x="648" y="140" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--mute)">W_out · 195</text></g>
  <g class="node" data-k="out0"><rect x="705" y="70" width="175" height="44" rx="8" fill="var(--panel)" stroke="var(--ink)"/><text x="792" y="97" text-anchor="middle" font-family="Bricolage Grotesque" font-size="15" fill="var(--ink)">turn (left or right)</text></g>
  <g class="node" data-k="out1"><rect x="705" y="130" width="175" height="44" rx="8" fill="var(--panel)" stroke="var(--amber)" stroke-width="2"/><text x="792" y="157" text-anchor="middle" font-family="Bricolage Grotesque" font-size="15" fill="var(--ink)">write gate (0 to 1)</text></g>
  <g class="node" data-k="out2"><rect x="705" y="190" width="175" height="44" rx="8" fill="var(--panel)" stroke="var(--coral)" stroke-width="2"/><text x="792" y="217" text-anchor="middle" font-family="Bricolage Grotesque" font-size="15" fill="var(--ink)">erase gate (0 to 1)</text></g>
  <path d="M792,234 C792,300 540,310 540,265" fill="none" stroke="var(--coral)" stroke-width="1.5" stroke-dasharray="4 4" marker-end="url(#ar)"/>
  <path d="M792,174 C880,260 560,320 545,268" fill="none" stroke="var(--amber)" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="700" y="300" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">the gates feed back into F's rule</text>
  <g class="node" data-k="ws"><rect x="320" y="150" width="120" height="30" rx="6" fill="var(--soft)" stroke="var(--line)"/><text x="380" y="170" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--ink)">ws · 1 number</text></g>
 </svg>
 <div class="detail" id="machineDetail">Click a box. Start with the four inputs on the left.</div>
</div>
<div class="panel real">
 <div class="eyebrow">Real data: run 19, the average size of the weights from each input wire into the 64 neurons</div>
 <p style="font-size:15px">The four input wires each connect to all 64 neurons through W_in. If we take the 64 weights belonging to one input wire, ignore their signs and average their sizes, we get one number that says how strongly that input is used by the network. The chart shows that number for each of the four inputs. All four are used, and the speed input is used slightly more than the others. The chart also shows the three output biases. A bias is the resting value of an output: the value it would have if no neuron were pushing on it at all. The erase gate's bias is the one to notice. It started at −5, and after five hand-made shifts and further training it now sits at +1.86. Question 3 explains why that journey mattered.</p>
 <canvas id="winBars" width="1600" height="300"></canvas>
</div>



<h3>Two kinds of number: what changes every tick, and what never does</h3>
<p>Before we do any arithmetic, here is the most important distinction in the machine. Some of its numbers are recomputed on every tick. Other numbers are looked up on every tick but never change during a trip. Press the clock buttons below and watch which boxes flash.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: the machine as a set of boxes; press the clock and see which boxes are recomputed</div>
 <div class="row"><button class="btn" id="clockTick">advance one tick</button><button class="btn" id="clockRun">run ten ticks</button><span class="eyebrow" id="clockN">tick 0</span></div>
 <svg viewBox="0 0 900 330" id="clock"></svg>
 <div class="how"><b>How to read it.</b> Each box is one group of numbers inside the machine. When you press "advance one tick", the boxes that flash are the ones that get recomputed on that tick: the 64 activities, the three outputs, and the whole F table. The boxes marked with a padlock are the ones that never change during a trip: W, A, W_in, W_out and ws. Training set those numbers once, and after that they are frozen. Every parameter mentioned anywhere on this page is one of the padlock boxes. Anything that carries a memory of the current trip must be one of the flashing boxes, because those are the only numbers that change while the trip is happening.</div>
</div>

<h3>Counting the numbers: every square is one number</h3>
<p>Where do the numbers 320, 195, 4,096 and 8,708 come from? You can get every one of them by counting squares in the drawing below. Every wire between two things has one weight, drawn as one square. Every neuron and every output also has one bias, drawn as a strip of squares along the side of its table. Hover over any square and the caption will tell you which number it is.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: the five parameter tables drawn to scale, one square per number, with the F table beside them</div>
 <canvas id="squares" width="1700" height="620"></canvas>
 <div class="detail" id="squareDetail">Hover a square.</div>
 <div class="how"><b>How to read it.</b> W_in: 4 input wires × 64 neurons = 256 weights (the 4 × 64 block) + 64 biases (the strip) = 320. W and A: 64 × 64 = 4,096 each. W_out: 64 neurons × 3 outputs = 192 + 3 biases = 195. ws: one square. Add them all up: 320 + 4,096 + 4,096 + 195 + 1 = 8,708 parameters. F is drawn in grey because, although it is the same size as W, it is not a parameter: it starts at zero at the beginning of every episode and the rule rewrites it on every tick, so training never sets it directly.</div>
</div>

<h3>One connection, up close: what W + A·F means</h3>
<p>Pick any one pair of neurons, sender j and receiver i. Their connection is a wire made of two strands. One strand is permanent: W[i,j]. The other is temporary: A[i,j] × F[i,j], the allowance times whatever the trip has written so far. What the receiver feels is the two added together. Move the sliders.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: one connection as a wire with two strands, one permanent and one temporary</div>
 <div class="controls"><div class="ctl"><label>W[i,j], permanent <output id="oW1">+0.30</output></label><input id="W1" type="range" min="-1" max="1" step="0.05" value="0.3"><small>Set by training. Same on every trip.</small></div>
 <div class="ctl"><label>A[i,j], allowance <output id="oA1">0.60</output></label><input id="A1" type="range" min="0" max="1" step="0.05" value="0.6"><small>Set by training. How much this wire can be rewritten during a trip. Zero means never.</small></div>
 <div class="ctl"><label>F[i,j], written so far <output id="oF1">0.00</output></label><input id="F1" type="range" min="-1" max="1" step="0.05" value="0"><small>Zero at the start of an episode; changed by the rule every tick.</small></div></div>
 <svg viewBox="0 0 900 200" id="wire"></svg>
</div>
<h3>W means the whole table of 4,096 cells</h3>
<p>When this page says "W", it means all 4,096 cells together, in the same way that "the spreadsheet" means every cell in a spreadsheet and not some total at the bottom. W[i,j] is one cell of that table. Nothing is averaged when the network runs: it needs every cell separately, on every tick. Below is run 19's actual W, all 4,096 cells, and beside it the A table drawn the same way.</p>
<div class="panel real">
 <div class="eyebrow">Real data: run 19's W, all 4,096 cells, with its A table drawn beside it</div>
 <div class="two"><div><canvas id="Wfull" width="820" height="860"></canvas></div><div><canvas id="Afull" width="820" height="860"></canvas></div></div>
 <div class="detail" id="wfullDetail">Hover a cell to read it.</div>
 <div class="how"><b>How to read it.</b> Each small square is one cell of the table. The square in row i and column j is the cell W[i,j], which says how hard neuron j pushes neuron i. Red means a positive value (neuron j excites neuron i), blue means a negative value (neuron j quiets neuron i), and white means the value is near zero. This whole picture is what the word "W" refers to. Two summary numbers are written at the bottom of the picture: the average of all the cells (+0.00) and the average size of a cell ignoring its sign (0.10). Those summaries tell you almost nothing about how the network works. The reason is that the network's behaviour depends on the pattern of the cells, on which particular cells are positive and which are negative, and a single total cannot capture a pattern.</div>
</div>
<div class="sketch">
 <div class="eyebrow">Drawing: W as a wiring diagram, on a six-neuron version of the network</div>
 <svg viewBox="0 0 900 300" id="wsketch"></svg>
 <p style="font-size:15px;margin:8px 0 0">Each arrow is one cell of W. Cell W[i,j] answers "how strongly does neuron j's activity last tick push neuron i this tick?" Positive (red) means j excites i, negative (blue) means j quiets i, near zero means i barely listens to j. Six neurons have 6 × 6 = 36 cells; our network has 64 × 64 = 4,096. So W is nothing more than the complete list of who listens to whom and by how much, and that list does not change during a trip. It helps to keep two ideas apart here. The activities are what each neuron is saying on this tick, and they change every tick. W is how much each neuron trusts each other neuron, and it stays fixed for the whole trip.</p>
</div>

<h3>How the gates feed back into F, one tick, one cell at a time</h3>
<p>The write and erase gates are two single numbers the network emits each tick, and the rule applies them to all 4,096 cells of F at once. Here is a 4-by-4 corner of F. Set the gates, then step through the three moves the rule makes every tick.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: a 4-by-4 corner of the F table, with one tick shown as three separate moves</div>
 <div class="controls"><div class="ctl"><label>erase gate this tick <output id="oE2">0.01</output></label><input id="E2" type="range" min="0" max="1" step="0.01" value="0.01"><small>Fraction of every cell removed. 0.01 is a slow fade; 0.77 is what run 19 does at food.</small></div>
 <div class="ctl"><label>write gate this tick <output id="oWr2">0.40</output></label><input id="Wr2" type="range" min="0" max="1" step="0.01" value="0.4"><small>Multiplier on the new deposit. 0 means nothing at all is added this tick; 1 means the whole deposit is added.</small></div></div>
 <div class="row"><button class="btn" id="fb0">start: F before</button><button class="btn" id="fb1">move 1: shrink by (1 − erase)</button><button class="btn" id="fb2">move 2: add ws × write × deposit</button><button class="btn" id="fb3">move 3: clamp to ±1</button><button class="btn" id="fbNext">make this the new "before"</button><button class="btn" id="fbTen">ten full ticks with write 1 and erase 0</button></div>
 <canvas id="fboard" width="1700" height="520"></canvas>
 <div class="how"><b>Why the rule multiplies by (1 − erase) rather than by erase.</b> The erase gate is named for the amount it removes. An erase value of 0.28 means that 28% of each cell is removed, so 72% of it stays, and "keep 72%" is written as multiplying by (1 − 0.28) = 0.72. If the rule multiplied by the gate itself instead, then erase = 1 would keep everything, which is the opposite of what the word "erase" says. Either convention works mathematically, because training would simply learn the opposite sign for the gate. This convention was chosen so that the sentence "the erase gate fires at food" describes the fly's reset directly. The LSTM, a common kind of network with a built-in memory, has a "forget gate" that uses the other convention: there, forget = 1 means keep everything. That is why the name "forget gate" confuses people.</div>
<div class="how"><b>Why move 3 often changes nothing.</b> Move 3 is the clamp: any cell above +1 is set back to +1, and any cell below −1 is set back to −1. It only affects cells that are already past those limits. After a single deposit on this board no cell is past them, so move 3 does nothing. To see it act, press "ten full ticks with write 1 and erase 0". The cells climb tick by tick until some of them reach +1 or −1 and the clamp stops them. Cells that were clipped get an orange border, and the number of clipped cells is written underneath. This clipping is the same "lid" described on the Counter With a Lid page, here shown happening to one cell at a time.</div>
<div class="how"><b>How to read it.</b> The left grid shows the 16 cells of F as they are at the start of the tick, each with its colour (red for positive, blue for negative) and its number. The middle grid shows the deposit. Each cell of the deposit is the receiving neuron's activity now multiplied by the sending neuron's activity one tick ago, so there is one product per cell. A table of all such products is called an "outer product". There are four neurons here, and their activities are written along the edges of the grid. The right grid shows the result of the tick. Move 1 multiplies every cell by the same number, (1 − erase). Move 2 adds ws × write × deposit to every cell. Move 3 clips anything past +1 or −1 back to those limits. After the three moves, the right grid becomes the "before" grid for the next tick. Try setting erase to 0.77, which is what run 19 does at food, and watch move 1 nearly empty the board. That emptying is the reset.</div>
</div>
<h3>The rule that changes F, explained one piece at a time</h3>
<p>Everything about ws, the write gate and the erase gate comes from one rule. It is applied every tick to every one of the 4,096 cells of F. Here it is, and then we will take it apart slowly.</p>
<div class="eq">new F[i,j]  =  (1 − <span class="b">erase</span>) × old F[i,j]   +   ws × <span class="c">write</span> × x_new[i] × x_old[j]</div>
<p>Read it as a sentence: <b>the new value of a cell is its old value shrunk a little, plus a small amount added.</b> That is the whole rule. Two things can happen to a cell each tick, it can shrink and it can have something added, and the rule says exactly how much of each.</p>

<h4>Step 1. What one cell is</h4>
<p>Pick one cell, F[i,j]. It is a single number that belongs to the wire running from neuron j to neuron i. It starts at zero when an episode begins. Its purpose is to remember something about this trip: specifically, how much neurons j and i have been active together, built up tick after tick. Later, when neuron i adds up its inputs, this number gets added on top of the permanent strength W[i,j] (scaled by A[i,j], which we come to at the end). For now, just picture the cell as a box holding a number.</p>
<div class="sketch">
 <div class="eyebrow">Drawing 1 · one cell, and the two things that can happen to it each tick</div>
 <svg viewBox="0 0 900 220">
  <rect x="330" y="60" width="240" height="100" rx="12" fill="var(--panel)" stroke="var(--teal)" stroke-width="3"/><text x="450" y="95" text-anchor="middle" font-family="Bricolage Grotesque" font-size="16" font-weight="700" fill="var(--ink)">F[i,j]</text><text x="450" y="120" text-anchor="middle" font-family="Literata" font-size="14" fill="var(--mute)">one number, e.g. 0.40</text><text x="450" y="142" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">lives on the wire from neuron j to neuron i</text>
  <path d="M330,110 L120,110" stroke="var(--coral)" stroke-width="3" marker-end="url(#ar)"/><text x="225" y="95" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--coral)">1. some of it is removed</text><text x="225" y="135" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">the erase gate decides how much</text>
  <path d="M780,110 L570,110" stroke="var(--amber)" stroke-width="3" marker-end="url(#ar)"/><text x="675" y="95" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--amber)">2. something is added</text><text x="675" y="135" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">ws, the write gate and the two</text><text x="675" y="152" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">neurons' activities decide how much</text>
  <text x="450" y="200" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--mute)">new value = (what is left after removing) + (what is added)</text>
 </svg>
</div>

<h4>Step 2. The removing part: (1 − erase) × old value</h4>
<p>The erase gate is a number between 0 and 1 that the network outputs each tick. It means <b>the fraction of the cell that is thrown away this tick</b>. If the cell is left with a fraction, that fraction is 1 minus what was thrown away. So:</p>
<p>erase = 0 means throw away nothing, keep all of it: the cell is multiplied by 1.<br>erase = 0.01 means throw away one percent, keep 99%: the cell is multiplied by 0.99.<br>erase = 0.28 means throw away 28%, keep 72%: the cell is multiplied by 0.72.<br>erase = 0.77 (what run 19 does at food) means throw away 77%, keep 23%: multiplied by 0.23.<br>erase = 1 means throw away everything: multiplied by 0.</p>
<p>There is no extra number on this side of the rule. The gate alone decides the fraction. That is the reason the erase half of the rule is shorter than the write half: a fraction is already a complete instruction, "keep this much", and does not need anything else to make sense.</p>
<div class="sketch">
 <div class="eyebrow">Drawing 2 · a cell worth 0.40 after the removing step, for five values of the erase gate</div>
 <svg viewBox="0 0 900 250">
  <g id="eraseBars"></g>
 </svg>
</div>

<h4>Step 3. The adding part: ws × write × x_new[i] × x_old[j]</h4>
<p>One word first. Elsewhere on this page the amount that gets added to a cell in one tick is sometimes called the <b>deposit</b>. That is all the word means: the amount added to one cell during one tick. It is not a separate thing in the machine.</p>
<p>This is three ingredients multiplied together. Take them one at a time, starting from the right.</p>
<p><b>x_new[i] × x_old[j]</b>, the pairing. x_new[i] is the receiving neuron's activity right now. x_old[j] is the sending neuron's activity one tick ago. Multiply them. If both are strongly active, this is a large positive number. If one of them is negative, it is negative. If either is near zero, it is near zero. This product is <em>different for every cell</em>, because every cell sits between a different pair of neurons. It is the raw thing being recorded: "were these two neurons active together just now, and how strongly?" This is what "fire together, wire together" means in numbers.</p>
<p><b>write</b>, the write gate. A number between 0 and 1 that the network outputs each tick, the same number for every cell. It means <b>how much of this tick's pairing to actually record</b>. At 0 nothing is recorded this tick; at 1 all of it; at 0.4, forty percent of it. This is the network's moment-to-moment decision about whether what is happening now is worth remembering. In run 19 this gate follows the fly's speed: it opens more when the fly is moving fast, so fast steps are recorded more strongly than slow ones, which is what a distance count needs.</p>
<p><b>ws</b>, the write strength. A single fixed number, 0.074 in run 19. It is not decided tick by tick; training chose it once and it stays. It multiplies every recording, on every cell, on every tick. Why does it exist? Because the pairing x_new × x_old can be as large as 1, and the cell's lid is at 1. Without ws, one tick could fill a cell to the lid, and a count of steps would be over before it started. ws makes each recording small enough that many ticks of walking fit under the lid: at 0.074, even a perfect pairing of 1 with the gate fully open adds only 0.074, so it takes about fourteen such ticks to fill a cell. Training picked 0.074 because that made the counts work best for 30-second trips. You can think of ws as the size of one unit of the count.</p>
<p>So the amount added to a cell this tick is: (the size of one unit) × (how much of this tick to record) × (how strongly these two neurons were active together). Try it with numbers.</p>
<div class="sketch">
 <div class="eyebrow">Drawing 3 · build the amount added, with your own numbers</div>
 <div class="controls">
  <div class="ctl"><label>x_new[i], receiver now <output id="oxn">0.80</output></label><input id="xn" type="range" min="-1" max="1" step="0.05" value="0.8"></div>
  <div class="ctl"><label>x_old[j], sender a tick ago <output id="oxo">0.60</output></label><input id="xo" type="range" min="-1" max="1" step="0.05" value="0.6"></div>
  <div class="ctl"><label>write gate this tick <output id="owr">0.40</output></label><input id="wr" type="range" min="0" max="1" step="0.01" value="0.4"></div>
  <div class="ctl"><label>ws, fixed by training <output id="ows">0.074</output></label><input id="wsv" type="range" min="0.01" max="0.5" step="0.001" value="0.074"></div>
  <div class="ctl"><label>erase gate this tick <output id="oer">0.01</output></label><input id="er" type="range" min="0" max="1" step="0.01" value="0.01"></div>
  <div class="ctl"><label>old F[i,j] <output id="ofo">0.40</output></label><input id="fo" type="range" min="-1" max="1" step="0.05" value="0.4"></div>
 </div>
 <svg viewBox="0 0 900 330" id="depositSvg"></svg>
</div>

<h4>Why "sender a tick ago" and "receiver now", rather than the other way round</h4>
<p>The order is not arbitrary. It matches the direction the wire is used in when the neuron computes its activity. At every tick, neuron i's new activity is worked out from the other neurons' activities from the <em>previous</em> tick. So the wire from j to i always carries "what j was doing a tick ago" into "what i does now". The cell F[i,j] sits on that wire, and when it is read it multiplies x_old[j] and feeds x_new[i].</p>
<p>If the cell records the same pairing, "j a tick ago, i now", then the next time j is active the strengthened cell pushes i toward what i did last time. The memory is written in the same direction of time that it is later used in. If we recorded the opposite pairing, "i a tick ago, j now", the cell would remember something about i-then-j but would still be used to push i from j, so the record would run backwards relative to how it is applied.</p>
<p>For counting steps, the order matters less than you might think. While the fly walks steadily in one direction the same neurons stay active tick after tick, so x_old and x_new are almost equal and either order adds almost the same amount. The order shows itself at turns: for one tick the sender is the old direction and the receiver is the new one, which is why the off-diagonal cell E→N grows in the walker below exactly when the fly turns from east to north. We kept this order because it is the one Hebb's rule, differentiable plasticity and Backpropamine all use.</p>
<div class="sketch">
 <div class="eyebrow">Drawing 3a: the wire carries "a tick ago" into "now", and the record is made the same way</div>
 <svg viewBox="0 0 900 300">
  <text x="30" y="30" font-family="Bricolage Grotesque" font-size="14" font-weight="700" fill="var(--ink)">reading the wire (every tick)</text>
  <circle cx="120" cy="100" r="26" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="120" y="105" text-anchor="middle" font-family="Bricolage Grotesque" font-size="13" fill="var(--ink)">j</text><text x="120" y="145" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">x_old[j]</text><text x="120" y="160" text-anchor="middle" font-family="Literata" font-size="12" fill="var(--mute)">a tick ago</text>
  <line x1="150" y1="100" x2="330" y2="100" stroke="var(--blue)" stroke-width="3" marker-end="url(#ar)"/><text x="240" y="88" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--blue)">× (W + A·F)[i,j]</text>
  <circle cx="360" cy="100" r="26" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="360" y="105" text-anchor="middle" font-family="Bricolage Grotesque" font-size="13" fill="var(--ink)">i</text><text x="360" y="145" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">x_new[i]</text><text x="360" y="160" text-anchor="middle" font-family="Literata" font-size="12" fill="var(--mute)">now</text>
  <text x="500" y="30" font-family="Bricolage Grotesque" font-size="14" font-weight="700" fill="var(--ink)">writing the cell (every tick)</text>
  <rect x="520" y="70" width="330" height="60" rx="10" fill="var(--panel)" stroke="var(--amber)" stroke-width="2"/><text x="685" y="96" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--ink)">F[i,j] += ws × write × x_new[i] × x_old[j]</text><text x="685" y="116" text-anchor="middle" font-family="Literata" font-size="12" fill="var(--mute)">the same two activities, in the same time order</text>
  <text x="450" y="215" text-anchor="middle" font-family="Literata" font-size="14" fill="var(--ink)">time runs the same way in both: from j a tick ago, to i now.</text>
  <text x="450" y="240" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">While walking steadily, x_old ≈ x_new, so the order barely matters. At a turn, it is what makes the E→N cell grow.</text>
 </svg>
</div>
<h4>One cell, or the whole grid? Both: the same rule runs on every cell at once</h4>
<p>Drawing 3a is about one cell, the one on the wire from j to i. But the rule is applied to all 4,096 cells in the same tick. The gates and ws are shared: one erase value, one write value and one ws for the whole board. What differs from cell to cell is the pairing, because each cell sits between a different pair of neurons. If you write the 64 "now" activities down the left edge of the grid and the 64 "a tick ago" activities along the top edge, then every cell's amount added is simply its row's number times its column's number, times the shared ws × write. Move your pointer over the grid to see this for any cell.</p>
<p>Before the grid, one thing to be clear about, because the grid can mislead. <b>Activities belong to neurons; cells belong to wires.</b> A neuron has one activity number. A cell sits on the wire between two neurons, and the grid is not a map of anything; its rows and columns are just the list of neurons written twice, once as receivers (down the side) and once as senders (along the top). So for the cell in row i and column j: the row names the receiving neuron i, and you take that neuron's activity now; the column names the sending neuron j, and you take that neuron's activity a tick ago; then you multiply. Usually i and j are two different neurons. On the diagonal, where i equals j, it is the same neuron at two moments, now and a tick ago, which is the wire from a neuron back to itself.</p>
<div class="sketch">
 <div class="eyebrow">Drawing 3b′: the eight neurons and their activities, and where two cells get their numbers from</div>
 <svg viewBox="0 0 900 330" id="neurCells"></svg>
</div>
<div class="sketch">
 <div class="eyebrow">Drawing 3c: one tick's additions for the whole grid, an eight-neuron version</div>
 <canvas id="gridPair" width="1700" height="640"></canvas>
 <div class="detail" id="gridPairDetail">Move the pointer over a cell.</div>
 <div class="how"><b>How to read it.</b> The column of numbers on the left is x_new, each neuron's activity now. The row of numbers along the top is x_old, each neuron's activity a tick ago. The cell where row i meets column j is coloured by x_new[i] × x_old[j]: red positive, blue negative, pale near zero. When you point at a cell, its row and column light up and the arithmetic is written underneath. The real board is 64 by 64 instead of 8 by 8, and the same construction fills all 4,096 cells in one tick.</div>
</div>
<h4>Why record the pairing at all? Because that is how a count of steps gets stored</h4>
<p>This is the part that deserves the most patience, because it is the reason the whole design works.</p>
<p>A connection between two neurons can only know two things: what the sending neuron is doing and what the receiving neuron is doing. If we want the connections to record something about the trip, those two activities are the only raw material available at each connection. Multiplying them gives a number that is large only when both neurons were active at the same moment. So over a whole trip, each cell adds up "how often, and how strongly, did these two neurons fire together?" This way of changing a connection was proposed by Donald Hebb in 1949 and is usually summarised as "cells that fire together wire together". We chose it as the rule for this network (it is the "learning rule" knob on the board in question 1). The network did not invent it. What the network does learn is which neurons should carry which signals, so that this fixed rule ends up storing something useful.</p>
<p>Now connect it to homing. The network has compass cells: neurons that are active when the fly faces a particular direction. Suppose neuron N is active while the fly walks north and quiet otherwise. Then during every tick of northward walking, the cell between N and itself (and the cells between N and any other neuron active at the same time) receives a positive addition. Fifty ticks of walking north means fifty small additions to those cells. Walking east makes a different set of cells grow, the ones around the east-tuned neurons. So at the end of a wander, the pattern of which cells have grown says which directions were walked, and the size of each says how far. That is a count of steps in each direction, held in the connections. The write gate, by opening more at higher speed, makes each addition roughly proportional to the distance covered in that tick rather than just the time spent.</p>
<p>On the way home the fly walks the opposite directions, so the opposite cells grow. The reading side of the machine (A, then W_out) has learned to compare them: roughly, north minus south and east minus west, which together point at home. The drawing below is a four-neuron version of exactly this. Walk the fly around and watch the cells.</p>
<div class="sketch">
 <div class="eyebrow">Drawing 3b: a four-compass-cell fly, its F table, and the count that appears in it</div>
 <div class="row"><button class="btn" id="wN">walk north one tick</button><button class="btn" id="wE">walk east one tick</button><button class="btn" id="wS">walk south one tick</button><button class="btn" id="wW">walk west one tick</button><button class="btn" id="wReset">new trip (F to zero)</button></div>
 <canvas id="compassF" width="1700" height="520"></canvas>
 <div class="how"><b>How to read it.</b> Left: the fly's path, starting at home (the black dot). Middle: the 4 × 4 table of F for four neurons named N, E, S, W, each active (value 1) only while the fly walks in its direction. Each tick, the amount added to a cell is ws × write × (receiver now) × (sender a tick ago), with ws = 0.1 and the write gate held at 1 for simplicity. The cell N→N grows by 0.1 for every tick of walking north; the cell E→N grows once at the moment the fly turns from east to north, because for that one tick the sender (east, a tick ago) and the receiver (north, now) are both 1. Right: what a reader can get from the table by subtraction: (N→N minus S→S) is the net number of northward ticks, (E→E minus W→W) the net eastward ticks, and the arrow is the direction back to home that those two numbers imply. The real network does the same thing with 32 compass cells whose activities are not clean 0s and 1s, so its table is messier, but the principle is this one.</div>
</div>
<h4>Step 4. Put the two halves together, and watch a cell over several ticks</h4>
<p>Now the rule is just: what is left after removing, plus what is added. Below, the same cell is followed for eight ticks using the sliders above, as if the two neurons kept firing the same way and the gates stayed where you set them. With a small erase and a steady pairing you will see the cell climb by the same amount each tick, which is a count. With a large erase you will see it collapse toward zero, which is a reset.</p>
<div class="sketch">
 <div class="eyebrow">Drawing 4 · eight ticks of the same cell, from the sliders above</div>
 <canvas id="cellTicks" width="1700" height="420"></canvas>
</div>

<h4>Step 5. Where ws and A each act</h4>
<p>You asked whether ws is "the weight of F", and whether that is what A is. They act at two different moments in the tick, and the drawing shows the two moments.</p>
<p>ws acts when something is <b>put into</b> the cell. It is part of the adding step above and appears nowhere else in the machine. It never touches W, A, W_in or W_out, and it never touches the activities directly. Its only job is to size the recordings that go into F.</p>
<p>A acts when the cell is <b>read out</b>. That happens in a different line of the tick: when neuron i adds up its inputs, the wire from j contributes (W[i,j] + A[i,j] × F[i,j]) × x_old[j]. A[i,j] says how much of what is stored in the cell neuron i should actually feel. A is a different number for every cell (4,096 of them); ws is one number for all.</p>
<p>Why does the network need both? Because of the lid. ws decides how fast a cell fills and therefore how many ticks of walking fit before it hits ±1. A decides how loudly a filled cell is heard. If there were no lid, you could trade one for the other (write twice as hard and listen half as loudly). With the lid, they are genuinely separate: no amount of A can undo a cell that has already been pushed against the lid by a large ws.</p>
<div class="sketch">
 <div class="eyebrow">Drawing 5 · the two moments: ws when writing in, A when reading out</div>
 <svg viewBox="0 0 900 260">
  <rect x="340" y="80" width="220" height="90" rx="12" fill="var(--panel)" stroke="var(--teal)" stroke-width="3"/><text x="450" y="115" text-anchor="middle" font-family="Bricolage Grotesque" font-size="16" font-weight="700" fill="var(--ink)">the cell F[i,j]</text><text x="450" y="140" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">holds a number between −1 and +1</text>
  <path d="M60,125 L335,125" stroke="var(--amber)" stroke-width="3" marker-end="url(#ar)"/><text x="195" y="70" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" font-weight="700" fill="var(--amber)">writing in (the rule)</text><text x="195" y="92" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--ink)">+ ws × write × pairing</text><text x="195" y="150" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">ws is here, and only here</text><text x="195" y="168" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">one number for all 4,096 cells</text>
  <path d="M565,125 L840,125" stroke="var(--blue)" stroke-width="3" marker-end="url(#ar)"/><text x="705" y="70" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" font-weight="700" fill="var(--blue)">reading out (the neuron's sum)</text><text x="705" y="92" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--ink)">(W + A × F) × x_old[j]</text><text x="705" y="150" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">A is here, and only here</text><text x="705" y="168" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">a different number for each cell</text>
  <text x="450" y="225" text-anchor="middle" font-family="Literata" font-size="14" fill="var(--ink)">ws sets how fast the cell fills up (and so when it hits the lid). A sets how loudly neuron i hears what is in it.</text>
 </svg>
</div>
<p>The chart below makes the last point measurable. Move ws and the moment the cell hits the lid moves. Move A and the height of what the neuron feels changes, but the moment it flattens does not.</p>
<div class="sketch">
 <div class="eyebrow">Drawing 6 · ws changes when the lid is reached; A does not</div>
 <div class="controls"><div class="ctl"><label>ws <output id="oWS3">0.10</output></label><input id="WS3" type="range" min="0.01" max="0.5" step="0.01" value="0.1"></div>
 <div class="ctl"><label>A for this cell <output id="oA3">0.50</output></label><input id="A3" type="range" min="0" max="1.5" step="0.05" value="0.5"></div></div>
 <canvas id="wsA" width="1700" height="480"></canvas>
</div>
<table><thead><tr><th>number</th><th>how many</th><th>changes during a trip?</th><th>who sets it</th></tr></thead><tbody>
<tr><td>activity of a neuron</td><td class="n">64</td><td>every tick</td><td>the arithmetic of the tick</td></tr>
<tr><td>turn, write gate, erase gate</td><td class="n">3</td><td>every tick</td><td>the arithmetic of the tick</td></tr>
<tr><td>F, the fast table</td><td class="n">4,096</td><td>every tick</td><td>the rule, using the two gates and ws</td></tr>
<tr><td>W, A, W_in, W_out</td><td class="n">8,707</td><td>never</td><td>training, then frozen</td></tr>
<tr><td>ws</td><td class="n">1</td><td>never</td><td>training, then frozen</td></tr>
</tbody></table>

<h3>The math of one tick, with all the numbers</h3>
<p>Now every piece has been drawn. The calculator below does the whole tick on a three-neuron machine and prints each step.</p>
<table><thead><tr><th>table</th><th>shape</th><th class="n">weights</th><th class="n">biases</th><th class="n">total</th><th>trained?</th></tr></thead><tbody>
<tr><td>W_in</td><td>4 inputs × 64 neurons</td><td class="n">256</td><td class="n">64</td><td class="n">320</td><td>yes</td></tr>
<tr><td>W</td><td>64 × 64</td><td class="n">4,096</td><td class="n">0</td><td class="n">4,096</td><td>yes</td></tr>
<tr><td>A</td><td>64 × 64</td><td class="n">4,096</td><td class="n">0</td><td class="n">4,096</td><td>yes</td></tr>
<tr><td>W_out</td><td>64 neurons × 3 outputs</td><td class="n">192</td><td class="n">3</td><td class="n">195</td><td>yes</td></tr>
<tr><td>ws</td><td>one number</td><td class="n">1</td><td class="n">0</td><td class="n">1</td><td>yes</td></tr>
<tr><td><b>parameters</b></td><td></td><td></td><td></td><td class="n"><b>8,708</b></td><td></td></tr>
<tr><td>F</td><td>64 × 64</td><td class="n">4,096</td><td class="n"></td><td class="n">4,096</td><td>no: state, zero at episode start, rewritten every tick</td></tr>
</tbody></table>
<p>So the machine holds more than 8,708 numbers, but only 8,708 are <span class="term" title="parameter: a number that training sets and then freezes">parameters</span>. F is the same size as W but it is state, like the neurons' activity: nothing about training ever touches it directly. Training shapes the rule that writes it.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: one tick worked out by hand, on a three-neuron version of the same machine</div>
 <p style="font-size:15px;margin-top:6px">Same equations, 3 neurons instead of 64 so every number fits on screen. Set the four inputs, press "one tick", and read the five steps. The little tables are made-up trained weights; the F table starts at zero and changes as you tick, exactly as the real one does. Press "at food" and watch what the erase gate does to F.</p>
 <div class="controls">
  <div class="ctl"><label>compass east-west <output id="oi0">0.7</output></label><input id="i0" type="range" min="-1" max="1" step="0.1" value="0.7"></div>
  <div class="ctl"><label>compass north-south <output id="oi1">0.7</output></label><input id="i1" type="range" min="-1" max="1" step="0.1" value="0.7"></div>
  <div class="ctl"><label>speed <output id="oi2">1.0</output></label><input id="i2" type="range" min="0" max="1.4" step="0.1" value="1"></div>
  <div class="ctl"><label>at food <output id="oi3">0</output></label><input id="i3" type="range" min="0" max="1" step="1" value="0"></div>
 </div>
 <div class="row"><button class="btn" id="tick">one tick</button><button class="btn" id="tick10">ten ticks</button><button class="btn" id="tickReset">new episode (F and activity to zero)</button><span class="eyebrow" id="tickCount">tick 0</span></div>
 <div id="tickOut" style="font-size:14.5px;margin-top:12px"></div>
</div>

<h3>How training changes the 8,708 numbers</h3>
<p>Training never touches F or the activities. It changes only the parameters, and it does so with one rule applied to every one of the 8,708 numbers after each batch of 32 episodes. The rule needs two ideas. The <span class="term" title="loss: a single number that says how badly the network did on a batch of episodes; training tries to make it smaller">loss</span> is a single number that says how badly the network did on the batch, and lower is better. The <span class="term" title="learning rate: a fixed number that sets how big each adjustment to the parameters is">learning rate</span> is a fixed number that sets how big each adjustment is. The picture below shows the rule acting on a single parameter.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: one parameter, moved one step downhill on the loss curve</div>
 <div class="controls"><div class="ctl"><label>learning rate <output id="oLR">0.30</output></label><input id="LR" type="range" min="0.02" max="1.2" step="0.02" value="0.3"><small>The step size. The real runs used 0.001, 0.0003 and 0.0001. The curve here is drawn much steeper than a real one so that the steps are visible.</small></div></div>
 <div class="row"><button class="btn" id="gdStep">one training step</button><button class="btn" id="gdReset">reset the ball</button><span class="eyebrow" id="gdN">step 0</span></div>
 <canvas id="gd" width="1700" height="420"></canvas>
 <div class="how"><b>How to read it.</b> Across the bottom is the value of one parameter, for example the erase gate's bias. Up the side is the loss the network would get with that value, if every other parameter were held fixed. The black curve therefore shows how the loss changes as this one parameter changes. The ball marks the parameter's current value. Each time you press "one training step", the ball measures the slope of the curve directly underneath it and moves downhill by the learning rate multiplied by that slope. Where the curve is steep the ball moves a long way. Where the curve is nearly flat the ball barely moves at all, because the slope is close to zero. That flat-part behaviour is the same thing as the "deaf gate" of question 3, seen from the other side: a gate resting on a flat part of its own curve gives training a tiny slope to work with, so training barely moves it. Now try turning the learning rate up to 1.0. The ball overshoots the bottom of the valley and bounces from side to side instead of settling. That bouncing is what happened in run 5, where the loss suddenly got worse instead of better; the pages call this run 5's collapse.</div>
</div>
<h3>So what is a knob?</h3>
<p>A knob is any number or choice that we fix <em>before</em> a run starts and hold fixed while it runs. A knob is never something the network learns. The 8,708 slow weights are learned by training, so they are not knobs. The fast weights F are rewritten by the network itself while it runs, so they are not knobs either. Every other number or choice that we fix beforehand is a knob. Here is the whole board of them, grouped by the part of the experiment each one belongs to. Click a knob to see what it does and which runs changed it.</p>
<div class="panel" id="knobBoard"></div>
<div class="detail" id="knobDetail">Click a knob above.</div>

<!-- ============ Q2 ============ -->
<h2 id="q2"><span class="q">QUESTION 2</span>Why the erase-bias shift was "not a knob change but something else"</h2>
<p>Look at the last group on the board: <b>where the network starts</b>. Most knobs describe the world the fly lives in or the way training is run. The bias shift is a different kind of thing. It reaches inside the network and moves one of the 8,708 learned numbers by hand, before training resumes. It does not change what the network is asked to do, and it does not change how the network is scored. What it changes is the network's starting position before training begins to move it. In the drawing below, the curved line is the loss curve from the training picture in question 1 (the "hill"), and the dot on it is the network's current set of parameter values (the "climber"). Training moves the climber downhill.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: an ordinary knob changes the shape of the hill; the bias shift moves the climber instead</div>
 <svg viewBox="0 0 900 260">
  <g transform="translate(40,20)">
   <text x="0" y="0" font-family="Bricolage Grotesque" font-size="16" font-weight="700" fill="var(--ink)">A knob: reshape the hill</text>
   <path id="hillA" d="M0,180 C60,170 90,60 150,80 C210,100 250,180 320,120 C360,90 380,40 400,60" fill="none" stroke="var(--mute)" stroke-width="3"/>
   <circle cx="150" cy="80" r="9" fill="var(--teal)"/><text x="150" y="65" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--teal)">network</text>
   <text x="0" y="215" font-family="Literata" font-size="13" fill="var(--mute)">food stand, penalty, world speed: the valleys move,</text><text x="0" y="232" font-family="Literata" font-size="13" fill="var(--mute)">the climber stays where it was.</text>
  </g>
  <g transform="translate(480,20)">
   <text x="0" y="0" font-family="Bricolage Grotesque" font-size="16" font-weight="700" fill="var(--ink)">The bias shift: move the climber</text>
   <path d="M0,180 C60,170 90,60 150,80 C210,100 250,180 320,120 C360,90 380,40 400,60" fill="none" stroke="var(--mute)" stroke-width="3"/>
   <circle cx="150" cy="80" r="9" fill="var(--mute)" opacity=".4"/><circle cx="300" cy="140" r="9" fill="var(--coral)"/>
   <path d="M160,78 C220,60 260,110 292,134" fill="none" stroke="var(--coral)" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#ar)"/>
   <text x="300" y="165" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--coral)">+2.5 on one bias</text>
   <text x="0" y="215" font-family="Literata" font-size="13" fill="var(--mute)">same hill, same score, same rules; the climber is lifted</text><text x="0" y="232" font-family="Literata" font-size="13" fill="var(--mute)">out of a flat spot it could not leave on its own.</text>
  </g>
 </svg>
</div>
<p>Why count it separately from the other knobs? There are three reasons, and each one limits what we are allowed to conclude from the runs.</p>
<p><b>It is not a property of the task.</b> If someone else reproduces our world and our training exactly, they will not rediscover the reset unless they also perform the shift by hand. So we cannot claim that "the fly's reset emerges from this task on its own." What we can say is "once the erase gate is in a position where training can move it, the task rewards a reset."</p>
<p><b>It is a warm start plus one adjustment made by hand.</b> A warm start means that a run begins from the previous run's trained weights instead of from random ones. Every shifted run was a warm start. On top of that, we changed one number out of the 8,708, the erase gate's bias, by hand, and only then let gradient descent take over. So the finding is real: the network itself chose to fire the gate at food rather than away from food. But the starting point from which it made that choice was chosen by us.</p>
<p><b>It was repeated, which turns it from a one-off into a measured series.</b> We made the same move five times (runs 7B, 10, 12, 14 and 16), and before each run we wrote down what we predicted would happen. Because the move was repeated, we can report the outcome as a series of measurements rather than a single event: the ratio of erasing at food to erasing away from food went 3, then 7, then 20, then 33, then 53. Question 3 explains why the move works at all.</p>

<!-- ============ Q3 ============ -->
<h2 id="q3"><span class="q">QUESTION 3</span>What "the sigmoid was parked at −5" means</h2>
<p>The erase gate is one output of the network: a raw number, call it z, that can be anything from very negative to very positive. But a gate has to be between 0 (erase nothing) and 1 (erase everything). The <span class="term" title="sigmoid: the S-shaped squashing function, 1 / (1 + e^−z). It turns any number into a value between 0 and 1">sigmoid</span> does that squashing. It is a <span class="term" title="A function whose output is not simply proportional to its input: doubling the input does not double the output. Every squashing function is nonlinear">nonlinearity</span>: its output is not proportional to its input. That squashing is the reason the gate was "deaf" to training, and the drawing below shows how. Drag the bias slider and watch the dot move along the curve.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: the S-shaped sigmoid curve, and how far one training nudge moves the gate at each resting position</div>
 <div class="controls"><div class="ctl"><label>bias (where the gate rests) <output id="oB">−5.0</output></label><input id="B" type="range" min="-8" max="4" step="0.1" value="-5"><small>The raw number z when no neuron is pushing on the gate. Training moves this number slowly; the bias shift moved it by hand.</small></div>
 <div class="ctl"><label>size of the nudge from training <output id="oG">1.0</output></label><input id="G" type="range" min="0.2" max="3" step="0.1" value="1"><small>How hard one training step pushes on z. The same push moves the gate's output by very different amounts depending on where the gate rests.</small></div></div>
 <canvas id="sig" width="1700" height="520"></canvas>
 <div class="row"><span class="eyebrow">the campaign's path</span><button class="btn" data-b="-5">start −5</button><button class="btn" data-b="-2.5">run 7B −2.5</button><button class="btn" data-b="-1">run 10 −1</button><button class="btn" data-b="0.5">run 12 +0.5</button><button class="btn" data-b="2">run 14 +2</button><button class="btn" data-b="3.5">run 16 +3.5</button><button class="btn" data-b="1.86">run 19 trained: +1.86</button></div>
 <div class="how"><b>How to read it.</b> Across the bottom is the raw input z, which can be any number. Up the side is the gate's output, which is always between 0 and 1. The curve shows the output for every possible raw input. The dot marks where the gate rests when no neuron is pushing on it, which is set by the bias slider. The short bar under the dot shows how far one training nudge would move the gate's output from that resting position. Its length is the size of the nudge multiplied by the curve's <span class="term" title="slope: how steep the curve is at that point, which is exactly how much the output changes for a small change in the input">slope</span> at the dot. At z = −5 the slope is 0.007, so a nudge of 1 moves the gate by only seven thousandths. At z = 0 the slope is 0.25, which is thirty-five times larger, so the same nudge moves the gate thirty-five times as far. The buttons under the chart move the dot to each resting position the campaign actually used.</div>
</div>
<div class="panel">
 <div class="eyebrow">The sigmoid in numbers</div>
 <div class="eq">σ(z) = 1 / (1 + e<sup>−z</sup>)     slope at z = σ(z) × (1 − σ(z))</div>
 <table><thead><tr><th class="n">raw z</th><th class="n">gate σ(z)</th><th class="n">slope</th><th>meaning</th></tr></thead><tbody>
 <tr><td class="n">−5</td><td class="n">0.0067</td><td class="n">0.0066</td><td>where the erase gate started: the gate is nearly shut, and the slope is so small that training can barely move it</td></tr>
 <tr><td class="n">−2.5</td><td class="n">0.076</td><td class="n">0.070</td><td>after the first shift: the slope is ten times larger, so each training step has ten times the effect</td></tr>
 <tr><td class="n">0</td><td class="n">0.5</td><td class="n">0.25</td><td>the steepest point on the curve, where each training step has the largest effect</td></tr>
 <tr><td class="n">+1.86</td><td class="n">0.87</td><td class="n">0.11</td><td>run 19's trained resting position</td></tr>
 <tr><td class="n">+5</td><td class="n">0.9933</td><td class="n">0.0066</td><td>nearly flat again, at the top: the gate is almost fully open and training can barely move it</td></tr>
 </tbody></table>
 <p style="font-size:15px"><b>Why the slope multiplies the nudge.</b> Training wants to change the gate's output. But it cannot touch the output directly; it can only change the raw number z, through the bias and through W_out. When z changes by a small amount, the output changes by the slope multiplied by that amount. That is what "slope" means: how much the output moves for each unit the input moves. So every training signal that reaches the gate is multiplied by the slope on its way to the bias. At z = −5 the multiplier is 0.0066. A push that would have moved the gate by 0.1 if the gate were resting at z = 0 moves it by only 0.0026 when the gate is resting at z = −5.</p>
</div>
<h3>How that played out for us</h3>
<p>We started the erase gate at −5 on purpose. This is the same precaution people take with the "forget gate" of an LSTM, which they usually start mostly closed. The worry is this: if the network erased freely from the very first training iteration, the tallies could never build up, and with nothing to build on nothing would be learned. The precaution worked, and the tallies did build up. The cost was that the gate sat on the flat part of the S curve, where <span class="term" title="gradient descent: the training method. Compute which direction each number should move to lower the loss, then move a small step that way">gradient descent</span> could barely move it. Runs 2, 5 and 7 pushed on the gate with penalties of 0.5 and 20 and got no movement, because every push was multiplied by 0.007 before it reached the bias.</p>
<p>The bias shift lifts the dot up the curve. At −2.5 the slope is 0.07, ten times larger than at −5; at 0 it is 0.25. Once the gate was on a steeper part of the curve, the same training signals that had been having no effect started to work. The network reduced erasing away from food, because erasing there loses part of the distance count, and it increased erasing at food, because that clears the board for the next trip. Each later shift moved the resting position higher again. Each time, training then settled the gate a little lower than where we had put it, at a spot where erasing at food is large and erasing away from food is near 0.01. Run 19's trained bias is +1.86. That means the gate now rests at 0.87 open, and the neurons that read the food input push it down hard whenever the fly is not at food.</p>
<div class="panel real">
 <div class="eyebrow">Real data: erase per tick while at food and while away from food, for every run</div>
 <canvas id="eraseRuns" width="1700" height="520"></canvas>
 <div class="how"><b>How to read it.</b> Each run gets a pair of bars. The coral bar is the average erase gate value per tick while the fly stands at food. The grey bar is the average erase gate value per tick everywhere else. The vertical axis is a <span class="term" title="log scale: each step up the axis multiplies by ten instead of adding a fixed amount, so 0.001, 0.01, 0.1 and 1 are evenly spaced">log scale</span>, which means each step up the axis multiplies the value by ten; this is used because the values range from below 0.001 to nearly 1, and on an ordinary scale the small ones would be invisible. What to look for: before run 7B, the two bars in each pair are about equal, or the coral bar is lower, which means the gate erases a little all the time and does not prefer food (a fade). From run 7B onward, the coral bar climbs with each shift while the grey bar stays put near 0.01. That is the reset appearing, one shift at a time.</div>
</div>

<!-- ============ Q4 ============ -->
<h2 id="q4"><span class="q">QUESTION 4</span>What Peter's delta rule was</h2>
<p>Our rule writes the whole pattern every tick. Peter's note pointed out that this is a very old rule (Hebb, 1949: "fire together, wire together") and that the modern sequence-model world has moved to a cousin of it, the <b>delta rule</b>: write only the part you could not already predict. Here are both, with the words under the symbols.</p>
<div class="eq">Hebb (ours): F ← (1 − <span class="b">erase</span>)·F + ws·<span class="c">write</span>·<span class="a">x_new ⊗ x_old</span></div>
<p style="font-size:15px;margin-top:6px">Read: shrink the board a little (erase), then add the write strength times the write gate times <span class="term" title="outer product: a table with one row per neuron now and one column per neuron a tick ago; each cell is the product of those two activities. It records 'who was active after whom'">the table of who was active after whom</span>.</p>
<div class="eq">Delta (Peter's): pred = F·x_old;   F ← (1 − <span class="b">erase</span>)·F + ws·<span class="c">write</span>·<span class="a">(x_new − pred) ⊗ x_old</span></div>
<p style="font-size:15px;margin-top:6px">Read: first ask F what it expects the new activity to be, given the old. Then write only the difference between what happened and what F expected. Once F predicts well, the difference is zero and writing stops on its own.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: one connection under each rule, while the fly walks in the same direction for many ticks</div>
 <div class="controls"><div class="ctl"><label>ticks walking the same direction <output id="oN">60</output></label><input id="N" type="range" min="5" max="150" step="1" value="60"></div>
 <div class="ctl"><label>write strength <output id="oS">0.10</output></label><input id="S" type="range" min="0.02" max="0.4" step="0.01" value="0.1"></div></div>
 <canvas id="delta" width="1700" height="460"></canvas>
 <div class="legend"><span><i style="background:var(--teal)"></i>Hebb: keeps adding, hits the lid</span><span><i style="background:var(--blue)"></i>delta: writes the surprise, then settles</span><span><i style="background:var(--coral)"></i>the ±1 lid</span></div>
 <div class="how"><b>How to read it.</b> Across the bottom is time in ticks. Up the side is the strength of one connection. The fly holds one heading for the whole time, so the same two neurons fire together tick after tick. The teal line is the connection under the Hebb rule: it grows on every tick, until it reaches the coral line, which is the ±1 lid. This is what a tally needs, because a tally has to keep counting the steps for as long as the fly keeps walking. The blue line is the same connection under the delta rule: it grows only until it can predict the pattern, and then it flattens out. That is what a memory of "what usually follows what" needs, because once the pattern is learned there is nothing more to learn. But it is exactly the wrong behaviour for counting: after the line flattens, twenty steps and sixty steps leave the connection at the same value, so the count is lost. Move the "ticks walking" slider to see this.</div>
</div>
<h3>Why it was a good idea and why it failed here</h3>
<p>Peter's argument was sound: Hebb has no natural stopping point, which is why F needs a lid and why the erase gate had to fight saturation. Delta self-limits, so the lid becomes unnecessary and the erase gate is freed to do only one job, forgetting the last trip. Written down before running: delta should keep a wider F-versus-no-F gap and find the reset sooner.</p>
<p>What happened: run 15 (a cold start, with the rule swapped and nothing else changed) never formed a memory at all; the gap between the score with F and the score without F stayed at zero for 800 iterations, and the write strength never moved. Run 18 (a warm start from run 14's working Hebb tally) lost its memory within 100 iterations of the rule swap. The drawing above shows why. This task needs a counter. A rule that stops writing as soon as it can predict its input stops counting at exactly the moment the count matters. The negative result is clear, and it appeared in both forms of the test, the cold start and the warm start. But it is a result about this task, not about the delta rule in general. On a task that asks "what usually follows what", the outcome would very likely be the other way round.</p>

<!-- ============ Q5 ============ -->
<h2 id="q5"><span class="q">QUESTION 5</span>Is comparing "F allowed" with "F held at zero" a fair test?</h2>
<p>Your instinct is right, and it is worth being precise about what the test does and does not show. There are two different comparisons in the campaign and they answer two different questions.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: the two kinds of comparison used in the campaign</div>
 <svg viewBox="0 0 900 300">
  <g transform="translate(20,20)">
   <text x="0" y="0" font-family="Bricolage Grotesque" font-size="16" font-weight="700" fill="var(--ink)">1. Ablation: same brain, one part switched off at exam time</text>
   <rect x="0" y="20" width="180" height="90" rx="10" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="90" y="50" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">brain A</text><rect x="55" y="62" width="70" height="30" rx="5" fill="var(--chalk)" stroke="var(--teal)"/><text x="90" y="82" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--teal)">F on</text>
   <rect x="220" y="20" width="180" height="90" rx="10" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="310" y="50" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">brain B (same weights)</text><rect x="275" y="62" width="70" height="30" rx="5" fill="var(--soft)" stroke="var(--coral)"/><text x="310" y="82" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--coral)">F = 0</text>
   <text x="0" y="140" font-family="Literata" font-size="13.5" fill="var(--mute)">Answers: "where does the trained brain keep its memory?"</text>
   <text x="0" y="160" font-family="Literata" font-size="13.5" fill="var(--mute)">Does not answer: "is a fast-weight memory better than an activity memory?"</text>
  </g>
  <g transform="translate(480,20)">
   <text x="0" y="0" font-family="Bricolage Grotesque" font-size="16" font-weight="700" fill="var(--ink)">2. Rival: a brain trained without the part</text>
   <rect x="0" y="20" width="180" height="90" rx="10" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="90" y="50" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">run 3 line</text><rect x="55" y="62" width="70" height="30" rx="5" fill="var(--chalk)" stroke="var(--teal)"/><text x="90" y="82" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--teal)">F on</text>
   <rect x="220" y="20" width="180" height="90" rx="10" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="310" y="50" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">run 20 (own training)</text><rect x="275" y="62" width="70" height="30" rx="5" fill="var(--soft)" stroke="var(--coral)"/><text x="310" y="82" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="var(--coral)">no F, ever</text>
   <text x="0" y="140" font-family="Literata" font-size="13.5" fill="var(--mute)">Answers: "can this network do the job without fast weights,</text>
   <text x="0" y="160" font-family="Literata" font-size="13.5" fill="var(--mute)">given the same recipe and budget?"</text>
  </g>
  <g transform="translate(20,215)"><rect x="0" y="0" width="860" height="60" rx="8" fill="var(--soft)"/><text x="16" y="24" font-family="Literata" font-size="14" fill="var(--ink)">Your worry applies to comparison 1: brain B was never trained to live without F, so of course it fails. That is what an</text><text x="16" y="44" font-family="Literata" font-size="14" fill="var(--ink)"><tspan class="term">ablation</tspan> is for: remove one part and see what breaks. It shows where the memory is kept. It does not say which design is better; comparison 2 does that, with its own caveats.</text></g>
 </svg>
</div>
<p><b>So how should you think about A versus B?</b> Think of it as a way of finding out where the memory is kept, rather than as a contest between two designs. When brain A homes and brain B walks randomly, we learn that whatever brain A uses to find home is stored in F and not in the neurons' activity. That is a real fact about the trained brain, and it is the fact the roadmap called "memory in the synapses." The comparison would only be unfair if we used it to claim "fast weights are better than activity memory," and that is a claim the ablation cannot support.</p>
<p><b>The real contest between two designs is the rival, run 20.</b> It used the same 64 neurons, the same inputs, the same training recipe as run 3 and the same random seed, but with the plastic part switched off before training began. It never learned to home, even on 10-second trips. That is evidence that, for this network and this recipe, a memory held in the neurons' activity alone did not form. But a fair skeptic still has three objections, and all three are valid:</p>
<p>First, one recipe and one seed is a single sample, and a single sample can be unlucky. Second, the learning rate and the initial weights were tuned over twenty runs for the fast-weight version and over zero runs for the rival. Third, 64 tanh neurons with all-to-all connections is a design in which activity memories are known to be hard to train by gradient descent anyway. This is called the vanishing-gradient problem: the training signal shrinks each time it is passed back through one more tick, so a memory that must last many ticks receives almost no signal. LSTMs were invented to get around it. So the rival was at a disadvantage from the start. A fair level 4 would give the rival several learning rates to choose from, a longer first stage, and ideally an LSTM-style cell that is built to hold activity over time. Until that is done, the honest way to state the result is: "the memory we trained lives in F, and a matched attempt with activity memory only did not learn." It would be an overstatement to say "fast weights win."</p>

<!-- ============ Q6 ============ -->
<h2 id="q6"><span class="q">QUESTION 6</span>Reset: why "yes", "fade" or "never" when the number is continuous</h2>
<p>You are right that nothing about the erase gate is binary. It is a number between 0 and 1 at every tick. The labels are a summary, and this is the exact rule the report uses, so you can disagree with it knowingly. Two averages are computed over the 200-trip test: erase per tick while standing at food, and erase per tick everywhere else.</p>
<div class="eq"><span class="b">reset</span> if (erase at food > 0.30) and (erase at food > 5 × erase away)<br><span class="c">fade</span> otherwise, if erase away > 0.003<br><span class="d">never erases</span> otherwise</div>
<p style="font-size:15px">In words: "reset" needs the gate to open at least 30% on the average food tick <em>and</em> to prefer food over elsewhere by at least five to one. "Fade" means a small constant erase that is not food-selective, the thing gradient descent finds when left alone. "Never" means the gate is shut everywhere, which is what happened when a penalty was applied before any memory existed.</p>
<div class="panel real">
 <div class="eyebrow">Real data: every run placed by its two erase numbers, with the labelling rule drawn on top</div>
 <canvas id="resetMap" width="1700" height="640"></canvas>
 <div class="how"><b>How to read it.</b> Across the bottom is the average erase per tick away from food. Up the side is the average erase per tick at food. Both axes are log scales, so each step along an axis multiplies the value by ten. Every run is one dot. The diagonal line marks "erase at food equals erase away from food"; a run on or below that line erases at least as much away from food as at food, which is a fade or worse. The shaded corner in the upper left is the region where the rule's two conditions are both met, so any run inside it is labelled "reset". What to look for: the shifted runs (7B, 10, 12, 14, 16 and 19) climb almost straight up, with the away-from-food value staying near 0.01 the whole time. That means the network sharpened its preference for erasing at food without ever changing how much it fades between food visits. The two sliders move the rule's thresholds, so you can check how much the labels depend on the exact numbers chosen.</div>
 <div class="controls"><div class="ctl"><label>at-food threshold <output id="oT1">0.30</output></label><input id="T1" type="range" min="0.05" max="0.6" step="0.01" value="0.3"></div><div class="ctl"><label>preference ratio <output id="oT2">5</output></label><input id="T2" type="range" min="1.5" max="30" step="0.5" value="5"></div></div>
</div>

<!-- ============ Q7 ============ -->
<h2 id="q7"><span class="q">QUESTION 7</span>Every run in order: why that knob, what I predicted, what happened</h2>
<p>This is questions 2 and 7 from your list in one place. Step through the runs. Each card has four parts: the situation I was looking at, the one knob I chose and why that one, the prediction written before the run started, and the finding with a verdict. The chart above the cards is the 30-second score for the run on the card and its ancestors, so you can see the line it belongs to.</p>
<div class="panel">
 <div class="eyebrow">The two numbers on every card</div>
 <p style="font-size:15px;margin:8px 0 0"><b>Score</b> is the exam: 200 fresh trips (seed 4242), and for each trip the closest the fly ever gets to home on its return, averaged. Lower is better; 0 would be perfect; a random walk scores about 4.4 at 30 s; the hand-built brain 0.75. "With F" is the trained brain; "without F" is the same brain with F forced to zero every tick. <b>Loss</b> is what training minimises: the mean distance from home over the last ten seconds of each return, plus the erase penalty. The two track each other but are not the same number, which is why the dashboard shows both.</p>
</div>
<div class="panel">
 <div class="stepper" id="steps"></div>
 <canvas id="lineage" width="1700" height="300"></canvas>
 <div class="card" id="runCard"></div>
</div>

<!-- ============ Q8 ============ -->
<h2 id="q8"><span class="q">QUESTION 8</span>The circuit motifs, in depth</h2>
<p>A <span class="term" title="motif: a small, recognisable pattern of wiring or activity that does one job, like a compass cell or a gate that reads one input">motif</span> is a small recurring pattern in how the neurons are wired or how they behave, one that does a nameable job. We look for three because the real fly has three: compass cells, a tally whose writing depends on speed, and a wipe at food. All of the pictures below are from run 19's final network unless labelled otherwise. First the sketch of what each motif should look like if it is there, then the real measurement.</p>

<h3>Motif 1: compass cells</h3>
<div class="sketch">
 <div class="eyebrow">Drawing: the tuning curve of a compass cell, next to the tuning curve of a cell that is not tuned</div>
 <p style="font-size:15px;margin-top:6px">Turn the fly through all sixteen directions and record one neuron's activity at each. A compass cell fires for one preferred direction and goes quiet opposite it (left). A cell that is not a compass cell fires about the same everywhere (right). The <span class="term" title="tuning curve: a neuron's average activity plotted against some feature of the world, here the heading; 'tuned' means the curve has a clear peak">tuning curve</span> is the shape; a cell counts as tuned if its curve is "one-bumped" enough, by the rule in the panel below.</p>
 <svg viewBox="0 0 900 220"><g transform="translate(60,20)"><text x="120" y="0" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" font-weight="700" fill="var(--ink)">tuned to north-east</text><polyline points="0,150 20,120 40,80 60,40 80,20 100,30 120,70 140,110 160,140 180,155 200,160 220,158 240,150" fill="none" stroke="var(--blue)" stroke-width="3"/><line x1="0" y1="170" x2="240" y2="170" stroke="var(--line)"/><text x="0" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">E</text><text x="60" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">N</text><text x="120" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">W</text><text x="180" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">S</text><text x="240" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">E</text></g>
 <g transform="translate(520,20)"><text x="120" y="0" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" font-weight="700" fill="var(--ink)">not tuned</text><polyline points="0,100 20,96 40,104 60,99 80,101 100,97 120,103 140,100 160,98 180,102 200,99 220,101 240,100" fill="none" stroke="var(--mute)" stroke-width="3"/><line x1="0" y1="170" x2="240" y2="170" stroke="var(--line)"/><text x="0" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">E</text><text x="60" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">N</text><text x="120" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">W</text><text x="180" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">S</text><text x="240" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">E</text></g></svg>
</div>
<div class="panel">
 <div class="eyebrow">How the tuning curves and the other leaderboard numbers are computed</div>
 <p style="font-size:15px;margin:8px 0 0"><b>Tuning curve.</b> Run the frozen network on eight fresh trips. At every tick while the fly is moving, note its heading and every neuron's activity. Sort the ticks into sixteen heading bins (east, east-north-east, and so on) and average each neuron's activity within each bin. That gives 64 curves of 16 points.</p>
 <p style="font-size:15px"><b>Tuning strength.</b> Treat the 16 points as weights on a circle and find how far the average leans in one direction (the <span class="term" title="resultant: add up 16 arrows, one per heading bin, each as long as that bin's activity; the resultant is the single arrow you get. A curve with one bump gives a long resultant; a flat or two-bumped curve gives a short one">resultant</span>), divided by the total size of the curve. A clean single bump scores high, a flat curve near zero. The cutoff for "compass cell" is 0.25. It is a choice; the count of 32 depends on it.</p>
 <p style="font-size:15px"><b>Write follows speed.</b> The <span class="term" title="correlation: a number from −1 to +1 saying how much two series rise and fall together; +1 is lockstep, 0 is no relation">correlation</span> between the write gate and the fly's speed, tick by tick over the traced trip, ignoring pauses. Run 19: +0.69.</p>
 <p style="font-size:15px;margin-bottom:0"><b>Erase at food versus away.</b> The mean of the erase gate over ticks with the food input on, and over ticks with it off, across the 200 exam trips.</p>
</div>
<div class="panel real">
 <div class="eyebrow">Real data: all 64 tuning curves from run 19, sorted with the strongest first</div>
 <div class="grid16" id="curves"></div>
 <div class="how"><b>How to read it.</b> There is one small chart per neuron. Across the bottom of each chart is the fly's heading, going east, north, west, south and back to east. Up the side is the neuron's average activity at that heading. Teal curves belong to the 32 neurons whose tuning strength passes the 0.25 cutoff, so they count as compass cells. Grey curves belong to the rest. The number in the corner of each chart is that neuron's tuning strength. Notice that the tuned cells are not copies of one another: their peaks fall at different headings. The bar chart below the grid counts how many compass cells prefer each of the sixteen directions. A perfect compass would have its cells spread evenly around the circle. Ours are bunched: six cells prefer north-north-east, six prefer west-south-west, and two of the sixteen direction bins have no cells at all. This bunching is one of the ways our compass is still cruder than the fly's.</div>
 <canvas id="prefHist" width="1700" height="260"></canvas>
</div>

<h3>Motif 2: the write gate reads speed</h3>
<div class="sketch">
 <div class="eyebrow">Drawing: the wiring path that lets a gate follow one input</div>
 <p style="font-size:15px;margin-top:6px">A gate is a sigmoid of a weighted sum of all 64 neurons. For it to follow speed, some neurons must (a) listen to the speed wire strongly through W_in and (b) feed the gate strongly through W_out, with the two signs agreeing. If a neuron has a negative speed weight and a negative gate weight, faster still means more writing: two negatives multiply to a positive. The sketch shows the path; the real chart below checks whether run 19 built it.</p>
 <svg viewBox="0 0 900 150"><rect x="20" y="50" width="120" height="44" rx="8" fill="var(--panel)" stroke="var(--blue)"/><text x="80" y="77" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">speed</text><line x1="140" y1="72" x2="300" y2="72" stroke="var(--amber)" stroke-width="3" marker-end="url(#ar)"/><text x="220" y="60" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">W_in[n, speed]</text><circle cx="340" cy="72" r="30" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="340" y="77" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">neuron n</text><line x1="370" y1="72" x2="560" y2="72" stroke="var(--amber)" stroke-width="3" marker-end="url(#ar)"/><text x="465" y="60" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">W_out[write, n]</text><rect x="565" y="50" width="150" height="44" rx="8" fill="var(--panel)" stroke="var(--amber)" stroke-width="2"/><text x="640" y="77" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">write gate</text><text x="740" y="77" font-family="Literata" font-size="13" fill="var(--mute)">product of the two = effect</text></svg>
</div>
<div class="panel real">
 <div class="eyebrow">Real data: the eight neurons that push each gate hardest, and how strongly each of them listens to the relevant input</div>
 <div class="two"><div><canvas id="writeWiring" width="820" height="420"></canvas></div><div><canvas id="eraseWiring" width="820" height="420"></canvas></div></div>
 <div class="how"><b>How to read it.</b> The left chart is about the write gate. It shows the eight neurons that push the write gate hardest. For each neuron there are two bars and a dot. The pale bar is that neuron's weight from the speed wire (how strongly it listens to speed). The dark bar is its weight into the write gate (how strongly it pushes the gate). The dot is the product of the two bars. A positive product means "when the fly goes faster, this neuron makes the gate write more." Seven of the eight products are positive. The right chart shows the same thing for the erase gate, but with the food wire in place of the speed wire, so a positive product there means "when the fly is at food, this neuron makes the gate erase more." Five of the eight products are positive, and the strongest driver, neuron 40, is strongly positive. These charts show the wiring that produces the numbers on the leaderboard: the correlation between the write gate and speed is +0.69, and the erase gate averages 0.38 at food against 0.008 away from food.</div>
</div>

<h3>Motif 3: the wipe at food, seen in F itself</h3>
<div class="panel real">
 <div class="eyebrow">Real data: the twelve strongest fast weights, followed through the whole two-trip test</div>
 <canvas id="Ftrace" width="1700" height="440"></canvas>
 <div class="how"><b>How to read it.</b> Across the bottom is time in seconds over the full 90-second test, which contains two trips. Up the side is the value of a fast weight, between −1 and +1, with the ±1 lid drawn as dashed coral lines. Each teal line follows one of the twelve strongest fast weights. The grey line is the fly's distance from home. The shaded columns are the periods when the fly stands at food. What to look for: the teal lines build up while the fly wanders out, hold roughly steady on the way home, and then drop sharply inside a shaded column. That drop is the erase gate firing at 0.38 per tick for forty ticks in a row, which clears the board so that the next trip starts fresh. The Night Report's run cards show a drawn version of this same picture, which you can compare with the real one here.</div>
</div>

<h3>What the wiring between neurons looks like, sorted the way Peter sorts it</h3>
<p>Peter's paper (question 10) has a signature analysis: order the compass cells by preferred direction, then plot the connection strength from each to each. In a ring attractor, cells with similar preferred directions excite each other and cells with opposite directions inhibit each other, so the plot shows a bright diagonal and dark far corners. Below is that plot for run 19, for both the slow table W and the allowance table A.</p>
<div class="panel real">
 <div class="eyebrow">Real data: the connections between the 32 compass cells, sorted by preferred direction</div>
 <div class="two"><div><canvas id="Wsorted" width="820" height="820"></canvas></div><div><canvas id="Asorted" width="820" height="820"></canvas></div></div>
 <canvas id="profile" width="1700" height="360"></canvas>
 <div class="how"><b>How to read it.</b> In the two square pictures, each row is a receiving cell and each column is a sending cell. Both rows and columns are in order of preferred direction, starting at east and going round the circle back to east. Red means a positive weight and blue means a negative weight. The chart underneath takes all those weights and averages them according to how far apart the two cells' preferred directions are, from −180° to +180°. If the cells were wired as a ring, this chart would show a positive hump at 0° (cells that like the same direction excite each other) and a negative dip at ±180° (cells that like opposite directions quiet each other); the dashed blue line shows that ideal shape. Run 19's W (the black line) shows only a faint version of it, with the mean weight ranging from −0.04 to +0.05, and A (the teal line) shows none at all. So our compass cells are real in the sense that they have clear tuning curves, but they are not wired together as a ring. They do not need to be. Our fly is handed its heading on the input wires every tick, so the network never has to hold on to a heading by itself, which is what Peter's network had to do. This is the clearest difference between the two projects. It comes from a difference between the two tasks, so it should not be read as a failure of our network.</div>
</div>
<p class="caveat">Honest limits of this analysis. Preferred direction is read from a 16-bin tuning curve, so it is coarse. The sorted plots use 32 cells, which is few; Peter's used 33 ring cells out of 100 but with much sharper tuning. And "no ring" is a statement about the slow weights; the effective connection at any moment is W + A·F, and F changes every tick.</p>

<!-- ============ Q9 ============ -->
<h2 id="q9"><span class="q">QUESTION 9</span>Backpropamine, and how our network compares</h2>
<p><b>Backpropamine</b> is a 2019 paper by Miconi, Rawal, Clune and Stanley. The name is a pun on backpropagation and dopamine. The idea in one sentence: let a network have connections that change while it runs, in a Hebbian way, and let the network itself produce a signal (like dopamine in the brain) that says how much those changes should happen right now; then train everything by ordinary gradient descent. Press the buttons below to step through the family of rules, from a plain network up to ours, and see where our network sits in it.</p>
<div class="panel">
 <div class="eyebrow">Notation used below</div>
 <p style="font-size:15px;margin:8px 0 0"><b>x_old ⊗ x_new</b> is the <span class="term" title="outer product">outer product</span>: a table with one cell per pair of neurons, each cell the product of the sender's activity last tick and the receiver's now. Step 6 of the calculator in question 1 fills exactly this table. <b>clip</b> and <b>clamp</b> both mean "if above +1 make it +1, if below −1 make it −1". <b>σ</b> is the sigmoid from question 3. <b>tanh</b> is its cousin that runs from −1 to +1 instead of 0 to 1. <b>η</b> (eta) is a fixed writing rate; <b>α</b> (alpha) is a per-connection scale, the same thing as our A.</p>
</div>
<div class="panel">
 <div class="row"><button class="btn rule on" data-r="0">plain recurrent network</button><button class="btn rule" data-r="1">differentiable plasticity (2018)</button><button class="btn rule" data-r="2">Backpropamine, simple (2019)</button><button class="btn rule" data-r="3">Backpropamine, retroactive</button><button class="btn rule" data-r="4">FlyNet (ours)</button></div>
 <div id="ruleBox"></div>
</div>
<h3>What they showed</h3>
<p>Three tasks. In a cue-reward task (each episode picks a secret target cue; the network must learn within the episode which of four cues pays off), plastic networks with neuromodulation learned it and both non-plastic and non-modulated plastic networks failed. In a 9-by-9 maze where the reward moves every episode, neuromodulated networks again did best. And on Penn Treebank, a standard text-prediction benchmark, adding neuromodulated plastic connections to an LSTM lowered <span class="term" title="perplexity: a score for how surprised a language model is by real text; lower is better">perplexity</span> from 104.26 to 102.48 for the small model and from 62.48 to 61.44 for the large one, with the number of parameters held fixed.</p>
<h3>Side by side with FlyNet</h3>
<table><thead><tr><th>piece</th><th>Backpropamine</th><th>FlyNet</th></tr></thead><tbody>
<tr><td>fixed weight</td><td>w, trained</td><td>W, trained</td></tr>
<tr><td>plastic part</td><td>Hebb, zero at episode start, clipped to ±1</td><td>F, zero at episode start, clamped to ±1</td></tr>
<tr><td>how much the plastic part counts</td><td>α per connection, trained</td><td>A per connection, trained (the "allowance table")</td></tr>
<tr><td>how fast it writes</td><td>M(t), a network output (replaces the fixed η)</td><td>ws × write(t): a trained constant times a network output</td></tr>
<tr><td>how it forgets</td><td>only the clip; no decay in the simple form</td><td>erase(t), a second network output; this is our addition</td></tr>
<tr><td>what is written</td><td>x_old ⊗ x_new, full Hebb</td><td>same (delta variant tried in runs 15 and 18)</td></tr>
<tr><td>trained by</td><td>backprop through the episode</td><td>same</td></tr>
<tr><td>what the paper set out to show</td><td>neuromodulation helps on RL and language tasks</td><td>does a fly-like circuit emerge, and where does the memory live</td></tr>
</tbody></table>
<p>So FlyNet is "simple Backpropamine plus an erase gate," applied to a navigation task and then taken apart to see how it works. Nothing about our learning rule is new. What is ours is the question we ask (do the three fly motifs appear?), the world the fly lives in, and the analysis of the trained network. Peter's note says the same thing in the words the field uses. His note also places the delta rule and the newer sequence models (Gated DeltaNet, Titans) as the next steps along the same line of ideas.</p>

<!-- ============ Q10 ============ -->
<h2 id="q10"><span class="q">QUESTION 10</span>Peter's paper, and what it teaches us to do next</h2>
<p><i>Emergence of functional and structural properties of the head direction system by optimization of recurrent neural networks</i>, Cueva, Wang, Chin and Wei, ICLR 2020. It is the template for the kind of analysis you are about to do on our runs, so it is worth understanding what they did step by step.</p>
<div class="sketch">
 <div class="eyebrow">Drawing: the task in Peter's paper, and the ring of cells that emerged from training on it</div>
 <svg viewBox="0 0 900 300">
  <g transform="translate(30,30)">
   <text x="0" y="0" font-family="Bricolage Grotesque" font-size="15" font-weight="700" fill="var(--ink)">The task: keep track of heading from turning speed alone</text>
   <rect x="0" y="20" width="150" height="40" rx="8" fill="var(--panel)" stroke="var(--blue)"/><text x="75" y="45" text-anchor="middle" font-family="Bricolage Grotesque" font-size="13" fill="var(--ink)">turning speed</text>
   <rect x="0" y="70" width="150" height="40" rx="8" fill="var(--panel)" stroke="var(--blue)"/><text x="75" y="95" text-anchor="middle" font-family="Bricolage Grotesque" font-size="13" fill="var(--ink)">starting heading</text>
   <line x1="150" y1="65" x2="200" y2="65" stroke="var(--mute)" stroke-width="2" marker-end="url(#ar)"/>
   <rect x="205" y="20" width="150" height="90" rx="12" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="280" y="60" text-anchor="middle" font-family="Bricolage Grotesque" font-size="13" fill="var(--ink)">100 neurons</text><text x="280" y="80" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">no plasticity</text>
   <line x1="355" y1="65" x2="405" y2="65" stroke="var(--mute)" stroke-width="2" marker-end="url(#ar)"/>
   <rect x="410" y="45" width="150" height="40" rx="8" fill="var(--panel)" stroke="var(--ink)"/><text x="485" y="70" text-anchor="middle" font-family="Bricolage Grotesque" font-size="13" fill="var(--ink)">current heading</text>
   <text x="0" y="140" font-family="Literata" font-size="13.5" fill="var(--mute)">No compass input after the first tick. The network must add up every turn it has made, which is what</text>
   <text x="0" y="158" font-family="Literata" font-size="13.5" fill="var(--mute)">the fly's ellipsoid body does. Our fly gets its heading handed to it every tick; theirs has to remember it.</text>
  </g>
  <g transform="translate(620,30)">
   <text x="0" y="0" font-family="Bricolage Grotesque" font-size="15" font-weight="700" fill="var(--ink)">What emerged: a ring</text>
   <circle cx="120" cy="110" r="70" fill="none" stroke="var(--line)" stroke-width="10"/>
   <g id="ring"></g>
   <text x="120" y="215" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">compass cells around a ring, a bump of</text><text x="120" y="232" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">activity at the heading, shifter cells that</text><text x="120" y="249" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">push it left or right when the animal turns</text>
  </g>
 </svg>
</div>
<h3>Their five analyses, and our status on each</h3>
<div class="map">
 <div><b>1. Tuning to two things at once</b>They plotted each neuron's activity against heading <em>and</em> turning speed together (a heat map with heading across and turning speed up). Two classes fell out: compass cells (tuned to heading only) and shifters (tuned to both, split into clockwise and counter-clockwise). <span class="status part">ours: partly</span> We plotted tuning to heading only. The natural second axis for us is speed, or "at food or not", to see if there are separate "counting" and "wiping" classes.</div>
 <div><b>2. Preferred directions tile the circle</b>Within each class, preferred headings were spread evenly. <span class="status part">ours: partly</span> Run 19's 32 compass cells cluster (question 8); the fly-like even tiling is not there.</div>
 <div><b>3. Connectivity sorted by preferred direction</b>Local excitation and long-range inhibition among compass cells; shifters excite compass cells slightly ahead of themselves in their turning direction, which is how the bump moves. This matched known fly wiring between the protocerebral bridge and the ellipsoid body and predicted a lagging inhibition not yet seen in the fly. <span class="status done">ours: done above</span> No ring in our slow weights, for a reason we understand.</div>
 <div><b>4. Lesions</b>They cut classes of connections mid-trial. Cutting compass-cell outputs destroyed the bump and the heading estimate; when restored, the bump re-formed by itself. Cutting clockwise shifters made the bump drift counter-clockwise even at rest, showing the two shifter groups push against each other constantly. Cutting both shifter groups left a stable bump that could no longer turn. <span class="status todo">ours: not yet</span> Our only lesion is F to zero. The obvious next ones: silence the 32 compass cells; silence the 8 erase drivers; silence the 8 write drivers. Each is a one-line change to the test.</div>
 <div><b>5. Change the input statistics</b>Train with slow turning and you get more compass cells; train with fast turning and you get more shifters. The circuit adapts its mix to the world. <span class="status done">ours: done, by accident of design</span> The "legs" world (runs 13, 19) is exactly this move: change the speed statistics, see what the network reallocates. It made the write gate lean harder on speed and improved the score on the ordinary world.</div>
 <div><b>The method behind all five</b>Train an unconstrained network on the animal's task, then treat it like a specimen: record from every unit, sort by what they prefer, look at the wiring in that order, cut things and watch. Everything in the Night Report follows this recipe, which is why the "look inside" panels exist at all.</div>
</div>
<p>One more parallel is worth saying out loud. Their claim was not "this network is the fly." Their claim was that the fly's design is what optimisation arrives at when the task is this task, and therefore that you can predict anatomy from function. Our version of that claim is smaller, and it carries the caveats listed in question 2. It is this: given a homing task with a place to reset, gradient descent will build a compass, a speed-weighted tally and a wipe at food, provided that the gate which does the wiping is resting where training can move it.</p>
<p class="caveat">Two reading notes on the paper text you sent. The arXiv version has a draft paragraph left in ("Now mention something about the P-EN2 neurons here"), which is a nice reminder that papers are written by people. And the numbers in its figure titles (33 ring, 29 and 26 shifters, error 0.57%) are from one trained network; they trained many and report the pattern was consistent.</p>

<!-- ============ Q11 ============ -->
<h2 id="q11"><span class="q">QUESTION 11</span>Follow-ups on the Counter With a Lid page</h2>
<h3>Are we only tallying on the way out?</h3>
<p>No. The rule runs on every tick of every trip, on the way out and on the way back, and there is no switch that turns it off. That is what a home vector is: walking away from home adds to it, walking towards home subtracts from it, and it reads zero when you are back. Whether the network actually does the subtracting on the way back is a question the data can answer, so here is the same run 19 trip as before, with the average size of the twelve traced fast weights written down at a few moments.</p>
<div class="panel real">
 <div class="eyebrow">Real data: one exam trip from run 19, showing the tally rising on the way out and falling on the way back</div>
 <table><thead><tr><th class="n">time</th><th class="n">distance from home</th><th class="n">mean |F| of the twelve</th><th>what the fly is doing</th></tr></thead><tbody>
 <tr><td class="n">0 s</td><td class="n">0.00</td><td class="n">0.00</td><td>standing at food, board wiped (erase 0.77)</td></tr>
 <tr><td class="n">10 s</td><td class="n">3.88</td><td class="n">0.41</td><td>wandering out</td></tr>
 <tr><td class="n">16 s</td><td class="n">8.50</td><td class="n">0.68</td><td>the far point, turns for home</td></tr>
 <tr><td class="n">25 s</td><td class="n">6.20</td><td class="n">0.47</td><td>walking home: the tally is being counted down</td></tr>
 <tr><td class="n">35 s</td><td class="n">4.26</td><td class="n">0.30</td><td>still walking home, tally still shrinking</td></tr>
 <tr><td class="n">50 s</td><td class="n">2.80</td><td class="n">0.46</td><td>searching near home; tally grows again as it circles</td></tr>
 </tbody></table>
 <div class="how"><b>How to read it.</b> The first column is time in seconds, the second is the fly's distance from home, and the third is the average size (ignoring sign) of the twelve traced fast weights at that moment. On the way out, the size of the fast weights climbs as the distance climbs. On the way back, it falls as the fly gets closer to home. It does not fall all the way to zero, because on this trip the fly never quite reached home: its closest approach was a distance of 1.5, and after that it circled, and every circle adds a little back into the tally. So the table confirms two-way counting on a real trace, with the return leg less clean than the outbound leg. That is the same conclusion the stress test reached by a different route.</div>
</div>
<h3>How do we know the count is in the fast weights? Isn't that what the experiment is for?</h3>
<p>Yes, exactly, and it is worth separating two claims. The first, <b>"the memory that homes lives in F"</b>, is what the F-held-at-zero test establishes: the same weights, F forced to zero, and the fly walks at random. There is also a structural reason: the neurons' activity is wiped to zero at the start of every trip, so inside an episode nothing except F can carry information across a trip boundary. That claim is solid.</p>
<p>The second, <b>"F holds a running distance count"</b>, is a hypothesis about <em>what</em> F stores, and it is only partly tested. The evidence for it is circumstantial: the write gate follows speed (+0.69), the network has compass cells, the size of F rises and falls with distance as in the table above, and the hand-built vector tally is the simplest thing that fits. What we have not done is read the count out of F directly: take the 4,096 numbers at each tick and fit a straight-line readout to the true home vector. If that fit is good, the tally is in there in a form we can point to. If it is poor, the network homes some other way and the "counter with a lid" story is only an analogy. That decoding test is a one-afternoon job and it is the first thing I would add to the level 4 list.</p>
<h3>How can the lid be 5 or 50 if every fast weight is between −1 and +1?</h3>
<p>It cannot, and I muddled two different scales on that page. In the network, every one of the 4,096 fast weights is clamped to lie between −1 and +1, with no exceptions. The "lid" slider on the drawn page was in counts of a toy counter, and 25 was an arbitrary number chosen so the shape was visible. It was not a weight value. The mapping is: the toy's lid ↔ the ±1 clamp; the toy's "count per second" ↔ how much a weight moves per tick, which is ws × write × the product of two activities (run 19: 0.074 × about 0.4 × something under 1, so a few hundredths per tick).</p>
<p>Two more things clear the rest of the confusion up. First, a fast weight is <em>not</em> squashed after the clamp. It enters the effective connection W + A·F as it is, and it is the receiving neuron's total input that gets squashed by tanh. So raising the clamp really does give the count more room. But A can scale F up or down, and if A·F gets large the neuron saturates instead, which is the risk of raising the lid that the page mentioned. Second, the tally is not one weight. It is spread across many weights, each holding a piece. Total room = the clamp × how many weights are used × how A weights them. That is why "more neurons" and "spread the count" are on the same list as "raise the lid": they are three ways to make the same room bigger.</p>
<h3>How does counting in smaller steps help, and how does training on longer trips help?</h3>
<p><b>Smaller steps.</b> The clamp is fixed at 1. If a weight moves by 0.05 per tick of walking in one direction, it hits the clamp after 20 ticks, two seconds. If it moves by 0.005 per tick, it lasts 200 ticks, twenty seconds. Smaller steps do not add room; they make the existing room last longer. The price is a fainter count: the readout through A has to be more sensitive, so noise and the small always-on erase matter more. That trade-off is what training would have to find, and a penalty on the size of F is one way to tilt it toward smaller steps. It is a hypothesis, not a known fix.</p>
<p><b>Longer trips in training.</b> This one does not change the network's capacity at all. It changes what the network is punished for. Gradient descent only fixes what costs loss. Today the network is never scored on a trip longer than 30 seconds, so a counter that overflows at 40 seconds costs nothing and nothing pushes it to change. Train at 45 seconds and the overflow starts to cost, and the optimiser is pushed toward whichever of the fixes above it can reach: smaller steps, more weights sharing the count, less leak. It is the same move as the "legs" world in runs 13 and 19, and the same move as Peter's slow-turning and fast-turning conditions: change the statistics of the world and the network reallocates. Whether it can reallocate enough is the experiment.</p>
</main></div>
<script>
const D=__DATA__;
const css=n=>getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const $=id=>document.getElementById(id);
const ctx=id=>{const c=$(id);const x=c.getContext('2d');x.setTransform(2,0,0,2,0,0);return [x,c.width/2,c.height/2]};
const txt=(x,s,px,py,col,al='left',f='12px "JetBrains Mono"')=>{x.fillStyle=col;x.font=f;x.textAlign=al;x.fillText(s,px,py);};
const frame=(x,W,H,p)=>{x.strokeStyle=css('--line');x.lineWidth=1;x.beginPath();x.moveTo(p.l,p.t);x.lineTo(p.l,H-p.b);x.lineTo(W-p.r,H-p.b);x.stroke();};
const sig=z=>1/(1+Math.exp(-z));
// ---- Q1 machine
const EXPL={in0:'<b>Compass, east-west part.</b> The fly has a compass sense. We hand the network its heading as two numbers, the cosine and sine of the angle, because an angle on its own has a nasty jump at north (359° and 1° are neighbours but the numbers are far apart). Cosine is the east-west part: +1 facing east, −1 facing west. Noise is added so it is a slightly untrustworthy compass.',
in1:'<b>Compass, north-south part.</b> The sine of the heading: +1 facing north, −1 facing south. Together the two parts point exactly where the fly faces.',
in2:'<b>Speed.</b> How fast the fly is moving this tick, from 0 (a pause) to about 1.4 in the fast half of the legs world. A tally of distance has to multiply direction by speed, so the network needs this wire.',
in3:'<b>At food?</b> A 1 while the fly stands at the food, 0 everywhere else. This is the only signal that says "a trip is ending", so it is the only thing a reset can be keyed to.',
win:'<b>W_in, 4 × 64 weights plus 64 biases.</b> Each of the four input wires connects to every one of the 64 neurons, and each of those connections has its own strength. These strengths are trained and then frozen, so they count as part of the slow weights.',
net:'<b>The 64 neurons.</b> Every tick each neuron adds up its inputs (the four wires through W_in, and all 64 neurons a tick ago through the effective connections W + A·F), then squashes the sum with tanh so it lies between −1 and +1. Activity is wiped to zero at the start of every trip, so nothing can be carried between trips in the neurons themselves.',
W:'<b>W, the slow table, 64 × 64.</b> The permanent strength of every connection from neuron j to neuron i. It is trained by gradient descent across thousands of episodes and then frozen. Because it never changes during a trip, it holds the network\'s long-term habits: the parts of its behaviour that are the same on every trip.',
A:'<b>A, the allowance table, 64 × 64.</b> How much each connection is allowed to be changed by the fast table. Effective strength = W + A·F. If A is zero on a connection, that connection can never learn during a trip. Trained, then frozen. Set to zero and frozen for the rival (run 20).',
F:'<b>F, the fast table, 64 × 64.</b> Starts at zero every episode. Rewritten every tick by the rule, with the write and erase gates deciding how much. Never trained directly; the network learns a rule for changing it. This is where the memory of the trip lives, and it is the only thing that survives from one trip to the next inside an episode.',
ws:'<b>ws, the write strength.</b> A single trained number that multiplies every write into F. In level 1 this was a dial you could turn by hand; here training sets it. Run 19 settled it at 0.074.',
wout:'<b>W_out, 64 × 3 weights plus 3 biases.</b> Reads all 64 neurons into the three outputs. The three biases are the outputs\' resting positions: run 19 has turn −0.14, write +0.96, erase +1.86.',
out0:'<b>Turn.</b> How much to rotate this tick, left or right, capped smoothly at 8 radians per second. It is the only output that moves the fly.',
out1:'<b>Write gate.</b> A number between 0 and 1, produced by a sigmoid. It multiplies the amount written into F this tick. If the gate opens more when the fly moves faster, then fast steps are recorded more strongly than slow ones, and the tally counts distance walked rather than time spent.',
out2:'<b>Erase gate.</b> A number between 0 and 1, produced by a sigmoid. It is the fraction of every cell of F that is removed this tick. If it stays near 0.01 everywhere, the memory slowly fades. If it is near 1 at food and near 0 everywhere else, it acts as the fly\'s reset: the board is wiped at food and kept intact the rest of the time.'};
document.querySelectorAll('#machine .node').forEach(g=>{g.style.cursor='pointer';g.addEventListener('click',()=>{$('machineDetail').innerHTML=EXPL[g.dataset.k];document.querySelectorAll('#machine .node rect').forEach(r=>r.style.filter='');const r=g.querySelector('rect');if(r)r.style.filter='drop-shadow(0 0 6px var(--blue))';});});
(function(){const g=$('dots');let s='';for(let i=0;i<64;i++){const r=75+((i*37)%29)-14,a=i/64*6.283;const cx=450+Math.cos(a)*r,cy=140+Math.sin(a)*r*0.6;s+=`<circle cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="4" fill="var(--teal)" opacity=".7"/>`;}g.innerHTML=s;})();
(function(){const [x,W,H]=ctx('winBars');x.clearRect(0,0,W,H);const Win=D.motif.Win;const names=['compass east-west','compass north-south','speed','at food'];const m=[0,1,2,3].map(k=>Win.reduce((a,r)=>a+Math.abs(r[k]),0)/64);
 const p={l:30,r:30,t:36,b:40};const bw=(W/2-p.l-p.r)/4-20;txt(x,'mean |weight| from each input wire (W_in)',p.l,22,css('--mute'));const mx=0.4;
 m.forEach((v,k)=>{const bx=p.l+k*(bw+20),bh=v/mx*(H-p.t-p.b);x.fillStyle=css('--blue');x.fillRect(bx,H-p.b-bh,bw,bh);txt(x,v.toFixed(3),bx+bw/2,H-p.b-bh-6,css('--ink'),'center','13px "Bricolage Grotesque"');txt(x,names[k],bx+bw/2,H-p.b+16,css('--mute'),'center','11px "JetBrains Mono"');});
 const b=D.motif.bout;const L=W/2+40;txt(x,'output biases (resting position of each output, W_out.bias)',L,22,css('--mute'));const mid=(H-p.b+p.t)/2;const sc=(H-p.t-p.b)/2/6;
 [['turn',b[0],css('--ink')],['write',b[1],css('--amber')],['erase',b[2],css('--coral')]].forEach(([n,v,c],k)=>{const bx=L+k*(bw+20);x.strokeStyle=css('--line');x.beginPath();x.moveTo(bx,mid);x.lineTo(bx+bw,mid);x.stroke();x.fillStyle=c;x.fillRect(bx,v>0?mid-v*sc:mid,bw,Math.abs(v)*sc);txt(x,(v>0?'+':'')+v.toFixed(2),bx+bw/2,v>0?mid-v*sc-6:mid+Math.abs(v)*sc+14,css('--ink'),'center','13px "Bricolage Grotesque"');txt(x,n,bx+bw/2,H-p.b+16,css('--mute'),'center','11px "JetBrains Mono"');});
 txt(x,'erase started at −5',L+2*(bw+20)+bw/2,H-p.b+30,css('--coral'),'center','11px "JetBrains Mono"');})();
// ---- knob board
const KNOBS=[
 ['World the fly lives in',[
  ['food stand','--food_stand','How long the fly must stand at the food before the trip ends: 0.5 s at first, 2 s from run 3, 4 s from run 8B. More ticks at food means more chances for the erase gate to be taught.','runs 3, 8B'],
  ['trips per episode','--trips','How many wander-and-return trips share one fast table before it is wiped. Two throughout except run 4 (five). More trips make a dirty board hurt more.','run 4'],
  ['speed profile','--speed_profile','How the fly\'s speed varies during a wander. "drift" is gentle random change; "legs" is a slow half then a fast half, so time and distance disagree on purpose.','runs 13, 19'],
  ['wander length (stage)','--stages','How long the fly wanders before turning for home: 10, 20 or 30 s. The curriculum climbs these; a run can also be pinned at one.','every run'],
 ]],
 ['How training is run',[
  ['erase penalty','--erase_penalty','A cost added to the loss for erasing away from food. 0.05 baseline; 0.5 (runs 2, 5) did nothing because it was tiny next to a loss of about 2; 20 (from run 7) is a real cost.','runs 2, 5, 7, 9, 9B'],
  ['learning rate','--lr','The size of every step gradient descent takes. 1e-3 for cold starts, 3e-4 for warm starts after run 6 collapsed, 1e-4 for the polish. Changed as hygiene, not as a hypothesis.','runs 6B, 7, 17 (hygiene)'],
  ['learning-rate decay','--lr_decay','Whether the step size shrinks along a cosine curve during the run. On from run 6. Hygiene.','run 6 on (hygiene)'],
  ['iterations and stage cap','--iters, --stage_cap','How many training steps in total and how many a stage may take before promotion is forced.','every run'],
  ['batch','--batch','How many flies train at once, 32 throughout. More flies smooth the gradient; never changed.','never'],
  ['seed','--seed','The random number that sets the starting weights and the world\'s dice. 0 for almost everything; 1 for the replication.','runs 11, 11B'],
  ['warm start','--init','Which earlier checkpoint to start from, instead of random weights. Half the runs are warm starts; it is what makes the family tree.','runs 4 onward'],
 ]],
 ['Where the network starts, and its shape',[
  ['erase-bias shift','--erase_bias_shift','Add a number to the erase gate\'s bias before training resumes. +2.5 in run 7B, then +1.5 in runs 10, 12, 14, 16, and −2.5 from the start in 9 and 9B. See question 2.','runs 7B, 9, 9B, 10, 12, 14, 16'],
  ['learning rule','--rule','Hebb (write the whole pattern) or delta (write the surprise). See question 4.','runs 15, 18'],
  ['fast weights on','--use_fast','Whether A exists at all. Off for the rival, run 20.','run 20'],
  ['tally ceiling','--f_max','The lid on every fast weight, ±1 throughout. The knob option 4 would turn first.','never'],
  ['neurons','--neurons','64 throughout.','never'],
 ]],
 ['Held fixed on purpose (the exam must not move)',[
  ['heading noise','fixed','The compass jitter. Same for every run so scores compare.','never'],
  ['arrival radius','fixed','How close counts as home. Same for every run.','never'],
  ['loss','fixed','Mean distance from home over the last 10 s of each return, plus the erase penalty. Never changed.','never'],
  ['steering','fixed','How turn output moves the fly, capped at 8 rad/s.','never'],
  ['test seed and exam world','fixed','Seed 4242, 200 trips, the standard world. Every score on the leaderboard is this exam.','never'],
 ]]];
(function(){const b=$('knobBoard');KNOBS.forEach(([g,items])=>{const d=document.createElement('div');d.className='group';d.innerHTML=`<h4>${g}</h4>`;const k=document.createElement('div');k.className='knobs';items.forEach(([n,f,e,t])=>{const el=document.createElement('div');el.className='knob';el.tabIndex=0;el.innerHTML=`<b>${n}</b><span class="flag">${f}</span><span class="turned">turned in: ${t}</span>`;const go=()=>{document.querySelectorAll('.knob').forEach(q=>q.classList.remove('on'));el.classList.add('on');$('knobDetail').innerHTML=`<b>${n}</b> · <span class="flag" style="font-family:'JetBrains Mono';font-size:12px;color:var(--mute)">${f}</span><br>${e}`;};el.addEventListener('click',go);el.addEventListener('keydown',ev=>{if(ev.key==='Enter'||ev.key===' '){ev.preventDefault();go();}});k.appendChild(el);});d.appendChild(k);b.appendChild(d);});})();
// ---- Q3 sigmoid
function drawSig(){const b=+$('B').value,g=+$('G').value;$('oB').textContent=(b>0?'+':'')+b.toFixed(1);$('oG').textContent=g.toFixed(1);const [x,W,H]=ctx('sig');x.clearRect(0,0,W,H);const p={l:44,r:30,t:24,b:40};const cw=W-p.l-p.r,ch=H-p.t-p.b;const X=z=>p.l+(z+8)/16*cw,Y=v=>H-p.b-v*ch;frame(x,W,H,p);
 [-8,-4,0,4,8].forEach(z=>txt(x,z,X(z),H-p.b+16,css('--mute'),'center'));[0,0.5,1].forEach(v=>txt(x,v,p.l-6,Y(v)+4,css('--mute'),'right'));txt(x,'raw input z →',W-p.r,H-6,css('--mute'),'right');txt(x,'gate output',p.l+4,p.t-6,css('--mute'));
 x.strokeStyle=css('--ink');x.lineWidth=3;x.beginPath();for(let z=-8;z<=8;z+=0.05){const px=X(z),py=Y(sig(z));z===-8?x.moveTo(px,py):x.lineTo(px,py);}x.stroke();
 const s=sig(b),sl=s*(1-s);x.fillStyle=css('--coral');x.beginPath();x.arc(X(b),Y(s),8,0,7);x.fill();
 const dz=g;x.strokeStyle=css('--blue');x.lineWidth=4;x.beginPath();x.moveTo(X(b),Y(s));x.lineTo(X(b+dz),Y(sig(b+dz)));x.stroke();x.strokeStyle=css('--blue');x.setLineDash([4,4]);x.lineWidth=1.5;x.beginPath();x.moveTo(X(b+dz),Y(sig(b+dz)));x.lineTo(X(b+dz),Y(s));x.moveTo(X(b),Y(s));x.lineTo(X(b+dz),Y(s));x.stroke();x.setLineDash([]);
 const dy=sig(b+dz)-s;txt(x,`rests at ${s.toFixed(3)} open · slope ${sl.toFixed(3)}`,X(b)+14,Y(s)-14,css('--coral'),'left','13px "Bricolage Grotesque"');txt(x,`a nudge of ${g.toFixed(1)} moves the gate by ${dy.toFixed(3)}`,X(b)+14,Y(s)+22,css('--blue'),'left','13px "Bricolage Grotesque"');
 x.fillStyle=css('--coral');x.globalAlpha=.08;x.fillRect(X(-8),p.t,X(-3.5)-X(-8),ch);x.globalAlpha=1;txt(x,'deaf zone: slope under 0.03',X(-7.8),p.t+16,css('--coral'));}
['B','G'].forEach(id=>$(id).addEventListener('input',drawSig));document.querySelectorAll('button[data-b]').forEach(b=>b.addEventListener('click',()=>{$('B').value=b.dataset.b;drawSig();}));
// ---- Q3 erase per run
const ORDER=D.runs.map(r=>r.run);
function pick(r){const t=r.tests;return t['test_final_30.json']||t['test_final_20.json']||Object.values(t)[0]||null;}
(function(){const [x,W,H]=ctx('eraseRuns');x.clearRect(0,0,W,H);const p={l:44,r:20,t:30,b:50};const cw=W-p.l-p.r,ch=H-p.t-p.b;const rows=D.runs.filter(r=>pick(r));const n=rows.length,bw=cw/n;const lo=1e-4;const Y=v=>H-p.b-(Math.log10(Math.max(lo,v))+4)/4*ch;frame(x,W,H,p);
 [1,0.1,0.01,0.001,0.0001].forEach(v=>{txt(x,v,p.l-6,Y(v)+4,css('--mute'),'right');x.strokeStyle=css('--line');x.setLineDash([2,4]);x.beginPath();x.moveTo(p.l,Y(v));x.lineTo(W-p.r,Y(v));x.stroke();x.setLineDash([]);});txt(x,'erase per tick (log scale)',p.l+4,p.t-8,css('--mute'));
 rows.forEach((r,i)=>{const m=pick(r);const bx=p.l+i*bw+4;const w=(bw-8)/2;x.fillStyle=css('--coral');x.fillRect(bx,Y(m.ef),w,H-p.b-Y(m.ef));x.fillStyle=css('--rand');x.fillRect(bx+w,Y(m.en),w,H-p.b-Y(m.en));x.save();x.translate(bx+bw/2-4,H-p.b+8);x.rotate(Math.PI/2);txt(x,r.run.replace('run',''),0,0,css('--mute'),'left','11px "JetBrains Mono"');x.restore();});
 txt(x,'coral: at food · grey: away',W-p.r,p.t-8,css('--mute'),'right');})();
// ---- Q4 delta toy
function drawDelta(){const N=+$('N').value,S=+$('S').value;$('oN').textContent=N;$('oS').textContent=S.toFixed(2);const [x,W,H]=ctx('delta');x.clearRect(0,0,W,H);const p={l:44,r:20,t:24,b:36};const cw=W-p.l-p.r,ch=H-p.t-p.b;
 let fh=0,fd=0;const hh=[],dd=[];const xo=0.8,xn=0.8;for(let t=0;t<=N;t++){hh.push(fh);dd.push(fd);fh=Math.min(1,fh+S*xn*xo);const pred=fd*xo;fd=fd+S*(xn-pred)*xo;}
 const X=t=>p.l+t/N*cw,Y=v=>H-p.b-v/1.1*ch;frame(x,W,H,p);[0,0.5,1].forEach(v=>txt(x,v,p.l-6,Y(v)+4,css('--mute'),'right'));txt(x,'ticks →',W-p.r,H-6,css('--mute'),'right');txt(x,'one connection strength',p.l+4,p.t-6,css('--mute'));
 x.setLineDash([6,5]);x.strokeStyle=css('--coral');x.lineWidth=2;x.beginPath();x.moveTo(p.l,Y(1));x.lineTo(W-p.r,Y(1));x.stroke();x.setLineDash([]);
 x.strokeStyle=css('--teal');x.lineWidth=3;x.beginPath();hh.forEach((v,i)=>i?x.lineTo(X(i),Y(v)):x.moveTo(X(i),Y(v)));x.stroke();
 x.strokeStyle=css('--blue');x.lineWidth=3;x.beginPath();dd.forEach((v,i)=>i?x.lineTo(X(i),Y(v)):x.moveTo(X(i),Y(v)));x.stroke();
 txt(x,`Hebb after ${N} ticks: ${hh[N].toFixed(2)}`,X(N)-6,Y(hh[N])-10,css('--teal'),'right','13px "Bricolage Grotesque"');txt(x,`delta after ${N} ticks: ${dd[N].toFixed(2)} (settles at ${(xn/xo).toFixed(2)})`,X(N)-6,Y(dd[N])+20,css('--blue'),'right','13px "Bricolage Grotesque"');}
['N','S'].forEach(id=>$(id).addEventListener('input',drawDelta));
// ---- Q6 reset map
function drawReset(){const T1=+$('T1').value,T2=+$('T2').value;$('oT1').textContent=T1.toFixed(2);$('oT2').textContent=T2;const [x,W,H]=ctx('resetMap');x.clearRect(0,0,W,H);const p={l:54,r:30,t:30,b:50};const cw=W-p.l-p.r,ch=H-p.t-p.b;const lo=-4.2,hi=0.1;const X=v=>p.l+(Math.log10(Math.max(1e-4,v))-lo)/(hi-lo)*cw,Y=v=>H-p.b-(Math.log10(Math.max(1e-4,v))-lo)/(hi-lo)*ch;frame(x,W,H,p);
 [1,0.1,0.01,0.001,0.0001].forEach(v=>{txt(x,v,p.l-6,Y(v)+4,css('--mute'),'right');txt(x,v,X(v),H-p.b+16,css('--mute'),'center');});txt(x,'erase away from food →',W-p.r,H-6,css('--mute'),'right');txt(x,'erase at food',p.l+4,p.t-8,css('--mute'));
 // reset region: ef>T1 and ef>T2*en  => en < ef/T2
 x.fillStyle=css('--green');x.globalAlpha=.1;x.beginPath();x.moveTo(X(1e-4),Y(T1));x.lineTo(X(T1/T2),Y(T1));x.lineTo(X(1/T2),Y(1));x.lineTo(X(1e-4),Y(1));x.closePath();x.fill();x.globalAlpha=1;txt(x,'reset region',X(2e-4),Y(0.8),css('--green'),'left','13px "Bricolage Grotesque"');
 x.strokeStyle=css('--mute');x.setLineDash([4,4]);x.beginPath();x.moveTo(X(1e-4),Y(1e-4));x.lineTo(X(1),Y(1));x.stroke();x.setLineDash([]);txt(x,'equal at food and away',X(0.2),Y(0.2)+16,css('--mute'),'center');
 x.strokeStyle=css('--line');x.beginPath();x.moveTo(p.l,Y(0.003));x.lineTo(W-p.r,Y(0.003));x.stroke();
 D.runs.forEach(r=>{const m=pick(r);if(!m)return;const ef=Math.max(1e-4,m.ef),en=Math.max(1e-4,m.en);const isR=ef>T1&&ef>T2*en;const col=isR?css('--green'):en>0.003?css('--amber'):css('--coral');x.fillStyle=col;x.beginPath();x.arc(X(en),Y(ef),6,0,7);x.fill();txt(x,r.run.replace('run',''),X(en)+8,Y(ef)+4,col,'left','11px "JetBrains Mono"');});
 txt(x,'green: reset · amber: fade · coral: never erases',W-p.r,p.t-8,css('--mute'),'right');}
['T1','T2'].forEach(id=>$(id).addEventListener('input',drawReset));
// ---- Q7 stepper
const WHY={run1:'The plan\'s first run. There was nothing to look at yet, so no knob was turned. The purpose was to establish a baseline and see what gradient descent does when left on its own.',
run2:'Run 1 produced a slow fade instead of a reset. The simplest thing we can change that bears on erasing is the penalty charged for erasing away from food. So this run multiplies that penalty by ten.',
run3:'Run 2 showed that a penalty can shut the gate completely rather than teach it when to fire. The other way to teach a reset is to give the network more evidence: more ticks spent at the food. So this run has the fly stand at food for 2 seconds instead of 0.5 seconds.',
run4:'Run 3 learned to home on 20-second trips but its memory still faded rather than reset. If the board has to carry five trips in a row instead of two, then leftovers from an old trip do more damage, and the erase gate has a stronger reason to fire at food. This run is a warm start from run 3\'s best weights.',
run5:'Run 2\'s penalty had been tried from a cold start and the network died. This run tries the same penalty from a warm start, on a network that already knows how to home, so that the penalty cannot kill the memory before the memory has formed.',
run6:'Two runs aimed at the erase gate had done nothing. So this run stops working on the gate and instead trains properly at the 30-second stage, because until now 30-second scores were being reported for networks that had never trained on 30-second trips. It also adds a piece of good practice after run 5\'s collapse: cosine decay, which means the learning rate is gradually lowered over the run so that late steps are small.',
run6B:'Run 6 collapsed at iteration 500 even with the decay in place. This run repeats the same experiment with a step size (learning rate) one third as large.',
run7:'A penalty of 0.5 is tiny next to a loss of about 2, so it was never going to matter. This run makes the penalty large enough to matter: 20. The reasoning was that if the gate still does not move under a penalty of 20, the problem is not that the penalty is too small; something else is stopping the gate from moving.',
run7B:'Run 7 gave the diagnosis: with the gate parked at −5 on its sigmoid curve, the slope there is 0.007, so training can barely move it. This run tests that diagnosis directly by lifting the bias by 2.5 and keeping everything else the same, including the penalty.',
run8:'Run 7B made the gate erase three times as much at food as away from it (a ratio of 3). Before pushing harder, this run checks whether simply training for longer sharpens that preference on its own. Nothing is changed; training just continues.',
run8B:'Run 8 stalled at a ratio between 1.5 and 3. Now that the gate is in a position where training can move it, this run retries the idea from run 3: more ticks at food (4 seconds) should give training more evidence in favour of erasing at food.',
run9:'Every shifted run so far had been a warm start. This run is the decisive version of the test: a cold start (random weights) whose gate is placed where training can move it from the very first iteration. The question is whether the reset emerges on its own when the gate can be trained from the beginning.',
run9B:'In run 9, the penalty of 20 shut the gate before any memory had formed. This run cuts the penalty to 2, so that the gate stays in a trainable position while the tally is still forming.',
run10:'The first shift lifted the food-to-away ratio to 3, and then training settled there. This run makes the same move again (a further +1.5 on the bias) to find out whether the preference climbs another step or falls back to 3.',
run11:'Every finding so far comes from a single random seed, seed 0. This run repeats run 3\'s recipe from a different random starting point, to see whether the compass cells and the speed-following write gate appear again or were luck.',
run11B:'The automatic stop rule ended run 11 just as it was being promoted to a longer trip length, which was unfair to it. This run continues run 11 with the stop rule switched off.',
run12:'The ratio went from 3 to 7 after the second shift. This run makes a third shift to test whether each shift keeps adding to the preference.',
run13:'A different kind of change altogether: a world in which time and distance disagree, because the fly walks slowly for one half of the trip and fast for the other half. In such a world, the only way to home is to make the write gate follow speed, so the prediction is that the write gate\'s link to speed should sharpen.',
run14:'The ratio has gone 3, 7, 20. This run makes a fourth shift and asks whether the gate reaches a full wipe at food.',
run15:'Peter\'s note proposed the delta rule. This run is a cold start using run 3\'s recipe with only the learning rule changed. Peter\'s prediction was written down before the run.',
run16:'The ratio has gone 3, 7, 20, 33, and the gate now peaks near 0.9 at food. This run makes a fifth shift and asks whether the wipe becomes complete.',
run17:'The best-scoring line of runs (run 13) had only ever been trained with a learning rate of 3e-4, that is, 0.0003. This run continues it at one tenth of that rate, with nothing else changed, to polish the result with smaller steps.',
run18:'Run 15 failed from a cold start. The fair second form of the test is to switch the rule on a network that already has a working tally (run 14), so that the rule is the only thing that differs.',
run19:'Two separate lines of runs existed: the one with the best score (the legs world, run 13) and the one with the best reset (run 14). This run applies the legs world to the best-reset network, to see whether the two improvements can be combined.',
run20:'This is the comparison the whole plan was built for, and it belongs to level 4: the same network with the fast weights switched off, trained with run 3\'s recipe.'};
const VERD={run1:'baseline',run2:'failed',run3:'partly',run4:'failed',run5:'failed',run6:'partly',run6B:'met',run7:'failed (and diagnosed)',run7B:'partly',run8:'failed',run8B:'failed',run9:'failed',run9B:'failed',run10:'met',run11:'partly',run11B:'partly',run12:'met',run13:'partly',run14:'partly',run15:'failed (negative result)',run16:'met',run17:'met',run18:'failed (negative result)',run19:'met',run20:'one-sided'};
let cur='run19';
function parentOf(r){const p=(D.runs.find(q=>q.run===r)||{}).parent||'';const m=/run(\d+B?)/.exec(p);return m?'run'+m[1]:null;}
function drawStep(){const R=D.runs.find(q=>q.run===cur);document.querySelectorAll('#steps button').forEach(b=>b.classList.toggle('on',b.dataset.r===cur));
 const tests=Object.values(R.tests);const t30=R.tests['test_final_30.json'],t20=R.tests['test_final_20.json']||tests[0];const v=VERD[cur]||'';const pill=v.startsWith('met')?'ok':v.startsWith('partly')?'part':v.startsWith('failed')?'bad':'';
 const scoreLine=(t30?`30 s: ${t30.A} with F, ${t30.B} without · `:'')+(t20?`${t20.t} s: ${t20.A} with F, ${t20.B} without`:'')+(R.minutes?` · ${R.minutes} min`:'');
 $('runCard').innerHTML=`<div class="box"><h4>the situation and the knob</h4><p style="margin:0 0 8px"><b>${R.run}</b> · ${R.knob||''}</p><p style="margin:0;color:var(--mute)">from: ${R.parent||'random start'}</p><p style="margin-top:10px">${WHY[cur]||''}</p></div>
 <div class="box"><h4>prediction, written before the run</h4><p style="margin:0">${R.pred||'(runs 1 to 3 predate the written-prediction rule)'}</p></div>
 <div class="box" style="grid-column:1/-1"><h4>finding <span class="pill ${pill}">${v}</span></h4><p style="margin:0"><b>${R.title}.</b> ${R.lesson}</p><p style="margin:10px 0 0;font-family:'JetBrains Mono';font-size:12.5px;color:var(--mute)">${scoreLine}${R.stopped?' · stopped early: '+R.stopped:''}</p></div>`;
 // lineage chart
 const chain=[];let r=cur;while(r&&!chain.includes(r)){chain.unshift(r);r=parentOf(r);}
 const [x,W,H]=ctx('lineage');x.clearRect(0,0,W,H);const p={l:44,r:20,t:26,b:40};const cw=W-p.l-p.r,ch=H-p.t-p.b;frame(x,W,H,p);const Y=v=>H-p.b-Math.min(6,v)/6*ch;[0,2,4,6].forEach(v=>txt(x,v,p.l-6,Y(v)+4,css('--mute'),'right'));txt(x,'30 s score (or 20 s where no 30 s test), lower is better · the run and its ancestors',p.l+4,p.t-8,css('--mute'));
 x.strokeStyle=css('--green');x.setLineDash([4,4]);x.beginPath();x.moveTo(p.l,Y(0.75));x.lineTo(W-p.r,Y(0.75));x.stroke();x.setLineDash([]);txt(x,'hand brain 0.75',W-p.r-4,Y(0.75)-5,css('--green'),'right');
 const pts=chain.map((rn,i)=>{const Q=D.runs.find(q=>q.run===rn);const t=Q.tests['test_final_30.json']||Object.values(Q.tests)[0];return {rn,A:t?t.A:null,B:t?t.B:null,X:p.l+(chain.length===1?cw/2:i/(chain.length-1)*cw)};});
 x.strokeStyle=css('--rand');x.lineWidth=2;x.beginPath();pts.forEach((q,i)=>{if(q.B===null)return;i?x.lineTo(q.X,Y(q.B)):x.moveTo(q.X,Y(q.B));});x.stroke();
 x.strokeStyle=css('--teal');x.lineWidth=3;x.beginPath();pts.forEach((q,i)=>{if(q.A===null)return;i?x.lineTo(q.X,Y(q.A)):x.moveTo(q.X,Y(q.A));});x.stroke();
 pts.forEach(q=>{if(q.A===null)return;x.fillStyle=q.rn===cur?css('--coral'):css('--teal');x.beginPath();x.arc(q.X,Y(q.A),q.rn===cur?7:5,0,7);x.fill();txt(x,q.rn.replace('run',''),q.X,H-p.b+16,css('--mute'),'center');txt(x,q.A.toFixed(2),q.X,Y(q.A)-12,css('--ink'),'center','12px "Bricolage Grotesque"');});
 txt(x,'teal: with F · grey: F held at zero',W-p.r,p.t-8,css('--mute'),'right');}
(function(){const s=$('steps');D.runs.forEach(r=>{const b=document.createElement('button');b.dataset.r=r.run;b.textContent=r.run.replace('run','');b.addEventListener('click',()=>{cur=r.run;drawStep();});s.appendChild(b);});})();
// ---- Q8 curves
(function(){const g=$('curves');const M=D.motif;M.curves.forEach((c,k)=>{const d=document.createElement('div');const cv=document.createElement('canvas');cv.width=200;cv.height=120;d.appendChild(cv);g.appendChild(d);const x=cv.getContext('2d');const tuned=M.strength[k]>0.25;const col=tuned?css('--teal'):css('--rand');const mn=Math.min(...c),mx=Math.max(...c);x.strokeStyle=css('--line');x.beginPath();x.moveTo(8,100);x.lineTo(192,100);x.stroke();x.strokeStyle=col;x.lineWidth=2.5;x.beginPath();c.concat([c[0]]).forEach((v,i)=>{const px=8+i/16*184,py=95-(v+1)/2*80;i?x.lineTo(px,py):x.moveTo(px,py);});x.stroke();x.fillStyle=css('--mute');x.font='10px "JetBrains Mono"';x.fillText(M.strength[k].toFixed(2),8,14);['E','N','W','S','E'].forEach((s,i)=>x.fillText(s,6+i*46,113));});})();
(function(){const [x,W,H]=ctx('prefHist');x.clearRect(0,0,W,H);const M=D.motif;const bins=new Array(16).fill(0);M.curves.forEach((c,k)=>{if(M.strength[k]>0.25)bins[c.indexOf(Math.max(...c))]++;});const p={l:30,r:20,t:26,b:34};const cw=W-p.l-p.r,ch=H-p.t-p.b;const bw=cw/16;const names=['E','ENE','NE','NNE','N','NNW','NW','WNW','W','WSW','SW','SSW','S','SSE','SE','ESE'];txt(x,'how many compass cells prefer each of the sixteen directions (32 tuned cells)',p.l,p.t-8,css('--mute'));
 bins.forEach((v,i)=>{const bh=v/6*ch;x.fillStyle=css('--teal');x.fillRect(p.l+i*bw+6,H-p.b-bh,bw-12,bh);txt(x,v,p.l+i*bw+bw/2,H-p.b-bh-5,css('--ink'),'center','12px "Bricolage Grotesque"');txt(x,names[i],p.l+i*bw+bw/2,H-p.b+16,css('--mute'),'center','10px "JetBrains Mono"');});})();
function wiring(id,drivers,outRow,inCol,label,inName){const [x,W,H]=ctx(id);x.clearRect(0,0,W,H);const M=D.motif;const p={l:40,r:16,t:40,b:40};const cw=W-p.l-p.r,ch=H-p.t-p.b;const mid=p.t+ch/2;const sc=ch/2/1.1;const n=drivers.length,bw=cw/n;txt(x,label,p.l,18,css('--ink'),'left','14px "Bricolage Grotesque"');txt(x,`pale: weight from ${inName} wire · dark: weight into gate · dot: product`,p.l,34,css('--mute'));
 x.strokeStyle=css('--line');x.beginPath();x.moveTo(p.l,mid);x.lineTo(W-p.r,mid);x.stroke();
 drivers.forEach((nn,i)=>{const a=M.Win[nn][inCol],b=M.Wout[outRow][nn];const bx=p.l+i*bw+6,w=(bw-12)/2;x.fillStyle=css('--blue');x.globalAlpha=.4;x.fillRect(bx,a>0?mid-a*sc:mid,w,Math.abs(a)*sc);x.globalAlpha=1;x.fillRect(bx+w,b>0?mid-b*sc:mid,w,Math.abs(b)*sc);const pr=a*b;x.fillStyle=pr>0?css('--green'):css('--coral');x.beginPath();x.arc(bx+w,mid-pr*sc*2,6,0,7);x.fill();txt(x,'n'+nn,bx+w,H-p.b+16,css('--mute'),'center');txt(x,(pr>0?'+':'')+pr.toFixed(2),bx+w,mid-pr*sc*2-10,pr>0?css('--green'):css('--coral'),'center','11px "JetBrains Mono"');});}
wiring('writeWiring',D.motif.write_drivers,1,2,'write gate · its eight strongest drivers','speed');wiring('eraseWiring',D.motif.erase_drivers,2,3,'erase gate · its eight strongest drivers','food');
(function(){const [x,W,H]=ctx('Ftrace');x.clearRect(0,0,W,H);const p={l:40,r:20,t:20,b:34};const cw=W-p.l-p.r,ch=H-p.t-p.b;const t=D.Ft,tmax=t[t.length-1];const X=v=>p.l+v/tmax*cw,Y=v=>p.t+ch/2-v*ch/2*.92;frame(x,W,H,p);[1,0,-1].forEach(v=>txt(x,v>0?'+1':v,p.l-6,Y(v)+4,css('--mute'),'right'));txt(x,'seconds →',W-p.r,H-6,css('--mute'),'right');
 x.fillStyle=css('--soft');let s=null;const food=D.motif.food;food.forEach((f,i)=>{if(f&&s===null)s=i;if((!f||i===food.length-1)&&s!==null){x.fillRect(X(t[s]),p.t,Math.max(2,X(t[i])-X(t[s])),ch);s=null;}});
 x.setLineDash([6,5]);x.strokeStyle=css('--coral');[1,-1].forEach(v=>{x.beginPath();x.moveTo(p.l,Y(v));x.lineTo(W-p.r,Y(v));x.stroke();});x.setLineDash([]);
 x.strokeStyle=css('--teal');x.lineWidth=1.6;x.globalAlpha=.85;D.F.forEach(row=>{x.beginPath();row.forEach((v,i)=>i?x.lineTo(X(t[i]),Y(v)):x.moveTo(X(t[i]),Y(v)));x.stroke();});x.globalAlpha=1;
 const dm=Math.max(...D.dist);const Yd=v=>H-p.b-v/dm*ch*.9;x.strokeStyle=css('--rand');x.lineWidth=2;x.beginPath();D.dist.forEach((v,i)=>i?x.lineTo(X(t[i]),Yd(v)):x.moveTo(X(t[i]),Yd(v)));x.stroke();txt(x,'grey: distance from home',W-p.r,p.t+12,css('--mute'),'right');})();
function heat(id,Mx,title){const [x,W,H]=ctx(id);x.clearRect(0,0,W,H);const n=Mx.length;const p={l:40,r:10,t:36,b:30};const s=Math.min(W-p.l-p.r,H-p.t-p.b)/n;txt(x,title,p.l,20,css('--ink'),'left','14px "Bricolage Grotesque"');const mx=Math.max(...Mx.flat().map(Math.abs));
 Mx.forEach((row,i)=>row.forEach((v,j)=>{const a=Math.min(1,Math.abs(v)/mx);x.fillStyle=v>0?`rgba(217,72,43,${a})`:`rgba(47,91,234,${a})`;x.fillRect(p.l+j*s,p.t+i*s,s,s);}));
 const pr=D.motif.pref;['E','N','W','S'].forEach((d,k)=>{const idx=pr.findIndex(v=>v>=k*90);if(idx>=0){txt(x,d,p.l+idx*s,H-p.b+16,css('--mute'),'left');txt(x,d,p.l-14,p.t+idx*s+10,css('--mute'),'left');}});txt(x,'sending cell →',W-p.r,H-4,css('--mute'),'right');txt(x,'max |'+(id[0])+'| '+mx.toFixed(2),W-p.r,20,css('--mute'),'right');}
heat('Wsorted',D.motif.W_sorted,'W, slow table, compass cells sorted by preferred direction');heat('Asorted',D.motif.A_sorted,'A, allowance table, same order');
(function(){const [x,W,H]=ctx('profile');x.clearRect(0,0,W,H);const p={l:44,r:20,t:26,b:36};const cw=W-p.l-p.r,ch=H-p.t-p.b;frame(x,W,H,p);const X=i=>p.l+(i+0.5)/12*cw,Y=v=>p.t+ch/2-v/0.15*ch/2;[-0.1,0,0.1].forEach(v=>txt(x,v,p.l-6,Y(v)+4,css('--mute'),'right'));x.strokeStyle=css('--line');x.beginPath();x.moveTo(p.l,Y(0));x.lineTo(W-p.r,Y(0));x.stroke();
 ['−180°','−90°','0°','+90°','+180°'].forEach((s,k)=>txt(x,s,p.l+k/4*cw,H-p.b+16,css('--mute'),'center'));txt(x,'mean weight by difference in preferred direction (a ring would show a hump at 0° and a dip at ±180°)',p.l+4,p.t-8,css('--mute'));
 const line=(arr,col)=>{x.strokeStyle=col;x.lineWidth=3;x.beginPath();arr.forEach((v,i)=>i?x.lineTo(X(i),Y(v)):x.moveTo(X(i),Y(v)));x.stroke();};line(D.motif.profW,css('--ink'));line(D.motif.profA,css('--teal'));
 // ring sketch expectation
 x.strokeStyle=css('--blue');x.setLineDash([4,4]);x.lineWidth=2;x.beginPath();for(let i=0;i<12;i++){const d=(i+0.5)/12*360-180;const v=0.1*Math.cos(d*Math.PI/180);i?x.lineTo(X(i),Y(v)):x.moveTo(X(i),Y(v));}x.stroke();x.setLineDash([]);
 txt(x,'black: W · teal: A · dashed blue: what a ring attractor would look like',W-p.r,p.t-8,css('--mute'),'right');})();
(function(){const g=$('ring');let s='';for(let i=0;i<12;i++){const a=i/12*6.283;const cx=120+Math.cos(a)*70,cy=110+Math.sin(a)*70;const hot=i===2||i===3||i===1;s+=`<circle cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="9" fill="${hot?'var(--coral)':'var(--panel)'}" stroke="var(--ink)" stroke-width="1.5"/>`;}s+='<text x="120" y="115" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">bump = heading</text><path d="M60,30 C90,10 150,10 180,30" fill="none" stroke="var(--blue)" stroke-width="2" marker-end="url(#ar)"/><text x="120" y="12" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="var(--blue)">shifters push it</text>';g.innerHTML=s;})();
// ---- Q9 rules
const RULES=[
 ['<div class="eq">x_new = tanh( <span class="d">W</span> · x_old + input )</div><p style="font-size:15px">A plain recurrent network. Every connection has one strength, W, and that strength never changes while the network runs. So the only place a memory can live is in the neurons\' activity, passed round and round the loop from one tick to the next. Run 20, the rival, is essentially this kind of network.</p>'],
 ['<div class="eq">x_new = tanh( (<span class="d">W</span> + <span class="a">α</span>·Hebb) · x_old + input )<br>Hebb ← clip( Hebb + <span class="c">η</span>·x_old ⊗ x_new )</div><p style="font-size:15px">Miconi, Stanley and Clune, 2018. Each connection gets a plastic part, Hebb, that grows with the product of the two neurons\' activities and is clipped to ±1. Two new trained numbers: α per connection (how much the plastic part counts) and η (how fast it writes). Both of those are learned by backprop across episodes. Hebb itself is not set by training; it is produced by the network\'s own activity while it runs, and it starts again from zero in each episode.</p>'],
 ['<div class="eq">Hebb ← clip( Hebb + <span class="c">M(t)</span>·x_old ⊗ x_new )</div><p style="font-size:15px">Backpropamine, simple form. The fixed writing rate η is replaced by M(t), a number the network itself outputs on every tick. So the network now decides, moment by moment, how much its connections should change. M(t) can also be negative, in which case it removes what was written earlier. This is where the dopamine analogy comes from: in the brain, dopamine is a chemical signal, sent to many neurons at once, that tells them to strengthen their recent connections. M(t) plays the same role here, a single "learn now" signal that the network controls itself.</p>'],
 ['<div class="eq">E ← (1 − <span class="c">η</span>)·E + <span class="c">η</span>·x_old ⊗ x_new<br>Hebb ← clip( Hebb + <span class="c">M(t)</span>·E )</div><p style="font-size:15px">Backpropamine, retroactive form. Activity first leaves a fading trace E (an <span class="term" title="eligibility trace: a short-lived record of which connections were recently active, waiting to be confirmed or discarded">eligibility trace</span>). Only when M(t) fires does the trace turn into a real change in the connection. This means a reward signal can arrive up to about a second late and still strengthen the connections that were active just before it, which is what dopamine is believed to do at real synapses.</p>'],
 ['<div class="eq">x_new = tanh( (<span class="d">W</span> + <span class="a">A</span>·F) · x_old + input )<br>F ← clamp( (1 − <span class="b">erase(t)</span>)·F + ws·<span class="c">write(t)</span>·x_new ⊗ x_old )</div><p style="font-size:15px">FlyNet. Start from the simple Backpropamine rule. Rename α to "A" and Hebb to "F". Set M(t) equal to ws × write(t), a trained constant times a gate the network produces. Then add a second gate that the network also produces, erase(t), which multiplies the old F on every tick. The erase gate is the only real difference between the two rules, and it was added because the fly needs to wipe its tally when it reaches food. Every other part of the rule is inherited from Backpropamine.</p>']];
document.querySelectorAll('.rule').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.rule').forEach(q=>q.classList.remove('on'));b.classList.add('on');$('ruleBox').innerHTML=RULES[+b.dataset.r][0];}));$('ruleBox').innerHTML=RULES[0][0];

// ---- Q1 one tick by hand (3 neurons)
const M3={Win:[[0.8,0.1,0.3,-0.2],[-0.2,0.9,0.4,0.1],[0.1,-0.3,0.2,0.9]],bin:[0,0,-0.2],W:[[0,0.3,-0.2],[0.4,0,0.1],[-0.1,0.2,0]],A:[[0,0.6,0.2],[0.5,0,0.3],[0.1,0.4,0]],Wout:[[0.5,-0.6,0.1],[0.3,0.4,-0.2],[-0.3,-0.2,0.9]],bout:[0,1.0,-1.0],ws:0.3};
let S3={x:[0,0,0],F:[[0,0,0],[0,0,0],[0,0,0]],n:0};
const f2=v=>(v>=0?'+':'')+v.toFixed(2);
function tick3(show=true){const inp=[+$('i0').value,+$('i1').value,+$('i2').value,+$('i3').value];['i0','i1','i2','i3'].forEach((id,k)=>$('o'+id).textContent=inp[k].toFixed(1));
 const xo=S3.x;const drive=[],rec=[],xn=[];for(let i=0;i<3;i++){let d=M3.bin[i];for(let k=0;k<4;k++)d+=M3.Win[i][k]*inp[k];drive.push(d);let r=0;for(let j=0;j<3;j++)r+=(M3.W[i][j]+M3.A[i][j]*S3.F[i][j])*xo[j];rec.push(r);xn.push(Math.tanh(d+r));}
 const out=[0,1,2].map(m=>{let o=M3.bout[m];for(let i=0;i<3;i++)o+=M3.Wout[m][i]*xn[i];return o;});const turn=8*Math.tanh(out[0]/8),write=sig(out[1]),erase=sig(out[2]);
 const Fn=S3.F.map((row,i)=>row.map((v,j)=>Math.max(-1,Math.min(1,(1-erase)*v+M3.ws*write*xn[i]*xo[j]))));
 if(show){const T=(name,rows,head)=>`<div><div class="eyebrow" style="margin-bottom:4px">${name}</div><table style="margin:0;font-family:'JetBrains Mono';font-size:12.5px"><tr>${head.map(h=>`<th>${h}</th>`).join('')}</tr>${rows.map(r=>`<tr>${r.map(v=>`<td class="n">${typeof v==='number'?f2(v):v}</td>`).join('')}</tr>`).join('')}</table></div>`;
  const eff=S3.F.map((row,i)=>row.map((v,j)=>M3.W[i][j]+M3.A[i][j]*v));
  $('tickOut').innerHTML=`
  <p style="margin:0 0 10px"><b>Step 1, input drive.</b> For each neuron: the four inputs times its four W_in weights, plus its bias. Neuron 1: ${M3.Win[0].map((w,k)=>`${f2(w)}×${inp[k].toFixed(1)}`).join(' + ')} + ${f2(M3.bin[0])} = <b>${f2(drive[0])}</b>. Same for neurons 2 and 3: ${f2(drive[1])}, ${f2(drive[2])}.</p>
  <p style="margin:0 0 10px"><b>Step 2, effective connections.</b> W + A·F, cell by cell. F right now is what the trip has written so far.</p>
  <div class="three">${T('W (permanent)',M3.W,['from 1','from 2','from 3'])}${T('A·F (fast part, allowance × state)',S3.F.map((row,i)=>row.map((v,j)=>M3.A[i][j]*v)),['from 1','from 2','from 3'])}${T('W + A·F (used this tick)',eff,['from 1','from 2','from 3'])}</div>
  <p style="margin:10px 0"><b>Step 3, recurrent drive.</b> Each neuron adds up the other neurons' activity from last tick (${xo.map(f2).join(', ')}) times the effective connections in its row: ${rec.map(f2).join(', ')}.</p>
  <p style="margin:0 0 10px"><b>Step 4, squash.</b> New activity = tanh(input drive + recurrent drive) = <b>${xn.map(f2).join(', ')}</b>. Always between −1 and +1.</p>
  <p style="margin:0 0 10px"><b>Step 5, outputs.</b> Each output = its three W_out weights times the three activities, plus its bias, then squashed. Raw: ${out.map(f2).join(', ')}. Turn = 8·tanh(raw/8) = <b>${f2(turn)}</b>. Write gate = sigmoid(${f2(out[1])}) = <b>${write.toFixed(2)}</b>. Erase gate = sigmoid(${f2(out[2])}) = <b>${erase.toFixed(2)}</b>.</p>
  <p style="margin:0 0 10px"><b>Step 6, rewrite F.</b> Every cell: (1 − ${erase.toFixed(2)}) × old + ${M3.ws} × ${write.toFixed(2)} × (activity of the receiving neuron now) × (activity of the sending neuron last tick), then clamped to ±1. The deposit this tick is what "fire together, wire together" means: cells where both are active get a bigger number.</p>
  <div class="two">${T('F before',S3.F,['from 1','from 2','from 3'])}${T('F after this tick',Fn,['from 1','from 2','from 3'])}</div>
  <p style="margin:10px 0 0;color:var(--mute)">Note the sizes: 3 neurons here means W_in has 3×4 = 12 weights + 3 biases, W and A have 3×3 = 9 each, W_out has 3×3 = 9 + 3 biases. The real network does the identical arithmetic with 64 in place of 3.</p>`;}
 S3.x=xn;S3.F=Fn;S3.n++;$('tickCount').textContent='tick '+S3.n;}
$('tick').addEventListener('click',()=>tick3(true));$('tick10').addEventListener('click',()=>{for(let k=0;k<9;k++)tick3(false);tick3(true);});$('tickReset').addEventListener('click',()=>{S3={x:[0,0,0],F:[[0,0,0],[0,0,0],[0,0,0]],n:0};$('tickCount').textContent='tick 0';$('tickOut').innerHTML='<p style="color:var(--mute)">Fresh episode: F is all zeros and so is the activity. Press "one tick".</p>';});
['i0','i1','i2','i3'].forEach(id=>$(id).addEventListener('input',()=>$('o'+id).textContent=(+$(id).value).toFixed(1)));
$('tickReset').click();

(function(){const g=$('wsketch');const n=6;const cx=450,cy=150,R=100;const pos=[];for(let i=0;i<n;i++){const a=-Math.PI/2+i/n*2*Math.PI;pos.push([cx+Math.cos(a)*R,cy+Math.sin(a)*R]);}
 const W=[[0,0.6,-0.3,0,0.2,0],[0.5,0,0.4,-0.5,0,0],[0,0.3,0,0.6,0,-0.4],[-0.2,0,0.5,0,0.7,0],[0,0,-0.3,0.4,0,0.6],[0.3,-0.6,0,0,0.5,0]];
 let s='';for(let i=0;i<n;i++)for(let j=0;j<n;j++){const w=W[i][j];if(!w)continue;const [x1,y1]=pos[j],[x2,y2]=pos[i];const dx=x2-x1,dy=y2-y1,L=Math.hypot(dx,dy);const ux=dx/L,uy=dy/L;const sx=x1+ux*22,sy=y1+uy*22,ex=x2-ux*22,ey=y2-uy*22;const mx=(sx+ex)/2-uy*14,my=(sy+ey)/2+ux*14;s+=`<path d="M${sx},${sy} Q${mx},${my} ${ex},${ey}" fill="none" stroke="${w>0?'var(--coral)':'var(--blue)'}" stroke-width="${Math.abs(w)*6}" opacity=".85" marker-end="url(#ar)"/><text x="${mx}" y="${my}" font-family="JetBrains Mono" font-size="10" fill="var(--mute)" text-anchor="middle">${(w>0?'+':'')+w.toFixed(1)}</text>`;}
 for(let i=0;i<n;i++){const [x,y]=pos[i];s+=`<circle cx="${x}" cy="${y}" r="20" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="${x}" y="${y+5}" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">${i+1}</text>`;}
 s+='<text x="30" y="30" font-family="JetBrains Mono" font-size="12" fill="var(--mute)">arrow from j to i, thickness = |W[i,j]|, red excites, blue quiets</text><text x="30" y="280" font-family="JetBrains Mono" font-size="12" fill="var(--mute)">e.g. W[2,1] = +0.5: when neuron 1 was active last tick, neuron 2 is pushed up by half that much now</text>';g.innerHTML=s;})();

// ---- clock
(function(){const g=$('clock');let n=0;const boxes=[['x','64 activities',330,60,180,50,true],['out','turn · write · erase',700,60,180,50,true],['F','F, 4,096 cells',330,230,180,50,true],['Win','W_in · 320',80,60,150,50,false],['W','W · 4,096',330,130,85,50,false],['A','A · 4,096',425,130,85,50,false],['Wout','W_out · 195',700,130,180,50,false],['ws','ws · 1',330,300,85,26,false]];
 function draw(flash){let s='<text x="20" y="30" font-family="JetBrains Mono" font-size="12" fill="var(--mute)">flashing = recomputed this tick · padlock = frozen by training</text>';boxes.forEach(([k,l,x,y,w,h,live])=>{const on=flash&&live;s+=`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="8" fill="${on?'var(--chalk)':'var(--panel)'}" stroke="${live?'var(--teal)':'var(--line)'}" stroke-width="${on?3:1.5}"/><text x="${x+w/2}" y="${y+h/2+5}" text-anchor="middle" font-family="Bricolage Grotesque" font-size="13" fill="var(--ink)">${l}</text>`;if(!live)s+=`<text x="${x+w-14}" y="${y+14}" font-size="12">🔒</text>`;});
  s+='<path d="M230,85 L330,85" stroke="var(--mute)" stroke-width="2" marker-end="url(#ar)"/><path d="M510,85 L700,85" stroke="var(--mute)" stroke-width="2" marker-end="url(#ar)"/><path d="M420,180 L420,230" stroke="var(--mute)" stroke-width="2"/><path d="M420,230 L420,180" stroke="var(--mute)" stroke-width="2" marker-end="url(#ar)"/><path d="M790,110 C790,260 520,290 512,258" fill="none" stroke="var(--coral)" stroke-width="1.5" stroke-dasharray="4 4" marker-end="url(#ar)"/><text x="600" y="300" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">gates → F rule</text><text x="20" y="320" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">inputs → W_in → activities (using W + A·F) → W_out → outputs; then the rule rewrites F using the gates</text>';g.innerHTML=s;}
 draw(false);const tick=()=>{n++;$('clockN').textContent='tick '+n;draw(true);setTimeout(()=>draw(false),350);};$('clockTick').addEventListener('click',tick);$('clockRun').addEventListener('click',()=>{let k=0;const id=setInterval(()=>{tick();if(++k>=10)clearInterval(id);},500);});})();
// ---- squares
(function(){const c=$('squares');const [x,W,H]=ctx('squares');x.clearRect(0,0,W,H);const blocks=[];const u=3.6;
 function block(name,x0,y0,rows,cols,col,label,bias){for(let i=0;i<rows;i++)for(let j=0;j<cols;j++){x.fillStyle=col;x.globalAlpha=.75;x.fillRect(x0+j*u,y0+i*u,u-0.6,u-0.6);}x.globalAlpha=1;blocks.push({name,x0,y0,rows,cols,label,bias:false});
  if(bias){for(let i=0;i<bias;i++){x.fillStyle=css('--amber');x.fillRect(x0+cols*u+4,y0+i*u,u-0.6,u-0.6);}blocks.push({name:name+' bias',x0:x0+cols*u+4,y0,rows:bias,cols:1,label:'bias',bias:true});}
  txt(x,label,x0,y0-8,css('--ink'),'left','13px "Bricolage Grotesque"');}
 block('W_in',20,40,64,4,css('--blue'),'W_in: 4 × 64 = 256, + 64 biases = 320',64);
 block('W',90,40,64,64,css('--ink'),'W: 64 × 64 = 4,096');
 block('A',350,40,64,64,css('--ink'),'A: 64 × 64 = 4,096');
 block('W_out',610,40,3,64,css('--blue'),'W_out: 64 × 3 = 192, + 3 biases = 195',3);
 x.fillStyle=css('--teal');x.fillRect(610,90,u*3,u*3);txt(x,'ws: 1',610,84,css('--ink'),'left','13px "Bricolage Grotesque"');blocks.push({name:'ws',x0:610,y0:90,rows:1,cols:1,label:'',bias:false});
 x.globalAlpha=.3;block('F',610,140,64,64,css('--teal'),'F: 64 × 64 = 4,096, state, not a parameter');x.globalAlpha=1;
 txt(x,'parameters: 320 + 4,096 + 4,096 + 195 + 1 = 8,708',20,H-14,css('--ink'),'left','15px "Bricolage Grotesque"');
 c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect();const px=(e.clientX-r.left)/r.width*W,py=(e.clientY-r.top)/r.height*H;for(const b of blocks){if(px>=b.x0&&px<b.x0+b.cols*u&&py>=b.y0&&py<b.y0+b.rows*u){const i=Math.floor((py-b.y0)/u),j=Math.floor((px-b.x0)/u);let m='';if(b.name==='W_in')m=`W_in[neuron ${i+1}, input ${['compass E-W','compass N-S','speed','food'][j]}]: how loudly neuron ${i+1} hears that input`;else if(b.name==='W')m=`W[${i+1}, ${j+1}]: permanent push from neuron ${j+1} onto neuron ${i+1}`;else if(b.name==='A')m=`A[${i+1}, ${j+1}]: how much the fast part of the wire from neuron ${j+1} to neuron ${i+1} counts`;else if(b.name==='W_out')m=`W_out[${['turn','write gate','erase gate'][i]}, neuron ${j+1}]: how much neuron ${j+1} pushes that output`;else if(b.name==='F')m=`F[${i+1}, ${j+1}]: what this trip has written on the wire from neuron ${j+1} to neuron ${i+1} (state, not a parameter)`;else if(b.name==='ws')m='ws: the one write strength, multiplies every deposit';else m=`${b.name} for row ${i+1}: the resting offset added before squashing`;$('squareDetail').textContent=m;return;}}});})();
// ---- wire
function drawWire(){const w=+$('W1').value,a=+$('A1').value,f=+$('F1').value;$('oW1').textContent=(w>=0?'+':'')+w.toFixed(2);$('oA1').textContent=a.toFixed(2);$('oF1').textContent=(f>=0?'+':'')+f.toFixed(2);const eff=w+a*f;const g=$('wire');const col=v=>v>=0?'var(--coral)':'var(--blue)';
 g.innerHTML=`<circle cx="120" cy="100" r="28" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="120" y="105" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">j</text><text x="120" y="150" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">sender, last tick</text>
 <circle cx="780" cy="100" r="28" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="780" y="105" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">i</text><text x="780" y="150" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">receiver, now</text>
 <line x1="150" y1="88" x2="750" y2="88" stroke="${col(w)}" stroke-width="${Math.max(1,Math.abs(w)*14)}" opacity=".9"/><text x="450" y="70" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="${col(w)}">permanent strand W = ${(w>=0?'+':'')+w.toFixed(2)}</text>
 <line x1="150" y1="112" x2="750" y2="112" stroke="${col(a*f)}" stroke-width="${Math.max(0.5,Math.abs(a*f)*14)}" stroke-dasharray="8 5" opacity=".9"/><text x="450" y="140" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="${col(a*f)}">temporary strand A × F = ${a.toFixed(2)} × ${(f>=0?'+':'')+f.toFixed(2)} = ${(a*f>=0?'+':'')+(a*f).toFixed(2)}</text>
 <text x="450" y="185" text-anchor="middle" font-family="Bricolage Grotesque" font-size="16" font-weight="700" fill="var(--ink)">what neuron i feels from j this tick: W + A·F = ${(eff>=0?'+':'')+eff.toFixed(2)}</text>`;}
['W1','A1','F1'].forEach(id=>$(id).addEventListener('input',drawWire));
// ---- F board
const FB={before:[[0.2,-0.1,0.4,0],[0.3,0.5,-0.2,0.1],[-0.4,0.2,0.6,0.3],[0.1,0,0.2,-0.3]],xn:[0.8,-0.3,0.5,0.1],xo:[0.6,0.2,-0.4,0.7],ws:0.3,stage:0};
function drawFB(){const e=+$('E2').value,w=+$('Wr2').value;$('oE2').textContent=e.toFixed(2);$('oWr2').textContent=w.toFixed(2);const [x,W,H]=ctx('fboard');x.clearRect(0,0,W,H);const u=48;
 const dep=FB.xn.map(a=>FB.xo.map(b=>a*b));const m1=FB.before.map(r=>r.map(v=>(1-e)*v));const m2=m1.map((r,i)=>r.map((v,j)=>v+FB.ws*w*dep[i][j]));const m3=m2.map(r=>r.map(v=>Math.max(-1,Math.min(1,v))));
 const grid=(M,x0,y0,title,sub)=>{txt(x,title,x0,y0-22,css('--ink'),'left','14px "Bricolage Grotesque"');if(sub)txt(x,sub,x0,y0-7,css('--mute'));M.forEach((r,i)=>r.forEach((v,j)=>{const a=Math.min(1,Math.abs(v));x.fillStyle=v>0?`rgba(217,72,43,${0.15+a*0.8})`:`rgba(47,91,234,${0.15+a*0.8})`;x.fillRect(x0+j*u,y0+i*u,u-2,u-2);txt(x,(v>=0?'+':'')+v.toFixed(2),x0+j*u+u/2-1,y0+i*u+u/2+4,'#fff','center','11px "JetBrains Mono"');}));};
 grid(FB.before,40,60,'F before',FB.stage>0?'':'the board at the start of this tick');
 // deposit with activities on edges
 grid(dep,330,60,'deposit = x_new[i] × x_old[j]','receiver now (rows) × sender last tick (cols)');FB.xo.forEach((v,j)=>txt(x,(v>=0?'+':'')+v.toFixed(1),330+j*u+u/2,60+4*u+16,css('--teal'),'center'));FB.xn.forEach((v,i)=>txt(x,(v>=0?'+':'')+v.toFixed(1),322,60+i*u+u/2+4,css('--teal'),'right'));
 const stageM=[FB.before,m1,m2,m3][FB.stage];const clipped=m2.map(r=>r.map(v=>Math.abs(v)>1));const nclip=clipped.flat().filter(Boolean).length;const titles=['result: nothing yet',`after move 1: every cell × (1 − ${e.toFixed(2)})`,`after move 2: + ${FB.ws} × ${w.toFixed(2)} × deposit`,'after move 3: clamped to ±1'];
 grid(stageM,620,60,titles[FB.stage],'');if(FB.stage===3){clipped.forEach((r,i)=>r.forEach((c,j)=>{if(c){x.strokeStyle=css('--amber');x.lineWidth=4;x.strokeRect(620+j*u+1,60+i*u+1,u-4,u-4);}}));txt(x,`cells clipped by the lid this tick: ${nclip}`,620,60+4*u+36,nclip?css('--amber'):css('--mute'),'left','13px "Bricolage Grotesque"');}
 if(FB.stage===2&&nclip)txt(x,`${nclip} cell${nclip>1?'s':''} now past ±1 (move 3 will clip)`,620,60+4*u+36,css('--amber'),'left','13px "Bricolage Grotesque"');
 txt(x,`mean |F| before ${(FB.before.flat().reduce((a,v)=>a+Math.abs(v),0)/16).toFixed(3)} → now ${(stageM.flat().reduce((a,v)=>a+Math.abs(v),0)/16).toFixed(3)}`,40,H-16,css('--mute'));
 FB.result=m3;}
['E2','Wr2'].forEach(id=>$(id).addEventListener('input',drawFB));[['fb0',0],['fb1',1],['fb2',2],['fb3',3]].forEach(([id,st])=>$(id).addEventListener('click',()=>{FB.stage=st;drawFB();}));$('fbTen').addEventListener('click',()=>{$('E2').value=0;$('Wr2').value=1;for(let k=0;k<10;k++){const dep=FB.xn.map(a=>FB.xo.map(b=>a*b));FB.before=FB.before.map((r,i)=>r.map((v,j)=>Math.max(-1,Math.min(1,v+FB.ws*1*dep[i][j]))));}FB.stage=3;drawFB();});
$('fbNext').addEventListener('click',()=>{FB.before=FB.result.map(r=>r.slice());FB.xo=FB.xn.slice();FB.xn=FB.xn.map(v=>Math.tanh(v*1.3+0.1));FB.stage=0;drawFB();});
// ---- gradient descent ball
const GD={p:-3.2,n:0};const lossF=p=>0.6*Math.cos(p*0.9)+0.12*p*p+1.0+0.5*Math.exp(-((p+4)**2)*2);
function drawGD(){const lr=+$('LR').value;$('oLR').textContent=lr.toFixed(2);const [x,W,H]=ctx('gd');x.clearRect(0,0,W,H);const p={l:44,r:20,t:30,b:40};const cw=W-p.l-p.r,ch=H-p.t-p.b;const X=v=>p.l+(v+5)/10*cw,Y=v=>H-p.b-v/5*ch;frame(x,W,H,p);txt(x,'parameter value →',W-p.r,H-6,css('--mute'),'right');txt(x,'loss',p.l+4,p.t-8,css('--mute'));
 x.strokeStyle=css('--ink');x.lineWidth=3;x.beginPath();for(let v=-5;v<=5;v+=0.05){const px=X(v),py=Y(lossF(v));v===-5?x.moveTo(px,py):x.lineTo(px,py);}x.stroke();
 const sl=(lossF(GD.p+1e-3)-lossF(GD.p-1e-3))/2e-3;x.strokeStyle=css('--blue');x.lineWidth=2;x.beginPath();x.moveTo(X(GD.p-0.8),Y(lossF(GD.p)-0.8*sl));x.lineTo(X(GD.p+0.8),Y(lossF(GD.p)+0.8*sl));x.stroke();
 x.fillStyle=css('--coral');x.beginPath();x.arc(X(GD.p),Y(lossF(GD.p)),9,0,7);x.fill();
 txt(x,`value ${GD.p.toFixed(2)} · slope ${sl.toFixed(2)} · next step = −${lr.toFixed(2)} × ${sl.toFixed(2)} = ${(-lr*sl).toFixed(2)}`,X(GD.p)+14,Y(lossF(GD.p))-14,css('--ink'),'left','13px "Bricolage Grotesque"');
 txt(x,'flat here: a big push moves it a little',X(-4),Y(lossF(-4))-24,css('--mute'));}
$('LR').addEventListener('input',drawGD);$('gdStep').addEventListener('click',()=>{const lr=+$('LR').value;const sl=(lossF(GD.p+1e-3)-lossF(GD.p-1e-3))/2e-3;GD.p=Math.max(-5,Math.min(5,GD.p-lr*sl));GD.n++;$('gdN').textContent='step '+GD.n;drawGD();});$('gdReset').addEventListener('click',()=>{GD.p=-3.2;GD.n=0;$('gdN').textContent='step 0';drawGD();});

function fullHeat(id,Mx,title,det){const c=$(id);const [x,W,H]=ctx(id);x.clearRect(0,0,W,H);const n=Mx.length;const p={l:30,r:10,t:36,b:40};const u=Math.min(W-p.l-p.r,H-p.t-p.b)/n;txt(x,title,p.l,20,css('--ink'),'left','14px "Bricolage Grotesque"');const mx=Math.max(...Mx.flat().map(Math.abs));
 Mx.forEach((row,i)=>row.forEach((v,j)=>{const a=Math.min(1,Math.abs(v)/mx);x.fillStyle=v>0?`rgba(217,72,43,${a})`:`rgba(47,91,234,${a})`;x.fillRect(p.l+j*u,p.t+i*u,u,u);}));
 const flat=Mx.flat();const mean=flat.reduce((a,v)=>a+v,0)/flat.length,mabs=flat.reduce((a,v)=>a+Math.abs(v),0)/flat.length;txt(x,`summary numbers: average ${(mean>=0?'+':'')+mean.toFixed(2)}, mean size ${mabs.toFixed(2)}, largest ${mx.toFixed(2)}`,p.l,H-12,css('--mute'));txt(x,'sender j →',W-p.r,p.t-6,css('--mute'),'right');txt(x,'receiver i ↓',p.l-24,p.t+12,css('--mute'),'left','10px "JetBrains Mono"');
 c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect();const px=(e.clientX-r.left)/r.width*W,py=(e.clientY-r.top)/r.height*H;const j=Math.floor((px-p.l)/u),i=Math.floor((py-p.t)/u);if(i>=0&&i<n&&j>=0&&j<n)$(det).textContent=`${id[0]}[${i+1}, ${j+1}] = ${(Mx[i][j]>=0?'+':'')+Mx[i][j].toFixed(2)}: ${id[0]==='W'?'permanent push from neuron '+(j+1)+' onto neuron '+(i+1):'how much the fast part of the wire from neuron '+(j+1)+' to neuron '+(i+1)+' counts'}`;});}
fullHeat('Wfull',D.motif.W_full,'W: the whole table (run 19)','wfullDetail');fullHeat('Afull',D.motif.A_full,'A: the whole allowance table (run 19)','wfullDetail');
function drawWsA(){const ws=+$('WS3').value,A=+$('A3').value;$('oWS3').textContent=ws.toFixed(2);$('oA3').textContent=A.toFixed(2);const [x,W,H]=ctx('wsA');x.clearRect(0,0,W,H);const N=60;const f=[];let v=0;for(let t=0;t<=N;t++){f.push(v);v=Math.min(1,v+ws*0.5*0.6);}
 const half=W/2;const draw=(x0,vals,ymax,title,col,lid)=>{const p={l:x0+44,r:x0+half-20,t:30,b:36};const cw=p.r-p.l,ch=H-p.t-p.b;const X=t=>p.l+t/N*cw,Y=q=>H-p.b-q/ymax*ch;x.strokeStyle=css('--line');x.beginPath();x.moveTo(p.l,p.t);x.lineTo(p.l,H-p.b);x.lineTo(p.r,H-p.b);x.stroke();txt(x,title,p.l,p.t-10,css('--ink'),'left','14px "Bricolage Grotesque"');txt(x,'ticks →',p.r,H-6,css('--mute'),'right');[0,ymax/2,ymax].forEach(q=>txt(x,q.toFixed(1),p.l-6,Y(q)+4,css('--mute'),'right'));
  if(lid!==null){x.setLineDash([6,5]);x.strokeStyle=css('--coral');x.lineWidth=2;x.beginPath();x.moveTo(p.l,Y(lid));x.lineTo(p.r,Y(lid));x.stroke();x.setLineDash([]);txt(x,'lid',p.r-4,Y(lid)-6,css('--coral'),'right');}
  x.strokeStyle=col;x.lineWidth=3;x.beginPath();vals.forEach((q,t)=>t?x.lineTo(X(t),Y(q)):x.moveTo(X(t),Y(q)));x.stroke();const hit=vals.findIndex(q=>q>=0.999);if(hit>0){x.fillStyle=css('--coral');x.beginPath();x.arc(X(hit),Y(vals[hit]),6,0,7);x.fill();txt(x,`hits the lid at tick ${hit}`,X(hit)+8,Y(vals[hit])+18,css('--coral'));}};
 draw(0,f,1.1,'the board: one cell of F, written at ws × write × deposit per tick',css('--teal'),1);draw(half,f.map(q=>A*q),1.6,'what the neuron feels: A × F',css('--blue'),null);}
['WS3','A3'].forEach(id=>$(id).addEventListener('input',drawWsA));

(function(){const g=$('eraseBars');const vals=[0,0.01,0.28,0.77,1];let out='';vals.forEach((e,k)=>{const x0=40+k*170;const keep=0.4*(1-e);out+=`<text x="${x0+60}" y="30" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" font-weight="700" fill="var(--ink)">erase = ${e}</text><text x="${x0+60}" y="50" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">keep ${(100*(1-e)).toFixed(0)}%</text>
 <rect x="${x0+20}" y="${200-0.4*300}" width="34" height="${0.4*300}" fill="var(--line)"/><text x="${x0+37}" y="215" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">before</text><text x="${x0+37}" y="${200-0.4*300-6}" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">0.40</text>
 <rect x="${x0+66}" y="${200-keep*300}" width="34" height="${Math.max(keep*300,1)}" fill="var(--coral)"/><text x="${x0+83}" y="215" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">after</text><text x="${x0+83}" y="${200-keep*300-6}" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--coral)">${keep.toFixed(2)}</text>`;});out+='<text x="450" y="245" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">after = (1 − erase) × before. Nothing else is multiplied in on this side.</text>';g.innerHTML=out;})();
function drawDeposit(){const xn=+$('xn').value,xo=+$('xo').value,wr=+$('wr').value,ws=+$('wsv').value,er=+$('er').value,fo=+$('fo').value;$('oxn').textContent=xn.toFixed(2);$('oxo').textContent=xo.toFixed(2);$('owr').textContent=wr.toFixed(2);$('ows').textContent=ws.toFixed(3);$('oer').textContent=er.toFixed(2);$('ofo').textContent=fo.toFixed(2);
 const pair=xn*xo,rec=wr*pair,add=ws*rec,kept=(1-er)*fo,newF=Math.max(-1,Math.min(1,kept+add));const f=v=>(v>=0?'+':'')+v.toFixed(3);
 $('depositSvg').innerHTML=`<text x="20" y="30" font-family="Bricolage Grotesque" font-size="15" font-weight="700" fill="var(--ink)">The adding part</text>
 <text x="20" y="62" font-family="JetBrains Mono" font-size="13" fill="var(--ink)">pairing        = x_new[i] × x_old[j] = ${xn.toFixed(2)} × ${xo.toFixed(2)} = <tspan fill="var(--teal)" font-weight="700">${f(pair)}</tspan></text>
 <text x="20" y="90" font-family="JetBrains Mono" font-size="13" fill="var(--ink)">recorded part  = write × pairing    = ${wr.toFixed(2)} × ${f(pair)} = <tspan fill="var(--amber)" font-weight="700">${f(rec)}</tspan></text>
 <text x="20" y="118" font-family="JetBrains Mono" font-size="13" fill="var(--ink)">amount added   = ws × recorded part = ${ws.toFixed(3)} × ${f(rec)} = <tspan fill="var(--amber)" font-weight="700">${f(add)}</tspan></text>
 <text x="20" y="160" font-family="Bricolage Grotesque" font-size="15" font-weight="700" fill="var(--ink)">The removing part</text>
 <text x="20" y="192" font-family="JetBrains Mono" font-size="13" fill="var(--ink)">what is left   = (1 − erase) × old F = ${(1-er).toFixed(2)} × ${f(fo)} = <tspan fill="var(--coral)" font-weight="700">${f(kept)}</tspan></text>
 <text x="20" y="234" font-family="Bricolage Grotesque" font-size="15" font-weight="700" fill="var(--ink)">Put together</text>
 <text x="20" y="266" font-family="JetBrains Mono" font-size="13" fill="var(--ink)">new F[i,j]     = ${f(kept)} + ${f(add)} = <tspan font-weight="700">${f(kept+add)}</tspan>${Math.abs(kept+add)>1?`  → clipped to ${f(newF)}`:''}</text>
 <text x="20" y="305" font-family="Literata" font-size="13" fill="var(--mute)">Notice the sizes: the pairing can be up to 1, the write gate cuts it to a share, and ws makes that share small enough that many ticks fit under the lid.</text>`;
 // eight ticks
 const [x,W,H]=ctx('cellTicks');x.clearRect(0,0,W,H);const p={l:44,r:20,t:30,b:40};const cw=W-p.l-p.r,ch=H-p.t-p.b;const vals=[fo];let v=fo;for(let t=1;t<=8;t++){v=Math.max(-1,Math.min(1,(1-er)*v+add));vals.push(v);}
 const X=t=>p.l+t/8*cw,Y=q=>p.t+ch/2-q*ch/2*0.9;frame(x,W,H,p);[1,0,-1].forEach(q=>txt(x,q>0?'+1':q,p.l-6,Y(q)+4,css('--mute'),'right'));txt(x,'tick →',W-p.r,H-6,css('--mute'),'right');x.setLineDash([6,5]);x.strokeStyle=css('--coral');[1,-1].forEach(q=>{x.beginPath();x.moveTo(p.l,Y(q));x.lineTo(W-p.r,Y(q));x.stroke();});x.setLineDash([]);x.strokeStyle=css('--line');x.beginPath();x.moveTo(p.l,Y(0));x.lineTo(W-p.r,Y(0));x.stroke();
 x.strokeStyle=css('--teal');x.lineWidth=3;x.beginPath();vals.forEach((q,t)=>t?x.lineTo(X(t),Y(q)):x.moveTo(X(t),Y(q)));x.stroke();vals.forEach((q,t)=>{x.fillStyle=css('--teal');x.beginPath();x.arc(X(t),Y(q),5,0,7);x.fill();txt(x,q.toFixed(2),X(t),Y(q)-12,css('--ink'),'center','12px "JetBrains Mono"');});
 txt(x,`each tick: keep ${((1-er)*100).toFixed(0)}% of the cell, then add ${f(add)}`,p.l+4,p.t-10,css('--mute'),'left','13px "Bricolage Grotesque"');}
['xn','xo','wr','wsv','er','fo'].forEach(id=>$(id).addEventListener('input',drawDeposit));

const CF={pos:[0,0],path:[[0,0]],F:[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],xo:[0,0,0,0],last:''};
function walk(d){const dirs={N:[0,1],E:[1,0],S:[0,-1],W:[-1,0]};const idx={N:0,E:1,S:2,W:3};const xn=[0,0,0,0];xn[idx[d]]=1;const ws=0.1,write=1;
 CF.F=CF.F.map((row,i)=>row.map((v,j)=>Math.min(1,v+ws*write*xn[i]*CF.xo[j])));CF.xo=xn;CF.pos=[CF.pos[0]+dirs[d][0],CF.pos[1]+dirs[d][1]];CF.path.push(CF.pos.slice());CF.last=d;drawCF();}
function drawCF(){const [x,W,H]=ctx('compassF');x.clearRect(0,0,W,H);const names=['N','E','S','W'];
 // left: path
 const L={x0:30,y0:30,w:300,h:H-60};txt(x,'the path (each tick = one step)',L.x0,20,css('--ink'),'left','13px "Bricolage Grotesque"');const cx=L.x0+L.w/2,cy=L.y0+L.h/2;const sc=12;x.strokeStyle=css('--line');x.strokeRect(L.x0,L.y0,L.w,L.h);
 x.strokeStyle=css('--teal');x.lineWidth=2.5;x.beginPath();CF.path.forEach((p,i)=>{const px=cx+p[0]*sc,py=cy-p[1]*sc;i?x.lineTo(px,py):x.moveTo(px,py);});x.stroke();x.fillStyle=css('--ink');x.beginPath();x.arc(cx,cy,5,0,7);x.fill();txt(x,'home',cx+8,cy+4,css('--mute'));const e=CF.pos;x.fillStyle=css('--coral');x.beginPath();x.arc(cx+e[0]*sc,cy-e[1]*sc,5,0,7);x.fill();
 // middle: F table
 const T={x0:380,y0:60};const u=70;txt(x,'F, four compass cells (receiver rows, sender columns)',T.x0,20,css('--ink'),'left','13px "Bricolage Grotesque"');names.forEach((n,k)=>{txt(x,'from '+n,T.x0+k*u+u/2,T.y0-8,css('--mute'),'center');txt(x,'to '+n,T.x0-8,T.y0+k*u+u/2+4,css('--mute'),'right');});
 CF.F.forEach((row,i)=>row.forEach((v,j)=>{x.fillStyle=`rgba(217,72,43,${0.1+Math.min(1,v)*0.85})`;x.fillRect(T.x0+j*u,T.y0+i*u,u-3,u-3);txt(x,v.toFixed(2),T.x0+j*u+u/2-1,T.y0+i*u+u/2+5,'#fff','center','13px "JetBrains Mono"');}));
 txt(x,`this tick: ${CF.last?'walked '+CF.last+', so the cell '+CF.last+'→'+CF.last+' gained 0.1':'no steps yet'}`,T.x0,T.y0+4*u+24,css('--mute'));
 // right: readout
 const R={x0:760};const nn=CF.F[0][0]-CF.F[2][2],ee=CF.F[1][1]-CF.F[3][3];txt(x,'what a reader gets by subtracting',R.x0,20,css('--ink'),'left','13px "Bricolage Grotesque"');
 txt(x,`N→N minus S→S = ${CF.F[0][0].toFixed(2)} − ${CF.F[2][2].toFixed(2)} = ${nn.toFixed(2)}  → net ${Math.round(nn/0.1)} ticks north`,R.x0,60,css('--ink'),'left','13px "JetBrains Mono"');
 txt(x,`E→E minus W→W = ${CF.F[1][1].toFixed(2)} − ${CF.F[3][3].toFixed(2)} = ${ee.toFixed(2)}  → net ${Math.round(ee/0.1)} ticks east`,R.x0,86,css('--ink'),'left','13px "JetBrains Mono"');
 txt(x,`true position: ${CF.pos[0]} east, ${CF.pos[1]} north`,R.x0,112,css('--mute'),'left','12px "JetBrains Mono"');
 const ax=R.x0+60,ay=300;x.strokeStyle=css('--line');x.beginPath();x.moveTo(ax-50,ay);x.lineTo(ax+50,ay);x.moveTo(ax,ay-50);x.lineTo(ax,ay+50);x.stroke();const L2=Math.hypot(ee,nn);if(L2>0){const ux=-ee/L2,uy=nn/L2;x.strokeStyle=css('--teal');x.lineWidth=4;x.beginPath();x.moveTo(ax,ay);x.lineTo(ax+ux*45,ay+uy*45);x.stroke();txt(x,'home is this way',ax+60,ay+4,css('--teal'),'left','13px "Bricolage Grotesque"');}else txt(x,'at home: nothing to point to',ax+60,ay+4,css('--mute'));
 txt(x,'N',ax,ay-56,css('--mute'),'center');txt(x,'E',ax+58,ay+4,css('--mute'),'left');}
[['wN','N'],['wE','E'],['wS','S'],['wW','W']].forEach(([id,d])=>$(id).addEventListener('click',()=>walk(d)));$('wReset').addEventListener('click',()=>{CF.pos=[0,0];CF.path=[[0,0]];CF.F=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];CF.xo=[0,0,0,0];CF.last='';drawCF();});

(function(){const c=$('gridPair');const xn=[0.8,-0.3,0.5,0.1,-0.7,0.0,0.6,-0.2],xo=[0.6,0.2,-0.4,0.7,0.1,-0.5,0.3,0.0];let hov=null;
 function draw(){const [x,W,H]=ctx('gridPair');x.clearRect(0,0,W,H);const u=54,x0=120,y0=80;txt(x,'x_old, a tick ago →',x0,30,css('--mute'));txt(x,'x_new, now ↓',20,y0-16,css('--mute'));
  xo.forEach((v,j)=>txt(x,(v>=0?'+':'')+v.toFixed(1),x0+j*u+u/2,y0-8,hov&&hov[1]===j?css('--amber'):css('--ink'),'center','13px "JetBrains Mono"'));xn.forEach((v,i)=>txt(x,(v>=0?'+':'')+v.toFixed(1),x0-10,y0+i*u+u/2+5,hov&&hov[0]===i?css('--amber'):css('--ink'),'right','13px "JetBrains Mono"'));
  xn.forEach((a,i)=>xo.forEach((b,j)=>{const v=a*b;const al=0.1+Math.min(1,Math.abs(v))*0.85;x.fillStyle=v>0?`rgba(217,72,43,${al})`:`rgba(47,91,234,${al})`;x.fillRect(x0+j*u,y0+i*u,u-2,u-2);if(hov&&(hov[0]===i||hov[1]===j)){x.strokeStyle=css('--amber');x.lineWidth=hov[0]===i&&hov[1]===j?4:1.5;x.strokeRect(x0+j*u+1,y0+i*u+1,u-4,u-4);}txt(x,(v>=0?'+':'')+v.toFixed(2),x0+j*u+u/2-1,y0+i*u+u/2+4,'#fff','center','10px "JetBrains Mono"');}));
  txt(x,'each cell = (its row number) × (its column number); then the whole grid is multiplied by the shared ws × write and added to F',x0,y0+8*u+30,css('--mute'));
  const u2=u;c.onmousemove=e=>{const r=c.getBoundingClientRect();const px=(e.clientX-r.left)/r.width*W,py=(e.clientY-r.top)/r.height*H;const j=Math.floor((px-x0)/u2),i=Math.floor((py-y0)/u2);if(i>=0&&i<8&&j>=0&&j<8){hov=[i,j];$('gridPairDetail').textContent=`cell F[${i+1}, ${j+1}]: x_new[${i+1}] × x_old[${j+1}] = ${xn[i].toFixed(1)} × ${xo[j].toFixed(1)} = ${(xn[i]*xo[j]).toFixed(2)}; with ws 0.074 and write 0.4 the amount added this tick is ${(0.074*0.4*xn[i]*xo[j]).toFixed(4)}`;draw();}};}
 draw();})();

(function(){const g=$('neurCells');const xn=[0.8,-0.3,0.5,0.1,-0.7,0.0,0.6,-0.2],xo=[0.6,0.2,-0.4,0.7,0.1,-0.5,0.3,0.0];let out='';const f=v=>(v>=0?'+':'')+v.toFixed(1);
 out+='<text x="20" y="24" font-family="Bricolage Grotesque" font-size="14" font-weight="700" fill="var(--ink)">the eight neurons (each has one activity now, and one from a tick ago)</text>';
 for(let k=0;k<8;k++){const cx=80+k*100;out+=`<circle cx="${cx}" cy="70" r="22" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="${cx}" y="75" text-anchor="middle" font-family="Bricolage Grotesque" font-size="13" fill="var(--ink)">${k+1}</text><text x="${cx}" y="108" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--teal)">now ${f(xn[k])}</text><text x="${cx}" y="124" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">ago ${f(xo[k])}</text>`;}
 // two cells
 const cell=(x,y,i,j,label)=>`<rect x="${x}" y="${y}" width="150" height="70" rx="8" fill="var(--panel)" stroke="var(--amber)" stroke-width="2"/><text x="${x+75}" y="${y+22}" text-anchor="middle" font-family="Bricolage Grotesque" font-size="13" font-weight="700" fill="var(--ink)">cell [${i+1}, ${j+1}]${label}</text><text x="${x+75}" y="${y+42}" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--ink)">now of ${i+1} × ago of ${j+1}</text><text x="${x+75}" y="${y+60}" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--ink)">${f(xn[i])} × ${f(xo[j])} = ${(xn[i]*xo[j]).toFixed(2)}</text>`;
 out+=cell(150,220,2,4,'');out+=`<path d="M280,108 C280,170 225,180 225,220" fill="none" stroke="var(--teal)" stroke-width="2" marker-end="url(#ar)"/><path d="M480,124 C480,180 235,180 235,220" fill="none" stroke="var(--mute)" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#ar)"/>`;
 out+=cell(560,220,2,2,' (diagonal)');out+=`<path d="M280,108 C280,150 620,160 625,220" fill="none" stroke="var(--teal)" stroke-width="2" marker-end="url(#ar)"/><path d="M280,124 C300,170 640,170 645,220" fill="none" stroke="var(--mute)" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#ar)"/>`;
 out+='<text x="450" y="315" text-anchor="middle" font-family="Literata" font-size="13" fill="var(--mute)">solid teal: the receiving neuron\'s activity now · dashed grey: the sending neuron\'s activity a tick ago</text>';
 g.innerHTML=out;})();
function all(){drawSig();drawCF();drawDeposit();drawWsA();drawWire();drawFB();drawGD();drawDelta();drawReset();drawStep();}
all();matchMedia('(prefers-color-scheme: dark)').addEventListener('change',all);new MutationObserver(all).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
</script>
'''
open('before-the-deep-dive.html','w').write(html.replace('__DATA__',data))
print('ok',len(html)//1024,'KB template', len(data)//1024,'KB data')
