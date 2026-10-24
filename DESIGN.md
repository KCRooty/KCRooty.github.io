# DESIGN.md · staticforge.dpdns.org

Dirección dada por Rooty el 2026-10-24: "una mezcla de estilos entre CRT, retro y minimalista, un híbrido, algo hermoso".
Referencias de partida: los cuatro prototipos `paleta-demo*.html` (forge, minimal, retro 70s, CRT/VHS). Se toman el
CRT, el retro 70s y el minimal; el forge/cyberpunk queda fuera (dirección retirada en el CLAUDE.md global).

## Identidad

Static Forge como **un canal de televisión de madrugada que emite desde un taller**: la calidez de una carátula
de los 70, el resplandor de un tubo de fósforo, y el orden y el aire de una página minimal. Lo analógico pone el
carácter, lo minimal pone la legibilidad.

Línea roja: nunca nombre real ni ubicación real en la web (incidente de doxxing de 2025). Se firma como **Core**.

## Dial

`Dial: ENERGY 2 / RHYTHM 3 / MOTION 2`

- ENERGY 2: tiene que tener presencia (título grande, tele en el hero) pero el contenido manda.
- RHYTHM 3: cada sección tiene composición propia (hero a dos columnas, guía de canales, bloque editorial, rejilla de galería).
- MOTION 2: movimiento ambiental solo en el hero (banda de tracking en la pantalla, contador VHS) y transiciones de tema. Todo se apaga con `prefers-reduced-motion` y con el interruptor CRT.

## Paleta (2 neutros + 3 franjas + 1 acento)

| Token | Noche (por defecto) | Papel | Uso |
|---|---|---|---|
| `--bg` | `#14100C` | `#FBF1E3` | fondo |
| `--surface` | `#1D1813` | `#FFF8EE` | superficies |
| `--ink` | `#F3E6CF` | `#2B2420` | texto |
| `--muted` | `#A89A80` | `#6B5D50` | texto secundario |
| `--s1` | `#E79D56` | `#E79D56` | franja 1, naranja atardecer |
| `--s2` | `#B25781` | `#B25781` | franja 2, rosa |
| `--s3` | `#4C9DB0` | `#305166` | franja 3, petróleo |
| `--phosphor` | `#FFB000` | `#A4520F` | acento único: texto CRT, foco, estado activo |

Las tres franjas son decorativas (motivo de marca), nunca color de texto sobre fondo.

## Tipografía

- **Fraunces** (display, eje SOFT): la voz de carátula 70s en títulos.
- **DM Sans** (cuerpo): neutra y muy legible para que el resto respire.
- **VT323** (acentos CRT): solo en etiquetas cortas (OSD, números de canal, metadatos). Nunca en párrafos.

## Motivo de identidad

Las **tres franjas curvas** (naranja / rosa / petróleo) + el **número de canal en VT323**. Aparecen en el nav, en
los divisores y en la guía de proyectos, y se repiten en el pie.

## Reglas

- Cristal (backdrop-filter) solo en la barra de navegación.
- El brillo de fósforo solo en el acento y en la pantalla de la tele.
- Scanlines y viñeta: capa global sutil, desactivable (interruptor CRT, recordado por visitante).
- Idiomas: ES (por defecto), EN, CA.

## Forge OS (`forge-os/`): Windows 7-10 dentro de un monitor CRT ámbar

Identidad propia, aparte del estilo híbrido y de Static Linux. Petición de KCRooty (Core), 2026-10-24: primero "solo CRT", después "mezcla Windows 7-10 con el CRT".

- Monocromo de fósforo ámbar sobre negro cálido: fondo `#070502`, panel `#0E0904`, ámbar `#FFB000` (texto, 11.1:1), ámbar claro `#FFD27A` (títulos, 14.3:1), tenue `#C48A1E` (secundario, 6.8:1), error `#FF7A5C`. Bordes decorativos `#5C3F0A`; bordes de campos y ventanas `#8C6214`.
- Estructura de escritorio: cada sección es una **ventana** (barra de título con brillo de cristal tipo Windows 7 en la ventana activa, botones de ventana planos tipo Windows 10, decorativos y ocultos a lectores de pantalla) y abajo una **barra de tareas** fija con botón Inicio (menú con los enlaces), accesos a las secciones con indicador de ventana activa (subrayado tipo 10), botón CRT y reloj real.
- Ventanas con nombre de programa: `forge_os.exe`, `arranque.log · Visor`, `Propiedades del sistema`, `Administrador de tareas` (tabla de estado) y `Asistente para unirse`.
- Tipografía: **Segoe UI** (pila del sistema) solo en el cromo de Windows (barras de título, botones, barra de tareas, menú); **VT323** en títulos y el bloque de arranque; **IBM Plex Mono** en párrafos y formularios.
- Sin logotipos de Microsoft: el botón Inicio lleva una rejilla genérica de 3x3 y la palabra Inicio.
- Scanlines, viñeta, parpadeo y brillo se apagan con el botón CRT de la bandeja (clave `sf-crt`); parpadeo y animación de arranque respetan reducir movimiento.
- El bloque de arranque y la tabla de estado resumen el README real del repo; no son salidas literales del sistema.
