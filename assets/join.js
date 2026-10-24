/* Static Forge · formulario para unirse.
   Uso: <form class="joinf" data-join="sf|linux|forgeos" novalidate></form> y cargar este script.
   Las solicitudes van a la API del foro (POST /api/apply). Las listas de valores tienen que
   coincidir con TRACKS en static-forge-forum/src/worker.js. */
(function () {
  'use strict';
  var forms = document.querySelectorAll('form[data-join]');
  if (!forms.length) return;

  var host = location.hostname;
  var API = (host === '127.0.0.1' || host === 'localhost')
    ? 'http://127.0.0.1:8787'
    : 'https://static-forge-foro.staticforge.workers.dev';
  var MAIL = ['StaticForge', 'proton.me'].join('@');

  /* ── Textos ── */
  var S = {
    es: {
      'opt': '(opcional)',
      'lg.you': 'Quién eres', 'lg.what': 'Qué quieres hacer', 'lg.exp': 'Tu experiencia',
      'lg.areas': 'Qué se te da bien', 'lg.why': 'Por qué',
      'f.name': 'Nombre o alias', 'h.name': 'Como quieras que te llamemos. No hace falta tu nombre real.',
      'f.age': 'Edad', 'age.pick': 'Elige un tramo',
      'age.u14': 'Menos de 14', 'age.14-15': '14 o 15', 'age.16-17': '16 o 17', 'age.18-24': 'De 18 a 24', 'age.25+': '25 o más',
      'f.guardian': 'Tengo permiso de mi madre, padre o tutor para enviar esta solicitud.',
      'f.contact': 'Cómo te escribimos', 'h.contact': 'Correo, usuario de Discord u otra forma de contactarte.',
      'f.links': 'Redes y portfolio', 'h.links': 'Un enlace por línea: redes, portfolio, GitHub, ArtStation, SoundCloud…',
      'f.who': 'Cuéntanos quién eres', 'h.who': 'Qué haces, qué has hecho y con qué herramientas trabajas.',
      'f.mode': 'Qué te gustaría hacer',
      'mode.join': 'Unirme a proyectos de Static Forge', 'mode.own': 'Traer un proyecto mío para publicarlo con Static Forge', 'mode.both': 'Las dos cosas',
      'f.projects': 'Proyectos que te interesan',
      'p.donnies': "Donnie's Origins", 'p.fnafas': 'FNAF AS', 'p.linux': 'Static Linux', 'p.forgeos': 'Forge OS',
      'p.winforge': 'WinForge', 'p.rck': 'RCK', 'p.kcdl': 'KC Downloader', 'p.any': 'Donde haga falta',
      'f.own': 'Tu proyecto', 'h.own': 'Qué es, en qué punto está y un enlace si lo tienes.',
      'f.areas': 'Marca todo lo que haces',
      'a.art2d': 'Arte 2D', 'a.art3d': 'Arte 3D', 'a.music': 'Producción musical', 'a.code': 'Programación',
      'a.gamedev': 'Desarrollo de juegos y apps', 'a.voice': 'Doblaje y voz', 'a.writing': 'Guion y escritura',
      'a.video': 'Vídeo y edición', 'a.other': 'Otra cosa (cuéntalo arriba)',
      'f.why': 'Por qué quieres unirte', 'h.why': 'Qué te atrae y qué te gustaría aportar.',
      'f.avail': 'Tiempo que podrías dedicarle',
      'av.': 'Sin especificar', 'av.month': 'Unas horas al mes', 'av.week': 'Unas horas a la semana',
      'av.lots': 'Bastante tiempo', 'av.depends': 'Depende de la época',
      'f.consent': 'He leído el aviso de privacidad y acepto que Static Forge guarde estos datos para valorar mi solicitud.',
      'privacy': 'Aviso de privacidad: estos datos solo sirven para valorar tu solicitud y escribirte. Solo los lee KCRooty (Core) y no se comparten con nadie. Se borran solos a los 6 meses. Si quieres borrarlos antes, escribe a ',
      'send': 'Enviar solicitud', 'sending': 'Enviando…',
      'done.h': 'Solicitud enviada', 'done.p': 'Ha llegado bien. Si encaja, te escribiremos al contacto que has dejado.', 'done.again': 'Enviar otra',
      'e.req': 'Este campo hace falta.', 'e.min': 'Escribe al menos {n} caracteres.', 'e.pick': 'Elige una opción.',
      'e.checks': 'Marca al menos una opción.', 'e.consent': 'Tienes que aceptar el aviso para enviar la solicitud.',
      'e.guardian': 'Con menos de 14 años necesitas este permiso.', 'e.fix': 'Revisa los campos marcados.',
      'e.net': 'No se ha podido conectar con el servidor. Comprueba tu conexión y vuelve a intentarlo.',
      'e.slow': 'Has enviado varias solicitudes hoy. Prueba mañana o escribe a ' + MAIL + '.',
      // Static Linux
      'lx.areas.1': 'Paquetes y repositorio', 'lx.areas.2': 'ISO e instalador', 'lx.areas.3': 'sl-detect y soporte de hardware',
      'lx.areas.4': 'Escritorios, temas y acentos', 'lx.areas.5': 'Documentación y wiki', 'lx.areas.6': 'Probar en hardware real',
      'lx.areas.7': 'Traducción', 'lx.areas.8': 'Otra cosa (cuéntalo arriba)',
      'f.exp': 'Experiencia con Linux',
      'exp.new': 'Estoy empezando con Linux', 'exp.daily': 'Uso Linux a diario', 'exp.arch': 'Uso Arch o una derivada', 'exp.maint': 'Empaqueto o mantengo software',
      'f.hw': 'Equipos donde podrías probar', 'h.hw': 'Por ejemplo: portátil con gráfica Intel, sobremesa con NVIDIA.',
      'lx.why': 'Por qué te interesa Static Linux',
      // Forge OS
      'fo.areas.1': 'Kernel: memoria, procesos, planificador', 'fo.areas.2': 'Drivers', 'fo.areas.3': 'Sistemas de archivos',
      'fo.areas.4': 'Userland: Ember, Bellows, Crucible, Anvil', 'fo.areas.5': 'libc y portar programas', 'fo.areas.6': 'Herramientas y compilación',
      'fo.areas.7': 'Documentación', 'fo.areas.8': 'Pruebas y depuración',
      'f.rust': 'Nivel de Rust',
      'rust.none': 'No he usado Rust', 'rust.basic': 'Lo básico', 'rust.ok': 'Me muevo bien', 'rust.nostd': 'He hecho no_std o embebido',
      'f.lowlevel': 'Experiencia en bajo nivel', 'h.lowlevel': 'C, ensamblador, OSDev, emuladores, lo que sea.',
      'fo.why': 'Por qué te interesa Forge OS'
    },
    en: {
      'opt': '(optional)',
      'lg.you': 'About you', 'lg.what': 'What you want to do', 'lg.areas': 'What you are good at', 'lg.why': 'Why',
      'f.name': 'Name or alias', 'h.name': 'Whatever you want us to call you. Your real name is not needed.',
      'f.age': 'Age', 'age.pick': 'Pick a range',
      'age.u14': 'Under 14', 'age.14-15': '14 or 15', 'age.16-17': '16 or 17', 'age.18-24': '18 to 24', 'age.25+': '25 or older',
      'f.guardian': 'My mother, father or guardian has given me permission to send this application.',
      'f.contact': 'How can we reach you', 'h.contact': 'Email, Discord username or another way to contact you.',
      'f.links': 'Social media and portfolio', 'h.links': 'One link per line: social media, portfolio, GitHub, ArtStation, SoundCloud…',
      'f.who': 'Tell us who you are', 'h.who': 'What you do, what you have made and the tools you work with.',
      'f.mode': 'What would you like to do',
      'mode.join': 'Join Static Forge projects', 'mode.own': 'Bring a project of mine to publish with Static Forge', 'mode.both': 'Both',
      'f.projects': 'Projects you are interested in', 'p.any': 'Wherever help is needed',
      'f.own': 'Your project', 'h.own': 'What it is, how far along it is, and a link if you have one.',
      'f.areas': 'Tick everything you do',
      'a.art2d': '2D art', 'a.art3d': '3D art', 'a.music': 'Music production', 'a.code': 'Programming',
      'a.gamedev': 'Game and app development', 'a.voice': 'Voice acting', 'a.writing': 'Scripts and writing',
      'a.video': 'Video and editing', 'a.other': 'Something else (tell us above)',
      'f.why': 'Why do you want to join', 'h.why': 'What draws you in and what you would like to bring.',
      'f.avail': 'Time you could spend on it',
      'av.': 'Not specified', 'av.month': 'A few hours a month', 'av.week': 'A few hours a week', 'av.lots': 'Quite a lot', 'av.depends': 'It depends on the time of year',
      'f.consent': 'I have read the privacy notice and agree that Static Forge keeps this data to review my application.',
      'privacy': 'Privacy notice: this data is only used to review your application and get back to you. Only KCRooty (Core) reads it and it is never shared. It is deleted automatically after 6 months. To have it deleted sooner, write to ',
      'send': 'Send application', 'sending': 'Sending…',
      'done.h': 'Application sent', 'done.p': 'It arrived. If it is a fit, we will write to the contact you left.', 'done.again': 'Send another',
      'e.req': 'This field is required.', 'e.min': 'Write at least {n} characters.', 'e.pick': 'Pick an option.',
      'e.checks': 'Tick at least one option.', 'e.consent': 'You need to accept the notice to send the application.',
      'e.guardian': 'Under 14 you need this permission.', 'e.fix': 'Check the highlighted fields.',
      'e.net': 'Could not reach the server. Check your connection and try again.',
      'e.slow': 'You have sent several applications today. Try tomorrow or write to ' + MAIL + '.'
    },
    ca: {
      'opt': '(opcional)',
      'lg.you': 'Qui ets', 'lg.what': 'Què vols fer', 'lg.areas': 'Què se’t dona bé', 'lg.why': 'Per què',
      'f.name': 'Nom o àlies', 'h.name': 'Com vulguis que et diguem. No cal el teu nom real.',
      'f.age': 'Edat', 'age.pick': 'Tria una franja',
      'age.u14': 'Menys de 14', 'age.14-15': '14 o 15', 'age.16-17': '16 o 17', 'age.18-24': 'De 18 a 24', 'age.25+': '25 o més',
      'f.guardian': 'Tinc permís de la meva mare, pare o tutor per enviar aquesta sol·licitud.',
      'f.contact': 'Com t’escrivim', 'h.contact': 'Correu, usuari de Discord o una altra manera de contactar-te.',
      'f.links': 'Xarxes i portfolio', 'h.links': 'Un enllaç per línia: xarxes, portfolio, GitHub, ArtStation, SoundCloud…',
      'f.who': 'Explica’ns qui ets', 'h.who': 'Què fas, què has fet i amb quines eines treballes.',
      'f.mode': 'Què t’agradaria fer',
      'mode.join': 'Unir-me a projectes de Static Forge', 'mode.own': 'Portar un projecte meu per publicar-lo amb Static Forge', 'mode.both': 'Les dues coses',
      'f.projects': 'Projectes que t’interessen', 'p.any': 'On faci falta',
      'f.own': 'El teu projecte', 'h.own': 'Què és, en quin punt està i un enllaç si en tens.',
      'f.areas': 'Marca tot el que fas',
      'a.art2d': 'Art 2D', 'a.art3d': 'Art 3D', 'a.music': 'Producció musical', 'a.code': 'Programació',
      'a.gamedev': 'Desenvolupament de jocs i apps', 'a.voice': 'Doblatge i veu', 'a.writing': 'Guió i escriptura',
      'a.video': 'Vídeo i edició', 'a.other': 'Una altra cosa (explica-ho a dalt)',
      'f.why': 'Per què vols unir-t’hi', 'h.why': 'Què t’atrau i què t’agradaria aportar.',
      'f.avail': 'Temps que hi podries dedicar',
      'av.': 'Sense especificar', 'av.month': 'Unes hores al mes', 'av.week': 'Unes hores a la setmana', 'av.lots': 'Bastant de temps', 'av.depends': 'Depèn de l’època',
      'f.consent': 'He llegit l’avís de privacitat i accepto que Static Forge guardi aquestes dades per valorar la meva sol·licitud.',
      'privacy': 'Avís de privacitat: aquestes dades només serveixen per valorar la teva sol·licitud i escriure’t. Només les llegeix KCRooty (Core) i no es comparteixen amb ningú. S’esborren soles als 6 mesos. Si vols que s’esborrin abans, escriu a ',
      'send': 'Enviar la sol·licitud', 'sending': 'Enviant…',
      'done.h': 'Sol·licitud enviada', 'done.p': 'Ha arribat bé. Si encaixa, t’escriurem al contacte que has deixat.', 'done.again': 'Enviar-ne una altra',
      'e.req': 'Aquest camp és necessari.', 'e.min': 'Escriu almenys {n} caràcters.', 'e.pick': 'Tria una opció.',
      'e.checks': 'Marca almenys una opció.', 'e.consent': 'Has d’acceptar l’avís per enviar la sol·licitud.',
      'e.guardian': 'Amb menys de 14 anys necessites aquest permís.', 'e.fix': 'Revisa els camps marcats.',
      'e.net': 'No s’ha pogut connectar amb el servidor. Comprova la connexió i torna-ho a provar.',
      'e.slow': 'Avui ja has enviat diverses sol·licituds. Prova demà o escriu a ' + MAIL + '.'
    }
  };
  var root = document.documentElement;
  function lang() { var l = root.getAttribute('lang'); return S[l] ? l : 'es'; }
  function t(k) { var l = S[lang()]; return (l[k] != null ? l[k] : S.es[k] != null ? S.es[k] : k); }

  /* ── Definición de cada formulario ── */
  var AGES = ['u14', '14-15', '16-17', '18-24', '25+'];
  var AVAIL = ['', 'month', 'week', 'lots', 'depends'];
  function opts(keys, prefix) { return keys.map(function (k) { return { v: k, k: prefix + k }; }); }
  function numbered(keys, prefix) { return keys.map(function (k, i) { return { v: k, k: prefix + (i + 1) }; }); }

  var YOU = [
    { type: 'text', name: 'name', label: 'f.name', hint: 'h.name', min: 2, max: 60, ac: 'nickname' },
    { type: 'select', name: 'age', label: 'f.age', options: opts(AGES, 'age.'), placeholder: 'age.pick' },
    { type: 'check', name: 'guardian', label: 'f.guardian', showIf: function (v) { return v.age === 'u14'; } },
    { type: 'text', name: 'contact', label: 'f.contact', hint: 'h.contact', min: 3, max: 120 },
    { type: 'area', name: 'links', label: 'f.links', hint: 'h.links', min: 0, max: 800, rows: 3, optional: true },
    { type: 'area', name: 'who', label: 'f.who', hint: 'h.who', min: 20, max: 2000, rows: 5 }
  ];
  function WHY(label) {
    return [
      { type: 'area', name: 'why', label: label, hint: 'h.why', min: 20, max: 2000, rows: 5 },
      { type: 'select', name: 'avail', label: 'f.avail', options: opts(AVAIL, 'av.'), optional: true }
    ];
  }
  var TRACKS = {
    sf: [
      { legend: 'lg.you', fields: YOU },
      { legend: 'lg.what', fields: [
        { type: 'radios', name: 'mode', label: 'f.mode', options: opts(['join', 'own', 'both'], 'mode.') },
        { type: 'checks', name: 'projects', label: 'f.projects', options: opts(['donnies', 'fnafas', 'linux', 'forgeos', 'winforge', 'rck', 'kcdl', 'any'], 'p.'),
          showIf: function (v) { return v.mode === 'join' || v.mode === 'both'; } },
        { type: 'area', name: 'own', label: 'f.own', hint: 'h.own', min: 20, max: 2000, rows: 4,
          showIf: function (v) { return v.mode === 'own' || v.mode === 'both'; } }
      ] },
      { legend: 'lg.areas', fields: [
        { type: 'checks', name: 'areas', label: 'f.areas', options: opts(['art2d', 'art3d', 'music', 'code', 'gamedev', 'voice', 'writing', 'video', 'other'], 'a.') }
      ] },
      { legend: 'lg.why', fields: WHY('f.why') }
    ],
    linux: [
      { legend: 'lg.you', fields: YOU },
      { legend: 'lg.exp', fields: [
        { type: 'radios', name: 'exp', label: 'f.exp', options: opts(['new', 'daily', 'arch', 'maint'], 'exp.') },
        { type: 'text', name: 'hw', label: 'f.hw', hint: 'h.hw', min: 0, max: 300, optional: true }
      ] },
      { legend: 'lg.areas', fields: [
        { type: 'checks', name: 'areas', label: 'f.areas', options: numbered(['pkgs', 'iso', 'detect', 'desktops', 'docs', 'testing', 'i18n', 'other'], 'lx.areas.') }
      ] },
      { legend: 'lg.why', fields: WHY('lx.why') }
    ],
    forgeos: [
      { legend: 'lg.you', fields: YOU },
      { legend: 'lg.exp', fields: [
        { type: 'radios', name: 'rust', label: 'f.rust', options: opts(['none', 'basic', 'ok', 'nostd'], 'rust.') },
        { type: 'area', name: 'lowlevel', label: 'f.lowlevel', hint: 'h.lowlevel', min: 0, max: 1500, rows: 3, optional: true }
      ] },
      { legend: 'lg.areas', fields: [
        { type: 'checks', name: 'areas', label: 'f.areas', options: numbered(['kernel', 'drivers', 'fs', 'userland', 'libc', 'tooling', 'docs', 'testing'], 'fo.areas.') }
      ] },
      { legend: 'lg.why', fields: WHY('fo.why') }
    ]
  };

  /* ── Pintado ── */
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function J(k) { return '<span data-j="' + k + '">' + esc(t(k)) + '</span>'; }

  function fieldHtml(f, id) {
    var fid = id + '-' + f.name, hid = fid + '-h', eid = fid + '-e';
    var opt = f.optional ? ' <span class="jopt" data-j="opt">' + esc(t('opt')) + '</span>' : '';
    var hint = f.hint ? '<p class="jh" id="' + hid + '" data-j="' + f.hint + '">' + esc(t(f.hint)) + '</p>' : '';
    var err = '<p class="jerr" id="' + eid + '" aria-live="polite"></p>';
    var desc = (f.hint ? hid + ' ' : '') + eid;
    var req = f.optional ? '' : ' aria-required="true"';
    var wrap = '<div class="jf" data-field="' + f.name + '"' + (f.showIf ? ' hidden' : '') + '>';
    if (f.type === 'text') {
      return wrap + '<label for="' + fid + '">' + J(f.label) + opt + '</label>' + hint +
        '<input type="text" id="' + fid + '" name="' + f.name + '" maxlength="' + f.max + '"' + (f.ac ? ' autocomplete="' + f.ac + '"' : ' autocomplete="off"') +
        ' aria-describedby="' + desc + '"' + req + '>' + err + '</div>';
    }
    if (f.type === 'area') {
      return wrap + '<label for="' + fid + '">' + J(f.label) + opt + '</label>' + hint +
        '<textarea id="' + fid + '" name="' + f.name + '" rows="' + f.rows + '" maxlength="' + f.max + '" aria-describedby="' + desc + '"' + req + '></textarea>' + err + '</div>';
    }
    if (f.type === 'select') {
      var o = (f.placeholder ? '<option value="" data-j="' + f.placeholder + '">' + esc(t(f.placeholder)) + '</option>' : '') +
        f.options.map(function (x) { return '<option value="' + x.v + '" data-j="' + x.k + '">' + esc(t(x.k)) + '</option>'; }).join('');
      return wrap + '<label for="' + fid + '">' + J(f.label) + opt + '</label>' + hint +
        '<select id="' + fid + '" name="' + f.name + '" aria-describedby="' + desc + '"' + req + '>' + o + '</select>' + err + '</div>';
    }
    if (f.type === 'check') {
      return wrap + '<label class="jchk solo"><input type="checkbox" id="' + fid + '" name="' + f.name + '" aria-describedby="' + eid + '"' + req + '>' + J(f.label) + '</label>' + err + '</div>';
    }
    // radios / checks: grupo con su propia leyenda
    var kind = f.type === 'radios' ? 'radio' : 'checkbox';
    var items = f.options.map(function (x, i) {
      return '<label class="jchk"><input type="' + kind + '" name="' + f.name + '" value="' + x.v + '" id="' + fid + '-' + i + '">' + J(x.k) + '</label>';
    }).join('');
    return wrap + '<fieldset class="jgroup" aria-describedby="' + desc + '"><legend class="jq">' + J(f.label) + opt + '</legend>' + hint +
      '<div class="jchecks' + (kind === 'radio' ? ' one' : '') + '">' + items + '</div></fieldset>' + err + '</div>';
  }

  function build(form) {
    var track = form.getAttribute('data-join');
    var spec = TRACKS[track];
    if (!spec) return;
    var id = 'j' + track;
    var html = spec.map(function (sec) {
      return '<fieldset class="jsec"><legend data-j="' + sec.legend + '">' + esc(t(sec.legend)) + '</legend>' +
        sec.fields.map(function (f) { return fieldHtml(f, id); }).join('') + '</fieldset>';
    }).join('');
    html +=
      '<div class="jtrap" aria-hidden="true"><label>Web<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>' +
      '<div class="jfoot">' +
        '<p class="jprivacy"><span data-j="privacy">' + esc(t('privacy')) + '</span><a href="mailto:' + MAIL + '">' + MAIL + '</a>.</p>' +
        '<div class="jf" data-field="consent"><label class="jchk solo"><input type="checkbox" name="consent" id="' + id + '-consent" aria-describedby="' + id + '-consent-e" aria-required="true">' + J('f.consent') + '</label>' +
        '<p class="jerr" id="' + id + '-consent-e" aria-live="polite"></p></div>' +
        '<div class="jts" hidden></div>' +
        '<div class="jsend"><button type="submit" class="btn pri jbtn">' + J('send') + '</button><p class="jstatus" role="status" aria-live="polite"></p></div>' +
      '</div>';
    form.innerHTML = html;
    form.setAttribute('novalidate', '');

    var fields = [];
    spec.forEach(function (sec) { fields = fields.concat(sec.fields); });
    form._fields = fields;
    form.addEventListener('change', function () { sync(form); });
    form.addEventListener('input', function (e) {
      var w = e.target.closest('.jf');
      if (w && w.classList.contains('bad')) clearErr(w);
    });
    form.addEventListener('submit', function (e) { e.preventDefault(); submit(form, track); });
    sync(form);
  }

  function values(form) {
    var v = {};
    form._fields.forEach(function (f) {
      if (f.type === 'checks') {
        v[f.name] = [].map.call(form.querySelectorAll('input[name="' + f.name + '"]:checked'), function (x) { return x.value; });
      } else if (f.type === 'radios') {
        var c = form.querySelector('input[name="' + f.name + '"]:checked'); v[f.name] = c ? c.value : '';
      } else if (f.type === 'check') {
        v[f.name] = form.elements[f.name].checked;
      } else {
        v[f.name] = form.elements[f.name].value.trim();
      }
    });
    v.consent = form.elements.consent.checked;
    v.website = form.elements.website.value;
    return v;
  }

  function sync(form) {
    var v = values(form);
    form._fields.forEach(function (f) {
      if (!f.showIf) return;
      var w = form.querySelector('[data-field="' + f.name + '"]');
      var show = f.showIf(v);
      if (w.hidden === show) { w.hidden = !show; if (!show) clearErr(w); }
    });
  }

  function setErr(w, msg) {
    w.classList.add('bad');
    w.querySelector('.jerr').textContent = msg;
    w.querySelectorAll('input:not([type=hidden]),textarea,select').forEach(function (x) { x.setAttribute('aria-invalid', 'true'); });
  }
  function clearErr(w) {
    w.classList.remove('bad');
    var e = w.querySelector('.jerr'); if (e) e.textContent = '';
    w.querySelectorAll('[aria-invalid]').forEach(function (x) { x.removeAttribute('aria-invalid'); });
  }

  function validate(form, v) {
    var bad = [];
    form._fields.forEach(function (f) {
      var w = form.querySelector('[data-field="' + f.name + '"]');
      if (w.hidden) return;
      clearErr(w);
      var val = v[f.name], msg = '';
      if (f.type === 'text' || f.type === 'area') {
        if (!f.optional && !val) msg = t('e.req');
        else if (val && val.length < f.min) msg = t('e.min').replace('{n}', f.min);
      } else if (f.type === 'select' || f.type === 'radios') {
        if (!f.optional && !val) msg = t('e.pick');
      } else if (f.type === 'checks') {
        if (!val.length) msg = t('e.checks');
      } else if (f.type === 'check') {
        if (!val) msg = t('e.guardian');
      }
      if (msg) { setErr(w, msg); bad.push(w); }
    });
    var cw = form.querySelector('[data-field="consent"]');
    clearErr(cw);
    if (!v.consent) { setErr(cw, t('e.consent')); bad.push(cw); }
    return bad;
  }

  function status(form, msg, kind) {
    var s = form.querySelector('.jstatus');
    s.textContent = msg || '';
    s.className = 'jstatus' + (kind ? ' ' + kind : '');
  }

  function submit(form, track) {
    if (form._busy) return;
    var v = values(form);
    var bad = validate(form, v);
    if (bad.length) {
      status(form, t('e.fix'), 'err');
      var first = bad[0].querySelector('input:not([type=hidden]),textarea,select');
      if (first) first.focus();
      return;
    }
    status(form, '');
    var payload = { track: track };
    form._fields.forEach(function (f) {
      var w = form.querySelector('[data-field="' + f.name + '"]');
      if (!w.hidden) payload[f.name] = v[f.name];
    });
    payload.consent = v.consent;
    payload.website = v.website;
    if (form._ts) payload.turnstile = form._tsToken || '';

    var btn = form.querySelector('.jbtn'), label = btn.querySelector('[data-j]');
    form._busy = true; btn.disabled = true; btn.setAttribute('aria-busy', 'true');
    label.setAttribute('data-j', 'sending'); label.textContent = t('sending');

    fetch(API + '/api/apply', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (d) { return { ok: r.ok, d: d }; }); })
      .then(function (res) {
        if (res.ok) { done(form, track); return; }
        var d = res.d || {};
        if (d.error === 'slow_down') status(form, t('e.slow'), 'err');
        else {
          var w = d.error && form.querySelector('[data-field="' + d.error + '"]');
          if (w && !w.hidden) { setErr(w, d.message || t('e.fix')); status(form, t('e.fix'), 'err'); }
          else status(form, d.message || t('e.net'), 'err');
        }
        if (form._ts && window.turnstile) { try { window.turnstile.reset(form._ts); } catch (e) {} }
      })
      .catch(function () { status(form, t('e.net'), 'err'); })
      .then(function () {
        form._busy = false; btn.disabled = false; btn.removeAttribute('aria-busy');
        if (label.isConnected) { label.setAttribute('data-j', 'send'); label.textContent = t('send'); }
      });
  }

  function done(form, track) {
    form.innerHTML = '<div class="jdone"><h3 tabindex="-1" data-j="done.h">' + esc(t('done.h')) + '</h3>' +
      '<p data-j="done.p">' + esc(t('done.p')) + '</p>' +
      '<button type="button" class="btn jbtn-again">' + J('done.again') + '</button></div>';
    form.querySelector('h3').focus();
    form.querySelector('.jbtn-again').addEventListener('click', function () {
      var f2 = form.cloneNode(false); form.parentNode.replaceChild(f2, form); build(f2); initTurnstile(f2);
      var first = f2.querySelector('input,textarea,select'); if (first) first.focus();
    });
  }

  /* ── Turnstile (solo si la API tiene clave configurada) ── */
  var sitekey = null, tsLoading = null;
  function initTurnstile(form) {
    if (!sitekey) return;
    var box = form.querySelector('.jts');
    if (!box) return;
    box.hidden = false;
    var render = function () {
      form._ts = window.turnstile.render(box, { sitekey: sitekey, callback: function (tok) { form._tsToken = tok; } });
    };
    if (window.turnstile) { render(); return; }
    if (!tsLoading) {
      tsLoading = new Promise(function (res) {
        var s = document.createElement('script');
        s.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit';
        s.async = true; s.onload = res; document.head.appendChild(s);
      });
    }
    tsLoading.then(render);
  }

  /* ── Cambio de idioma de la página ── */
  function relabel() {
    document.querySelectorAll('form[data-join] [data-j]').forEach(function (el) { el.textContent = t(el.getAttribute('data-j')); });
  }
  new MutationObserver(relabel).observe(root, { attributes: true, attributeFilter: ['lang'] });

  [].forEach.call(forms, build);
  fetch(API + '/api/config').then(function (r) { return r.json(); }).then(function (c) {
    if (c && c.turnstileSiteKey) { sitekey = c.turnstileSiteKey; document.querySelectorAll('form[data-join]').forEach(initTurnstile); }
  }).catch(function () {});
})();
