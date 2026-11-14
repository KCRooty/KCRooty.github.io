"""Static Linux · notas de desarrollo. Una entrada por nota; _build.py las convierte en páginas.

Cada nota: slug, date, cat ("version" | "desarrollo"), tags, title/title_en,
sub/sub_en (la entradilla) y es/en (el cuerpo en HTML). Bilingüe siempre.
Estado honesto: lo que no está hecho se dice.
"""

from datetime import date

POSTS = [
    {
        "slug": "2026-11-primera-iso-publica",
        "date": date(2026, 11, 14),
        "cat": "version",
        "tags": ["iso", "privacidad", "instalador", "prueba"],
        "title": "La primera ISO pública de prueba: 2026.11.14",
        "title_en": "The first public test ISO: 2026.11.14",
        "sub": "Ya se puede descargar Static Linux. Es una ISO de prueba de 4,8 GB que instala sin conexión: el sistema, cualquiera de los diez escritorios, los tres kernels y el perfil de privacidad van dentro. Firmada, y con la lista de lo que aún falla.",
        "sub_en": "Static Linux can be downloaded now. It is a 4.8 GB test ISO that installs with no connection: the system, any of the ten desktops, the three kernels and the privacy profile are inside. Signed, and with the list of what still fails.",
        "es": """
<h2>Qué es esta ISO</h2>
<p>Una <strong>versión de prueba</strong>. Se instala de principio a fin en máquinas virtuales y la he probado con varios escritorios y perfiles, pero todavía no en un PC real con la ISO: esa prueba llega cuando tenga otro equipo a mano. Si la pruebas en el tuyo, mejor en un disco que no te importe o en una máquina virtual, y cuéntanos qué pasa en Discord.</p>

<h2>Una sola ISO, con o sin red</h2>
<p>En vez de dos ISO (online y offline), una: la <strong>universal</strong>. Lleva dentro 1.300 paquetes (2,6 GB): la base, los diez escritorios, <code>linux-lts</code>, <code>linux-zen</code> y <code>linux-hardened</code>, y las herramientas de privacidad. Así:</p>
<ul>
<li><strong>Sin conexión</strong> instala el sistema completo, con el escritorio y el perfil que elijas. Probado en una VM sin salida a internet: KDE Plasma y el perfil Máximo, en unos 7 minutos.</li>
<li><strong>Con conexión</strong> instala lo mismo desde la ISO, pone el sistema al día y añade los sabores.</li>
<li>Los <strong>sabores</strong> (Gaming, Oficina…) no van dentro: doblarían el tamaño. Si instalas sin red, quedan apuntados y se añaden después con <code>sudo sl-ctl flavor add pending</code>.</li>
</ul>
<p>La ISO pesa <strong>4,8 GB</strong>: cabe en un USB de 8 GB. No se copia a la RAM al arrancar, así que también arranca en equipos de 2 GB.</p>

<h2>private, comprobado</h2>
<p>Antes de publicar dejé un sistema recién instalado en reposo con la red grabada y miré a quién hablaba. Salieron dos cosas, ya arregladas:</p>
<ul>
<li>dnscrypt-proxy probaba unos 170 servidores DNS públicos en cada arranque, algunos caseros. Ahora usa una lista corta: Quad9, Mullvad y dnscry.pt (Madrid, París, Fráncfort, Ámsterdam).</li>
<li>NetworkManager preguntaba a <code>ping.archlinux.org</code> cada 5 minutos, por HTTP sin cifrar. Apagado. Lo único que se pierde es la página que abren solos los wifis de hotel.</li>
</ul>
<p>Tras eso, en reposo solo quedan el DNS cifrado y la hora (NTP). <code>sl-ctl audit</code> enseña lo mismo en tu equipo.</p>

<h2>También en esta versión</h2>
<ul>
<li><strong>Repositorio propio firmado</strong>: las correcciones de Static Linux llegan con <code>sudo pacman -Syu</code>, sin reinstalar.</li>
<li><strong>Instantáneas</strong> antes y después de cada actualización en BTRFS, y en el menú de arranque.</li>
<li><code>sl-ctl flavor add/remove</code> y <code>sl-ctl audit</code>.</li>
<li>AppArmor se carga de verdad en Mejorado y Máximo, y Máximo instala <code>linux-hardened</code> como prometía.</li>
<li>Fondos nuevos para Aero y Nube, de fotos libres de Wikimedia Commons.</li>
</ul>

<h2>Problemas conocidos</h2>
<ul>
<li>Sin probar todavía en hardware real con la ISO, ni el arranque en BIOS antigua ni el cifrado LUKS.</li>
<li>XFCE en reposo usa unos 700 MB de RAM, por encima de nuestro límite de 650 MB. Toca recortar.</li>
<li>Secure Boot tiene que ir apagado.</li>
<li>Los estilos (minimal, aero, ventanas, estante) solo dan forma a XFCE.</li>
</ul>

<h2>Descargar y comprobar</h2>
<p>En la <a href="/linux/descargar/">página de descarga</a>: la ISO, su suma SHA256 y su firma con la clave de Static Forge (<code>3E61 7ED0 6C90 C757 35C9 C45E 51D5 8FA3 5045 B8D0</code>).</p>
""",
        "en": """
<h2>What this ISO is</h2>
<p>A <strong>test release</strong>. It installs from start to finish in virtual machines and I have tried it with several desktops and profiles, but not yet on a real PC from the ISO: that test comes when I have another machine at hand. If you try it on yours, better on a disk you do not mind losing or in a virtual machine, and tell us how it goes on Discord.</p>

<h2>One ISO, with or without a network</h2>
<p>Instead of two ISOs (online and offline), one: the <strong>universal</strong> one. It carries 1,300 packages (2.6 GB): the base, the ten desktops, <code>linux-lts</code>, <code>linux-zen</code> and <code>linux-hardened</code>, and the privacy tools. So:</p>
<ul>
<li><strong>With no connection</strong> it installs the whole system, with the desktop and profile you pick. Tested in a VM with no internet access: KDE Plasma and the Maximum profile, in about 7 minutes.</li>
<li><strong>With a connection</strong> it installs the same from the ISO, updates the system and adds the flavors.</li>
<li><strong>Flavors</strong> (Gaming, Office…) are not inside: they would double the size. If you install offline, they are noted down and added later with <code>sudo sl-ctl flavor add pending</code>.</li>
</ul>
<p>The ISO is <strong>4.8 GB</strong>: it fits on an 8 GB USB stick. It is not copied to RAM at boot, so it also boots on 2 GB machines.</p>

<h2>private, checked</h2>
<p>Before publishing I left a freshly installed system idle with its network traffic recorded and looked at who it talked to. Two things came up, both fixed:</p>
<ul>
<li>dnscrypt-proxy probed about 170 public DNS servers at every boot, some of them home servers. It now uses a short list: Quad9, Mullvad and dnscry.pt (Madrid, Paris, Frankfurt, Amsterdam).</li>
<li>NetworkManager asked <code>ping.archlinux.org</code> every 5 minutes, over plain HTTP. Off. The only loss is the page hotel wifi opens on its own.</li>
</ul>
<p>After that, at idle only encrypted DNS and the clock (NTP) remain. <code>sl-ctl audit</code> shows the same on your machine.</p>

<h2>Also in this release</h2>
<ul>
<li><strong>Our own signed repository</strong>: Static Linux fixes arrive with <code>sudo pacman -Syu</code>, no reinstall.</li>
<li><strong>Snapshots</strong> before and after every update on BTRFS, and in the boot menu.</li>
<li><code>sl-ctl flavor add/remove</code> and <code>sl-ctl audit</code>.</li>
<li>AppArmor really loads in Enhanced and Maximum, and Maximum installs <code>linux-hardened</code> as promised.</li>
<li>New wallpapers for Aero and Cloud, from free photos on Wikimedia Commons.</li>
</ul>

<h2>Known issues</h2>
<ul>
<li>Not tested yet on real hardware from the ISO, nor old BIOS boot, nor LUKS encryption.</li>
<li>XFCE at idle uses about 700 MB of RAM, above our 650 MB limit. Trimming is next.</li>
<li>Secure Boot must be off.</li>
<li>Styles (minimal, aero, ventanas, estante) only shape XFCE.</li>
</ul>

<h2>Download and verify</h2>
<p>On the <a href="/linux/descargar/">download page</a>: the ISO, its SHA256 sum and its signature with the Static Forge key (<code>3E61 7ED0 6C90 C757 35C9 C45E 51D5 8FA3 5045 B8D0</code>).</p>
""",
    },
    {
        "slug": "2026-11-idiomas-rendimiento",
        "date": date(2026, 11, 13),
        "cat": "version",
        "tags": ["idiomas", "rendimiento", "temas", "escritorios"],
        "title": "18 idiomas, rendimiento de serie y los temas en todas partes",
        "title_en": "18 languages, speed out of the box and themes everywhere",
        "sub": "Static Linux habla 18 idiomas, viene afinado para ir rápido desde el primer arranque (zram, earlyoom, sched_ext y sl-game) y los nueve temas llegan a los nueve escritorios, al inicio de sesión y al arranque. Con esto se cierra lo visual: ahora toca lo técnico.",
        "sub_en": "Static Linux speaks 18 languages, comes tuned for speed from the first boot (zram, earlyoom, sched_ext and sl-game) and the nine themes reach all nine desktops, the login screen and the boot. That closes the visual work: now it is the technical side's turn.",
        "es": """
<h2>Lo nuevo</h2>
<h3>18 idiomas</h3>
<p>Español (el original), inglés, catalán, euskera, gallego, francés, alemán, italiano, portugués, portugués de Brasil, neerlandés, polaco, ruso, ucraniano, turco, japonés, coreano y chino simplificado. Se traduce todo lo que es nuestro: el instalador (páginas, presentación y los pasos que va mostrando), sl-welcome, los ajustes rápidos, la guía de atajos de Hyprland, las capturas, <code>sl-ctl</code>, los nombres de temas y apps, la pantalla de bloqueo y hasta la contraseña del disco al arrancar. Si tu idioma no está, sale en inglés.</p>
<p>Va con gettext y los textos originales en español dentro del código: para añadir un idioma basta un fichero <code>.po</code>. Esta página también se puede leer en los 18 desde el selector de arriba.</p>

<h3>fast, de serie</h3>
<p>Siguiendo la guía de gaming de CachyOS, pero pensando también en un Celeron de 2013 con disco duro:</p>
<ul>
<li><strong>zram</strong> por fin activo, con los ajustes de memoria que pide (antes estaba instalado y apagado). Con menos de 4 GB de RAM, además, un swapfile de 2 GB por debajo.</li>
<li><strong>earlyoom</strong> configurado: si se acaba la memoria, cierra lo más grande antes de que el escritorio se congele. Nunca la sesión ni el audio.</li>
<li>Cada disco con su <strong>planificador</strong> (NVMe, SSD, disco duro) y escritura en bloques pequeños, para que una copia grande no lo frene todo. Red con BBR, journal limitado, caché de paquetes que se limpia sola y caché de shaders grande.</li>
<li><strong>Sabor Gaming:</strong> el planificador de CPU <code>scx_lavd</code> (sched_ext) desde el primer arranque, y <code>sl-game %command%</code> en las opciones de Steam pone la máquina en rendimiento solo mientras juegas.</li>
<li><code>sl-ctl perf</code> enseña todo eso de un vistazo y cambia el perfil de energía o el planificador.</li>
</ul>
<p>No se toca la línea de arranque del kernel y todo se puede deshacer. Lo que se descartó (ananicy-cpp, <code>mitigations=off</code>…) está explicado en la wiki, en <a href="https://staticforge.me/static-linux/rendimiento/">Rendimiento</a>.</p>

<h3>Los temas, en todas partes</h3>
<p>Los nueve temas visten ya los nueve escritorios: XFCE, KDE Plasma, GNOME, Cinnamon, Hyprland, Openbox, i3, bspwm y sway. Y también LightDM o SDDM, el menú de GRUB y una pantalla de arranque propia con la contraseña del disco. La sesión en vivo de la ISO arranca con escritorio y el instalador encima.</p>
<figure class="shot"><img src="/linux/img/temas/nube.webp" alt="Tema Nube con el estilo estante" loading="lazy" width="1280" height="720"><figcaption>Nube, con el estilo estante</figcaption></figure>

<h2>Arreglos</h2>
<ul>
<li>El tema elegido en el instalador no llegaba entero al usuario nuevo con temas claros: ahora sí.</li>
<li>Hyprland 0.57 daba error al entrar; hyprpaper fallaba en máquinas virtuales (ahora hay un plan B); kitty y LXTerminal ignoraban la paleta.</li>
<li>Los tweaks <code>swappiness-10</code> y <code>hdd-bfq</code> de <code>sl-ctl</code> desaparecen: iban en contra de zram o ya vienen de serie.</li>
</ul>

<h2>Problemas conocidos</h2>
<ul>
<li>Los estilos (minimal, aero, ventanas, estante) solo dan forma a XFCE.</li>
<li>Los escritorios nuevos y el sabor Gaming aún no se han probado en una instalación completa desde la ISO.</li>
<li>Las alertas de i3 y sway siguen en español.</li>
<li>Todavía no hay ISO pública.</li>
</ul>

<h2>Lo siguiente</h2>
<p>Se acabó lo visual. Ahora, lo técnico: que <em>fast, private, yours</em> se note en algo más que en el aspecto.</p>
""",
        "en": """
<h2>What's new</h2>
<h3>18 languages</h3>
<p>Spanish (the original), English, Catalan, Basque, Galician, French, German, Italian, Portuguese, Brazilian Portuguese, Dutch, Polish, Russian, Ukrainian, Turkish, Japanese, Korean and Simplified Chinese. Everything that is ours is translated: the installer (pages, slideshow and the steps it shows), sl-welcome, the quick settings, the Hyprland shortcut guide, screenshots, <code>sl-ctl</code>, theme and app names, the lock screen and even the disk password prompt at boot. If your language is missing, you get English.</p>
<p>It uses gettext with the original Spanish strings in the code: adding a language takes one <code>.po</code> file. This page can also be read in all 18 from the selector at the top.</p>

<h3>fast, out of the box</h3>
<p>Following CachyOS' gaming guide, while also keeping a 2013 Celeron with a hard drive in mind:</p>
<ul>
<li><strong>zram</strong> is finally on, with the memory settings it needs (it used to be installed but off). With less than 4 GB of RAM there is also a 2 GB swapfile below it.</li>
<li><strong>earlyoom</strong> configured: when memory runs out, it closes the biggest process before the desktop freezes. Never the session or the audio.</li>
<li>Each disk gets its own <strong>scheduler</strong> (NVMe, SSD, hard drive) and writes go out in small batches, so a big copy no longer slows everything down. BBR networking, a capped journal, a package cache that cleans itself and a large shader cache.</li>
<li><strong>Gaming flavor:</strong> the <code>scx_lavd</code> CPU scheduler (sched_ext) from the first boot, and <code>sl-game %command%</code> in Steam's launch options puts the machine in performance mode only while you play.</li>
<li><code>sl-ctl perf</code> shows all of that at a glance and changes the power profile or the scheduler.</li>
</ul>
<p>The kernel boot line is never touched and everything can be undone. What was left out (ananicy-cpp, <code>mitigations=off</code>…) is explained in the wiki, under <a href="https://staticforge.me/static-linux/rendimiento/">Rendimiento</a>.</p>

<h3>Themes, everywhere</h3>
<p>The nine themes now dress all nine desktops: XFCE, KDE Plasma, GNOME, Cinnamon, Hyprland, Openbox, i3, bspwm and sway. Also LightDM or SDDM, the GRUB menu and our own boot splash with the disk password. The ISO's live session boots to a desktop with the installer on top.</p>
<figure class="shot"><img src="/linux/img/temas/nube.webp" alt="Cloud theme with the estante style" loading="lazy" width="1280" height="720"><figcaption>Cloud, with the estante style</figcaption></figure>

<h2>Fixes</h2>
<ul>
<li>The theme picked in the installer did not fully reach the new user with light themes: now it does.</li>
<li>Hyprland 0.57 showed an error on login; hyprpaper failed in virtual machines (there is a fallback now); kitty and LXTerminal ignored the palette.</li>
<li>The <code>swappiness-10</code> and <code>hdd-bfq</code> tweaks in <code>sl-ctl</code> are gone: they worked against zram or now come by default.</li>
</ul>

<h2>Known issues</h2>
<ul>
<li>Styles (minimal, aero, ventanas, estante) only shape XFCE.</li>
<li>The new desktops and the Gaming flavor have not been tested in a full install from the ISO yet.</li>
<li>The i3 and sway alerts are still in Spanish.</li>
<li>There is no public ISO yet.</li>
</ul>

<h2>Next</h2>
<p>The visual work is done. Now the technical side: making <em>fast, private, yours</em> show in more than the looks.</p>
""",
    },
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
<p>Los diez acentos de antes se quedan cortos. Ahora un tema es un fondo de pantalla y la paleta que sale de él: acento, superficies, texto, bordes de ventana, carpetas y terminal. Hay ocho: Ámbar, Bosque, Nórdico, Papel, Sakura, Violeta, Aero y Ventanas.</p>
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
<p>The old ten accents were not enough. A theme is now a wallpaper and the palette that comes out of it: accent, surfaces, text, window borders, folders and terminal. There are eight: Ámbar, Bosque, Nórdico, Papel, Sakura, Violeta, Aero and Ventanas.</p>
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
