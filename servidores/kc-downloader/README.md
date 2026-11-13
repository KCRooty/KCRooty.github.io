# Servidor de KC Downloader Web

La página `/laboratorio/kc-downloader/` habla con una instancia propia de
[cobalt](https://github.com/imputnet/cobalt) (AGPL-3.0) publicada en `https://dl.staticforge.me`.
Esta carpeta no se publica en la web (está en `.assetsignore`).

## Montaje actual: Render (plan gratuito)

- **Servicio**: Web Service desde imagen existente `ghcr.io/imputnet/cobalt:11`, plan *Free*,
  región Frankfurt.
- **Variables**: las de `.env.example` más las fijas de abajo (Render lee `PORT=10000`, por eso
  `API_PORT=10000`). Se pegan todas a la vez con *Add from .env*.
  ```
  API_URL=https://dl.staticforge.me/
  API_PORT=10000
  CORS_WILDCARD=0
  CORS_URL=https://staticforge.me
  API_AUTH_REQUIRED=1
  RATELIMIT_WINDOW=60
  RATELIMIT_MAX=20
  DURATION_LIMIT=5400
  ```
- **Dominio**: en Render, *Settings → Custom Domains → dl.staticforge.me*; en Cloudflare, un
  CNAME `dl` → `<servicio>.onrender.com` en modo *Solo DNS* (nube gris) para que Render pueda
  emitir el certificado.
- **Turnstile**: widget "KC Downloader Web" (modo Managed, dominio staticforge.me).
- **Límites del plan gratuito**: se duerme tras 15 minutos sin uso y tarda hasta un minuto en
  despertar (la web lo avisa y espera); 512 MB de RAM. YouTube bloquea a menudo las IPs de
  centros de datos, así que puede fallar a ratos; Pinterest, TikTok, X, Instagram y SoundCloud
  van mejor.

## Alternativa: máquina propia con Docker

### Qué hace falta

- Una máquina encendida con Docker: un VPS, una mini PC, o el PC principal con Docker Desktop.
  YouTube bloquea mucho las IPs de centros de datos; una conexión de casa suele ir mejor.
- La cuenta de Cloudflare donde está `staticforge.me`.

El túnel de Cloudflare saca el servidor a internet sin abrir puertos en el router y sin mostrar la
IP de la máquina: quien use la web solo ve `dl.staticforge.me`.

### Pasos

1. **Túnel**: Cloudflare → Zero Trust → Networks → Tunnels → *Create a tunnel* → Cloudflared →
   nombre `kcdl` → entorno *Docker*. Copia el token (lo que va detrás de `--token`).
   En *Public hostname* añade: subdominio `dl`, dominio `staticforge.me`, servicio `HTTP`,
   URL `kcdl-cobalt:9000`.
2. **Turnstile**: Cloudflare → Turnstile → *Add widget* → dominio `staticforge.me`, modo *Managed*.
   Copia la *site key* y la *secret key*.
3. **Configuración**: en esta carpeta, copia `.env.example` como `.env` y rellena las cuatro
   variables (para `JWT_SECRET` hay un comando de ejemplo dentro).
4. **Arrancar**:
   ```sh
   docker compose up -d
   docker compose logs -f cobalt   # para ver que arranca sin errores
   ```
5. **Comprobar**: abre `https://dl.staticforge.me/` en el navegador. Tiene que devolver un JSON con
   `"cobalt"` y `"turnstileSitekey"`. En la web, el indicador pasa a *Servidor en línea*.

### Mantenimiento

- Watchtower actualiza cobalt y cloudflared solo. Cuando YouTube cambia algo, cobalt suele
  sacar el arreglo en unos días.
- Si YouTube empieza a fallar con `error.api.youtube.login`, descomenta el servicio `yt-session`
  y la variable `YOUTUBE_SESSION_SERVER` en `docker-compose.yml`, y vuelve a lanzar
  `docker compose up -d`.
- Para apagarlo: `docker compose down`. La web mostrará *Servidor fuera de línea* y no se rompe.
- Límites actuales: 20 peticiones por minuto y persona, vídeos de hasta 90 minutos. Se cambian en
  `docker-compose.yml`.

## Responsabilidad

El servidor no guarda enlaces ni archivos: hace de túnel y los entrega al momento. Aun así, un
descargador público puede recibir avisos de derechos de autor; si llega alguno, se puede limitar
con `DISABLED_SERVICES` o apagar el servidor sin tocar la web.
