"""Static Linux · notas de desarrollo. Una entrada por nota; _build.py las convierte en páginas.

Cada nota: slug, date, cat ("version" | "desarrollo"), tags, title/title_en,
sub/sub_en (la entradilla) y es/en (el cuerpo en HTML). Bilingüe siempre.
Estado honesto: lo que no está hecho se dice.
"""

from datetime import date

POSTS = [
    {
        "slug": "2026-11-temas-estilos-codigo-abierto",
        "date": date(2026, 11, 12),
        "cat": "version",
        "tags": ["temas", "estilos", "instalador", "código"],
        "title": "Temas, estilos y el código, abierto",
        "title_en": "Themes, styles and the code, in the open",
        "sub": "Ocho temas que son fondo más paleta, tres formas de escritorio (minimal, aero y ventanas), una página de tema en el instalador y el repositorio público con su wiki.",
        "sub_en": "Eight themes that are wallpaper plus palette, three desktop shapes (minimal, aero and ventanas), a theme page in the installer and the public repository with its wiki.",
        "es": """
<h2>Lo nuevo</h2>
<h3>Temas: un fondo y su paleta</h3>
<p>Los diez acentos de antes se quedan cortos. Ahora un tema es un fondo de pantalla y la paleta que sale de él: acento, superficies, texto, bordes de ventana, carpetas y terminal. Hay ocho: Ámbar, Bosque, Medianoche, Brasa, Niebla, Violeta, Aero y Ventanas.</p>
<figure class="shot"><img src="/linux/img/temas/ambar.webp" alt="Escritorio con el tema Ámbar" loading="lazy" width="1280" height="720"></figure>
<p>Todo lo genera <code>sl-theme</code> a partir de un <code>theme.conf</code> de unas pocas líneas: GTK 3 y 4, el tema de ventanas de xfwm4 (dibujado píxel a píxel con antialias), xsettings, la terminal y el panel.</p>

<h3>Tres estilos de escritorio</h3>
<p>Además del color, cada tema elige una forma:</p>
<ul>
<li><strong>minimal</strong>: barra fina arriba, esquinas suaves, nada que sobre. El de siempre.</li>
<li><strong>aero</strong>: cristal brillante, botones en cápsula y barra de tareas abajo con reloj y fecha. Homenaje a la estética de finales de los 2000, dibujado desde cero.</li>
<li><strong>ventanas</strong>: barra alta abajo con las apps centradas, botones de ventana anchos y planos, oscuro y azul. Para quien viene de Windows y no quiere aprender otro escritorio el primer día.</li>
</ul>
<div class="gal g2">
<figure class="shot"><img src="/linux/img/temas/aero.webp" alt="Tema Aero" loading="lazy" width="1280" height="720"><figcaption>Aero</figcaption></figure>
<figure class="shot"><img src="/linux/img/temas/ventanas.webp" alt="Tema Ventanas" loading="lazy" width="1280" height="720"><figcaption>Ventanas</figcaption></figure>
</div>
<p>Al cambiar de estilo el panel se reconstruye en caliente, sin cerrar sesión.</p>

<h3>Dónde se elige</h3>
<ul>
<li><strong>Instalador</strong>: página <em>Tema</em> con capturas reales de los ocho. Lo que eliges es lo que arranca.</li>
<li><strong>Bienvenida</strong> (sl-welcome): la pestaña Apariencia es ahora un selector de temas.</li>
<li><strong>Terminal</strong>: <code>sl-ctl theme</code> lista y aplica (<code>sl-ctl theme aero</code>).</li>
</ul>

<h3>Apps de Static Forge</h3>
<p>El catálogo de la bienvenida estrena una sección <em>Static Forge</em> con el software del estudio. Empieza con KC Downloader 3.0.1, el más maduro; irán llegando más.</p>

<h3>El código, abierto</h3>
<p>El repositorio <a href="https://github.com/KCRooty/static-linux">KCRooty/static-linux</a> ya tiene todo el código, con la historia completa. La wiki se publica sola en <a href="https://staticforge.me/static-linux/">staticforge.me/static-linux</a>.</p>

<h2>Arreglos</h2>
<ul>
<li>DNS cifrado: dnscrypt-proxy estaba instalado, pero las consultas no pasaban por él. Ahora todas lo hacen desde el primer arranque.</li>
<li>Copias de seguridad de <code>sl-theme</code>: si lo ejecutaba root primero, el usuario ya no podía cambiar de tema. Ahora las copias son del usuario.</li>
</ul>

<h2>Problemas conocidos</h2>
<ul>
<li>Los temas solo cubren XFCE de momento. KDE, Hyprland y Openbox vienen después.</li>
<li>Las apps que ya estaban abiertas cambian de aspecto al reabrirlas.</li>
<li>La sesión en vivo de la ISO todavía no tiene escritorio: arranca directa al instalador.</li>
<li>El fondo de Violeta es provisional.</li>
<li>Aún no hay ISO pública para descargar. Se compila desde el repositorio.</li>
</ul>

<h2>Lo siguiente</h2>
<p>Llevar los temas a KDE, Hyprland y Openbox; que la pantalla de inicio de sesión, Plymouth y GRUB sigan el tema; sesión en vivo con escritorio; y "tu fondo": que el sistema saque la paleta de cualquier imagen que elijas.</p>
""",
        "en": """
<h2>What's new</h2>
<h3>Themes: a wallpaper and its palette</h3>
<p>The old ten accents were not enough. A theme is now a wallpaper and the palette that comes out of it: accent, surfaces, text, window borders, folders and terminal. There are eight: Ámbar, Bosque, Medianoche, Brasa, Niebla, Violeta, Aero and Ventanas.</p>
<figure class="shot"><img src="/linux/img/temas/ambar.webp" alt="Desktop with the Ámbar theme" loading="lazy" width="1280" height="720"></figure>
<p><code>sl-theme</code> generates everything from a few-line <code>theme.conf</code>: GTK 3 and 4, the xfwm4 window theme (drawn pixel by pixel with antialiasing), xsettings, the terminal and the panel.</p>

<h3>Three desktop styles</h3>
<p>Besides colour, each theme picks a shape:</p>
<ul>
<li><strong>minimal</strong>: thin top bar, soft corners, nothing extra. The usual one.</li>
<li><strong>aero</strong>: glossy glass, capsule buttons and a bottom taskbar with time and date. A nod to late-2000s looks, drawn from scratch.</li>
<li><strong>ventanas</strong>: tall bottom bar with centred apps, wide flat window buttons, dark and blue. For people coming from Windows who don't want to learn a new desktop on day one.</li>
</ul>
<div class="gal g2">
<figure class="shot"><img src="/linux/img/temas/aero.webp" alt="Aero theme" loading="lazy" width="1280" height="720"><figcaption>Aero</figcaption></figure>
<figure class="shot"><img src="/linux/img/temas/ventanas.webp" alt="Ventanas theme" loading="lazy" width="1280" height="720"><figcaption>Ventanas</figcaption></figure>
</div>
<p>Switching style rebuilds the panel live, no logout needed.</p>

<h3>Where to pick it</h3>
<ul>
<li><strong>Installer</strong>: a <em>Theme</em> page with real screenshots of all eight. What you pick is what boots.</li>
<li><strong>Welcome</strong> (sl-welcome): the Appearance tab is now a theme picker.</li>
<li><strong>Terminal</strong>: <code>sl-ctl theme</code> lists and applies (<code>sl-ctl theme aero</code>).</li>
</ul>

<h3>Static Forge apps</h3>
<p>The welcome app catalog gets a <em>Static Forge</em> section with the studio's software. It starts with KC Downloader 3.0.1, the most mature one; more will follow.</p>

<h3>The code, in the open</h3>
<p>The <a href="https://github.com/KCRooty/static-linux">KCRooty/static-linux</a> repository now holds all the code, with full history. The wiki publishes itself at <a href="https://staticforge.me/static-linux/">staticforge.me/static-linux</a>.</p>

<h2>Fixes</h2>
<ul>
<li>Encrypted DNS: dnscrypt-proxy was installed, but queries did not go through it. Now they all do from the first boot.</li>
<li><code>sl-theme</code> backups: if root ran it first, the user could no longer switch themes. Backups now belong to the user.</li>
</ul>

<h2>Known issues</h2>
<ul>
<li>Themes only cover XFCE for now. KDE, Hyprland and Openbox come next.</li>
<li>Apps that were already open change look when reopened.</li>
<li>The ISO live session has no desktop yet: it boots straight into the installer.</li>
<li>The Violeta wallpaper is provisional.</li>
<li>No public ISO to download yet. It builds from the repository.</li>
</ul>

<h2>What's next</h2>
<p>Bring themes to KDE, Hyprland and Openbox; make the login screen, Plymouth and GRUB follow the theme; a live session with a desktop; and "your wallpaper": the system pulls the palette from any image you choose.</p>
""",
    },
    {
        "slug": "2026-10-instalador-pulido-kde-hyprland",
        "date": date(2026, 10, 23),
        "cat": "desarrollo",
        "tags": ["instalador", "kde", "hyprland"],
        "title": "Instalador pulido, KDE Plasma y Hyprland 0.56",
        "title_en": "Polished installer, KDE Plasma and Hyprland 0.56",
        "sub": "Una ronda grande tras la primera instalación real: el instalador en español y a pantalla completa, KDE Plasma como entorno, Hyprland al día y los fallos de la primera vez corregidos.",
        "sub_en": "A big round after the first real install: the installer in Spanish and fullscreen, KDE Plasma as an environment, Hyprland up to date and the first-time bugs fixed.",
        "es": """
<h2>Lo nuevo</h2>
<ul>
<li><strong>KDE Plasma</strong> se puede elegir en el instalador junto a XFCE, Hyprland y Openbox.</li>
<li><strong>Hyprland 0.56</strong>: configuración puesta al día con la sintaxis nueva.</li>
<li><strong>Instalador</strong> en español de punta a punta, a pantalla completa y con soporte HiDPI.</li>
<li>Brave viene preinstalado, la tecla Super abre el menú y los códecs multimedia van de serie.</li>
<li>Fondos de pantalla en 4K.</li>
</ul>
<h2>Arreglos</h2>
<p>Todo lo que falló en la primera instalación de principio a fin: textos sin traducir, páginas que se cortaban en pantallas pequeñas y pasos que fallaban si no había red.</p>
<h2>Pendiente</h2>
<p>Que el aspecto lo decida un tema completo y no solo un color de acento. Eso llega en la versión siguiente.</p>
""",
        "en": """
<h2>What's new</h2>
<ul>
<li><strong>KDE Plasma</strong> can be picked in the installer alongside XFCE, Hyprland and Openbox.</li>
<li><strong>Hyprland 0.56</strong>: config updated to the new syntax.</li>
<li><strong>Installer</strong> in Spanish end to end, fullscreen and with HiDPI support.</li>
<li>Brave comes preinstalled, the Super key opens the menu and multimedia codecs ship by default.</li>
<li>4K wallpapers.</li>
</ul>
<h2>Fixes</h2>
<p>Everything that broke on the first end-to-end install: untranslated strings, pages cut off on small screens and steps that failed without a network.</p>
<h2>Pending</h2>
<p>Let a full theme decide the look, not just an accent colour. That arrives in the next release.</p>
""",
    },
    {
        "slug": "2026-10-primera-iso-que-instala",
        "date": date(2026, 10, 11),
        "cat": "desarrollo",
        "tags": ["iso", "instalador"],
        "title": "La primera ISO que instala de principio a fin",
        "title_en": "The first ISO that installs end to end",
        "sub": "1,7 GB, arranque UEFI, instalación completa en QEMU/KVM y un sistema que arranca con su escritorio, su pantalla de inicio y su bienvenida.",
        "sub_en": "1.7 GB, UEFI boot, a full install in QEMU/KVM and a system that boots into its desktop, login screen and welcome app.",
        "es": """
<p>Hito: la ISO se construye con <code>iso/build.sh</code>, arranca en UEFI e instala un sistema que funciona sin tocar nada después.</p>
<ul>
<li>Imagen de 1,7 GB.</li>
<li>Probada en QEMU/KVM con UEFI, disco ext4.</li>
<li>Escritorio XFCE con su tema, LightDM como pantalla de inicio y sl-welcome al entrar.</li>
<li>Perfil de privacidad básico aplicado de serie.</li>
</ul>
<h2>Lo que falta</h2>
<p>Probarla en hardware real, pulir el instalador y sumar más entornos. La siguiente ronda va de eso.</p>
""",
        "en": """
<p>Milestone: the ISO builds with <code>iso/build.sh</code>, boots in UEFI and installs a system that works with nothing to fix afterwards.</p>
<ul>
<li>1.7 GB image.</li>
<li>Tested in QEMU/KVM with UEFI, ext4 disk.</li>
<li>XFCE desktop with its theme, LightDM as the login screen and sl-welcome on first login.</li>
<li>Basic privacy profile applied by default.</li>
</ul>
<h2>What's missing</h2>
<p>Testing on real hardware, polishing the installer and adding more environments. The next round is about that.</p>
""",
    },
    {
        "slug": "2026-09-bienvenida-instalador-entornos",
        "date": date(2026, 9, 21),
        "cat": "desarrollo",
        "tags": ["sl-welcome", "instalador", "wiki"],
        "title": "Bienvenida, instalador y más entornos",
        "title_en": "Welcome app, installer and more environments",
        "sub": "Llegan sl-welcome, la secuencia completa del instalador Calamares, Openbox e Hyprland, el paquete base y la wiki.",
        "sub_en": "sl-welcome arrives, along with the full Calamares installer sequence, Openbox and Hyprland, the base package and the wiki.",
        "es": """
<ul>
<li><strong>sl-welcome</strong>: la app de bienvenida, con resumen del sistema, catálogo de apps y ajustes rápidos.</li>
<li><strong>Calamares</strong>: la secuencia completa del instalador, de idioma a usuario.</li>
<li><strong>Entornos</strong>: Openbox e Hyprland se suman a XFCE.</li>
<li><strong>staticlinux-base</strong>: el paquete que trae las herramientas y la marca del sistema.</li>
<li><strong>Wiki</strong> en MkDocs y el primer <code>iso/build.sh</code>.</li>
</ul>
""",
        "en": """
<ul>
<li><strong>sl-welcome</strong>: the welcome app, with a system overview, an app catalog and quick settings.</li>
<li><strong>Calamares</strong>: the full installer sequence, from language to user.</li>
<li><strong>Environments</strong>: Openbox and Hyprland join XFCE.</li>
<li><strong>staticlinux-base</strong>: the package that brings the system's tools and branding.</li>
<li>An MkDocs <strong>wiki</strong> and the first <code>iso/build.sh</code>.</li>
</ul>
""",
    },
    {
        "slug": "2026-09-arranca-static-linux",
        "date": date(2026, 9, 10),
        "cat": "desarrollo",
        "tags": ["inicio", "xfce"],
        "title": "Arranca Static Linux",
        "title_en": "Static Linux begins",
        "sub": "Primer paso de la distribución de Static Forge: base Arch, detección de hardware y un XFCE con tema propio.",
        "sub_en": "First step of the Static Forge distribution: an Arch base, hardware detection and an XFCE desktop with its own theme.",
        "es": """
<p>Static Linux nace con una idea: un Arch que funciona nada más instalarlo, con buen aspecto y sin pelearse con él.</p>
<ul>
<li><strong>sl-detect</strong>: mira el hardware (gráfica, RAM, firmware, disco) y recomienda el entorno, el sistema de archivos y el kernel que mejor le van a esa máquina.</li>
<li><strong>XFCE con tema</strong>: el primer escritorio, con la marca del estudio.</li>
<li><strong>Diez acentos</strong> de color para elegir.</li>
</ul>
""",
        "en": """
<p>Static Linux starts with one idea: an Arch that works right after install, looks good and doesn't fight you.</p>
<ul>
<li><strong>sl-detect</strong>: looks at the hardware (GPU, RAM, firmware, disk) and recommends the environment, filesystem and kernel that suit that machine best.</li>
<li><strong>Themed XFCE</strong>: the first desktop, with the studio's branding.</li>
<li><strong>Ten colour accents</strong> to pick from.</li>
</ul>
""",
    },
]
