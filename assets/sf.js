/* Static Forge · controles compartidos de las subpáginas: tema, CRT y menú móvil.
   Usa las mismas claves de localStorage que index.html (sf-theme, sf-crt). */
(function(){
'use strict';
var d=document.documentElement;
function save(k,v){try{localStorage.setItem(k,v)}catch(e){}}

var themeBtn=document.getElementById('themeBtn');
function syncTheme(){
  var paper=d.getAttribute('data-theme')==='paper';
  themeBtn.setAttribute('aria-pressed',String(paper));
  themeBtn.setAttribute('aria-label',paper?'Tema: papel':'Tema: noche');
  themeBtn.textContent=paper?'NOCHE':'PAPEL';
  var m=document.querySelector('meta[name="theme-color"]'); if(m) m.setAttribute('content',paper?'#FBF1E3':'#14100C');
}
if(themeBtn){
  themeBtn.addEventListener('click',function(){
    var next=d.getAttribute('data-theme')==='paper'?'night':'paper';
    d.setAttribute('data-theme',next); save('sf-theme',next); syncTheme();
  });
  syncTheme();
}

var crtBtn=document.getElementById('crtBtn');
function syncCrt(){var on=d.getAttribute('data-crt')!=='off';crtBtn.setAttribute('aria-pressed',String(on));crtBtn.setAttribute('aria-label',on?'Efecto CRT activado':'Efecto CRT desactivado')}
if(crtBtn){
  crtBtn.addEventListener('click',function(){
    var next=d.getAttribute('data-crt')==='off'?'on':'off';
    d.setAttribute('data-crt',next); save('sf-crt',next); syncCrt();
  });
  syncCrt();
}

var menuBtn=document.getElementById('menuBtn'),links=document.getElementById('links');
if(menuBtn&&links){
  var setMenu=function(open){links.classList.toggle('open',open);menuBtn.setAttribute('aria-expanded',String(open))};
  menuBtn.addEventListener('click',function(){setMenu(!links.classList.contains('open'))});
  links.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&links.classList.contains('open')){setMenu(false);menuBtn.focus()}});
  document.addEventListener('click',function(e){if(!e.target.closest('.nav'))setMenu(false)});
}
})();
