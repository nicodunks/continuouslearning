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
</nav>
<main>
<div class="eyebrow">Level 3 · a study guide · ten questions</div>
<h1>Before the deep dive</h1>
<p class="lede">Your ten questions, answered in order, each with a drawn sketch you can push on and the real numbers next to it. Read it top to bottom once, then keep it open beside the Night Report.</p>
<p>Two conventions throughout. Boxes with a <span style="color:var(--blue)">dashed blue border</span> are drawn analogies: simplified on purpose, so a shape is easy to see. Boxes with a <span style="color:var(--teal)">teal label</span> are the real thing, computed from run files. Dotted words are <span class="term" title="like this">terms explained where they first appear</span>.</p>

<!-- ============ Q1 ============ -->
<h2 id="q1"><span class="q">QUESTION 1</span>What goes in, what comes out, and what is a knob</h2>
<p>Start with the machine itself. The network is 64 <span class="term" title="A neuron here is one number that gets recomputed every tick from the numbers feeding into it, then squashed to lie between −1 and +1">neurons</span>. Every tick (a tenth of a second of fly time) it receives four numbers, updates all 64 neurons, and emits three numbers. Click any part of the drawing.</p>
<div class="sketch">
 <div class="eyebrow">Drawn · the machine, click a part</div>
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
 <div class="eyebrow">Real · run 19, how much each input is listened to</div>
 <p style="font-size:15px">The four input wires each connect to all 64 neurons through W_in. Averaging the size of those 64 weights per input tells you how loudly each input is heard. All four are used, and speed is heard slightly loudest. The output biases (the resting position of each output before any neuron speaks) tell the story of the erase gate: it started at −5 and, after five shifts and training, sits at +1.86.</p>
 <canvas id="winBars" width="1600" height="300"></canvas>
</div>

<h3>So what is a knob?</h3>
<p>A knob is any number or choice we fix <em>before</em> a run starts and hold fixed during it. It is not something the network learns. The 8,708 slow weights are learned, so they are not knobs. The fast weights F are rewritten by the network itself, so they are not knobs either. Everything else is. Here is the whole board, grouped by what part of the experiment it lives in. Click a knob to see what it does and which runs turned it.</p>
<div class="panel" id="knobBoard"></div>
<div class="detail" id="knobDetail">Click a knob above.</div>

<!-- ============ Q2 ============ -->
<h2 id="q2"><span class="q">QUESTION 2</span>Why the erase-bias shift was "not a knob change but something else"</h2>
<p>Look at the last group on the board: <b>where the network starts</b>. Most knobs describe the world or the training. The bias shift is different in kind. It reaches inside the network and moves one of the 8,708 learned numbers by hand, before training resumes. It does not change what the network is asked to do or how it is scored. It changes the network's starting position on the hill it is about to climb.</p>
<div class="sketch">
 <div class="eyebrow">Drawn · a knob on the world versus a nudge to the climber</div>
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
<p>Why count it separately? Three reasons, and they matter for what you are allowed to conclude.</p>
<p><b>It is not a property of the task.</b> If someone reproduces our world and training, they will not rediscover the reset unless they also do the shift. So "the fly's reset emerges from this task" is not a claim we can make. What we can say is "the task rewards a reset once the gate can hear it."</p>
<p><b>It is a warm start with a hand on the scale.</b> Every shifted run began from the previous run's trained weights. The shift was applied to one number out of 8,708, the erase gate's bias, and then gradient descent took over. So the finding is real (the network chose to fire at food, not away from it), but the starting point was chosen by us.</p>
<p><b>It is repeatable, which makes it honest.</b> We did the same move five times (runs 7B, 10, 12, 14, 16) and wrote the prediction down each time. That turned a one-off intervention into a measured series: food-to-away ratios of 3, 7, 20, 33, 53. Question 3 shows why the move works at all.</p>

