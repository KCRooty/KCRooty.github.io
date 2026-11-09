# PENDIENTES · staticforge.me

Lista para seguir en el PC principal con Claude Code. Se excluye de la web (`_config.yml` y `.assetsignore`).
Apuntado el 2026-11-09 tras la revisión de la web.

## 1. Limpieza de estilo (punto 6 de la revisión)

Lo que quedó del audit `anti-slop/audit-001-2026-10-24.md` y ha ido a más:

- [ ] **Guiones largos (—)**: sustituir por coma, dos puntos o paréntesis según la frase. No tocar los que estén
      dentro de código, URLs o atributos que no se ven.
      Conteo a 2026-11-09: `donnies.html` 32 · `i3ds.html` 14 · `fnaf-as.html` 6 · `forge-os/index.html` 5.
      Comprobar con: `Select-String -Path *.html,*/index.html -Pattern '—' | Group-Object Path`
      Ojo: también los hay en los `data-en=""` (versión inglesa); esos también cuentan.
- [ ] **Brillo de fósforo (`.crt-txt`)**: hay 17 usos en `index.html`; la regla de `DESIGN.md` dice 1 o 2.
      Dejar el brillo solo en el OSD del hero (`.osd`) y la tele; el resto, ámbar plano. Lo más limpio es una clase
      nueva `.amber` (mismo color y fuente, sin `text-shadow`) y cambiar los kickers, la ficha técnica y el pie a esa.
      Revisar después en Noche y en Papel.

## 2. Decisión pendiente: Google Fonts

Las fuentes (Fraunces, DM Sans, VT323) se cargan desde los servidores de Google, así que cada visita le pasa la IP
del visitante a Google. Choca con el «Sin telemetría» del hero.

- [ ] Si se decide servirlas desde la web: descargar los `.woff2` (latin + latin-ext) a `assets/fonts/`, crear
      `assets/fonts.css` con los `@font-face` (con `font-display:swap`) y cambiar en **todas** las páginas los tres
      `<link>` de `fonts.googleapis.com` / `fonts.gstatic.com` por `<link rel="stylesheet" href="/assets/fonts.css">`.
      Fraunces es variable (ejes `opsz`, `wght`, `SOFT`): hay que bajar la versión variable, no estáticas.
      Las páginas de FNAF AS y Static Linux usan otras familias: revisar su `<link>` también.

## 3. Activar el canal secreto (hecho en código, falta desplegar)

El Worker del foro tiene ya los endpoints `/api/secret/unlock` y `/api/secret/claim` (repo `static-forge-forum`).
En ese repo, desde PowerShell:

```powershell
git pull
npx wrangler d1 execute static-forge-foro --remote --file=migrations/0004-canal-secreto.sql
npm run deploy
```

Hasta que se haga, la página del canal dice «No hay conexión con el estudio».

## 4. Estado en vivo de los proyectos

- [ ] La primera vez, lanzar a mano la Action: GitHub → pestaña **Actions** → «Estado de los proyectos» → **Run workflow**.
      Después corre sola cada 6 horas. Si falla con un error de permisos: Settings → Actions → General →
      Workflow permissions → **Read and write permissions**.
- [ ] Si se publica un repo nuevo (WinForge, Anvil…), añadirlo a `REPOS` en `.github/scripts/status.py` y poner
      `<span class="live" data-repo="id"></span>` en su fila de `index.html` (y `repo:'id'` en su canal de `CH`).
