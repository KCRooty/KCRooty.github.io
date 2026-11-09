/* Videoteca de Static Forge: el devlog como estantería de cintas VHS.
   ── Para añadir una cinta, copia una entrada de CINTAS (la más nueva arriba) ──
   fecha:  lo que sale en el lomo (texto libre, p. ej. 'NOV 2026')
   es/en:  título corto en el lomo · txt / txtEn: lo que cuenta la cinta al reproducirla
   img:    una o varias imágenes (se pasan solas como si fuese la grabación)
   color:  color de la etiqueta (usa los de la marca: '#E79D56', '#B25781', '#4C9DB0', '#FFB000')
   fit:    true si la imagen es un logo (se ve entero, sin recortar) · wide: true si es una imagen apaisada con texto
   rec:    la fecha que sale abajo a la izquierda, como en las cámaras (opcional) */
var CINTAS=[
  {fecha:'NOV 2026',es:'Nueva emisión',en:'New broadcast',color:'#FFB000',img:['assets/og/home.jpg'],wide:true,rec:'NOV 09 2026',
   txt:'La web se renueva: tele de proyectos con canales, galería más grande, Paint It! y un 404 que busca canales solo.',
   txtEn:'The site gets a refresh: a project TV with channels, a bigger gallery, Paint It! and a 404 that scans for channels on its own.'},
  {fecha:'NOV 2026',es:'Paint It!',en:'Paint It!',color:'#4C9DB0',img:['assets/og/paint-it.jpg'],wide:true,rec:'NOV 09 2026',
   txt:'El Paint de toda la vida, dentro de la web. Las dieciséis herramientas, los menús y los atajos de siempre.',
   txtEn:'Good old Paint, right inside the site. All sixteen tools, the menus and the classic shortcuts.'},
  {fecha:'NOV 2026',es:'Iron3D Studio',en:'Iron3D Studio',color:'#B25781',img:['assets/projects/iron3d-ui.webp'],rec:'NOV 07 2026',
   txt:'Primeras pantallas de la interfaz de Iron3D Studio, el programa 3D propio del estudio.',
   txtEn:"First screens of Iron3D Studio's interface, the studio's own 3D software."},
  {fecha:'OCT 2026',es:'X-USB 1.0',en:'X-USB 1.0',color:'#E79D56',img:['assets/projects/xusb.webp'],fit:true,rec:'OCT 30 2026',
   txt:'X-USB llega a la versión 1.0.0, publicada en GitHub.',
   txtEn:'X-USB reaches version 1.0.0, released on GitHub.'},
  {fecha:'OCT 2026',es:'KC Downloader',en:'KC Downloader',color:'#4C9DB0',img:['assets/projects/kc-downloader.webp'],fit:true,rec:'OCT 30 2026',
   txt:'Nueva versión de KC Downloader, la 2.4, en GitHub.',
   txtEn:'A new KC Downloader release, version 2.4, on GitHub.'},
  {fecha:'2025',es:'El salto a Source',en:'The jump to Source',color:'#B25781',img:['assets/donnies/history-2025-sketch.webp'],rec:'2025',
   txt:"Adiós a Clickteam: Donnie's Origins pasa a Source Engine.",
   txtEn:"Goodbye Clickteam: Donnie's Origins moves to Source Engine."},
  {fecha:'2024',es:"Donnie's Remastered",en:"Donnie's Remastered",color:'#E79D56',img:['assets/donnies/history-2024-title.webp','assets/donnies/donnie-suit-head.webp'],rec:'2024',
   txt:'Una cabeza de cosplay como referencia física para volver a modelar a Donnie y al resto del reparto en 3D.',
   txtEn:'A cosplay head as a physical reference to model Donnie and the rest of the cast in 3D again.'},
  {fecha:'2022',es:'ONAD Remastered',en:'ONAD Remastered',color:'#4C9DB0',img:['assets/donnies/history-2022-office.webp'],rec:'2022',
   txt:'Animatrónicos remodelados y vuelta a Clickteam, esta vez con la historia como prioridad.',
   txtEn:'Remodeled animatronics and back to Clickteam, this time with the story first.'},
  {fecha:'2021',es:'Nace Donnie',en:'Donnie is born',color:'#FFB000',img:['assets/donnies/history-2021-first-model.webp'],rec:'2021',
   txt:'Un personaje de Roblox salta a FNaF: Donnie (Dog + Bonnie). Así empieza One Night at Donnie’s.',
   txtEn:'A Roblox character jumps into FNaF: Donnie (Dog + Bonnie). That is how One Night at Donnie’s begins.'}
];

