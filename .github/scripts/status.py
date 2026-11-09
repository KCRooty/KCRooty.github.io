#!/usr/bin/env python3
"""Genera assets/data/status.json con el estado público de los repos de cada proyecto.

Lo ejecuta .github/workflows/status.yml (cada 6 horas y a mano). La web lee el JSON desde su propio
dominio, así que el visitante no hace ninguna petición a GitHub ni a nadie más: cero rastreo.
Para añadir un proyecto, añade su repo PÚBLICO a REPOS (clave = id que usa index.html en data-repo).
"""
import json, os, sys, urllib.request, urllib.error
from datetime import datetime, timezone

OWNER = "KCRooty"
REPOS = {
    "xusb": "X-USB",
    "rck": "RCK",
    "kcdl": "kc-downloader",
    "iron3d": "Iron3D-Studio",
    "linux": "static-linux",
    "forgeos": "ForgeOS",
}
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "data", "status.json")


def api(path):
    req = urllib.request.Request("https://api.github.com" + path, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "staticforge-status",
        **({"Authorization": "Bearer " + TOKEN} if TOKEN else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def main():
    try:
        with open(OUT, encoding="utf-8") as f:
            old = json.load(f)
    except (OSError, ValueError):
        old = {}
    projects = {}
    for key, repo in REPOS.items():
        info = api(f"/repos/{OWNER}/{repo}")
        if not info or info.get("private"):
            continue  # nunca se publica nada de un repo privado
        commits = api(f"/repos/{OWNER}/{repo}/commits?per_page=1") or []
        rel = api(f"/repos/{OWNER}/{repo}/releases/latest")
        tags = None if rel else api(f"/repos/{OWNER}/{repo}/tags?per_page=1")
        version = (rel or {}).get("tag_name") or ((tags or [{}])[0].get("name") if tags else None)
        projects[key] = {
            "repo": f"{OWNER}/{repo}",
            "last_commit": commits[0]["commit"]["committer"]["date"] if commits else info.get("pushed_at"),
            "version": version,
            "stars": info.get("stargazers_count", 0),
        }
    if projects == old.get("projects"):
        print("Sin cambios.")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "projects": projects},
                  f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps(projects, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
