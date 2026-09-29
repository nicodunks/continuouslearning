import './style.css';
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';

const $=s=>document.querySelector(s), clamp=THREE.MathUtils.clamp, lerp=THREE.MathUtils.lerp;
const smooth=(a,b,t)=>{const x=clamp((t-a)/(b-a),0,1);return x*x*(3-2*x)};
const V=(x=0,y=0,z=0)=>new THREE.Vector3(x,y,z);
const colors={gold:0xf0c66a,coral:0xff866c,blue:0x7dd5f1,violet:0xbba0ff,ivory:0xe6e8d9};
await Promise.all([document.fonts.load('600 120px "Barlow Condensed"'),document.fonts.load('400 22px "IBM Plex Mono"')]);
const canvas=$('#world');
let renderer;
try { renderer=new THREE.WebGLRenderer({canvas,antialias:true,alpha:false,preserveDrawingBuffer:true}); }
catch(e){$('#error').hidden=false;$('#error').textContent='This scene needs WebGL. Open it in a browser with hardware acceleration enabled.';throw e;}
renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.25;
const scene=new THREE.Scene();scene.background=new THREE.Color('#091722');scene.fog=new THREE.FogExp2('#091722',.021);
const camera=new THREE.PerspectiveCamera(38,1,.1,1500);
const composer=new EffectComposer(renderer);composer.addPass(new RenderPass(scene,camera));const bloom=new UnrealBloomPass(new THREE.Vector2(1,1),.3,.65,.9);composer.addPass(bloom);composer.addPass(new OutputPass());
scene.add(new THREE.HemisphereLight(0xc0e9ff,0x283747,1.5));
const key=new THREE.DirectionalLight(0xffe7b5,3.1);key.position.set(3,10,4);key.castShadow=true;key.shadow.mapSize.set(2048,2048);Object.assign(key.shadow.camera,{left:-15,right:15,top:15,bottom:-15});key.shadow.bias=-.0003;scene.add(key);
const rim=new THREE.DirectionalLight(0x73bddd,2.3);rim.position.set(-6,4,-8);scene.add(rim);
const floor=new THREE.Mesh(new THREE.PlaneGeometry(5000,5000),new THREE.MeshStandardMaterial({color:0x040b12,roughness:.82,metalness:.2}));floor.rotation.x=-Math.PI/2;floor.position.y=-.12;floor.receiveShadow=true;scene.add(floor);
const grid=new THREE.GridHelper(400,200,0x284353,0x203746);grid.position.y=-.1;grid.material.transparent=true;grid.material.opacity=.28;scene.add(grid);
const stage=new THREE.Group();stage.position.x=0;scene.add(stage);
function material(color,opts={}){return new THREE.MeshStandardMaterial({color,roughness:.46,metalness:.2,...opts})}
function ellipsoid(parent,pos,scale,mat,segments=32){let m=new THREE.Mesh(new THREE.SphereGeometry(1,segments,24),mat);m.position.copy(pos);m.scale.copy(scale);m.castShadow=true;parent.add(m);return m;}
function tube(parent,pts,color,r=.015,opacity=1){const curve=new THREE.CatmullRomCurve3(pts);const geo=new THREE.TubeGeometry(curve,Math.max(24,pts.length*12),r,6,false);const mat=new THREE.MeshBasicMaterial({color,transparent:true,opacity});const m=new THREE.Mesh(geo,mat);m.userData.count=geo.index.count;parent.add(m);return m;}
function reveal(mesh,p){mesh.visible=p>0;mesh.geometry.setDrawRange(0,Math.floor(mesh.userData.count*clamp(p,0,1)/3)*3)}
function label(text,width,color='#e6e8d9',size=120,sub=''){
 const c=document.createElement('canvas'),ctx=c.getContext('2d');
 const font=`600 ${size}px "Barlow Condensed", sans-serif`;
 ctx.font=font;const tw=ctx.measureText(text).width;ctx.font='24px "IBM Plex Mono", monospace';const sw=sub?ctx.measureText(sub).width:0;
 c.width=Math.ceil(Math.max(tw,sw)+48);c.height=Math.ceil(size*1.25+(sub?62:0));
 ctx.fillStyle=color;ctx.font=font;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(text,c.width/2,size*.64);
 if(sub){ctx.font='24px "IBM Plex Mono", monospace';ctx.fillStyle='#99acb6';ctx.fillText(sub,c.width/2,size*1.25+29)}
 const tex=new THREE.CanvasTexture(c);tex.colorSpace=THREE.SRGBColorSpace;
 const mat=new THREE.SpriteMaterial({map:tex,transparent:true,depthTest:false,depthWrite:false});
 const sprite=new THREE.Sprite(mat);sprite.scale.set(width,width*c.height/c.width,1);sprite.userData.baseScale=sprite.scale.clone();sprite.renderOrder=10;return sprite;
}
function worldLabel(text,pos,width,color,size=120,sub=''){const s=label(text,width,color,size,sub);s.position.copy(pos);stage.add(s);return s;}
function arrow(color){let g=new THREE.Group();let shaft=new THREE.Mesh(new THREE.CylinderGeometry(.025,.025,1,10),new THREE.MeshBasicMaterial({color,transparent:true}));let head=new THREE.Mesh(new THREE.ConeGeometry(.14,.36,20),new THREE.MeshBasicMaterial({color,transparent:true}));g.add(shaft,head);g.userData={shaft,head};stage.add(g);return g;}
function setArrow(g,a,b,p=1){const d=b.clone().sub(a),l=d.length()*p;g.visible=l>.01;if(!g.visible)return;g.position.copy(a);g.quaternion.setFromUnitVectors(V(0,1,0),d.normalize());g.userData.shaft.scale.y=Math.max(.01,l-.2);g.userData.shaft.position.y=(l-.2)/2;g.userData.head.position.y=l-.14;}