(function(){
'use strict';
var shelf=document.getElementById('vhsShelf');if(!shelf)return;
var d=document.documentElement,en=function(){return d.getAttribute('lang')==='en'};
var esc=function(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})};
var snd=function(k,a){try{window.SFSound&&window.SFSound[k](a)}catch(e){}};
var calm=false;try{calm=matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){}

function renderShelf(){
  shelf.innerHTML=CINTAS.map(function(c,i){
    return '<button type="button" class="tape" data-i="'+i+'" style="--lbl:'+c.color+'" aria-label="'+esc((en()?'Play tape: ':'Reproducir cinta: ')+(en()?c.en:c.es)+' · '+c.fecha)+'">'+
      '<span class="tape-lbl"><b>'+esc(en()?c.en:c.es)+'</b><i>'+esc(c.fecha)+'</i></span><span class="tape-brand" aria-hidden="true">SF·VHS</span></button>';
  }).join('');
}

/* ── Reproductor ── */
var dlg=document.getElementById('vhsPlayer'),scr=document.getElementById('vhsScr'),img=document.getElementById('vhsImg'),
    cap=document.getElementById('vhsCap'),ttl=document.getElementById('vhsTitle'),clock=document.getElementById('vhsClock'),
    stamp=document.getElementById('vhsRec'),cur=-1,slide=0,tSlide=null,tClock=null,tType=null,secs=0,opener=null;
function fmt(s){return '0:'+('0'+Math.floor(s/60)).slice(-2)+':'+('0'+s%60).slice(-2)}
function typeText(t){
  clearInterval(tType);if(calm){cap.textContent=t;return}
  var n=0;cap.textContent='';tType=setInterval(function(){n+=2;cap.textContent=t.slice(0,n);if(n>=t.length)clearInterval(tType)},28);
}
function showSlide(){
  var c=CINTAS[cur],src=c.img[slide%c.img.length];
  img.classList.toggle('fit',!!c.fit);img.classList.toggle('wide',!!c.wide);img.src=src;img.alt=en()?c.en:c.es;
}
function play(i){
  cur=(i+CINTAS.length)%CINTAS.length;var c=CINTAS[cur];slide=0;secs=0;
  clearInterval(tSlide);clearInterval(tClock);
  scr.classList.remove('playing');scr.classList.add('loading');snd('insert');
  ttl.textContent=(en()?c.en:c.es)+' · '+c.fecha;stamp.textContent=c.rec||'';
  clock.textContent=fmt(0);cap.textContent='';
  setTimeout(function(){
    scr.classList.remove('loading');scr.classList.add('playing');showSlide();snd('static',200);
    typeText(en()?(c.txtEn||c.txt):c.txt);
    tClock=setInterval(function(){secs++;clock.textContent=fmt(secs)},1000);
    if(c.img.length>1)tSlide=setInterval(function(){slide++;scr.classList.add('glitch');setTimeout(function(){showSlide();scr.classList.remove('glitch')},160)},3800);
  },calm?50:900);
}
function open(i,btn){
  opener=btn||null;
  if(typeof dlg.showModal==='function'){if(!dlg.open)dlg.showModal()}else dlg.setAttribute('open','');
  play(i);
}
function close(){
  clearInterval(tSlide);clearInterval(tClock);clearInterval(tType);snd('eject');
  if(dlg.open&&typeof dlg.close==='function')dlg.close();else dlg.removeAttribute('open');
  scr.classList.remove('playing','loading');if(opener)opener.focus();
}
shelf.addEventListener('click',function(e){var b=e.target.closest('.tape');if(b)open(+b.dataset.i,b)});
document.getElementById('vhsEject').addEventListener('click',close);
document.getElementById('vhsPrev').addEventListener('click',function(){snd('click');play(cur-1)});
document.getElementById('vhsNext').addEventListener('click',function(){snd('click');play(cur+1)});
dlg.addEventListener('cancel',function(e){e.preventDefault();close()});
dlg.addEventListener('click',function(e){if(e.target===dlg)close()});
dlg.addEventListener('keydown',function(e){if(e.key==='ArrowLeft'){snd('click');play(cur-1)}else if(e.key==='ArrowRight'){snd('click');play(cur+1)}});
document.addEventListener('sf:lang',function(){renderShelf();if(dlg.open&&cur>=0){var c=CINTAS[cur];ttl.textContent=(en()?c.en:c.es)+' · '+c.fecha;clearInterval(tType);cap.textContent=en()?(c.txtEn||c.txt):c.txt}});
renderShelf();
})();
