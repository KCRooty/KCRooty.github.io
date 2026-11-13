/* Static Forge · idioma de las subpáginas. Misma clave que la portada: sf-lang.
   El español es el contenido original de cada página, así que sin JS se lee entera en español.
   Cada texto traducible lleva su versión inglesa en data-en (admite HTML); los atributos, en
   data-en-alt, data-en-aria-label, data-en-title, data-en-content y data-en-placeholder.
   Los botones de idioma llevan data-setlang="es|en". Al cambiar se emite el evento "sf:lang".

   Más idiomas: una página con <html data-i18n="/ruta/i18n/"> carga <ruta>/<idioma>.json, un objeto
   {texto inglés exacto de data-en…: traducción}. Lo que no esté traducido sale en inglés (en
   catalán, euskera y gallego, en español). En esas páginas el selector es una lista con los 18. */
(function(){
'use strict';
var d=document.documentElement, ATTRS=['alt','aria-label','title','content','placeholder'];
var LANGS=[['es','Español'],['en','English'],['ca','Català'],['eu','Euskara'],['gl','Galego'],
  ['fr','Français'],['de','Deutsch'],['it','Italiano'],['pt','Português'],['pt-BR','Português (Brasil)'],
  ['nl','Nederlands'],['pl','Polski'],['ru','Русский'],['uk','Українська'],['tr','Türkçe'],
  ['ja','日本語'],['ko','한국어'],['zh-CN','简体中文']];
var CODES=LANGS.map(function(x){return x[0]});
var BASE=d.getAttribute('data-i18n');            /* null: página solo en español e inglés */
var cat={}, loading={};

function get(){try{return localStorage.getItem('sf-lang')}catch(e){return null}}
function save(v){try{localStorage.setItem('sf-lang',v)}catch(e){}}
function norm(l){
  if(!l) return 'es';
  if(CODES.indexOf(l)<0){                         /* pt_BR, zh-Hans-CN, fr-CA… */
    var low=String(l).replace('_','-').toLowerCase();
    if(low==='pt-br') l='pt-BR'; else if(low.indexOf('zh')===0) l='zh-CN'; else l=low.split('-')[0];
  }
  if(CODES.indexOf(l)<0) return 'es';
  if(!BASE && l!=='es' && l!=='en') return /^(ca|eu|gl)$/.test(l)?'es':'en';
  return l;
}
/* navegador: primer idioma soportado, solo en páginas con catálogos y si nunca se eligió uno */
function guess(){
  if(!BASE) return null;
  var ls=(navigator.languages&&navigator.languages.length)?navigator.languages:[navigator.language||''];
  for(var i=0;i<ls.length;i++){var n=norm(ls[i]); if(n!=='es'||/^es/i.test(ls[i])) return n}
  return null;
}
function tr(l,en){ var c=cat[l]; return (c&&c[en]!=null&&c[en]!=='')?c[en]:null }

function apply(l){
  l=norm(l); d.setAttribute('lang',l);
  var far=l!=='es'&&l!=='en', fb=/^(ca|eu|gl)$/.test(l)?'es':'en';
  if(far&&BASE&&!cat[l]) load(l);
  document.querySelectorAll('[data-en]').forEach(function(el){
    if(el.dataset.es==null) el.dataset.es=el.innerHTML;
    var v=l==='es'?el.dataset.es:l==='en'?el.dataset.en:(tr(l,el.dataset.en)||(fb==='es'?el.dataset.es:el.dataset.en));
    if(el.innerHTML!==v) el.innerHTML=v;
  });
  ATTRS.forEach(function(a){
    document.querySelectorAll('[data-en-'+a+']').forEach(function(el){
      if(!el.hasAttribute('data-es-'+a)) el.setAttribute('data-es-'+a,el.getAttribute(a)||'');
      var es=el.getAttribute('data-es-'+a), en=el.getAttribute('data-en-'+a);
      el.setAttribute(a,l==='es'?es:l==='en'?en:(tr(l,en)||(fb==='es'?es:en)));
    });
  });
  /* bloques con una copia por idioma (data-only): fuera del español se ve la inglesa */
  d.setAttribute('data-base',l==='es'||(far&&fb==='es')?'es':'en');
  document.querySelectorAll('[data-setlang]').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.setlang===l))});
  document.querySelectorAll('select.langsel').forEach(function(s){s.value=l});
  try{document.dispatchEvent(new CustomEvent('sf:lang',{detail:l}))}catch(e){}
}

function load(l){
  if(loading[l]) return; loading[l]=1;
  fetch(BASE+l+'.json').then(function(r){return r.ok?r.json():{}}).then(function(j){
    cat[l]=j||{}; if(norm(d.getAttribute('lang'))===l) apply(l);
  }).catch(function(){cat[l]={}});
}

/* en páginas con catálogos, una lista con todos los idiomas en lugar de las dos banderas */
if(BASE){
  document.querySelectorAll('.langsw').forEach(function(sw){
    var sel=document.createElement('select');
    sel.className='langsel';
    sel.setAttribute('aria-label','Idioma · Language');
    LANGS.forEach(function(x){var o=document.createElement('option');o.value=x[0];o.textContent=x[1];o.lang=x[0];sel.appendChild(o)});
    sel.addEventListener('change',function(){save(sel.value);apply(sel.value)});
    sw.querySelectorAll('[data-setlang]').forEach(function(b){b.hidden=true});
    sw.appendChild(sel);
  });
}

document.addEventListener('click',function(e){
  var b=e.target.closest('[data-setlang]'); if(!b) return;
  save(b.dataset.setlang); apply(b.dataset.setlang);
});
window.sfLang={get:function(){return norm(d.getAttribute('lang'))},apply:apply,langs:CODES};
apply(get()||guess()||d.getAttribute('lang'));
})();