// Sculpted insect: segmented abdomen, thorax, faceted compound eyes, six articulated legs,
// layered translucent wings with modeled veins, antennae and thoracic bristles.
const fly=new THREE.Group();fly.name="hero-fly";stage.add(fly);
const skinCanvas=document.createElement('canvas');skinCanvas.width=skinCanvas.height=512;const skinCtx=skinCanvas.getContext('2d');
let randomSeed=7823;function rand(){randomSeed=(randomSeed*1664525+1013904223)>>>0;return randomSeed/4294967296}
const skinData=skinCtx.createImageData(512,512);for(let i=0;i<skinData.data.length;i+=4){let v=110+Math.floor(rand()*100);skinData.data.set([v,v,v,255],i)}skinCtx.putImageData(skinData,0,0);const skinBump=new THREE.CanvasTexture(skinCanvas);skinBump.wrapS=skinBump.wrapT=THREE.RepeatWrapping;skinBump.repeat.set(3,2);
const shell=material(0xbcc0a7,{metalness:.18,roughness:.63});const dark=material(0x273b3a,{roughness:.65});const headMat=material(0x6e7962,{roughness:.55});shell.bumpMap=skinBump;shell.bumpScale=.028;headMat.bumpMap=skinBump;headMat.bumpScale=.012;
ellipsoid(fly,V(-.64,-.01,0),V(.79,.33,.37),shell);ellipsoid(fly,V(0,.08,0),V(.49,.41,.4),shell);ellipsoid(fly,V(.57,.12,0),V(.34,.3,.36),headMat);
for(let i=0;i<6;i++){const x=-1.22+i*.21;const s=Math.sqrt(Math.max(.05,1-((x+.64)/.8)**2));const curve=[];for(let j=0;j<=60;j++){let a=j/60*Math.PI*2;curve.push(V(x,-.01+.335*s*Math.cos(a),.375*s*Math.sin(a)))}tube(fly,curve,0x45574e,.012,.85);}
for(const side of [-1,1]){
 const eye=ellipsoid(fly,V(.67,.14,side*.265),V(.25,.265,.155),material(0xa14232,{roughness:.28,metalness:.35}));
 const facets=new THREE.InstancedMesh(new THREE.CircleGeometry(.012,6),material(0x9c4935,{roughness:.42,metalness:.15,side:THREE.DoubleSide}),700);let dummy=new THREE.Object3D();for(let i=0;i<700;i++){let a=i*2.399963,y=1-2*(i+.5)/700,rr=Math.sqrt(1-y*y);const n=V(rr*Math.cos(a),y,rr*Math.sin(a));dummy.position.set(.67+.251*n.x,.14+.266*n.y,side*.265+.156*n.z);dummy.quaternion.setFromUnitVectors(V(0,0,1),V(n.x/.25,n.y/.265,n.z/.155).normalize());dummy.updateMatrix();facets.setMatrixAt(i,dummy.matrix)}fly.add(facets);
 tube(fly,[V(.79,.21,side*.1),V(.97,.28,side*.19),V(1.08,.37,side*.23)],0x8c9f86,.018);ellipsoid(fly,V(1.075,.37,side*.23),V(.04,.04,.04),dark,12);
 for(let i=0;i<3;i++){const x=.28-i*.37;const points=[V(x,-.14,side*.24),V(x+.13,-.39,side*.55),V(x+.38-(i*.24),-.7,side*.65),V(x+.51-(i*.3),-.78,side*.72)];tube(fly,points,0x829386,.026);for(let k=1;k<3;k++)ellipsoid(fly,points[k],V(.038,.038,.038),dark,10);}
}
for(let i=0;i<38;i++){const a=i*2.3999,y=.2+((i*13)%29)/80;const z=Math.sin(a)*.33,x=Math.cos(a)*.37;const p=V(x,y,z);tube(fly,[p,p.clone().add(V(x*.25,.09,z*.35))],0xa6b8a0,.005,.6);}
const wings=[];
for(const side of [-1,1]){
 const pivot=new THREE.Group();pivot.position.set(-.05,.3,side*.16);fly.add(pivot);wings.push(pivot);
 const shape=new THREE.Shape();shape.moveTo(0,0);shape.bezierCurveTo(.45,.55,.28,1.68,-.37,1.95);shape.bezierCurveTo(-.98,2.04,-1.37,1.5,-.91,.76);shape.bezierCurveTo(-.6,.27,-.23,.05,0,0);
 const wm=new THREE.MeshPhysicalMaterial({color:0xc9e6e3,transparent:true,opacity:.21,metalness:.15,roughness:.25,side:THREE.DoubleSide,depthWrite:false,iridescence:1,iridescenceIOR:1.3});
 const mesh=new THREE.Mesh(new THREE.ShapeGeometry(shape,32),wm);mesh.rotation.x=side*Math.PI/2;pivot.add(mesh);
 const outline=shape.getPoints(60).map(p=>V(p.x,0,side*p.y));tube(pivot,outline,0xb4d1cc,.009,.65);
 for(let j=0;j<6;j++){let z=.85+j*.19;tube(pivot,[V(0,0,0),V(-.12-j*.08,0,side*.45),V(-.3-j*.1,0,side*z),V(-.3-j*.105,0,side*(z+.14))],0x8faea9,.006,.65);}
 tube(pivot,[V(-.75,0,side*.79),V(-.3,0,side*.92),V(.17,0,side*1.03)],0x9cb6af,.006,.5);
}
// The sugar cube is geometry: rounded core, granular bump, and thousands of tiny crystals.
const home=V(-7,0,6), origin=V(-7,1.65,6);
const sugar=new THREE.Group();sugar.position.copy(home);sugar.rotation.y=.17;stage.add(sugar);
const sugarMat=new THREE.MeshStandardMaterial({color:0xf2ebd4,roughness:.95,bumpMap:skinBump,bumpScale:.022});
const cube=new THREE.Mesh(new RoundedBoxGeometry(1.25,1.25,1.25,4,.07),sugarMat);cube.position.y=.65;cube.castShadow=true;cube.receiveShadow=true;sugar.add(cube);
const grains=new THREE.InstancedMesh(new THREE.IcosahedronGeometry(.017,0),material(0xf6eed9,{roughness:.55,metalness:.02}),2300);const grainDummy=new THREE.Object3D();
for(let i=0;i<2300;i++){const face=i%5;let a=(rand()-.5)*1.2,b=(rand()-.5)*1.2;grainDummy.position.set(face===0?.632:face===1?-.632:a,face===4?1.28:b+.65,face===2?.632:face===3?-.632:face===4?b:a);grainDummy.rotation.set(rand()*3,rand()*3,rand()*3);grainDummy.scale.setScalar(.5+rand());grainDummy.updateMatrix();grains.setMatrixAt(i,grainDummy.matrix)}sugar.add(grains);
for(let i=0;i<32;i++){let a=rand()*Math.PI*2,r=.8+rand();const g=new THREE.Mesh(new THREE.IcosahedronGeometry(.025+rand()*.022,0),sugarMat);g.position.set(Math.cos(a)*r,.02,Math.sin(a)*r);sugar.add(g)}
const beacon=new THREE.Mesh(new THREE.TorusGeometry(1.05,.009,6,100),new THREE.MeshBasicMaterial({color:colors.gold,transparent:true,opacity:.38}));beacon.rotation.x=Math.PI/2;beacon.position.y=.02;sugar.add(beacon);
const foodLabel=worldLabel('SUGAR / ORIGIN',home.clone().add(V(0,.15,1.8)),2.5,'#d9bc7c',66);
// A spatial trajectory with two broad banks: climb into the distance, cross, sweep back.
const route=new THREE.CatmullRomCurve3([origin,V(-6,3,1),V(-7,6,-7),V(-2,8,-13),V(7,7,-10),V(10,5,-3),V(6,4,4)],false,'centripetal');
const endpoint=route.getPoint(1);const displacement=endpoint.clone().sub(origin);
const flightBack=new THREE.CatmullRomCurve3([endpoint,V(8,4.7,6.5),V(4,4,10),V(-1,2.9,9),V(-5.5,2,7)],false,'centripetal');
const dots=[];const dotGeo=new THREE.SphereGeometry(.063,10,8);
for(let i=0;i<94;i++){const m=new THREE.Mesh(dotGeo,new THREE.MeshBasicMaterial({color:colors.gold,transparent:true,opacity:.7}));m.userData.progress=flightProgress(i/93*5);m.position.copy(route.getPointAt(m.userData.progress));stage.add(m);dots.push(m)}
const pulse=ellipsoid(stage,V(),V(.13,.13,.13),new THREE.MeshBasicMaterial({color:0xfff5cd}));
const pulseLight=new THREE.PointLight(colors.gold,2,4);stage.add(pulseLight);
const vector=arrow(colors.gold),returnVector=arrow(colors.coral),ghostVector=arrow(colors.gold);
const stepArrows=Array.from({length:4},()=>arrow(colors.gold));
const floorTrace=tube(stage,route.getPoints(100).map(p=>V(p.x,.018,p.z)),colors.gold,.008,.08);
const guides=[];for(const f of [.28,.53,.75,1]){const q=route.getPointAt(f);guides.push(tube(stage,[q,V(q.x,.03,q.z)],0x587585,.008,.24))}
const xyz=new THREE.Group();xyz.position.copy(home);stage.add(xyz);
for(const [d,n] of [[V(2,0,0),'X'],[V(0,2,0),'Y'],[V(0,0,-2),'Z']]){tube(xyz,[V(),d],0xa7bab8,.012,.4);const l=label(n,.3,'#a7bab8',60);l.position.copy(d).multiplyScalar(1.15);xyz.add(l)}
const storeLabel=worldLabel('hΔH · hΔA · hΔI · hΔG',V(1,10,1),9,'#f0c66a',120,'PROPOSED SYNAPTIC STORE');
const sumLabel=worldLabel('EVERY MOVEMENT. ONE VECTOR.',V(-1,1.2,9),8,'#f0c66a',90);
const inverterLabel=worldLabel('hΔM',V(4,9,3),4.8,'#ff967d',170,'PROPOSED RETURN PATH');
const halfLabel=worldLabel('180°',endpoint.clone().add(V(3,0,3)),2.0,'#ff967d',130);
const storeLeader=tube(stage,[V(2,8.8,1),V(4,7,2),endpoint],colors.gold,.013,.55);
const invertLeader=tube(stage,[V(4,7.9,3),V(5,6,3),endpoint],colors.coral,.013,.55);
const spinAxis=new THREE.Vector3().crossVectors(displacement,V(0,1,0)).normalize();
const spinArc=tube(stage,Array.from({length:101},(_,i)=>endpoint.clone().add(displacement.clone().normalize().applyAxisAngle(spinAxis,i/100*Math.PI).multiplyScalar(2.5))),colors.coral,.025,.8);
const velocityGroup=new THREE.Group();stage.add(velocityGroup);
for(let i=0;i<7;i++)tube(velocityGroup,[V(-3-i*.12,0,(i-3)*.2),V(-1.2,0,(i-3)*.2)],colors.blue,.016,.6);
tube(velocityGroup,Array.from({length:40},(_,i)=>V(Math.cos(i/39*2)*1.7,-.2,Math.sin(i/39*2)*1.7)),colors.blue,.02,.8);
const velocityLabel=worldLabel('FB3A',V(),4,'#8edff6',145,'FORWARD MOVEMENT / CANDIDATE');
const turningLabel=worldLabel('PS196_b',V(),5,'#8edff6',135,'TURNING / CANDIDATE');
const compass=new THREE.Group();stage.add(compass);compass.position.set(-2,.1,8);
for(let i=0;i<64;i++){let a=i/64*Math.PI*2;let r=i%8===0?2.55:2.75;tube(compass,[V(Math.cos(a)*r,0,Math.sin(a)*r),V(Math.cos(a)*2.95,0,Math.sin(a)*2.95)],colors.violet,.012,.7)}
for(const r of [2.4,3.1]){let ring=new THREE.Mesh(new THREE.TorusGeometry(r,.012,6,120),new THREE.MeshBasicMaterial({color:colors.violet,transparent:true,opacity:.55}));ring.rotation.x=Math.PI/2;compass.add(ring)}
const actualNeedle=arrow(colors.ivory),modelNeedle=arrow(colors.violet);
const compassLabel=worldLabel('EPG ↔ PEN',V(-1,8,6),6,'#c4adff',135,'FEEDBACK BRAKES THE MODEL');
const actualLabel=worldLabel('FLY HEADING',V(),1.6,'#e6e8d9',60),modelLabel=worldLabel('MODEL',V(),1.3,'#c4adff',60);
const questionLabel=worldLabel('WHAT KEEPS THE REAL COMPASS MOVING?',V(-2,.3,12.6),7,'#c4adff',80);
const dustGeo=new THREE.BufferGeometry();const particles=[];for(let i=0;i<430;i++)particles.push((rand()-.5)*85,rand()*23,(rand()-.5)*85);dustGeo.setAttribute('position',new THREE.Float32BufferAttribute(particles,3));scene.add(new THREE.Points(dustGeo,new THREE.PointsMaterial({color:0x96b4bf,size:.032,transparent:true,opacity:.4})));
// Fine bristles and a subtle wing afterimage preserve the insect's material character in flight.
const hairs=[];for(let i=0;i<700;i++){const x=-1.25+rand()*1.75,a=rand()*Math.PI*2,r=x<-.35?.29:.38;const p=V(x,Math.cos(a)*r,Math.sin(a)*r);const q=p.clone().add(V((rand()-.5)*.035,Math.cos(a)*(.035+rand()*.08),Math.sin(a)*(.035+rand()*.08)));hairs.push(...p.toArray(),...q.toArray())}
const hg=new THREE.BufferGeometry();hg.setAttribute('position',new THREE.Float32BufferAttribute(hairs,3));fly.add(new THREE.LineSegments(hg,new THREE.LineBasicMaterial({color:0x788579,transparent:true,opacity:.24})));
fly.scale.setScalar(1.35);
const chapters=[{name:'THE SYNAPTIC STORE',color:'#f0c66a'},{name:'THE RETURN PATH',color:'#ff967d'},{name:'THE MOVEMENT INPUTS',color:'#8edff6'},{name:'THE COMPASS BRAKE',color:'#c4adff'}];
let t=0,playing=!matchMedia('(prefers-reduced-motion: reduce)').matches,last=performance.now(),currentChapter=-1;
function show(obj,value){obj.visible=value}
function fadeLabel(obj,a,b){let f=smooth(a,a+.3,t)*(1-smooth(b-.25,b,t));obj.visible=f>0;obj.material.opacity=f;obj.scale.copy(obj.userData.baseScale).multiplyScalar(.96+.04*f)}
function flightProgress(t){return t<4.25? .95*Math.pow(t/4.25,.86):lerp(.95,1,smooth(4.25,5,t))}
function renderAt(time){
 t=clamp(time,0,20);const ch=t<9?0:t<15?1:t<17.5?2:3;
 if(ch!==currentChapter){currentChapter=ch;document.documentElement.style.setProperty('--accent',chapters[ch].color);$('#chapter-name').textContent=chapters[ch].name;document.querySelectorAll('nav button').forEach((b,i)=>b.classList.toggle('active',i===ch))}
 const out=clamp(flightProgress(Math.min(t,5)),0,1),back=smooth(12.5,18.5,t);
 let pos=t<12.5?route.getPointAt(out):flightBack.getPointAt(back),tangent=t<12.5?route.getTangentAt(Math.min(.999,out)):flightBack.getTangentAt(Math.min(.999,back));
 if(t>=17.5){const entry=flightBack.getPointAt(smooth(12.5,18.5,17.5));const d=entry.clone().sub(compass.position),r=Math.hypot(d.x,d.z),a=Math.atan2(d.z,d.x)+(t-17.5)*.85;pos=V(compass.position.x+Math.cos(a)*r,entry.y+.3*Math.sin(t-17.5),compass.position.z+Math.sin(a)*r);tangent=V(-Math.sin(a),0,Math.cos(a))}
 const frozen=t>=5&&t<12.5;fly.position.copy(pos);
 const yaw=-Math.atan2(tangent.z,tangent.x),pitch=Math.atan2(tangent.y,Math.hypot(tangent.x,tangent.z));
 fly.rotation.set(0,yaw,pitch);fly.rotateX(frozen?.1:lerp(Math.sin(t*2)*.27,.1,t<5?smooth(4.25,5,t):0));
 const wingTime=t<4.25?t: t<5?4.25+(t-4.25)*(1-smooth(4.25,5,t)):frozen?4.25:t;
 wings.forEach((w,i)=>{const side=i===0?-1:1;w.rotation.x=side*(.16+Math.sin(wingTime*105)*.63);w.rotation.y=side*.1});
 const scan=smooth(5.15,7.5,t);for(let i=0;i<dots.length;i++){const m=dots[i],f=m.userData.progress;m.visible=f<=out;m.material.opacity=t<5?.52: t<7.5? .28+.65*Math.exp(-Math.pow((f-scan)*18,2)):.2;m.scale.setScalar(t>=5&&t<7.5?1+1.1*Math.exp(-Math.pow((f-scan)*18,2)):1)}
 const readPoint=route.getPointAt(scan);pulse.position.copy(readPoint);pulseLight.position.copy(readPoint);pulse.visible=t>=5.15&&t<7.7;pulseLight.intensity=pulse.visible?2:0;
 setArrow(vector,origin,readPoint);vector.visible=t>=5.15&&t<12.5;vector.userData.shaft.material.opacity=t<9?.9:.28;
 for(let i=0;i<stepArrows.length;i++){let a=clamp(scan-i*.025,0,1),b=clamp(a+.012,0,1);setArrow(stepArrows[i],route.getPointAt(a),route.getPointAt(b));stepArrows[i].visible=t>=5.15&&t<7.5;}
 floorTrace.visible=t>=5&&t<9;guides.forEach(g=>g.visible=t>=5&&t<9);xyz.visible=t>=4.5&&t<9;
 fadeLabel(storeLabel,7.45,9);fadeLabel(sumLabel,7.45,9);storeLeader.visible=t>=7.5&&t<8.85;
 const rotation=smooth(10,12,t)*Math.PI;const rd=displacement.clone().normalize().applyAxisAngle(spinAxis,rotation);const length=lerp(4,displacement.length(),smooth(12,12.5,t));
 setArrow(returnVector,endpoint,endpoint.clone().addScaledVector(rd,length),smooth(9,9.6,t));returnVector.visible=t>=9&&t<15;
 setArrow(ghostVector,endpoint,endpoint.clone().addScaledVector(displacement.clone().normalize(),4));ghostVector.visible=t>=9&&t<12;ghostVector.children.forEach(m=>m.material.opacity=.2);
 reveal(spinArc,smooth(10,12,t));spinArc.visible=t>=10&&t<12.8;
 fadeLabel(inverterLabel,9.2,15);fadeLabel(halfLabel,10.1,13.5);invertLeader.visible=t>=9.3&&t<14.5;
 velocityGroup.position.copy(pos);velocityGroup.rotation.y=yaw;velocityGroup.visible=ch===2;
 velocityLabel.position.copy(pos).add(V(-4,3,1));turningLabel.position.copy(pos).add(V(3,4,-2));fadeLabel(velocityLabel,15,17.5);fadeLabel(turningLabel,15.1,17.5);
 compass.visible=ch===3;const a=-yaw;const entry=flightBack.getPointAt(smooth(12.5,18.5,17.5));const d=entry.clone().sub(compass.position);const held=Math.atan2(d.z,d.x)+.6*.85+Math.PI/2;const ma=t<18.1?a:held+(t-18.1)*.08;
 const centre=compass.position;setArrow(actualNeedle,centre,centre.clone().add(V(Math.cos(a)*2.7,.02,Math.sin(a)*2.7)));setArrow(modelNeedle,centre.clone().add(V(0,.04,0)),centre.clone().add(V(Math.cos(ma)*2.7,.04,Math.sin(ma)*2.7)));actualNeedle.visible=modelNeedle.visible=ch===3;
 actualLabel.position.copy(centre).add(V(Math.cos(a)*3.7,.1,Math.sin(a)*3.7));modelLabel.position.copy(centre).add(V(Math.cos(ma)*3.7,.1,Math.sin(ma)*3.7));fadeLabel(actualLabel,18.5,20.5);fadeLabel(modelLabel,18.5,20.5);fadeLabel(compassLabel,17.5,20.5);fadeLabel(questionLabel,18.7,20.5);
 // Full-frame cinematography: travel with the insect, then reveal the complete spatial trace.
 const overview=V(21,17,28),overviewTarget=V(0,3,-1);let cam,look;
 if(t<5){const p=route.getPointAt(out);const chase=p.clone().add(V(8,4.7,11));cam=chase.lerp(overview,smooth(2.7,5,t));look=p.clone().lerp(overviewTarget,smooth(2.7,5,t));}
 else if(t<12.5){const u=smooth(5,12.5,t);cam=overview.clone().lerp(V(15,15,30),u);look=overviewTarget.clone();}
 else {let u=smooth(12.5,16,t);cam=V(15,15,30).lerp(pos.clone().add(V(12,9,17)),u);look=overviewTarget.clone().lerp(pos.clone().add(V(0,1,0)),u);}
 camera.position.copy(cam);camera.lookAt(look);camera.fov=innerWidth/innerHeight<1?84:43;camera.updateProjectionMatrix();
 $('#freeze').style.opacity=frozen?'1':'0';$('#timeline').value=t;$('#timeline').style.setProperty('--progress',`${t/20*100}%`);$('#time').innerHTML=`${t.toFixed(1).padStart(4,'0')} <em>/ 20.0</em>`;$('#play').textContent=playing?'Ⅱ':'▶';$('#play').setAttribute('aria-label',playing?'Pause animation':'Play animation');
 $('#app').classList.toggle('paused',!playing);composer.render();
}
function resize(){renderer.setSize(innerWidth,innerHeight);composer.setSize(innerWidth,innerHeight);camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();renderAt(t)}addEventListener('resize',resize);
function toggle(){if(t>=20)t=0;playing=!playing;renderAt(t)}$('#play').onclick=toggle;$('#restart').onclick=()=>{t=0;playing=true;renderAt(t)};
$('#timeline').addEventListener('input',e=>{playing=false;renderAt(Number(e.target.value))});document.querySelectorAll('[data-time]').forEach(b=>b.onclick=()=>{t=Number(b.dataset.time);playing=true;renderAt(t)});
addEventListener('keydown',e=>{if(e.target instanceof HTMLInputElement)return;if(e.code==='Space'){e.preventDefault();toggle()}if(e.code==='ArrowRight'){playing=false;renderAt(t+.5)}if(e.code==='ArrowLeft'){playing=false;renderAt(t-.5)}});
$('#fullscreen').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await $('#app').requestFullscreen()}catch{}};
let uiTimer;addEventListener('pointermove',()=>{$('#app').classList.add('controls-visible');clearTimeout(uiTimer);uiTimer=setTimeout(()=>$('#app').classList.remove('controls-visible'),1800)});
window.__flight={seek:value=>{playing=false;renderAt(value)},play:()=>{playing=true},get time(){return t},get playing(){return playing},renderer,scene};
resize();renderer.setAnimationLoop(now=>{const dt=Math.min((now-last)/1000,.05);last=now;if(playing){t=Math.min(t+dt,20);if(t>=20)playing=false}renderAt(t)});
