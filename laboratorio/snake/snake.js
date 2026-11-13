/* Static Forge · Laboratorio · Snake (EXP-02)
   Lógica por casillas, dibujo continuo: la serpiente se interpola entre pasos para moverse fluida. */
(function(){
'use strict';
var N=20;
var cv=document.getElementById('game'),ctx=cv.getContext('2d');
var $score=document.getElementById('score'),$best=document.getElementById('best'),$play=document.getElementById('play');
var $walls=document.getElementById('walls'),$fast=document.getElementById('fast');
var $ov=document.getElementById('ov'),$ovT=document.getElementById('ovT'),$ovS=document.getElementById('ovS'),$ovStats=document.getElementById('ovStats'),$ovB=document.getElementById('ovB');
var DIRS={up:[0,-1],down:[0,1],left:[-1,0],right:[1,0]},OPP={up:'down',down:'up',left:'right',right:'left'};
var ANG={right:0,down:Math.PI/2,left:Math.PI,up:-Math.PI/2};
var FRUITS=[
  {a:'#ff8a8a',b:'#e5243b',c:'#9e0f22',p:'#ff5b6b'},   /* manzana */
  {a:'#ffd58a',b:'#ff9a1f',c:'#c95f00',p:'#ffb347'},   /* naranja */
  {a:'#d9b3ff',b:'#9b4dff',c:'#5a17b8',p:'#b47bff'},   /* uva */
  {a:'#ffc2e0',b:'#ff4fa3',c:'#b3155f',p:'#ff7ab8'}    /* fresa */
];
var BONUS_EVERY=6,BONUS_LIFE=6500,BONUS_PTS=5;

var snake,prev,dir,queue,food,bonus,score,eaten,state='ready',acc=0,last=0,stepMs=150,progress=1;
var walls=true,fast=false,best=0,newBest=false;
var px=28,W=560,dpr=1,bg=null;
var parts=[],pops=[],rings=[],bulges=[];
var headAng=0,blinkAt=0,blinkUntil=0,tongueAt=0,tongueUntil=0,shake=0,deathT=0,deathCount=0,overShown=false,startT=0;

function get(k){try{return localStorage.getItem(k)}catch(e){return null}}
function set(k,v){try{localStorage.setItem(k,v)}catch(e){}}
function L(){return document.documentElement.getAttribute('lang')==='en'?'en':'es'}
function T(es,en){return L()==='en'?en:es}
function bestKey(){return 'sf-snake-best'+(walls?'':'-wrap')+(fast?'-fast':'')}
function loadBest(){best=parseInt(get(bestKey()),10)||0;$best.textContent=best}
function rand(a,b){return a+Math.random()*(b-a)}
function easeOutBack(x){var c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)}
function clamp01(x){return x<0?0:x>1?1:x}
walls=get('sf-snake-walls')!=='0';fast=get('sf-snake-fast')==='1';
$walls.setAttribute('aria-pressed',walls);$fast.setAttribute('aria-pressed',fast);loadBest();

/* ---------- Lógica ---------- */
function reset(){
  var m=Math.floor(N/2);snake=[[m-1,m],[m-2,m],[m-3,m],[m-4,m]];prev=snake.map(function(c){return c.slice()});
  dir='right';queue=[];score=0;eaten=0;$score.textContent=0;bonus=null;parts=[];pops=[];rings=[];bulges=[];
  acc=0;progress=1;headAng=0;deathCount=0;overShown=false;newBest=false;food=null;placeFood(performance.now());
}
function freeCells(){
  var taken={};snake.forEach(function(s){taken[s[0]+','+s[1]]=1});
  if(food)taken[food.x+','+food.y]=1;if(bonus)taken[bonus.x+','+bonus.y]=1;
  var out=[];for(var x=0;x<N;x++)for(var y=0;y<N;y++)if(!taken[x+','+y])out.push([x,y]);return out;
}
function placeFood(now){
  var f=freeCells();if(!f.length){food=null;return}
  var c=f[Math.floor(Math.random()*f.length)];food={x:c[0],y:c[1],k:FRUITS[Math.floor(Math.random()*FRUITS.length)],born:now};
}
function placeBonus(now){
  var f=freeCells().filter(function(c){return Math.abs(c[0]-snake[0][0])+Math.abs(c[1]-snake[0][1])>4});
  if(!f.length)return;var c=f[Math.floor(Math.random()*f.length)];bonus={x:c[0],y:c[1],born:now};
}
function speed(){var base=fast?100:150,min=fast?52:72;return Math.max(min,base-score*1.6)}
function start(){
  reset();state='play';startT=performance.now();stepMs=speed();hideOverlay();$play.textContent=T('Pausa','Pause');
  try{cv.focus({preventScroll:true})}catch(e){}
}
function togglePause(){
  if(state==='play'){state='pause';$play.textContent=T('Seguir','Resume');showOverlay('pause')}
  else if(state==='pause'){state='play';$play.textContent=T('Pausa','Pause');hideOverlay();last=performance.now()}
  else if(state!=='dying')start();
}
function turn(d){
  if(state==='ready'||state==='over'||state==='won'){start()}
  if(state!=='play')return;
  var ref=queue.length?queue[queue.length-1]:dir;
  if(d!==ref&&d!==OPP[ref]&&queue.length<3)queue.push(d);
}
function step(now){
  if(queue.length)dir=queue.shift();
  var h=snake[0],v=DIRS[dir],nx=h[0]+v[0],ny=h[1]+v[1];
  if(!walls){nx=(nx+N)%N;ny=(ny+N)%N}
  var eatF=food&&nx===food.x&&ny===food.y,eatB=bonus&&nx===bonus.x&&ny===bonus.y,grow=eatF||eatB;
  var body=grow?snake:snake.slice(0,-1);
  if(nx<0||ny<0||nx>=N||ny>=N||body.some(function(s){return s[0]===nx&&s[1]===ny})){return die(now,false)}
  prev=snake.map(function(c){return c.slice()});
  snake.unshift([nx,ny]);
  if(grow){prev.push(prev[prev.length-1].slice())}else snake.pop();
  bulges.forEach(function(b){b.i++});bulges=bulges.filter(function(b){return b.i<snake.length});
  if(eatF){
    score++;eaten++;burst(nx,ny,food.k.p,16,1);popText(nx,ny,'+1',food.k.b);bulges.push({i:0});
    placeFood(now);if(eaten%BONUS_EVERY===0&&!bonus)placeBonus(now);bump();
    if(!food&&!bonus)return die(now,true);
  }
  if(eatB){score+=BONUS_PTS;burst(nx,ny,'#ffd23f',26,1.4);burst(nx,ny,'#ffffff',10,1);popText(nx,ny,'+'+BONUS_PTS,'#e09a00');bulges.push({i:0});bonus=null;bump();rings.push({x:nx,y:ny,t:now,c:'255,210,63'})}
  if(grow){$score.textContent=score;stepMs=speed()}
}
function die(now,won){
  newBest=score>best;if(newBest){best=score;set(bestKey(),best);$best.textContent=best}
  if(won){state='won';showOverlay('won');$play.textContent=T('Otra vez','Again');return}
  state='dying';deathT=now;shake=1;progress=1;prev=snake.map(function(c){return c.slice()});
  $play.textContent=T('Otra vez','Again');
}
function bump(){try{$score.animate([{transform:'scale(1.45)',color:'#36c3ff'},{transform:'scale(1)'}],{duration:320,easing:'cubic-bezier(.2,1.6,.4,1)'})}catch(e){}}

/* ---------- Efectos ---------- */
function cc(x){return (x+.5)*px}
function burst(x,y,color,n,power){
  for(var i=0;i<n;i++){var a=rand(0,Math.PI*2),sp=rand(.6,1.6)*power*px*.09;
    parts.push({x:cc(x),y:cc(y),vx:Math.cos(a)*sp,vy:Math.sin(a)*sp-px*.02,r:rand(.07,.16)*px,life:1,decay:rand(.018,.032),c:color})}
  rings.push({x:x,y:y,t:performance.now(),c:hexRgb(color)});
}
function hexRgb(h){if(h[0]!=='#')return '255,255,255';var n=parseInt(h.slice(1),16);return (n>>16&255)+','+(n>>8&255)+','+(n&255)}
function popText(x,y,txt,color){pops.push({x:cc(x),y:cc(y),t:performance.now(),txt:txt,c:color})}

/* ---------- Overlay ---------- */
function showOverlay(kind){
  var st='';
  if(kind==='ready'){$ovT.textContent='Snake';$ovS.textContent=T('Come fruta, crece y no te muerdas. Cada '+BONUS_EVERY+' piezas aparece una estrella dorada.','Eat fruit, grow and don\'t bite yourself. Every '+BONUS_EVERY+' pieces a golden star appears.');$ovB.textContent=T('Jugar','Play')}
  else if(kind==='pause'){$ovT.textContent=T('Pausa','Paused');$ovS.textContent=T('Respira. La serpiente te espera.','Take a breath. The snake will wait.');$ovB.textContent=T('Seguir','Resume')}
  else{
    $ovT.textContent=kind==='won'?T('¡Tablero lleno!','Board full!'):(newBest?T('¡Nuevo récord!','New best!'):'Game over');
    $ovS.textContent=kind==='won'?T('No queda ni una casilla libre.','Not a single free cell left.'):(newBest?T('Has superado tu mejor marca.','You beat your best score.'):T('Te has chocado. Otra ronda.','You crashed. One more round.'));
    st='<span>'+T('PUNTOS','SCORE')+'<b>'+score+'</b></span><span>'+T('LARGO','LENGTH')+'<b>'+snake.length+'</b></span><span>'+T('RÉCORD','BEST')+'<b>'+best+'</b></span>';
    $ovB.textContent=T('Otra vez','Again');
  }
  $ovStats.innerHTML=st;$ov.dataset.kind=kind;$ov.classList.add('show');
}
function hideOverlay(){$ov.classList.remove('show')}

/* ---------- Dibujo ---------- */
function resize(){
  var r=cv.getBoundingClientRect();dpr=Math.min(window.devicePixelRatio||1,2);var s=Math.round(r.width*dpr);
  if(s>0&&cv.width!==s){cv.width=cv.height=s}W=cv.width;px=W/N;buildBg();
}
function buildBg(){
  bg=document.createElement('canvas');bg.width=bg.height=W;var b=bg.getContext('2d');
  var g=b.createRadialGradient(W*.5,W*.38,W*.05,W*.5,W*.5,W*.75);g.addColorStop(0,'#144a78');g.addColorStop(.6,'#0d2f52');g.addColorStop(1,'#081a30');
  b.fillStyle=g;b.fillRect(0,0,W,W);
  b.fillStyle='rgba(140,210,255,.13)';
  for(var x=0;x<N;x++)for(var y=0;y<N;y++){b.beginPath();b.arc(cc(x),cc(y),Math.max(1,px*.055),0,7);b.fill()}
  var v=b.createRadialGradient(W/2,W/2,W*.45,W/2,W/2,W*.75);v.addColorStop(0,'rgba(0,0,0,0)');v.addColorStop(1,'rgba(0,8,20,.45)');b.fillStyle=v;b.fillRect(0,0,W,W);
  b.lineWidth=Math.max(2,px*.1);
  if(walls){b.strokeStyle='rgba(120,205,255,.55)';b.shadowColor='rgba(80,190,255,.8)';b.shadowBlur=px*.6;rr(b,b.lineWidth/2,b.lineWidth/2,W-b.lineWidth,W-b.lineWidth,px*.6);b.stroke();b.shadowBlur=0}
  else{b.strokeStyle='rgba(120,205,255,.3)';b.setLineDash([px*.4,px*.35]);rr(b,b.lineWidth/2,b.lineWidth/2,W-b.lineWidth,W-b.lineWidth,px*.6);b.stroke();b.setLineDash([])}
}
function rr(c,x,y,w,h,r){c.beginPath();c.moveTo(x+r,y);c.arcTo(x+w,y,x+w,y+h,r);c.arcTo(x+w,y+h,x,y+h,r);c.arcTo(x,y+h,x,y,r);c.arcTo(x,y,x+w,y,r);c.closePath()}

function points(){
  var out=[];
  for(var i=0;i<snake.length;i++){
    var a=prev[i]||snake[i],b=snake[i],dx=b[0]-a[0],dy=b[1]-a[1];
    if(Math.abs(dx)>1||Math.abs(dy)>1)out.push({x:cc(b[0]),y:cc(b[1]),jump:true});
    else out.push({x:cc(a[0]+dx*progress),y:cc(a[1]+dy*progress)});
  }
  return out;
}
function widthAt(i,n){
  var k=n>1?i/(n-1):0,w=px*(.92-.32*k);
  for(var j=0;j<bulges.length;j++){var d=Math.abs(bulges[j].i+progress-i);if(d<1.5)w+=px*.22*(1-d/1.5)}
  return w;
}
function colorAt(i,n,dead){
  var k=n>1?i/(n-1):0;
  if(dead)return 'hsl(350,'+Math.round(30+40*(1-k))+'%,'+Math.round(55-12*k)+'%)';
  return 'hsl('+Math.round(92+78*k)+','+Math.round(78-8*k)+'%,'+Math.round(52-10*k)+'%)';
}
function strokeBody(pts,n,from,pass,dead){
  for(var i=n-1;i>from;i--){
    var a=pts[i],b=pts[i-1];if(a.jump||b.jump||Math.hypot(a.x-b.x,a.y-b.y)>px*1.5)continue;
    var w=widthAt(i-1,n);ctx.lineWidth=pass==='glow'?w*1.7:pass==='shine'?w*.32:w;
    ctx.strokeStyle=pass==='glow'?'rgba(140,255,170,.10)':pass==='shadow'?'rgba(0,10,25,.45)':pass==='shine'?'rgba(255,255,255,.38)':colorAt(i-1,n,dead);
    var oy=pass==='shadow'?px*.14:pass==='shine'?-w*.2:0;
    ctx.beginPath();ctx.moveTo(a.x,a.y+oy);ctx.lineTo(b.x,b.y+oy);ctx.stroke();
  }
}
function drawFruit(f,now){
  var age=now-f.born,s=easeOutBack(clamp01(age/420)),bob=Math.sin(now/320)*px*.05,cx=cc(f.x),cy=cc(f.y)+bob,r=px*.38*s*(1+Math.sin(now/260)*.03);
  if(r<=0)return;
  ctx.fillStyle='rgba(0,10,25,.35)';ctx.beginPath();ctx.ellipse(cc(f.x),cc(f.y)+px*.36,r*.75,r*.22,0,0,7);ctx.fill();
  var g=ctx.createRadialGradient(cx-r*.35,cy-r*.4,r*.1,cx,cy,r*1.05);g.addColorStop(0,f.k.a);g.addColorStop(.55,f.k.b);g.addColorStop(1,f.k.c);
  ctx.fillStyle=g;ctx.beginPath();ctx.arc(cx,cy,r,0,7);ctx.fill();
  ctx.fillStyle='rgba(255,255,255,.75)';ctx.beginPath();ctx.ellipse(cx-r*.28,cy-r*.42,r*.36,r*.2,-.5,0,7);ctx.fill();
  ctx.strokeStyle='#5a3a12';ctx.lineWidth=Math.max(1.5,px*.07);ctx.lineCap='round';ctx.beginPath();ctx.moveTo(cx,cy-r*.8);ctx.quadraticCurveTo(cx+r*.1,cy-r*1.15,cx+r*.05,cy-r*1.25);ctx.stroke();
  ctx.fillStyle='#46c93a';ctx.beginPath();ctx.ellipse(cx+r*.38,cy-r*1.05,r*.38,r*.17,-.5,0,7);ctx.fill();
}
function star(c,x,y,r1,r2,rot){c.beginPath();for(var i=0;i<10;i++){var r=i%2?r2:r1,a=rot+i*Math.PI/5-Math.PI/2;c.lineTo(x+Math.cos(a)*r,y+Math.sin(a)*r)}c.closePath()}
function drawBonus(now){
  var age=now-bonus.born,left=1-age/BONUS_LIFE;
  if(left<=0){burst(bonus.x,bonus.y,'#ffe58a',10,.7);bonus=null;return}
  var s=easeOutBack(clamp01(age/450)),cx=cc(bonus.x),cy=cc(bonus.y)+Math.sin(now/240)*px*.06,r=px*.46*s;
  if(left<.3&&Math.floor(now/110)%2)return;
  ctx.strokeStyle='rgba(255,215,80,.25)';ctx.lineWidth=px*.08;ctx.beginPath();ctx.arc(cx,cy,px*.62,0,7);ctx.stroke();
  ctx.strokeStyle='#ffd23f';ctx.lineCap='round';ctx.beginPath();ctx.arc(cx,cy,px*.62,-Math.PI/2,-Math.PI/2+Math.PI*2*left);ctx.stroke();
  ctx.save();ctx.shadowColor='rgba(255,200,40,.9)';ctx.shadowBlur=px*.6;
  var g=ctx.createRadialGradient(cx-r*.3,cy-r*.3,r*.1,cx,cy,r);g.addColorStop(0,'#fff6c2');g.addColorStop(.5,'#ffd23f');g.addColorStop(1,'#e08a00');
  ctx.fillStyle=g;star(ctx,cx,cy,r,r*.48,now/900);ctx.fill();ctx.restore();
  ctx.fillStyle='rgba(255,255,255,.7)';ctx.beginPath();ctx.ellipse(cx-r*.15,cy-r*.3,r*.22,r*.1,-.4,0,7);ctx.fill();
}
function drawHead(p,w,now,dead){
  var r=w*.6;
  var g=ctx.createRadialGradient(p.x-r*.3,p.y-r*.35,r*.1,p.x,p.y,r*1.1);
  if(dead){g.addColorStop(0,'#ffb3bd');g.addColorStop(1,'#c2364b')}else{g.addColorStop(0,'#d9ff9e');g.addColorStop(.6,colorAt(0,snake.length,false));g.addColorStop(1,'#3c9a1a')}
  ctx.fillStyle=g;ctx.beginPath();ctx.arc(p.x,p.y,r,0,7);ctx.fill();
  var a=headAng,fx=Math.cos(a),fy=Math.sin(a),nx=-fy,ny=fx;
  /* lengua */
  if(!dead&&state==='play'&&now<tongueUntil){
    var tl=r*(.9+.5*Math.sin((tongueUntil-now)/250*Math.PI)),bx=p.x+fx*r*.9,by=p.y+fy*r*.9,ex=bx+fx*tl,ey=by+fy*tl;
    ctx.strokeStyle='#ff4d6d';ctx.lineWidth=Math.max(1.5,px*.07);ctx.lineCap='round';
    ctx.beginPath();ctx.moveTo(bx,by);ctx.lineTo(ex,ey);ctx.lineTo(ex+(fx+nx)*r*.25,ey+(fy+ny)*r*.25);ctx.moveTo(ex,ey);ctx.lineTo(ex+(fx-nx)*r*.25,ey+(fy-ny)*r*.25);ctx.stroke();
  }
  var blink=now<blinkUntil?.15:1,er=r*.36;
  var tx=food?cc(food.x):p.x+fx,ty=food?cc(food.y):p.y+fy,la=Math.atan2(ty-p.y,tx-p.x);
  [-1,1].forEach(function(sd){
    var ex=p.x+fx*r*.25+nx*r*.45*sd,ey=p.y+fy*r*.25+ny*r*.45*sd;
    if(dead){ctx.strokeStyle='#3a0a12';ctx.lineWidth=Math.max(1.5,px*.07);var q=er*.6;ctx.beginPath();ctx.moveTo(ex-q,ey-q);ctx.lineTo(ex+q,ey+q);ctx.moveTo(ex+q,ey-q);ctx.lineTo(ex-q,ey+q);ctx.stroke();return}
    ctx.fillStyle='#fff';ctx.beginPath();ctx.ellipse(ex,ey,er,er*blink,a,0,7);ctx.fill();
    if(blink===1){ctx.fillStyle='#0b2a4a';ctx.beginPath();ctx.arc(ex+Math.cos(la)*er*.38,ey+Math.sin(la)*er*.38,er*.52,0,7);ctx.fill();
      ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(ex+Math.cos(la)*er*.38-er*.18,ey+Math.sin(la)*er*.38-er*.2,er*.17,0,7);ctx.fill()}
  });
  ctx.fillStyle='rgba(255,255,255,.45)';ctx.beginPath();ctx.ellipse(p.x-r*.2,p.y-r*.5,r*.4,r*.18,-.3,0,7);ctx.fill();
}
function draw(now,dt){
  var sx=0,sy=0;if(shake>0){sx=rand(-1,1)*px*.35*shake;sy=rand(-1,1)*px*.35*shake}
  ctx.setTransform(1,0,0,1,sx,sy);ctx.clearRect(-px,-px,W+2*px,W+2*px);
  if(bg)ctx.drawImage(bg,0,0);
  /* luz que se mueve por el agua */
  var lx=W*(.5+.3*Math.sin(now/5200)),ly=W*(.35+.2*Math.cos(now/4300)),lg=ctx.createRadialGradient(lx,ly,0,lx,ly,W*.45);
  lg.addColorStop(0,'rgba(120,210,255,.10)');lg.addColorStop(1,'rgba(120,210,255,0)');ctx.fillStyle=lg;ctx.fillRect(0,0,W,W);
  if(food)drawFruit(food,now);
  if(bonus)drawBonus(now);
  var dead=state==='dying'||state==='over';
  var pts=points(),n=pts.length,from=dead?Math.min(n,deathCount):0;
  ctx.lineCap='round';ctx.lineJoin='round';
  if(from<n){
    strokeBody(pts,n,from,'shadow',dead);strokeBody(pts,n,from,'glow',dead);strokeBody(pts,n,from,'body',dead);strokeBody(pts,n,from,'shine',dead);
    for(var i=Math.max(from,1);i<n;i++)if(pts[i].jump||(i>0&&Math.hypot(pts[i].x-pts[i-1].x,pts[i].y-pts[i-1].y)>px*1.5)){ctx.fillStyle=colorAt(i,n,dead);ctx.beginPath();ctx.arc(pts[i].x,pts[i].y,widthAt(i,n)/2,0,7);ctx.fill()}
    if(from===0)drawHead(pts[0],widthAt(0,n),now,dead);
  }
  /* anillos */
  rings=rings.filter(function(r){var k=(now-r.t)/500;if(k>=1)return false;ctx.strokeStyle='rgba('+r.c+','+(1-k)*.7+')';ctx.lineWidth=px*.1*(1-k)+1;ctx.beginPath();ctx.arc(cc(r.x),cc(r.y),px*(.3+1.1*k),0,7);ctx.stroke();return true});
  /* partículas */
  var f=dt/16.7;
  parts=parts.filter(function(p){p.x+=p.vx*f;p.y+=p.vy*f;p.vy+=px*.004*f;p.vx*=.97;p.life-=p.decay*f;if(p.life<=0)return false;
    ctx.globalAlpha=p.life;ctx.fillStyle=p.c;ctx.beginPath();ctx.arc(p.x,p.y,p.r*(.5+.5*p.life),0,7);ctx.fill();ctx.globalAlpha=1;return true});
  /* textos +1 */
  ctx.textAlign='center';ctx.textBaseline='middle';
  pops=pops.filter(function(p){var k=(now-p.t)/800;if(k>=1)return false;var s=k<.2?easeOutBack(k/.2):1;
    ctx.globalAlpha=1-Math.max(0,(k-.5)/.5);ctx.font='900 '+Math.round(px*.75*s)+'px Nunito, "Segoe UI", sans-serif';
    ctx.lineWidth=px*.16;ctx.strokeStyle='#fff';ctx.lineJoin='round';ctx.strokeText(p.txt,p.x,p.y-k*px*1.4);ctx.fillStyle=p.c;ctx.fillText(p.txt,p.x,p.y-k*px*1.4);ctx.globalAlpha=1;return true});
  ctx.setTransform(1,0,0,1,0,0);
}

/* ---------- Bucle ---------- */
function loop(now){
  var dt=Math.min(100,now-(last||now));last=now;
  if(state==='play'){
    acc+=dt;
    while(acc>=stepMs&&state==='play'){acc-=stepMs;step(now)}
    progress=state==='play'?clamp01(acc/stepMs):1;
  }
  if(state==='dying'){
    var k=now-deathT,want=Math.min(snake.length,Math.floor(Math.max(0,k-250)/Math.max(18,500/snake.length)));
    while(deathCount<want){var c=snake[deathCount];burst(c[0],c[1],colorAt(deathCount,snake.length,true),deathCount===0?16:6,deathCount===0?1.3:.8);deathCount++}
    if(deathCount>=snake.length&&k>650){state='over';if(!overShown){overShown=true;showOverlay('over')}}
  }
  var target=ANG[dir];var d=target-headAng;while(d>Math.PI)d-=Math.PI*2;while(d<-Math.PI)d+=Math.PI*2;headAng+=d*Math.min(1,dt/70);
  if(now>blinkAt){blinkUntil=now+130;blinkAt=now+rand(2200,5200)}
  if(now>tongueAt){tongueUntil=now+260;tongueAt=now+rand(1800,4200)}
  shake=Math.max(0,shake-dt/420);
  draw(now,dt);requestAnimationFrame(loop);
}

/* ---------- Entrada ---------- */
var KEY={ArrowUp:'up',ArrowDown:'down',ArrowLeft:'left',ArrowRight:'right',KeyW:'up',KeyS:'down',KeyA:'left',KeyD:'right'};
document.addEventListener('keydown',function(e){
  if(e.target.closest&&e.target.closest('button,a,input')&&(e.code==='Space'||e.code==='Enter'))return;
  if(KEY[e.code]){e.preventDefault();turn(KEY[e.code])}
  else if(e.code==='Space'||e.code==='KeyP'){e.preventDefault();togglePause()}
  else if(e.code==='Enter'&&state!=='play'&&state!=='pause'&&state!=='dying'){e.preventDefault();start()}
});
var sx0=null,sy0=null;
cv.addEventListener('pointerdown',function(e){sx0=e.clientX;sy0=e.clientY});
cv.addEventListener('pointerup',function(e){
  if(sx0===null)return;var dx=e.clientX-sx0,dy=e.clientY-sy0;sx0=null;
  if(Math.max(Math.abs(dx),Math.abs(dy))<24)return;
  turn(Math.abs(dx)>Math.abs(dy)?(dx>0?'right':'left'):(dy>0?'down':'up'));
});
document.getElementById('pad').addEventListener('pointerdown',function(e){
  var b=e.target.closest('button[data-d]');if(!b)return;e.preventDefault();
  var d=b.getAttribute('data-d');if(d==='pause')togglePause();else turn(d);
});
$play.addEventListener('click',togglePause);
$ovB.addEventListener('click',function(){if(state==='pause')togglePause();else start()});
function opt(btn,key){btn.addEventListener('click',function(){
  if(key==='walls')walls=!walls;else fast=!fast;
  var v=key==='walls'?walls:fast;btn.setAttribute('aria-pressed',v);set('sf-snake-'+key,v?'1':'0');
  loadBest();buildBg();
  if(state!=='ready'){state='ready';reset();showOverlay('ready');$play.textContent=T('Jugar','Play')}
})}
opt($walls,'walls');opt($fast,'fast');
document.addEventListener('visibilitychange',function(){if(document.hidden&&state==='play')togglePause()});
document.addEventListener('sf:lang',function(){
  $play.textContent=state==='play'?T('Pausa','Pause'):state==='pause'?T('Seguir','Resume'):state==='ready'?T('Jugar','Play'):T('Otra vez','Again');
  if($ov.classList.contains('show'))showOverlay($ov.dataset.kind||'ready');
});
window.addEventListener('resize',resize);
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){});
reset();resize();showOverlay('ready');requestAnimationFrame(loop);
})();