<!-- ============ Q3 ============ -->
<h2 id="q3"><span class="q">QUESTION 3</span>What "the sigmoid was parked at −5" means</h2>
<p>The erase gate is one output of the network: a raw number, call it z, that can be anything from very negative to very positive. But a gate has to be between 0 (erase nothing) and 1 (erase everything). The <span class="term" title="sigmoid: the S-shaped squashing function, 1 / (1 + e^−z). It turns any number into a value between 0 and 1">sigmoid</span> does that squashing. It is a <span class="term" title="A function whose output is not simply proportional to its input: doubling the input does not double the output. Every squashing function is nonlinear">nonlinearity</span>: its output is not proportional to its input. And that is the whole story of the deaf gate. Drag the bias.</p>
<div class="sketch">
 <div class="eyebrow">Drawn · the S curve, and how much a nudge moves it</div>
 <div class="controls"><div class="ctl"><label>bias (where the gate rests) <output id="oB">−5.0</output></label><input id="B" type="range" min="-8" max="4" step="0.1" value="-5"><small>The raw number z when no neuron is saying anything. Training moves it; the shift moved it by hand.</small></div>
 <div class="ctl"><label>size of the nudge from training <output id="oG">1.0</output></label><input id="G" type="range" min="0.2" max="3" step="0.1" value="1"><small>How hard the gradient pushes on z. The same push moves the gate very differently depending on where it rests.</small></div></div>
 <canvas id="sig" width="1700" height="520"></canvas>
 <div class="row"><span class="eyebrow">the campaign's path</span><button class="btn" data-b="-5">start −5</button><button class="btn" data-b="-2.5">run 7B −2.5</button><button class="btn" data-b="-1">run 10 −1</button><button class="btn" data-b="0.5">run 12 +0.5</button><button class="btn" data-b="2">run 14 +2</button><button class="btn" data-b="3.5">run 16 +3.5</button><button class="btn" data-b="1.86">run 19 trained: +1.86</button></div>
 <div class="how"><b>How to read it.</b> The curve is the gate's output for every possible raw input. The dot is where the gate rests. The short bar under the dot is how far one training nudge moves the output: it is the nudge times the curve's <span class="term" title="slope: how steep the curve is at that point, which is exactly how much the output changes for a small change in the input">slope</span> there. At −5 the slope is 0.007, so a nudge of 1 moves the gate by seven thousandths. At 0 the slope is 0.25, thirty-five times more.</div>
</div>
<h3>How that played out for us</h3>
<p>We started the erase gate at −5 on purpose, the way people start the "forget gate" of an LSTM mostly closed: if the network erased freely from the first iteration, the tallies could never build up and nothing would be learned. That worked. The cost was that the gate sat on the flat part of the S, where <span class="term" title="gradient descent: the training method. Compute which direction each number should move to lower the loss, then move a small step that way">gradient descent</span> could barely move it. Runs 2, 5 and 7 pushed on the gate with penalties of 0.5 and 20 and got nothing, because every push was multiplied by 0.007 before it reached the bias.</p>
<p>The bias shift lifts the dot up the curve. At −2.5 the slope is 0.07, ten times louder; at 0 it is 0.25. Once there, the same gradients that had been ignored started to work: the network reduced erasing away from food (which costs distance) and increased it at food (which cleans the board for the next trip). Each later shift moved the rest position higher again, and each time training settled it a bit lower than where we put it, at a spot where erase at food is large and erase away is near 0.01. Run 19's trained bias is +1.86: the gate now rests at 0.87 open, and the neurons that read the food input push it down hard whenever the fly is not at food.</p>
<div class="panel real">
 <div class="eyebrow">Real · erase per tick at food versus away, every run</div>
 <canvas id="eraseRuns" width="1700" height="520"></canvas>
 <div class="how"><b>How to read it.</b> Each run is a pair of bars on a <span class="term" title="log scale: each step up the axis multiplies by ten instead of adding a fixed amount, so 0.001, 0.01, 0.1 and 1 are evenly spaced">log scale</span>: coral is erase per tick at food, grey is away from food. Before run 7B the two are equal or the food one is lower (a fade). From 7B on, the food bar climbs shift by shift while the away bar stays put near 0.01.</div>
</div>

