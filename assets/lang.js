/* Static Forge · idioma de las subpáginas (español e inglés). Misma clave que la portada: sf-lang.
   El español es el contenido original de cada página, así que sin JS se lee entera en español.
   Cada texto traducible lleva su versión inglesa en data-en (admite HTML); los atributos, en
   data-en-alt, data-en-aria-label, data-en-title, data-en-content y data-en-placeholder.
   Los botones de idioma llevan data-setlang="es|en". Al cambiar se emite el evento "sf:lang". */
(function(){
'use strict';
var d=document.documentElement, ATTRS=['alt','aria-label','title','content','placeholder'];
function get(){try{return localStorage.getItem('sf-lang')}catch(e){return null}}
function save(v){try{localStorage.setItem('sf-lang',v)}catch(e){}}
function norm(l){return l==='en'?'en':'es'}   /* un 'ca' guardado de antes vuelve a español */

function apply(l){
  l=norm(l); d.setAttribute('lang',l);
  document.querySelectorAll('[data-en]').forEach(function(el){
    if(el.dataset.es==null) el.dataset.es=el.innerHTML;
    var v=l==='en'?el.dataset.en:el.dataset.es;
    if(el.innerHTML!==v) el.innerHTML=v;
  });
  ATTRS.forEach(function(a){
    document.querySelectorAll('[data-en-'+a+']').forEach(function(el){
      if(!el.hasAttribute('data-es-'+a)) el.setAttribute('data-es-'+a,el.getAttribute(a)||'');
      el.setAttribute(a,el.getAttribute((l==='en'?'data-en-':'data-es-')+a));
    });
  });
  document.querySelectorAll('[data-setlang]').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.setlang===l))});
  try{document.dispatchEvent(new CustomEvent('sf:lang',{detail:l}))}catch(e){}
}

document.addEventListener('click',function(e){
  var b=e.target.closest('[data-setlang]'); if(!b) return;
  save(b.dataset.setlang); apply(b.dataset.setlang);
});
window.sfLang={get:function(){return norm(d.getAttribute('lang'))},apply:apply};
apply(get()||d.getAttribute('lang'));
})();
