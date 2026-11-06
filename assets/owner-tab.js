/* Pestaña «Solicitudes» en el menú, solo para la cuenta dueña del panel (hoy Core).
   No esconde nada por sí sola: la API comprueba la cuenta en cada petición (APPS_OWNER en el Worker),
   así que cualquier otra sesión, aunque fuerce la pestaña, recibe un 403. Aquí solo se decide si se ve.
   Usa la misma sesión que el foro (localStorage sf-forum-token). */
(function(){
'use strict';
var host=location.hostname, local=host==='127.0.0.1'||host==='localhost';
var API=local?'http://127.0.0.1:8787':'https://static-forge-foro.staticforge.workers.dev';

function list(){return document.getElementById('links')||document.querySelector('ul.tb-nav')}
function remove(){var li=document.getElementById('sfOwnerTab');if(li)li.remove()}
function token(){try{return localStorage.getItem('sf-forum-token')}catch(e){return null}}

function show(){
  var ul=list(); if(!ul||document.getElementById('sfOwnerTab')) return;
  if(ul.querySelector('a[href$="solicitudes.html"]')) return; /* el propio panel ya la lleva */
  var li=document.createElement('li'); li.id='sfOwnerTab';
  var a=document.createElement('a'); a.href='/solicitudes.html'; a.textContent='Solicitudes';
  a.setAttribute('data-en','Requests');
  li.appendChild(a); ul.appendChild(li);
  /* Cuántas hay sin mirar. */
  fetch(API+'/api/applications?status=nueva',{headers:{'Authorization':'Bearer '+token()}})
    .then(function(r){return r.ok?r.json():null})
    .then(function(d){
      var n=d&&d.applications?d.applications.length:0;
      if(n){var b=document.createElement('b');b.className='owner-new';b.textContent=' ('+n+')';
        b.setAttribute('aria-label',n+(n===1?' nueva':' nuevas'));a.appendChild(b)}
    }).catch(function(){});
}

/* user: el objeto de /api/me o del login (apps=true solo para la cuenta dueña). */
function sync(user){if(user&&user.apps) show(); else remove()}
window.sfOwnerTab=sync;

if(!token()) return;
fetch(API+'/api/me',{headers:{'Authorization':'Bearer '+token()}})
  .then(function(r){return r.ok?r.json():null})
  .then(function(d){sync(d&&d.user)})
  .catch(function(){});
})();
