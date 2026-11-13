# Servidor de KC Downloader Web

La página `/laboratorio/kc-downloader/` habla con este servidor, que es una instancia propia de
[cobalt](https://github.com/imputnet/cobalt) (AGPL-3.0) publicada en `https://dl.staticforge.me`.
Esta carpeta no se publica en la web (está en `.assetsignore`).

## Qué hace falta

- Una máquina encendida con Docker: un VPS, una mini PC, o el PC principal con Docker Desktop.
  YouTube bloquea mucho las IPs de centros de datos; una conexión de casa suele ir mejor.
- La cuenta de Cloudflare donde está `staticforge.me`.

El túnel de Cloudflare saca el servidor a internet sin abrir puertos en el router y sin mostrar la
IP de la máquina: quien use la web solo ve `dl.staticforge.me`.

## Pasos

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

## Mantenimiento

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
