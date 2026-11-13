#!/usr/bin/env python3
"""Static Linux · genera linux/galeria/ y linux/descargar/.

    python3 linux/_paginas.py

La cabecera, el pie y el CSS salen de linux/index.html y linux/sl.css (a través
de blog/_build.py), así las tres páginas no se separan. Los datos de cada tema
son los de branding/themes/<id>/theme.conf del repo de Static Linux: si cambia
una paleta o llega un tema nuevo, se toca TEMAS y se vuelve a ejecutar.
Las capturas: img/temas/<id>.webp (1280x720) y img/temas/mini/<id>.webp (640x360).
Jekyll no publica los archivos que empiezan por "_".
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "blog"))
from _build import document, esc  # noqa: E402

# id, nombre es/en, modo, estilo, paleta (bg, surface, line, text, accent, danger, warning),
# crédito del fondo es/en
TEMAS = [
    ("ambar", "Ámbar", "Amber", "dark", "minimal",
     ["262321", "302C29", "4A443F", "EBDDBF", "E0A84F", "EB6F68", "D8A657"],
     "Hokusai, «Tormenta bajo el Fuji» · tema por defecto", "Hokusai, Storm below Mount Fuji · default theme"),
    ("papel", "Papel", "Paper", "light", "minimal",
     ["F1E9D2", "E8DDBF", "CDBF9C", "2A2822", "666211", "A1271B", "845600"],
     "Hokusai, «Fujimigahara en Owari»", "Hokusai, Fujimigahara in Owari"),
    ("nordico", "Nórdico", "Nordic", "dark", "minimal",
     ["2B303B", "343A47", "465063", "E5E9F0", "88C0D0", "E48D95", "EBCB8B"],
     "Hiroshige, «Nieve al anochecer en Kanbara»", "Hiroshige, Evening Snow at Kanbara"),
    ("bosque", "Bosque", "Forest", "dark", "minimal",
     ["1C211E", "252B27", "38413B", "DCE2DA", "9BC4A0", "E0857A", "D9C27A"],
     "Hiroshige, «Lluvia de primavera en Tsuchiyama»", "Hiroshige, Spring Rain at Tsuchiyama"),
    ("sakura", "Sakura", "Sakura", "dark", "minimal",
     ["211B20", "2C2429", "45363F", "F3E6EA", "F2A7BC", "F07F7F", "F1C27D"],
     "Hokusai, «El Fuji desde Gotenyama»", "Hokusai, Fuji from Gotenyama"),
    ("violeta", "Violeta", "Violet", "dark", "minimal",
     ["14121D", "1D1A2A", "322D48", "E7E3F7", "8F86F2", "F2848F", "EFC97A"],
     "montañas al anochecer, dibujado por código (provisional)", "ridges at dusk, drawn by code (provisional)"),
    ("aero", "Aero", "Aero", "light", "aero",
     ["EAF4FB", "FFFFFF", "A9CBE4", "0F2537", "1667A8", "B3261E", "845600"],
     "cielo y burbujas, dibujado por código", "sky and bubbles, drawn by code"),
    ("ventanas", "Ventanas", "Ventanas", "dark", "ventanas",
     ["202020", "2B2B2B", "3D3D3D", "F3F3F3", "4CC2FF", "FF99A4", "FCE100"],
     "cintas de luz, dibujado por código", "light ribbons, drawn by code"),
    ("nube", "Nube", "Cloud", "light", "estante",
     ["EEF2F8", "FFFFFF", "D3DBE7", "1B1F26", "0B57D0", "B3261E", "845600"],
     "nubes y colinas, dibujado por código", "clouds and hills, drawn by code"),
]
MODO = {"dark": ("oscuro", "dark"), "light": ("claro", "light")}
ESTILOS = [
    ("minimal", "barra fina arriba", "thin top bar"),
    ("aero", "brillo Frutiger Aero", "Frutiger Aero gloss"),
    ("ventanas", "barra al estilo Windows", "Windows-like taskbar"),
    ("estante", "lanzador y estante", "launcher and shelf"),
]
SWATCH = [("fondo", "background"), ("superficie", "surface"), ("línea", "line"), ("texto", "text"),
          ("acento", "accent"), ("peligro", "danger"), ("aviso", "warning")]


def btn(group: str, value: str, es: str, en: str, n: int, on: bool = False) -> str:
    return (f'<li><button type="button" class="fbtn" data-f="{group}" data-v="{value}" aria-pressed="{str(on).lower()}">'
            f'<span data-en="{esc(en)}">{esc(es)}</span><small>{n}</small></button></li>')


def galeria() -> None:
    n = len(TEMAS)
    count = lambda k, v: sum(1 for t in TEMAS if (t[3] if k == "mode" else t[4]) == v)
    side = f'''<aside class="side" aria-label="Filtros" data-en-aria-label="Filters">
  <div><h2 data-en="desktop">escritorio</h2><ul>
    <li><button type="button" class="fbtn" aria-pressed="true" disabled><span>XFCE</span><small>{n}</small></button></li>
    <li><button type="button" class="fbtn" disabled><span>KDE Plasma</span><small data-en="soon">pronto</small></button></li>
    <li><button type="button" class="fbtn" disabled><span>Hyprland</span><small data-en="soon">pronto</small></button></li>
    <li><button type="button" class="fbtn" disabled><span>Openbox</span><small data-en="soon">pronto</small></button></li>
  </ul></div>
  <div><h2 data-en="mode">modo</h2><ul>
    {btn("mode", "all", "Todos", "All", n, True)}
    {btn("mode", "dark", "Oscuros", "Dark", count("mode", "dark"))}
    {btn("mode", "light", "Claros", "Light", count("mode", "light"))}
  </ul></div>
  <div><h2 data-en="style">estilo</h2><ul>
    {btn("style", "all", "Todos", "All", n, True)}
    {"".join(btn("style", s, s, s, count("style", s)) for s, _, _ in ESTILOS)}
  </ul></div>
</aside>'''
    cards = []
    for i, (tid, es, en, mode, style, pal, c_es, c_en) in enumerate(TEMAS):
        m_es, m_en = MODO[mode]
        stripes = "".join(f'<i style="background:#{h}"></i>' for h in pal)
        cards.append(f'''<article class="tcard" id="{tid}" data-mode="{mode}" data-style="{style}" data-i="{i}">
  <button type="button" class="open" aria-label="Ampliar {esc(es)}" data-en-aria-label="Enlarge {esc(en)}"><img src="/linux/img/temas/mini/{tid}.webp" width="640" height="360" loading="{"eager" if i < 3 else "lazy"}" alt="Escritorio XFCE con el tema {esc(es)}" data-en-alt="XFCE desktop with the {esc(en)} theme"></button>
  <div class="tc-b">
    <div class="tc-t"><h3 data-en="{esc(en)}">{esc(es)}</h3><code>sl-theme {tid}</code></div>
    <div class="chipsx"><span data-en="{m_en}">{m_es}</span><span>style={style}</span><span>XFCE</span></div>
    <div class="pal" aria-hidden="true">{stripes}</div>
    <p class="tc-c" data-en="{esc(c_en)}">{esc(c_es)}</p>
  </div>
</article>''')
    data = [{"id": t[0], "es": t[1], "en": t[2], "mode": t[3], "style": t[4], "pal": t[5], "ces": t[6], "cen": t[7]}
            for t in TEMAS]
    body = f'''<header class="gal-head">
  <p class="label" data-en="gallery">galería</p>
  <h1 data-en="Every theme, as it looks">Todos los temas, tal cual se ven</h1>
  <p class="intro" data-en="Real screenshots of Static Linux on XFCE, one per theme. Filter by mode or style, open any of them to see its palette, and apply it with the command under the name or from the welcome app. KDE Plasma, Hyprland and Openbox will get their own screenshots as the themes reach them.">Capturas reales de Static Linux en XFCE, una por tema. Filtra por modo o estilo, abre cualquiera para ver su paleta y aplícalo con la orden que hay bajo el nombre o desde la bienvenida. KDE Plasma, Hyprland y Openbox tendrán sus capturas cuando los temas lleguen a ellos.</p>
</header>
<div class="gal-layout">
{side}
<div>
<div class="cards" id="cards">
{chr(10).join(cards)}
</div>
<p class="empty" id="empty" hidden data-en="No theme matches both filters yet.">Ningún tema cumple los dos filtros todavía.</p>
</div>
</div>
<dialog class="lb" id="lb" aria-labelledby="lb-name">
  <img id="lb-img" src="" width="1280" height="720" alt="">
  <div class="lb-b">
    <div class="lb-meta">
      <h2 id="lb-name"></h2>
      <div class="chipsx" id="lb-chips"></div>
      <div class="lb-sw" id="lb-sw"></div>
      <p class="tc-c" id="lb-cred"></p>
      <p class="lb-cmd" id="lb-cmd"></p>
    </div>
    <div class="lb-nav">
      <button type="button" id="lb-prev" aria-label="Anterior" data-en-aria-label="Previous">←</button>
      <button type="button" id="lb-next" aria-label="Siguiente" data-en-aria-label="Next">→</button>
      <button type="button" id="lb-close" aria-label="Cerrar" data-en-aria-label="Close">✕</button>
    </div>
  </div>
</dialog>'''
    sw = json.dumps(SWATCH, ensure_ascii=False)
    scripts = f'''<script>
(function(){{
var T={json.dumps(data, ensure_ascii=False)}, SW={sw}, MODE={{dark:["oscuro","dark"],light:["claro","light"]}};
var f={{mode:"all",style:"all"}}, cards=[].slice.call(document.querySelectorAll(".tcard")), cur=0, lb=document.getElementById("lb");
function en(){{return document.documentElement.lang==="en"}}
function filter(){{
  var shown=0;
  cards.forEach(function(c){{var ok=(f.mode==="all"||c.dataset.mode===f.mode)&&(f.style==="all"||c.dataset.style===f.style);c.hidden=!ok;if(ok)shown++}});
  document.getElementById("empty").hidden=shown>0;
}}
document.querySelectorAll(".fbtn[data-f]").forEach(function(b){{
  b.addEventListener("click",function(){{
    f[b.dataset.f]=b.dataset.v;
    document.querySelectorAll('.fbtn[data-f="'+b.dataset.f+'"]').forEach(function(o){{o.setAttribute("aria-pressed",String(o===b))}});
    filter();
  }});
}});
function visible(){{return cards.filter(function(c){{return !c.hidden}}).map(function(c){{return +c.dataset.i}})}}
function show(i){{
  cur=i; var t=T[i], E=en(), img=document.getElementById("lb-img");
  img.src="/linux/img/temas/"+t.id+".webp"; img.alt=(E?"XFCE desktop with the "+t.en+" theme":"Escritorio XFCE con el tema "+t.es);
  document.getElementById("lb-name").textContent=E?t.en:t.es;
  document.getElementById("lb-chips").innerHTML="<span>"+MODE[t.mode][E?1:0]+"</span><span>style="+t.style+"</span><span>XFCE</span>";
  document.getElementById("lb-sw").innerHTML=t.pal.map(function(h,k){{return '<div><i style="background:#'+h+'"></i>'+SW[k][E?1:0]+' #'+h+'</div>'}}).join("");
  document.getElementById("lb-cred").textContent=(E?"Wallpaper: ":"Fondo: ")+(E?t.cen:t.ces);
  document.getElementById("lb-cmd").textContent="$ sl-theme "+t.id;
  if(history.replaceState) history.replaceState(null,"","#"+t.id);
}}
function step(d){{var v=visible(),k=v.indexOf(cur);if(k<0)k=0;show(v[(k+d+v.length)%v.length])}}
cards.forEach(function(c){{c.querySelector(".open").addEventListener("click",function(){{show(+c.dataset.i);lb.showModal()}})}});
document.getElementById("lb-prev").onclick=function(){{step(-1)}};
document.getElementById("lb-next").onclick=function(){{step(1)}};
document.getElementById("lb-close").onclick=function(){{lb.close()}};
lb.addEventListener("click",function(e){{if(e.target===lb)lb.close()}});
lb.addEventListener("close",function(){{if(history.replaceState)history.replaceState(null,"",location.pathname)}});
lb.addEventListener("keydown",function(e){{if(e.key==="ArrowRight")step(1);else if(e.key==="ArrowLeft")step(-1)}});
document.addEventListener("sf:lang",function(){{if(lb.open)show(cur)}});
var h=location.hash.slice(1);
T.forEach(function(t,i){{if(t.id===h){{show(i);lb.showModal()}}}});
}})();
</script>
'''
    out = HERE / "galeria" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(document("Galería · Static Linux", "Gallery · Static Linux",
                            "Todos los temas de Static Linux con capturas reales, su paleta y la orden para aplicarlos.",
                            "Every Static Linux theme in real screenshots, with its palette and the command to apply it.",
                            "/linux/galeria/", body, scripts), encoding="utf-8")


def descargar() -> None:
    body = '''<header class="dl-hero">
  <p class="label" data-en="download">descargar</p>
  <h1 data-en="Download Static Linux">Descarga Static Linux</h1>
  <p class="intro" data-en="One 64-bit ISO (x86_64, UEFI) that boots straight into the installer. You pick the desktop, theme, style, flavors and privacy profile while installing.">Una ISO de 64 bits (x86_64, UEFI) que arranca directamente en el instalador. El escritorio, el tema, el estilo, los sabores y el perfil de privacidad se eligen al instalar.</p>
  <div class="release">
    <p data-en="&lt;b&gt;There is no public ISO yet.&lt;/b&gt; The latest workshop build is &lt;code&gt;static-linux-2026.11.13-x86_64.iso&lt;/code&gt; and it installs from start to finish in a VM, but it still needs a network to install and has only been tested end to end with XFCE. It will be published signed when it is ready to use outside the workshop, and announced in the blog."><b>Todavía no hay ISO pública.</b> La última del taller es <code>static-linux-2026.11.13-x86_64.iso</code> y se instala de principio a fin en una máquina virtual, pero aún necesita red para instalar y solo se ha probado entera con XFCE. Se publicará firmada cuando esté lista para usarse fuera del taller, y se anunciará en el blog.</p>
    <a class="btn" href="/linux/blog/feed.xml" data-en="Follow by RSS">Seguir por RSS</a>
  </div>
</header>

<section id="espejos" aria-labelledby="h-mir">
  <p class="label" data-en="01 · where">01 · dónde</p>
  <h2 id="h-mir" data-en="Where it will be">Dónde estará</h2>
  <div class="mirrors">
    <article class="mirror"><h3>SourceForge</h3><p data-en="The main mirror: the ISO, its SHA256 sum and its GPG signature, side by side.">El espejo principal: la ISO, su suma SHA256 y su firma GPG, una al lado de la otra.</p><a class="btn" href="https://sourceforge.net/projects/static-linux/" target="_blank" rel="noopener" data-en="Project page ↗">Página del proyecto ↗</a></article>
    <article class="mirror"><h3>GitHub Releases</h3><p data-en="The release notes of each version: changes, fixes and known issues, with links to the files.">Las notas de cada versión: cambios, arreglos y problemas conocidos, con enlaces a los archivos.</p><a class="btn" href="https://github.com/KCRooty/static-linux/releases" target="_blank" rel="noopener" data-en="Releases ↗">Versiones ↗</a></article>
    <article class="mirror"><h3 data-en="Build it yourself">Constrúyela tú</h3><p data-en="Available today: the ISO comes out of the repository with one script, on any Arch system.">Disponible hoy: la ISO sale del repositorio con un script, en cualquier Arch.</p><a class="btn pri" href="#construir" data-en="How">Cómo</a></article>
  </div>
</section>

<section id="requisitos" aria-labelledby="h-req">
  <p class="label" data-en="02 · requirements">02 · requisitos</p>
  <h2 id="h-req" data-en="What your machine needs">Qué necesita tu equipo</h2>
  <div class="table-wrap" style="margin-top:32px">
    <table>
      <thead><tr><th data-en="Tier">Nivel</th><th>RAM</th><th data-en="Disk">Disco</th><th data-en="Recommended desktop">Entorno recomendado</th></tr></thead>
      <tbody>
        <tr><td data-en="Absolute minimum">Mínimo absoluto</td><td>512 MB</td><td>10 GB</td><td>Openbox minimal</td></tr>
        <tr><td data-en="Usable minimum">Mínimo funcional</td><td>1 GB</td><td>15 GB</td><td data-en="Themed XFCE">XFCE temático</td></tr>
        <tr><td data-en="Standard">Estándar</td><td>2 GB</td><td>20 GB</td><td data-en="XFCE or Hyprland lite">XFCE o Hyprland lite</td></tr>
        <tr><td data-en="Recommended">Recomendado</td><td>4 GB</td><td>30 GB</td><td>Hyprland · KDE Plasma</td></tr>
      </tbody>
    </table>
  </div>
  <p class="sub" data-en="64-bit x86 only, with UEFI. Secure Boot must be off (GRUB is unsigned). Old BIOS boot is still to be tested. The installer needs an internet connection for now.">Solo x86 de 64 bits, con UEFI. Secure Boot tiene que ir apagado (GRUB va sin firmar). El arranque en BIOS antigua está por probar. Por ahora el instalador necesita conexión a internet.</p>
</section>

<section id="construir" aria-labelledby="h-build">
  <p class="label" data-en="03 · build">03 · construir</p>
  <h2 id="h-build" data-en="Build the ISO">Construye la ISO</h2>
  <p class="intro" data-en="On Arch or Static Linux, with about 15 GB free. The script builds the local packages, then the ISO with archiso.">En Arch o Static Linux, con unos 15 GB libres. El script construye los paquetes propios y después la ISO con archiso.</p>
  <pre class="cmd"><span class="c"># herramientas</span>
sudo pacman -S --needed archiso git base-devel
<span class="c"># código</span>
git clone https://github.com/KCRooty/static-linux
cd static-linux
<span class="c"># paquetes propios, como usuario normal</span>
packages/local-repo.sh
<span class="c"># ISO online (~1,7 GB, sale en iso/out/)</span>
sudo iso/build.sh online</pre>
  <p class="sub" data-en="Details and options in &lt;code&gt;iso/README.md&lt;/code&gt; of the repository. To try it without touching your disk, boot it in QEMU or VirtualBox with UEFI enabled.">Detalles y opciones en <code>iso/README.md</code> del repositorio. Para probarla sin tocar tu disco, arráncala en QEMU o VirtualBox con UEFI activado.</p>
</section>

<section id="verificar" aria-labelledby="h-ver">
  <p class="label" data-en="04 · verify">04 · verificar</p>
  <h2 id="h-ver" data-en="Check the ISO">Comprueba la ISO</h2>
  <p class="intro" data-en="When the public ISO is out, each one will come with a SHA256 sum and a GPG signature. With the three files in the same folder:">Cuando salga la ISO pública, cada una llevará su suma SHA256 y su firma GPG. Con los tres archivos en la misma carpeta:</p>
  <pre class="cmd">sha256sum -c static-linux-<i>VERSION</i>-x86_64.iso.sha256
gpg --verify static-linux-<i>VERSION</i>-x86_64.iso.sig</pre>
  <p class="sub" data-en="The signing key will be published here and in the repository together with the first release.">La clave de firma se publicará aquí y en el repositorio junto con la primera versión.</p>
</section>

<section id="ciclo" aria-labelledby="h-cyc">
  <p class="label" data-en="05 · updates">05 · actualizaciones</p>
  <h2 id="h-cyc" data-en="Rolling, like Arch">Continua, como Arch</h2>
  <p class="intro" data-en="Once installed there is no reinstalling for new versions: the system updates as a whole. New ISOs only make the first install shorter.">Una vez instalada no hay que reinstalar para tener versiones nuevas: el sistema se actualiza entero. Las ISO nuevas solo acortan la primera instalación.</p>
  <pre class="cmd">sudo pacman -Syu   <span class="c"># o: paru</span></pre>
</section>'''
    out = HERE / "descargar" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(document("Descargar · Static Linux", "Download · Static Linux",
                            "Dónde estará la ISO de Static Linux, requisitos, cómo construirla y cómo comprobarla.",
                            "Where the Static Linux ISO will be, requirements, how to build it and how to check it.",
                            "/linux/descargar/", body), encoding="utf-8")


if __name__ == "__main__":
    galeria()
    descargar()
    print("galeria/ y descargar/ escritos")
