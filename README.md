<img src="assets/logo.png" alt="Static Forge" width="96" height="96">

# Static Forge · staticforge.me

Web del estudio, servida con GitHub Pages desde la rama `main`. **Desplegar = hacer push.**
El dominio lo fija el archivo `CNAME` del repo (`staticforge.me`): manda sobre lo que diga
el panel de GitHub Pages, así que no hay que volver a ponerle el dominio viejo.

| Página | Qué es |
|---|---|
| `index.html` | Portada: proyectos (tele con cambio de canal), estudio y galería |
| `unete.html` | Únete: solicitud para entrar en el estudio |
| `i3ds.html` | Iron3D Studio |
| `fnaf-as.html` | FNAF AS |
| `linux/` | Static Linux |
| `forge-os/` | Forge OS |
| `donnies.html` | DONNIES |
| `foros.html` | Foro del estudio (API aparte, en Cloudflare Workers) |
| `solicitudes.html` | Panel de solicitudes (solo cuentas admin del foro) |

`DESIGN.md` tiene la dirección de diseño; `assets/` los estilos, los scripts y los logos de
cada proyecto.

## Estado en vivo

`assets/data/status.json` lo genera la Action `.github/workflows/status.yml` cada 6 horas (último commit, versión y
estrellas de los repos públicos). La web lo lee desde su propio dominio: el visitante no hace peticiones a GitHub.

## Licencia

Código: [MIT](LICENSE). Arte y textos: [CC BY-NC-SA 4.0](LICENSE-CONTENIDO.md), con las excepciones que ahí se indican.

Lo que queda por hacer está en [`PENDIENTES.md`](PENDIENTES.md).
