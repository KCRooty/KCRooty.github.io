#!/usr/bin/env python3
"""Static Linux · notas de desarrollo: genera linux/blog/ a partir de _posts.py.

    python3 linux/blog/_build.py

Escribe linux/blog/index.html (la lista), linux/blog/<slug>/index.html (cada
nota) y linux/blog/feed.xml (RSS). La cabecera, el pie y los estilos salen de
linux/index.html y linux/sl.css, así el blog no se separa de la página.
Jekyll ignora los archivos que empiezan por "_", así que este script y
_posts.py no se publican.
"""

from __future__ import annotations

import html
import re
import sys
from datetime import date
from email.utils import format_datetime
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINUX = HERE.parent
SITE = "https://staticforge.me"
sys.path.insert(0, str(HERE))
from _posts import POSTS  # noqa: E402

MONTHS_ES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
             "septiembre", "octubre", "noviembre", "diciembre"]
MONTHS_EN = ["January", "February", "March", "April", "May", "June", "July", "August",
             "September", "October", "November", "December"]
CATS = {"version": ("versión", "release"), "desarrollo": ("desarrollo", "development")}


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def fecha(d: date) -> tuple[str, str]:
    return f"{d.day} de {MONTHS_ES[d.month - 1]} de {d.year}", f"{MONTHS_EN[d.month - 1]} {d.day}, {d.year}"


def chrome() -> tuple[str, str]:
    """(header, footer) copied from linux/index.html, links made absolute."""
    page = (LINUX / "index.html").read_text(encoding="utf-8")
    start = page.index('<a class="skip"')
    head_end = page.index("</header>", start) + len("</header>")
    header = page[start:head_end]
    header = re.sub(r'href="#(que|herramientas|temas|estado|wiki|unete)"', r'href="/linux/#\1"', header)
    header = header.replace('href="#main"', 'href="/linux/"')
    foot_start = page.index("<footer>")
    foot_end = page.index("</footer>") + len("</footer>")
    footer = page[foot_start:foot_end]
    mail = page[page.index("<script>/* correo del estudio"):]
    mail = mail[:mail.index("</script>") + len("</script>")]
    return header, footer + "\n" + mail


def document(title: str, title_en: str, desc: str, desc_en: str, url: str, body: str) -> str:
    header, footer = chrome()
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="/linux/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/linux/apple-touch-icon.png">
<title data-en="{esc(title_en)}">{esc(title)}</title>
<meta name="description" content="{esc(desc)}" data-en-content="{esc(desc_en)}">
<link rel="canonical" href="{SITE}{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{url}">
<meta property="og:site_name" content="Static Forge">
<meta property="og:image" content="{SITE}/assets/og/linux.jpg">
<meta name="theme-color" content="#0B0C10">
<link rel="alternate" type="application/rss+xml" title="Static Linux · notas de desarrollo" href="/linux/blog/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;700&family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<script>(function(){{var l;try{{l=localStorage.getItem('sf-lang')}}catch(e){{}}document.documentElement.setAttribute('lang',l==='en'?'en':'es')}})();</script>
<link rel="stylesheet" href="/linux/sl.css?v=20261112a">
<link rel="stylesheet" href="/assets/lang.css">
</head>
<body>
{header}
<main id="main">
<div class="wrap">
{body}
</div>
</main>
{footer}
<script src="/assets/lang.js"></script>
</body>
</html>
'''


def meta_line(p: dict) -> str:
    es, en = fecha(p["date"])
    c_es, c_en = CATS[p["cat"]]
    tags = " ".join(f'<span class="tag">{esc(t)}</span>' for t in p["tags"])
    return (f'<p class="post-meta"><time datetime="{p["date"].isoformat()}" data-en="{esc(en)}">{es}</time>'
            f' · <span data-en="{c_en}">{c_es}</span> {tags}</p>')


def build_post(p: dict) -> None:
    url = f"/linux/blog/{p['slug']}/"
    body = f'''<article class="post">
  <p class="crumb"><a href="/linux/blog/" data-en="← Development notes">← Notas de desarrollo</a></p>
  {meta_line(p)}
  <h1 data-en="{esc(p['title_en'])}">{esc(p['title'])}</h1>
  <p class="post-sub" data-en="{esc(p['sub_en'])}">{esc(p['sub'])}</p>
  <div class="post-body" data-only="es">
{p['es'].strip()}
  </div>
  <div class="post-body" data-only="en" lang="en">
{p['en'].strip()}
  </div>
  <p class="post-sign">KCRooty (Core) · Static Forge</p>
  <p class="crumb"><a href="/linux/blog/" data-en="← All notes">← Todas las notas</a></p>
</article>'''
    out = HERE / p["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(document(f"{p['title']} · Static Linux", f"{p['title_en']} · Static Linux",
                            p["sub"], p["sub_en"], url, body), encoding="utf-8")


def build_index(posts: list[dict]) -> None:
    rows = []
    for p in posts:
        rows.append(f'''    <li class="post-item">
      {meta_line(p)}
      <h2><a href="/linux/blog/{p['slug']}/" data-en="{esc(p['title_en'])}">{esc(p['title'])}</a></h2>
      <p data-en="{esc(p['sub_en'])}">{esc(p['sub'])}</p>
    </li>''')
    body = f'''<header class="blog-head">
  <p class="label" data-en="static linux · blog">static linux · blog</p>
  <h1 data-en="Development notes">Notas de desarrollo</h1>
  <p class="intro" data-en="What changes in Static Linux, when and why: every release and every big step, with what works, what got fixed and what is still missing. Also as &lt;a href=&quot;/linux/blog/feed.xml&quot;&gt;RSS&lt;/a&gt;.">Qué cambia en Static Linux, cuándo y por qué: cada versión y cada paso grande, con lo que funciona, lo que se arregló y lo que aún falta. También por <a href="/linux/blog/feed.xml">RSS</a>.</p>
</header>
<ol class="post-list">
{chr(10).join(rows)}
</ol>'''
    (HERE / "index.html").write_text(document(
        "Notas de desarrollo · Static Linux", "Development notes · Static Linux",
        "El blog de Static Linux: versiones, novedades, arreglos y lo que viene.",
        "The Static Linux blog: releases, news, fixes and what comes next.",
        "/linux/blog/", body), encoding="utf-8")


def build_feed(posts: list[dict]) -> None:
    items = []
    for p in posts:
        when = format_datetime(datetime(p["date"].year, p["date"].month, p["date"].day, 12, tzinfo=timezone.utc))
        items.append(f'''  <item>
    <title>{esc(p['title'])}</title>
    <link>{SITE}/linux/blog/{p['slug']}/</link>
    <guid>{SITE}/linux/blog/{p['slug']}/</guid>
    <pubDate>{when}</pubDate>
    <description>{esc(p['sub'])}</description>
  </item>''')
    (HERE / "feed.xml").write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>Static Linux · notas de desarrollo</title>
  <link>{SITE}/linux/blog/</link>
  <description>Versiones, novedades y arreglos de Static Linux, la distribución de Static Forge.</description>
  <language>es</language>
{chr(10).join(items)}
</channel>
</rss>
''', encoding="utf-8")


def main() -> int:
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)
    for p in posts:
        build_post(p)
    build_index(posts)
    build_feed(posts)
    print(f"{len(posts)} notas, índice y feed escritos en {HERE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
