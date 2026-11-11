# DESIGN.md · staticforge.me

Dirección dada por Rooty el 2026-10-24: "una mezcla de estilos entre CRT, retro y minimalista, un híbrido, algo hermoso".
Referencias de partida: los cuatro prototipos `paleta-demo*.html` (forge, minimal, retro 70s, CRT/VHS). Se toman el
CRT, el retro 70s y el minimal; el forge/cyberpunk queda fuera (dirección retirada en las guías de diseño del estudio).

**Revisado por Rooty el 2026-11-11** (antislop #7): identidad, paleta y tipografías aprobadas tal cual; dial más
calmado; la web queda en ES/EN; el brillo de fósforo se mantiene en todos los textos CRT. Lo que cambie aquí manda
sobre la web.

## Identidad

Static Forge como **un canal de televisión de madrugada que emite desde un taller**: la calidez de una carátula
de los 70, el resplandor de un tubo de fósforo, y el orden y el aire de una página minimal. Lo analógico pone el
carácter, lo minimal pone la legibilidad.

Línea roja: nunca nombre real ni ubicación real en la web (incidente de doxxing de 2025). Se firma como **Core**.

## Dial

`Dial: ENERGY 1 / RHYTHM 3 / MOTION 1` (antes 2 / 3 / 2; Rooty pidió "más calma" el 2026-11-11)

- ENERGY 1: presencia tranquila. El título y la tele del hero se quedan, pero nada nuevo compite por la atención.
- RHYTHM 3: cada sección tiene composición propia (hero a dos columnas, guía de canales, bloque editorial, rejilla de galería).
- MOTION 1: lo mínimo que se mueve, y solo dentro de la tele. Todo se apaga con `prefers-reduced-motion` y con el interruptor CRT.
- **Lo que ya se mueve se queda (Rooty, 2026-11-11: "así contrasta"):** fogonazo de encendido, parpadeo del REC,
  banda de tracking de la tele y estática entre canales. La calma del dial vale para lo nuevo: nada añadido debe
  sumar movimiento ni efectos fuera de la tele.

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
- El brillo de fósforo va en todos los textos CRT (`.crt-txt`: OSD, kickers, ficha, créditos, contacto, pie) y en la
  pantalla de la tele. **Decidido por Rooty el 2026-11-11** al ver el antes/después de limitarlo solo al OSD. También
  lo lleva el cursor (decisión del 2026-10-25).
- **Cursor:** flecha oscura con contorno de fósforo y halo leve (`assets/cursor/`); sobre lo pulsable, interior ámbar translucido. Sin halo en Papel ni con el CRT apagado. Solo con ratón (`pointer:fine`); con `prefers-contrast: more` se usa el del sistema. Mismo bloque en `index.html` y `assets/sf.css`. Static Linux, Forge OS y Donnies conservan el suyo.
- Scanlines y viñeta: capa global sutil, desactivable (interruptor CRT, recordado por visitante).
- Idiomas: ES (por defecto) y EN. Sin catalán (decidido por Rooty el 2026-11-11).
- Estados de proyecto en tipo frase ("En desarrollo", "Activo"); las mayúsculas quedan para kickers y números de canal.
- El punto REC del hero usa `--s2` y se alinea con la primera línea del OSD.
- Cada enlace de proyecto dice adónde lleva ("Ver qué funciona ya", "Ver la hoja de ruta"...), nunca "Ver la página".
- Hero con un solo botón ("Ver los proyectos"); la fila de valores empieza por "Nuestro software:".

## Forge OS (`forge-os/`): Windows 7-10 dentro de un monitor CRT ámbar

Identidad propia, aparte del estilo híbrido y de Static Linux. Petición de KCRooty (Core), 2026-10-24: primero "solo CRT", después "mezcla Windows 7-10 con el CRT".

- Monocromo de fósforo ámbar sobre negro cálido: fondo `#070502`, panel `#0E0904`, ámbar `#FFB000` (texto, 11.1:1), ámbar claro `#FFD27A` (títulos, 14.3:1), tenue `#C48A1E` (secundario, 6.8:1), error `#FF7A5C`. Bordes decorativos `#5C3F0A`; bordes de campos y ventanas `#8C6214`.
- Estructura de escritorio: cada sección es una **ventana** (barra de título con brillo de cristal tipo Windows 7 en la ventana activa, botones de ventana planos tipo Windows 10, decorativos y ocultos a lectores de pantalla) y abajo una **barra de tareas** fija con botón Inicio (menú con los enlaces), accesos a las secciones con indicador de ventana activa (subrayado tipo 10), botón CRT y reloj real.
- Ventanas con nombre de programa: `forge_os.exe`, `arranque.log · Visor`, `Propiedades del sistema`, `Administrador de tareas` (tabla de estado) y `Asistente para unirse`.
- Tipografía: **Segoe UI** (pila del sistema) solo en el cromo de Windows (barras de título, botones, barra de tareas, menú); **VT323** en títulos y el bloque de arranque; **IBM Plex Mono** en párrafos y formularios.
- Sin logotipos de Microsoft: el botón Inicio lleva una rejilla genérica de 3x3 y la palabra Inicio.
- Scanlines, viñeta, parpadeo y brillo se apagan con el botón CRT de la bandeja (clave `sf-crt`); parpadeo y animación de arranque respetan reducir movimiento.
- El bloque de arranque y la tabla de estado resumen el README real del repo; no son salidas literales del sistema.

## Añadidos del 2026-11-09

- **Tele de proyectos** (destacado de `#proyectos`): flechas ‹ › para cambiar de canal entre los proyectos (también
  con ← → y deslizando en móvil), con un golpe de estática de 0,3 s entre canales (se apaga con reducir movimiento).
  Los logos se ven enteros (`.fit`); LADA, sin imagen, sale con carta de ajuste de barras de color. La lista de abajo no cambia.
- **Estado en vivo**: línea en VT323 color franja 3 (`.live`) bajo el estado de cada proyecto con repo público.
- **`unete.html`**: la solicitud sale de la portada a su propia página (CH 14).
- **Imágenes para compartir** (`assets/og/`): 1200×630, misma tele y franjas, una por página.
- **Canal 00**: página oculta con identidad ámbar tipo Forge OS (monocromo de fósforo); se entra por el segundo botón
  de la tele del hero o tecleando «00» en la portada. Sin enlace visible ni entrada en el sitemap.
- **Encendido**: al entrar en la portada (una vez por sesión) la pantalla hace el fogonazo de tubo CRT; clic o tecla lo saltan; no sale con reducir movimiento ni con el CRT apagado.
- **Fotos de decoración** (`assets/deco/`, sin metadatos): naturaleza detrás del hero y el setup al final del pie, sin marco, con opacidad baja, sepia suave y degradado (`mask-image`).
- **Paint It!** (`paint-it/`, CH 15): réplica del Paint clásico con cromo estilo XP; iconos y código propios, sin recursos ni logos de Microsoft.
- **Sonido** (`assets/sound.js`): zumbido de tubo, clic de canal, estática, meter y expulsar cinta; todo sintetizado con Web Audio, apagado por defecto (botón del altavoz en la barra, se recuerda en `sf-sound`).