<!-- ============ Q4 ============ -->
<h2 id="q4"><span class="q">QUESTION 4</span>What Peter's delta rule was</h2>
<p>Our rule writes the whole pattern every tick. Peter's note pointed out that this is a very old rule (Hebb, 1949: "fire together, wire together") and that the modern sequence-model world has moved to a cousin of it, the <b>delta rule</b>: write only the part you could not already predict. Here are both, with the words under the symbols.</p>
<div class="eq">Hebb (ours): F ← (1 − <span class="b">erase</span>)·F + ws·<span class="c">write</span>·<span class="a">x_new ⊗ x_old</span></div>
<p style="font-size:15px;margin-top:6px">Read: shrink the board a little (erase), then add the write strength times the write gate times <span class="term" title="outer product: a table with one row per neuron now and one column per neuron a tick ago; each cell is the product of those two activities. It records 'who was active after whom'">the table of who was active after whom</span>.</p>
<div class="eq">Delta (Peter's): pred = F·x_old;   F ← (1 − <span class="b">erase</span>)·F + ws·<span class="c">write</span>·<span class="a">(x_new − pred) ⊗ x_old</span></div>
<p style="font-size:15px;margin-top:6px">Read: first ask F what it expects the new activity to be, given the old. Then write only the difference between what happened and what F expected. Once F predicts well, the difference is zero and writing stops on its own.</p>
<div class="sketch">
 <div class="eyebrow">Drawn · one connection under each rule while the fly walks the same heading</div>
 <div class="controls"><div class="ctl"><label>ticks walking the same direction <output id="oN">60</output></label><input id="N" type="range" min="5" max="150" step="1" value="60"></div>
 <div class="ctl"><label>write strength <output id="oS">0.10</output></label><input id="S" type="range" min="0.02" max="0.4" step="0.01" value="0.1"></div></div>
 <canvas id="delta" width="1700" height="460"></canvas>
 <div class="legend"><span><i style="background:var(--teal)"></i>Hebb: keeps adding, hits the lid</span><span><i style="background:var(--blue)"></i>delta: writes the surprise, then settles</span><span><i style="background:var(--coral)"></i>the ±1 lid</span></div>
 <div class="how"><b>How to read it.</b> The fly holds one heading, so the same two neurons fire together tick after tick. Under Hebb the connection grows every tick: that is what a tally needs, count the steps. Under delta the connection grows only until it predicts the pattern, then flattens: that is what a memory of "what usually follows what" needs, but it is exactly wrong for counting. Twenty steps and sixty steps leave the same connection.</div>
</div>
<h3>Why it was a good idea and why it failed here</h3>
<p>Peter's argument was sound: Hebb has no natural stopping point, which is why F needs a lid and why the erase gate had to fight saturation. Delta self-limits, so the lid becomes unnecessary and the erase gate is freed to do only one job, forgetting the last trip. Written down before running: delta should keep a wider F-versus-no-F gap and find the reset sooner.</p>
<p>What happened: run 15 (cold start, rule swapped, nothing else changed) never formed a memory at all; the F-versus-no-F gap stayed at zero for 800 iterations and the write strength never moved. Run 18 (warm start from run 14's working Hebb tally) lost its memory within 100 iterations of the rule swap. The drawing shows why. This task is a counter. A rule that stops writing when it can predict the input stops counting exactly when the count matters. The negative result is clean and it is in both forms, but it is about this task, not about the delta rule in general: on a "what follows what" task the outcome would likely flip.</p>

<!-- ============ Q5 ============ -->
<h2 id="q5"><span class="q">QUESTION 5</span>Is comparing "F allowed" with "F held at zero" a fair test?</h2>
<p>Your instinct is right, and it is worth being precise about what the test does and does not show. There are two different comparisons in the campaign and they answer two different questions.</p>
<div class="sketch">
 <div class="eyebrow">Drawn · two kinds of comparison</div>
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
  <g transform="translate(20,215)"><rect x="0" y="0" width="860" height="60" rx="8" fill="var(--soft)"/><text x="16" y="24" font-family="Literata" font-size="14" fill="var(--ink)">Your worry applies to comparison 1: brain B was never trained to live without F, so of course it fails. That is the point of an</text><text x="16" y="44" font-family="Literata" font-size="14" fill="var(--ink)"><tspan class="term">ablation</tspan>: remove a part and see what breaks. It locates the memory. It does not rank two designs. Comparison 2 does that, and it has its own caveats.</text></g>
 </svg>
</div>
<p><b>So how should you think about A versus B?</b> As a locator, not a contest. When A homes and B walks randomly, we learn that the thing A uses to home lives in F and not in the neurons' activity. That is a real fact about the trained brain, and it is the fact the roadmap called "memory in the synapses." It would be unfair only if we said "so fast weights beat activity," which the ablation cannot say.</p>
<p><b>The contest is the rival, run 20.</b> Same 64 neurons, same inputs, same training recipe as run 3, same seed, with the plastic part switched off before training. It never learned to home even at 10 seconds. That is evidence that, for this network and this recipe, an activity-only memory did not form. But a fair skeptic still gets three objections, and they are all right:</p>
<p>One recipe and one seed is a single sample. The learning rate and the initial weights were tuned over twenty runs for the fast-weight version and zero runs for the rival. And 64 tanh neurons with all-to-all connections is a design where activity memories are hard to train by gradient descent anyway (the vanishing-gradient problem; LSTMs exist because of it), so the rival was fighting with one hand tied. A fair level 4 would give the rival several learning rates, a longer first stage, and ideally an LSTM-style cell that is built to hold activity. Until that is done, the honest sentence is: "the memory we trained lives in F, and a matched activity-only attempt did not learn." Not: "fast weights win."</p>

<!-- ============ Q6 ============ -->
<h2 id="q6"><span class="q">QUESTION 6</span>Reset: why "yes", "fade" or "never" when the number is continuous</h2>
<p>You are right that nothing about the erase gate is binary. It is a number between 0 and 1 at every tick. The labels are a summary, and this is the exact rule the report uses, so you can disagree with it knowingly. Two averages are computed over the 200-trip test: erase per tick while standing at food, and erase per tick everywhere else.</p>
<div class="eq"><span class="b">reset</span> if (erase at food > 0.30) and (erase at food > 5 × erase away)<br><span class="c">fade</span> otherwise, if erase away > 0.003<br><span class="d">never erases</span> otherwise</div>
<p style="font-size:15px">In words: "reset" needs the gate to open at least 30% on the average food tick <em>and</em> to prefer food over elsewhere by at least five to one. "Fade" means a small constant erase that is not food-selective, the thing gradient descent finds when left alone. "Never" means the gate is shut everywhere, which is what happened when a penalty was applied before any memory existed.</p>
<div class="panel real">
 <div class="eyebrow">Real · every run placed on the two numbers, with the rule drawn on</div>
 <canvas id="resetMap" width="1700" height="640"></canvas>
 <div class="how"><b>How to read it.</b> Across: erase away from food. Up: erase at food. Both on log scales. The diagonal is "equal at food and away"; anything on or below it is a fade or worse. The shaded corner is the rule's "reset" region. Watch the shifted runs (7B, 10, 12, 14, 16, 19) climb straight up along a nearly fixed away-value of about 0.01: the network sharpened the preference without ever changing how much it fades between food visits. You can move the thresholds with the sliders to see how sensitive the labels are.</div>
 <div class="controls"><div class="ctl"><label>at-food threshold <output id="oT1">0.30</output></label><input id="T1" type="range" min="0.05" max="0.6" step="0.01" value="0.3"></div><div class="ctl"><label>preference ratio <output id="oT2">5</output></label><input id="T2" type="range" min="1.5" max="30" step="0.5" value="5"></div></div>
</div>

<!-- ============ Q7 ============ -->
<h2 id="q7"><span class="q">QUESTION 7</span>Every run in order: why that knob, what I predicted, what happened</h2>
<p>This is questions 2 and 7 from your list in one place. Step through the runs. Each card has four parts: the situation I was looking at, the one knob I chose and why that one, the prediction written before the run started, and the finding with a verdict. The chart above the cards is the 30-second score for the run on the card and its ancestors, so you can see the line it belongs to.</p>
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
 <div class="eyebrow">Drawn · what a compass cell is</div>
 <p style="font-size:15px;margin-top:6px">Turn the fly through all sixteen directions and record one neuron's activity at each. A compass cell fires for one preferred direction and goes quiet opposite it (left). A cell that is not a compass cell fires about the same everywhere (right). The <span class="term" title="tuning curve: a neuron's average activity plotted against some feature of the world, here the heading; 'tuned' means the curve has a clear peak">tuning curve</span> is the shape; a cell counts as tuned if the peak stands more than 0.25 above the trough.</p>
 <svg viewBox="0 0 900 220"><g transform="translate(60,20)"><text x="120" y="0" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" font-weight="700" fill="var(--ink)">tuned to north-east</text><polyline points="0,150 20,120 40,80 60,40 80,20 100,30 120,70 140,110 160,140 180,155 200,160 220,158 240,150" fill="none" stroke="var(--blue)" stroke-width="3"/><line x1="0" y1="170" x2="240" y2="170" stroke="var(--line)"/><text x="0" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">E</text><text x="60" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">N</text><text x="120" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">W</text><text x="180" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">S</text><text x="240" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">E</text></g>
 <g transform="translate(520,20)"><text x="120" y="0" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" font-weight="700" fill="var(--ink)">not tuned</text><polyline points="0,100 20,96 40,104 60,99 80,101 100,97 120,103 140,100 160,98 180,102 200,99 220,101 240,100" fill="none" stroke="var(--mute)" stroke-width="3"/><line x1="0" y1="170" x2="240" y2="170" stroke="var(--line)"/><text x="0" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">E</text><text x="60" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">N</text><text x="120" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">W</text><text x="180" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">S</text><text x="240" y="188" font-family="JetBrains Mono" font-size="10" fill="var(--mute)">E</text></g></svg>
</div>
<div class="panel real">
 <div class="eyebrow">Real · all 64 tuning curves of run 19, strongest first</div>
 <div class="grid16" id="curves"></div>
 <div class="how"><b>How to read it.</b> One small chart per neuron, headings east, north, west, south, east across the bottom, activity up. Teal curves are the 32 that pass the 0.25 test; grey are the rest. The number is the peak-to-trough height. Notice that the tuned cells are not all copies: their peaks fall in different places. The histogram below counts them by preferred direction. A perfect compass would spread evenly around the circle; ours clusters (six cells prefer north-north-east, six prefer west-south-west, and two of the sixteen bins are empty), which is one of the ways it is still cruder than the fly.</div>
 <canvas id="prefHist" width="1700" height="260"></canvas>
</div>

<h3>Motif 2: the write gate reads speed</h3>
<div class="sketch">
 <div class="eyebrow">Drawn · the wiring that makes a gate follow one input</div>
 <p style="font-size:15px;margin-top:6px">A gate is a sigmoid of a weighted sum of all 64 neurons. For it to follow speed, some neurons must (a) listen to the speed wire strongly through W_in and (b) feed the gate strongly through W_out, with the two signs agreeing. If a neuron has a negative speed weight and a negative gate weight, faster still means more writing: two negatives multiply to a positive. The sketch shows the path; the real chart below checks whether run 19 built it.</p>
 <svg viewBox="0 0 900 150"><rect x="20" y="50" width="120" height="44" rx="8" fill="var(--panel)" stroke="var(--blue)"/><text x="80" y="77" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">speed</text><line x1="140" y1="72" x2="300" y2="72" stroke="var(--amber)" stroke-width="3" marker-end="url(#ar)"/><text x="220" y="60" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">W_in[n, speed]</text><circle cx="340" cy="72" r="30" fill="var(--panel)" stroke="var(--ink)" stroke-width="2"/><text x="340" y="77" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">neuron n</text><line x1="370" y1="72" x2="560" y2="72" stroke="var(--amber)" stroke-width="3" marker-end="url(#ar)"/><text x="465" y="60" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="var(--mute)">W_out[write, n]</text><rect x="565" y="50" width="150" height="44" rx="8" fill="var(--panel)" stroke="var(--amber)" stroke-width="2"/><text x="640" y="77" text-anchor="middle" font-family="Bricolage Grotesque" font-size="14" fill="var(--ink)">write gate</text><text x="740" y="77" font-family="Literata" font-size="13" fill="var(--mute)">product of the two = effect</text></svg>
</div>
<div class="panel real">
 <div class="eyebrow">Real · the eight neurons that drive each gate hardest, and what they listen to</div>
 <div class="two"><div><canvas id="writeWiring" width="820" height="420"></canvas></div><div><canvas id="eraseWiring" width="820" height="420"></canvas></div></div>
 <div class="how"><b>How to read it.</b> Left, the write gate: for each of its eight strongest driver neurons, the pale bar is the neuron's weight from the speed wire and the dark bar is its weight into the gate. The dot is their product: positive means "faster, write more." Seven of eight products are positive. Right, the same for the erase gate against the food wire: positive means "at food, erase more." Five of eight are positive and the strongest driver, neuron 40, is strongly positive. This is the wiring behind the numbers in the leaderboard: write-versus-speed correlation +0.69, erase at food 0.38 versus 0.008 away.</div>
</div>

<h3>Motif 3: the wipe at food, seen in F itself</h3>
<div class="panel real">
 <div class="eyebrow">Real · the twelve strongest fast weights across the two-trip test</div>
 <canvas id="Ftrace" width="1700" height="440"></canvas>
 <div class="how"><b>How to read it.</b> Each teal line is one fast weight over the full 90-second test (two trips). Shaded columns are food stands. The lines build during a wander, hold on the way home, and drop at the food stand: that drop is the erase gate firing at 0.38 per tick for forty ticks. The board is cleared for the next trip. Compare the drawn version of this in the Night Report's run cards.</div>
</div>

<h3>What the wiring between neurons looks like, sorted the way Peter sorts it</h3>
<p>Peter's paper (question 10) has a signature analysis: order the compass cells by preferred direction, then plot the connection strength from each to each. In a ring attractor, cells with similar preferred directions excite each other and cells with opposite directions inhibit each other, so the plot shows a bright diagonal and dark far corners. Below is that plot for run 19, for both the slow table W and the allowance table A.</p>
<div class="panel real">
 <div class="eyebrow">Real · connections between the 32 compass cells, sorted by preferred direction</div>
 <div class="two"><div><canvas id="Wsorted" width="820" height="820"></canvas></div><div><canvas id="Asorted" width="820" height="820"></canvas></div></div>
 <canvas id="profile" width="1700" height="360"></canvas>
 <div class="how"><b>How to read it.</b> Rows are receiving cells, columns are sending cells, both in order of preferred direction from east round to east. Red is a positive weight, blue negative. The bottom chart averages the weights by how far apart the two cells' preferred directions are: a ring would show a positive hump at 0° and a negative dip at ±180°. Run 19's W shows only a faint version of this (mean weight ranges from −0.04 to +0.05), and A shows none. So our compass cells are real as tuning curves but are not wired as a ring. They do not need to be: the heading comes in on the input wires every tick, so the network never has to hold a heading by itself the way Peter's network did. This is the clearest difference between the two projects, and it is a difference in the task, not a failure.</div>
</div>
<p class="caveat">Honest limits of this analysis. Preferred direction is read from a 16-bin tuning curve, so it is coarse. The sorted plots use 32 cells, which is few; Peter's used 33 ring cells out of 100 but with much sharper tuning. And "no ring" is a statement about the slow weights; the effective connection at any moment is W + A·F, and F changes every tick.</p>

<!-- ============ Q9 ============ -->
<h2 id="q9"><span class="q">QUESTION 9</span>Backpropamine, and how our network compares</h2>
<p><b>Backpropamine</b> is a 2019 paper by Miconi, Rawal, Clune and Stanley. The name is a pun on backpropagation and dopamine. The idea in one sentence: let a network have connections that change while it runs, in a Hebbian way, and let the network itself produce a signal (like dopamine in the brain) that says how much those changes should happen right now; then train everything by ordinary gradient descent. Toggle the rules to see the family tree our network sits in.</p>
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
<tr><td>the point of the paper</td><td>neuromodulation helps on RL and language tasks</td><td>does a fly-like circuit emerge, and where does the memory live</td></tr>
</tbody></table>
<p>So FlyNet is "simple Backpropamine plus an erase gate," applied to a navigation task and then dissected. Nothing about our learning rule is new; what is ours is the question (do the three fly motifs appear), the world, and the analysis. Peter's note says the same thing in the field's words. It also places delta and the newer sequence models (Gated DeltaNet, Titans) as the next rungs of the same ladder.</p>

<!-- ============ Q10 ============ -->
<h2 id="q10"><span class="q">QUESTION 10</span>Peter's paper, and what it teaches us to do next</h2>
<p><i>Emergence of functional and structural properties of the head direction system by optimization of recurrent neural networks</i>, Cueva, Wang, Chin and Wei, ICLR 2020. It is the template for the kind of analysis you are about to do on our runs, so it is worth understanding what they did step by step.</p>
<div class="sketch">
 <div class="eyebrow">Drawn · their task and what emerged</div>
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
<p>One more parallel that is worth saying out loud. Their claim was not "this network is the fly." It was that the fly's design is what optimisation finds when the task is this task, and that anatomy can be predicted from function. Our version of that claim, smaller and with its caveats attached in question 2, is: given a homing task with a place to reset, gradient descent will build a compass, a speed-weighted tally and a wipe, provided the gate that does the wiping can hear its gradients.</p>
<p class="caveat">Two reading notes on the paper text you sent. The arXiv version has a draft paragraph left in ("Now mention something about the P-EN2 neurons here"), which is a nice reminder that papers are written by people. And the numbers in its figure titles (33 ring, 29 and 26 shifters, error 0.57%) are from one trained network; they trained many and report the pattern was consistent.</p>
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
win:'<b>W_in, 4 × 64 weights plus 64 biases.</b> Each input wire connects to every neuron with its own strength. Trained, then frozen: part of the slow weights.',
net:'<b>The 64 neurons.</b> Every tick each neuron adds up its inputs (the four wires through W_in, and all 64 neurons a tick ago through the effective connections W + A·F), then squashes the sum with tanh so it lies between −1 and +1. Activity is wiped to zero at the start of every trip, so nothing can be carried between trips in the neurons themselves.',
W:'<b>W, the slow table, 64 × 64.</b> The permanent strength of every connection from neuron j to neuron i. Trained by gradient descent across thousands of episodes, then frozen. This is the rulebook.',
A:'<b>A, the allowance table, 64 × 64.</b> How much each connection is allowed to be changed by the fast table. Effective strength = W + A·F. If A is zero on a connection, that connection can never learn during a trip. Trained, then frozen. Set to zero and frozen for the rival (run 20).',
F:'<b>F, the fast table, 64 × 64.</b> Starts at zero every episode. Rewritten every tick by the rule, with the write and erase gates deciding how much. Never trained directly; the network learns a rule for changing it. This is where the memory of the trip lives, and it is the only thing that survives from one trip to the next inside an episode.',
ws:'<b>ws, the write strength.</b> One trained number that scales every write into F. Level 1 had this as a dial; here it is learned. Run 19 settled it at 0.074.',
wout:'<b>W_out, 64 × 3 weights plus 3 biases.</b> Reads all 64 neurons into the three outputs. The three biases are the outputs\' resting positions: run 19 has turn −0.14, write +0.96, erase +1.86.',
out0:'<b>Turn.</b> How much to rotate this tick, left or right, capped smoothly at 8 radians per second. It is the only output that moves the fly.',
out1:'<b>Write gate.</b> A sigmoid, 0 to 1. Multiplies the write into F this tick. If it follows speed, the tally counts distance rather than time.',
out2:'<b>Erase gate.</b> A sigmoid, 0 to 1. The fraction of F that is wiped this tick. Near 0.01 it is a slow fade; near 1 at food and near 0 elsewhere it is the fly\'s reset.'};
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
const WHY={run1:'The plan\'s first run. Nothing to look at yet, so no knob: establish the baseline and see what gradient descent does on its own.',
run2:'Run 1 found a slow fade instead of a reset. The simplest lever on erasing is the penalty for erasing away from food. Multiply it by ten.',
run3:'Run 2 showed a penalty can shut the gate rather than aim it. The other way to teach a reset is more evidence: more ticks at the food. Stand for 2 s instead of 0.5 s.',
run4:'Run 3 homed at 20 s but still faded. If the board carries five trips instead of two, leftovers hurt more, so the erase gate has a stronger reason to fire at food. Warm start from run 3\'s best.',
run5:'Run 2\'s penalty had been tried cold and died. Try it warm, on a network that already homes, so the penalty cannot kill the memory before it forms.',
run6:'Two runs on the erase gate had done nothing. Stop and earn the 30-second stage, since 30 s scores were being reported on networks that never trained there. Hygiene: cosine decay, after run 5\'s collapse.',
run6B:'Run 6 collapsed at iteration 500 even with decay. Same experiment, a third of the step size.',
run7:'0.5 was a rounding error next to a loss of 2. Make the penalty real: 20. If the gate still does not move, the problem is not the price.',
run7B:'Run 7 gave the diagnosis: the sigmoid at −5 has slope 0.007. Test it directly: lift the bias by 2.5 and keep everything else, including the penalty.',
run8:'7B made the gate lean toward food (ratio 3). Before pushing harder, check whether time alone sharpens it: continue with nothing changed.',
run8B:'Run 8 stalled at ratio 1.5 to 3. Now that the gate can hear, retry the run 3 idea: more food ticks (4 s) should mean more gradient for erasing at food.',
run9:'Everything so far was warm starts. The decisive version: a cold start whose gate can hear from iteration 1. Does the reset emerge on its own?',
run9B:'Run 9\'s penalty of 20 shut the gate before any memory existed. Cut it to 2 so the gate stays audible while the tally forms.',
run10:'The first shift lifted the ratio to 3, then training settled. Do the same move again (+1.5) and see if the preference ratchets or returns to 3.',
run11:'Every finding is from seed 0. Replicate run 3\'s recipe from a different random start to see if compass cells and speed-following writing are robust.',
run11B:'The stop rule ended run 11 across a promotion, which was unfair. Continue it with the rule suspended.',
run12:'Ratio went 3 then 7. A third shift tests whether the ratchet keeps going.',
run13:'A different lever entirely: a world where time and distance disagree (slow half, fast half). If writing must follow speed to home, the write gate should sharpen.',
run14:'Ratio 3, 7, 20. A fourth shift: does it reach a full wipe?',
run15:'Peter\'s note proposed the delta rule. Cold start, run 3\'s recipe, only the rule changed. Prediction on record from Peter.',
run16:'Ratio 3, 7, 20, 33 and peaks near 0.9. Fifth shift: is the wipe complete?',
run17:'The best score line (run 13) had only ever trained at 3e-4. Polish at a tenth of that, nothing else changed.',
run18:'Run 15 failed cold. The fair second form: switch the rule on a working tally (run 14) so the rule is the only difference.',
run19:'Two lines existed: the best score (legs world, run 13) and the best reset (run 14). Apply the legs world to the reset network to see if the ingredients stack.',
run20:'The level 4 comparison the plan was built for: the same network with fast weights disabled, trained with run 3\'s recipe.'};
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
 ['<div class="eq">x_new = tanh( <span class="d">W</span> · x_old + input )</div><p style="font-size:15px">A plain recurrent network. Every connection has one strength, W, that never changes while the network runs. Memory can only live in the neurons\' activity, echoing round the loop. This is the rival, run 20, in spirit.</p>'],
 ['<div class="eq">x_new = tanh( (<span class="d">W</span> + <span class="a">α</span>·Hebb) · x_old + input )<br>Hebb ← clip( Hebb + <span class="c">η</span>·x_old ⊗ x_new )</div><p style="font-size:15px">Miconi, Stanley and Clune, 2018. Each connection gets a plastic part, Hebb, that grows with the product of the two neurons\' activities and is clipped to ±1. Two new trained numbers: α per connection (how much the plastic part counts) and η (how fast it writes). Both are learned by backprop across episodes; Hebb itself is not learned, it happens.</p>'],
 ['<div class="eq">Hebb ← clip( Hebb + <span class="c">M(t)</span>·x_old ⊗ x_new )</div><p style="font-size:15px">Backpropamine, simple form. The fixed η becomes M(t), a number the network outputs every tick. Now the network decides when to be plastic. M(t) can be negative, which un-writes. This is the dopamine analogy: a global "learn now" signal under the brain\'s own control.</p>'],
 ['<div class="eq">E ← (1 − <span class="c">η</span>)·E + <span class="c">η</span>·x_old ⊗ x_new<br>Hebb ← clip( Hebb + <span class="c">M(t)</span>·E )</div><p style="font-size:15px">Backpropamine, retroactive form. Activity first leaves a fading trace E (an <span class="term" title="eligibility trace: a short-lived record of which connections were recently active, waiting to be confirmed or discarded">eligibility trace</span>). Only when M(t) fires does the trace become a real change. So a reward signal can reach back about a second and stamp in what led to it, which is what dopamine does in real synapses.</p>'],
 ['<div class="eq">x_new = tanh( (<span class="d">W</span> + <span class="a">A</span>·F) · x_old + input )<br>F ← clamp( (1 − <span class="b">erase(t)</span>)·F + ws·<span class="c">write(t)</span>·x_new ⊗ x_old )</div><p style="font-size:15px">FlyNet. Take the simple Backpropamine rule, call α "A" and Hebb "F", make M(t) = ws × write(t), and add a second self-produced gate, erase(t), that multiplies the old F. That erase gate is the whole difference, and it exists because the fly needs to wipe its tally at food. Everything else is inherited.</p>']];
document.querySelectorAll('.rule').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.rule').forEach(q=>q.classList.remove('on'));b.classList.add('on');$('ruleBox').innerHTML=RULES[+b.dataset.r][0];}));$('ruleBox').innerHTML=RULES[0][0];
function all(){drawSig();drawDelta();drawReset();drawStep();}
all();matchMedia('(prefers-color-scheme: dark)').addEventListener('change',all);new MutationObserver(all).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
</script>
'''
open('before-the-deep-dive.html','w').write(html.replace('__DATA__',data))
print('ok',len(html)//1024,'KB template', len(data)//1024,'KB data')
