#!/usr/bin/env python3
"""Static Linux · catálogos de idiomas de la web (linux/i18n/<idioma>.json).

    python3 linux/_i18n.py            # lista lo que falta por traducir en cada idioma
    python3 linux/_i18n.py --dump     # todas las cadenas inglesas, numeradas

Las páginas llevan el texto original en español y el inglés en data-en / data-en-<atributo>.
assets/lang.js busca cada texto inglés, tal cual, en el catálogo del idioma elegido; si no lo
encuentra, sale en inglés. Al cambiar un texto inglés, su traducción deja de usarse: este script
lo avisa. Jekyll no publica los archivos que empiezan por "_".
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGES = [HERE / "index.html"]
LANGS = ["ca", "eu", "gl", "fr", "de", "it", "pt", "pt-BR", "nl", "pl", "ru", "uk", "tr", "ja", "ko", "zh-CN"]
ATTR = re.compile(r'\sdata-en(?:-(?:alt|aria-label|title|content|placeholder))?="([^"]*)"')


def sources() -> list[str]:
    out: list[str] = []
    for page in PAGES:
        for m in ATTR.finditer(page.read_text(encoding="utf-8")):
            text = html.unescape(m.group(1))
            if text not in out:
                out.append(text)
    return out


def main() -> int:
    src = sources()
    if "--dump" in sys.argv:
        for i, t in enumerate(src, 1):
            print(f"{i}\t{t}")
        return 0
    bad = 0
    for lang in LANGS:
        f = HERE / "i18n" / f"{lang}.json"
        cat = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
        missing = [t for t in src if not cat.get(t)]
        stale = [k for k in cat if k not in src]
        tags = [k for k in cat if k in src and sorted(re.findall(r"</?\w+", k)) != sorted(re.findall(r"</?\w+", cat[k]))]
        print(f"{lang:6} {len(src) - len(missing):4}/{len(src)}  sobran {len(stale)}  etiquetas distintas {len(tags)}")
        for k in tags:
            print("   ·", k[:70])
        bad += len(missing) + len(tags)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
