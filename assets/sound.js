/* Sonido de tele de Static Forge: todo sintetizado con Web Audio (sin archivos de audio).
   Apagado por defecto. Se activa con cualquier botón [data-sound]; la elección se guarda en localStorage (sf-sound).
   Uso desde otras partes: SFSound.click(), SFSound.zap(), SFSound.static(ms), SFSound.insert(), SFSound.eject(). */
(function(){
'use strict';
var KEY='sf-sound',on=false,ac=null,hum=null,noiseBuf=null,unlocked=false;
try{on=localStorage.getItem(KEY)==='on'}catch(e){}
var calm=false;try{calm=matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){}

function ctx(){
  if(!ac){var A=window.AudioContext||window.webkitAudioContext;if(!A)return null;ac=new A()}
  if(ac.state==='suspended')ac.resume();
  return ac;
}
function noise(){
  var c=ctx();if(!c)return null;
  if(!noiseBuf){var n=c.sampleRate*1.5;noiseBuf=c.createBuffer(1,n,c.sampleRate);var d=noiseBuf.getChannelData(0);for(var i=0;i<n;i++)d[i]=Math.random()*2-1}
  var s=c.createBufferSource();s.buffer=noiseBuf;s.loop=true;return s;
}
function env(g,t,a,peak,dur){g.gain.setValueAtTime(0.0001,t);g.gain.exponentialRampToValueAtTime(peak,t+a);g.gain.exponentialRampToValueAtTime(0.0001,t+dur)}

/* Zumbido de fondo: red eléctrica + pitido de línea del tubo (muy bajito) */
function startHum(){
  var c=ctx();if(!c||hum)return;
  var out=c.createGain();out.gain.value=0;out.connect(c.destination);
  var o=c.createOscillator();o.type='sawtooth';o.frequency.value=50;
  var lp=c.createBiquadFilter();lp.type='lowpass';lp.frequency.value=160;
  var g1=c.createGain();g1.gain.value=0.05;o.connect(lp);lp.connect(g1);g1.connect(out);
  var w=c.createOscillator();w.type='sine';w.frequency.value=15625;
  var g2=c.createGain();g2.gain.value=0.012;w.connect(g2);g2.connect(out);
  o.start();w.start();
  out.gain.linearRampToValueAtTime(0.35,c.currentTime+0.8);
  hum={out:out,o:o,w:w};
}
function stopHum(){
  if(!hum||!ac)return;var h=hum;hum=null;
  h.out.gain.cancelScheduledValues(ac.currentTime);h.out.gain.setValueAtTime(h.out.gain.value,ac.currentTime);
  h.out.gain.linearRampToValueAtTime(0,ac.currentTime+0.25);
  setTimeout(function(){try{h.o.stop();h.w.stop()}catch(e){}},400);
}

var S={
  /* clic de botón de canal */
  click:function(){
    if(!on)return;var c=ctx();if(!c)return;var t=c.currentTime;
    var o=c.createOscillator();o.type='square';o.frequency.setValueAtTime(2200,t);o.frequency.exponentialRampToValueAtTime(700,t+0.03);
    var g=c.createGain();env(g,t,0.002,0.08,0.05);o.connect(g);g.connect(c.destination);o.start(t);o.stop(t+0.06);
  },
  /* estática: ruido filtrado con un barrido */
  static:function(ms){
    if(!on)return;var c=ctx(),s=noise();if(!s)return;var t=c.currentTime,d=(ms||260)/1000;
    var bp=c.createBiquadFilter();bp.type='bandpass';bp.Q.value=0.7;bp.frequency.setValueAtTime(3500,t);bp.frequency.exponentialRampToValueAtTime(900,t+d);
    var g=c.createGain();env(g,t,0.01,0.22,d);s.connect(bp);bp.connect(g);g.connect(c.destination);s.start(t);s.stop(t+d+0.05);
  },
  /* cambio de canal: clic + estática corta */
  zap:function(){S.click();S.static(calm?120:240)},
  /* encendido: golpe grave + pitido que sube */
  power:function(){
    if(!on)return;var c=ctx();if(!c)return;var t=c.currentTime;
    var o=c.createOscillator();o.type='sine';o.frequency.setValueAtTime(90,t);o.frequency.exponentialRampToValueAtTime(40,t+0.25);
    var g=c.createGain();env(g,t,0.005,0.35,0.3);o.connect(g);g.connect(c.destination);o.start(t);o.stop(t+0.32);
    var w=c.createOscillator();w.type='sine';w.frequency.setValueAtTime(6000,t+0.05);w.frequency.exponentialRampToValueAtTime(15000,t+0.6);
    var g2=c.createGain();env(g2,t+0.05,0.05,0.025,0.7);w.connect(g2);g2.connect(c.destination);w.start(t+0.05);w.stop(t+0.8);
    S.static(350);
  },
  /* meter una cinta en el vídeo: deslizamiento + clac mecánico */
  insert:function(){
    if(!on)return;var c=ctx(),s=noise();if(!s)return;var t=c.currentTime;
    var lp=c.createBiquadFilter();lp.type='lowpass';lp.frequency.value=900;var g=c.createGain();env(g,t,0.05,0.12,0.35);
    s.connect(lp);lp.connect(g);g.connect(c.destination);s.start(t);s.stop(t+0.4);
    [0.38,0.5].forEach(function(dt,i){var o=c.createOscillator();o.type='square';o.frequency.value=i?160:120;var gg=c.createGain();env(gg,t+dt,0.003,0.18,0.07);o.connect(gg);gg.connect(c.destination);o.start(t+dt);o.stop(t+dt+0.08)});
    var m=c.createOscillator();m.type='sawtooth';m.frequency.value=55;var mg=c.createGain();mg.gain.setValueAtTime(0.0001,t+0.6);mg.gain.exponentialRampToValueAtTime(0.03,t+0.8);mg.gain.exponentialRampToValueAtTime(0.0001,t+1.5);
    m.connect(mg);mg.connect(c.destination);m.start(t+0.6);m.stop(t+1.6);
  },
  /* expulsar la cinta */
  eject:function(){
    if(!on)return;var c=ctx();if(!c)return;var t=c.currentTime;
    var o=c.createOscillator();o.type='square';o.frequency.setValueAtTime(140,t);var g=c.createGain();env(g,t,0.003,0.2,0.09);o.connect(g);g.connect(c.destination);o.start(t);o.stop(t+0.1);
    var s=noise();if(!s)return;var lp=c.createBiquadFilter();lp.type='lowpass';lp.frequency.value=1200;var g2=c.createGain();env(g2,t+0.08,0.03,0.1,0.3);s.connect(lp);lp.connect(g2);g2.connect(c.destination);s.start(t+0.08);s.stop(t+0.42);
  },
  isOn:function(){return on},
  toggle:function(){set(!on)}
};
function sync(){
  document.querySelectorAll('[data-sound]').forEach(function(b){
    b.setAttribute('aria-pressed',on?'true':'false');
    var en=document.documentElement.getAttribute('lang')==='en';
    b.setAttribute('aria-label',en?(on?'Sound on':'Sound off'):(on?'Sonido activado':'Sonido desactivado'));
    b.title=b.getAttribute('aria-label');
    b.innerHTML=on?'<svg width="16" height="14" viewBox="0 0 16 14" aria-hidden="true"><path d="M1 5h3l4-4v12L4 9H1z" fill="currentColor"/><path d="M11 4c1.2 1.6 1.2 4.4 0 6M13 2c2.2 2.8 2.2 7.2 0 10" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'
                  :'<svg width="16" height="14" viewBox="0 0 16 14" aria-hidden="true"><path d="M1 5h3l4-4v12L4 9H1z" fill="currentColor"/><path d="M11 4.5l4 5M15 4.5l-4 5" stroke="currentColor" stroke-width="1.4"/></svg>';
  });
}
function set(v){
  on=v;try{localStorage.setItem(KEY,on?'on':'off')}catch(e){}
  if(on){unlocked=true;startHum();S.power()}else stopHum();
  sync();
}
/* El navegador solo deja sonar tras un gesto: si el sonido estaba activado, arranca el zumbido con el primer clic o tecla */
function unlock(){if(unlocked)return;unlocked=true;if(on)startHum();document.removeEventListener('pointerdown',unlock,true);document.removeEventListener('keydown',unlock,true)}
document.addEventListener('pointerdown',unlock,true);document.addEventListener('keydown',unlock,true);
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-sound]');if(b){e.preventDefault();set(!on)}});
document.addEventListener('visibilitychange',function(){if(!on)return;if(document.hidden)stopHum();else if(unlocked)startHum()});
document.addEventListener('sf:lang',sync);
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',sync);else sync();
window.SFSound=S;
})();
