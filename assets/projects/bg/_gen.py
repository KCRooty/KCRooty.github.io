#!/usr/bin/env python3
"""Fondos de las filas de proyectos de la portada: un SVG por proyecto, dibujado por código.

    python3 assets/projects/bg/_gen.py

Arte original de Static Forge (sin logos de terceros). Todo se concentra a la derecha:
la izquierda queda tapada por el degradado de la fila para que el texto se lea.
Misma semilla, mismo dibujo.
"""

from __future__ import annotations

import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
W, H = 800, 240


def svg(body: str, bg: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMaxYMid slice">'
            f'<rect width="{W}" height="{H}" fill="{bg}"/>{body}</svg>\n')


def stars(rng: random.Random, n: int, x0: float = 260, col: str = "#fff", ymax: float = H) -> str:
    out = []
    for _ in range(n):
        x, y = rng.uniform(x0, W), rng.uniform(0, ymax)
        r = rng.choice([0.6, 0.8, 1, 1, 1.3, 1.8])
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}" opacity="{rng.uniform(.35, 1):.2f}"/>')
    for _ in range(n // 12):  # a few four-point sparkles
        x, y, s = rng.uniform(x0 + 80, W), rng.uniform(10, ymax - 10), rng.uniform(4, 8)
        out.append(f'<path d="M{x} {y-s}L{x+s*.22} {y-s*.22}L{x+s} {y}L{x+s*.22} {y+s*.22}L{x} {y+s}L{x-s*.22} {y+s*.22}'
                   f'L{x-s} {y}L{x-s*.22} {y-s*.22}Z" fill="{col}" opacity=".9"/>')
    return "".join(out)


def fnaf_as(rng):
    # pizzeria wall: dark tiles, checker band, party pennants, pizzas, scanlines
    b = ['<rect x="0" y="0" width="800" height="150" fill="#2A1A2E"/>']
    for x in range(300, 800, 40):  # wall panels
        b.append(f'<rect x="{x}" y="0" width="38" height="150" fill="#33203A"/>')
    b.append('<rect x="0" y="146" width="800" height="6" fill="#7A2A3A"/>')
    for i, x in enumerate(range(260, 800, 22)):  # checker band, two rows
        for j, y in enumerate((152, 174, 196, 218)):
            if (i + j) % 2 == 0:
                b.append(f'<rect x="{x}" y="{y}" width="22" height="22" fill="#E9E1D3"/>')
            else:
                b.append(f'<rect x="{x}" y="{y}" width="22" height="22" fill="#141014"/>')
    # pennant string
    pts = [(x, 18 + 10 * math.sin(x / 60)) for x in range(300, 801, 4)]
    b.append('<polyline fill="none" stroke="#C9B48A" stroke-width="1.5" points="' + " ".join(f"{x},{y:.1f}" for x, y in pts) + '"/>')
    cols = ["#E8483B", "#F2C14E", "#3FA7D6", "#8E5DD8"]
    for k, x in enumerate(range(316, 800, 36)):
        y = 18 + 10 * math.sin(x / 60)
        b.append(f'<path d="M{x-11} {y:.1f}L{x+11} {y:.1f}L{x} {y+20:.1f}Z" fill="{cols[k % 4]}" opacity=".9"/>')

    def pizza(cx, cy, r, rot):
        g = [f'<g transform="rotate({rot} {cx} {cy})">',
             f'<path d="M{cx} {cy-r}L{cx+r*.62} {cy+r*.7}Q{cx} {cy+r*.95} {cx-r*.62} {cy+r*.7}Z" fill="#F4C25B"/>',
             f'<path d="M{cx-r*.62} {cy+r*.7}Q{cx} {cy+r*.95} {cx+r*.62} {cy+r*.7}L{cx+r*.7} {cy+r*.82}Q{cx} {cy+r*1.1} {cx-r*.7} {cy+r*.82}Z" fill="#C9822E"/>']
        for dx, dy in ((-.18, .2), (.2, .38), (-.05, .55), (.05, .05)):
            g.append(f'<circle cx="{cx+dx*r:.1f}" cy="{cy+dy*r:.1f}" r="{r*.11:.1f}" fill="#C8352B"/>')
        g.append('</g>')
        return "".join(g)
    b.append(pizza(470, 78, 34, -12))
    b.append(pizza(610, 92, 28, 18))
    b.append(pizza(735, 70, 32, -24))
    # stars/confetti on the wall
    for _ in range(26):
        x, y = rng.uniform(320, 800), rng.uniform(40, 140)
        b.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="4" height="4" fill="{rng.choice(cols)}" opacity=".7" transform="rotate({rng.randint(0,90)} {x:.0f} {y:.0f})"/>')
    # analog scanlines
    b.append('<g opacity=".18">' + "".join(f'<rect x="0" y="{y}" width="800" height="1" fill="#000"/>' for y in range(0, H, 3)) + '</g>')
    return svg("".join(b), "#24162A")


def lada(rng):
    b = ['<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0E1230"/>'
         '<stop offset="1" stop-color="#2B1D3F"/></linearGradient></defs>',
         '<rect width="800" height="240" fill="url(#g)"/>', stars(rng, 140, 240, "#F4EBD9", 190)]
    b.append('<circle cx="690" cy="62" r="26" fill="#F3E3B8"/><circle cx="701" cy="55" r="23" fill="#151634"/>')
    # autumn tree line and falling leaves
    hill = "M260 240L260 206" + "".join(f"L{x} {206 - 10*math.sin(x/37) - 6*math.sin(x/11):.1f}" for x in range(260, 801, 10)) + "L800 240Z"
    b.append(f'<path d="{hill}" fill="#1A1020"/>')
    for _ in range(18):
        x, y, s = rng.uniform(320, 790), rng.uniform(80, 220), rng.uniform(4, 7)
        b.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{s:.1f}" ry="{s*.5:.1f}" fill="{rng.choice(["#D9772B","#B8452A","#E3A33A"])}" '
                 f'opacity=".85" transform="rotate({rng.randint(0,180)} {x:.0f} {y:.0f})"/>')
    return svg("".join(b), "#0E1230")


def xusb(rng):
    b = []
    # circuit traces
    for i in range(9):
        y = 20 + i * 25
        x0 = rng.uniform(330, 520)
        x1 = rng.uniform(560, 650)
        b.append(f'<path d="M{x0:.0f} {y}H{x1:.0f}L{x1+14:.0f} {y+12}H700" fill="none" stroke="#2C3A3F" stroke-width="2"/>')
        b.append(f'<circle cx="{x0:.0f}" cy="{y}" r="3.5" fill="#2C3A3F"/>')
    # vertical line with the stick hanging from it
    b.append('<rect x="709" y="0" width="4" height="110" fill="#E7EEF0"/>')
    b.append('<rect x="691" y="104" width="40" height="78" rx="7" fill="#E7EEF0"/>')
    b.append('<rect x="699" y="182" width="24" height="30" rx="2" fill="#AEB9BD"/>')
    b.append('<rect x="704" y="190" width="5" height="6" fill="#40504F"/><rect x="713" y="190" width="5" height="6" fill="#40504F"/>')
    b.append('<path d="M711 124l-9 14h6v14h6v-14h6z" fill="#101618"/>')
    b.append('<rect x="696" y="160" width="30" height="3" rx="1.5" fill="#3CC9C2"/>')
    return svg("".join(b), "#121A1D")


def rck(rng):
    b = []
    cx, cy = 650, 200
    for r, op in ((150, .25), (120, .4), (90, .6)):
        b.append(f'<path d="M{cx-r} {cy}A{r} {r} 0 0 1 {cx+r} {cy}" fill="none" stroke="#5B7BFF" stroke-width="10" opacity="{op}" stroke-linecap="round"/>')
    for k in range(13):
        a = math.pi * (1 - k / 12)
        x1, y1 = cx + 158 * math.cos(a), cy - 158 * math.sin(a)
        x2, y2 = cx + 170 * math.cos(a), cy - 170 * math.sin(a)
        b.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#9FB1FF" stroke-width="2"/>')
    a = math.pi * .28
    b.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+120*math.cos(a):.0f}" y2="{cy-120*math.sin(a):.0f}" stroke="#7CF0D0" stroke-width="5" stroke-linecap="round"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="10" fill="#7CF0D0"/>')
    for i, h in enumerate((40, 70, 55, 95, 80)):  # sliders
        x = 340 + i * 26
        b.append(f'<rect x="{x}" y="60" width="6" height="140" rx="3" fill="#2A3156"/><circle cx="{x+3}" cy="{200-h}" r="8" fill="#9FB1FF"/>')
    return svg("".join(b), "#141833")


def kc_downloader(rng):
    b = []
    for _ in range(40):  # confetti dots in the three colours
        x, y = rng.uniform(300, 800), rng.uniform(0, H)
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rng.uniform(1.5,4):.1f}" fill="{rng.choice(["#FF2D2D","#1ED760","#E60023"])}" opacity=".45"/>')
    # generic shapes in the three platforms' colours (no logos): play, waveform, pushpin
    b.append('<circle cx="468" cy="74" r="40" fill="none" stroke="#FF2D2D" stroke-width="6"/><path d="M455 54v40l34-20z" fill="#FF2D2D"/>')
    for i, h in enumerate((18, 34, 52, 70, 52, 40, 62, 30, 20)):
        b.append(f'<rect x="{566+i*12}" y="{150-h/2:.0f}" width="7" height="{h}" rx="3.5" fill="#1ED760"/>')
    b.append('<g transform="rotate(28 734 80)"><rect x="716" y="40" width="36" height="12" rx="4" fill="#E60023"/>'
             '<path d="M722 52h24l6 30h-36z" fill="#E60023"/><rect x="708" y="80" width="52" height="10" rx="4" fill="#E60023"/>'
             '<path d="M732 90h4l-2 38z" fill="#F3E6CF"/></g>')
    # download arrows and equalizer bars
    for i, h in enumerate((30, 58, 42, 70, 36, 50)):
        b.append(f'<rect x="{330+i*14}" y="{220-h}" width="8" height="{h}" rx="3" fill="#F3E6CF" opacity=".35"/>')
    b.append('<path d="M520 160v40m-14-14 14 14 14-14" fill="none" stroke="#F3E6CF" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" opacity=".7"/>')
    return svg("".join(b), "#16131C")


def winforge(rng):
    b = []
    for y in range(-10, H + 20, 20):
        for x in range(260, W + 20, 20):
            ox = x + (10 if (y // 20) % 2 else 0)
            t = max(0, 1 - math.hypot((ox - 260) / 540, 1 - y / H) / 1.05)
            r = t ** 1.3 * 9
            if r > .8:
                b.append(f'<circle cx="{ox}" cy="{y}" r="{r:.1f}" fill="#4A4762"/>')
    s, g, x0, y0 = 70, 6, 560, 44
    for (dx, dy), c in zip(((0, 0), (1, 0), (0, 1), (1, 1)), ("#FF3131", "#8C52FF", "#5CE1E6", "#FFDE59")):
        b.append(f'<rect x="{x0+dx*(s+g)}" y="{y0+dy*(s+g)}" width="{s}" height="{s}" rx="20" fill="{c}"/>')
    return svg("".join(b), "#29263B")


def iron3d(rng):
    b = []
    # perspective floor grid
    hz, vx = 120, 620
    for k in range(-12, 13):
        b.append(f'<line x1="{vx}" y1="{hz}" x2="{vx + k*70}" y2="{H}" stroke="#3B4A34" stroke-width="1"/>')
    for i in range(1, 8):
        y = hz + (H - hz) * (i / 7) ** 1.8
        b.append(f'<line x1="260" y1="{y:.1f}" x2="800" y2="{y:.1f}" stroke="#3B4A34" stroke-width="1"/>')
    # wireframe cube
    def P(x, y, z):
        return 600 + (x - z) * 0.87 * 46, 120 - y * 46 + (x + z) * 0.5 * 46
    v = {(x, y, z): P(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)}
    for a in v:
        for bb in v:
            if sum(p != q for p, q in zip(a, bb)) == 1 and a < bb:
                (x1, y1), (x2, y2) = v[a], v[bb]
                b.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#8FC46A" stroke-width="2"/>')
    o = P(0, -1, 0)
    for (dx, dy), c in (((60, 0), "#E5533D"), ((0, -60), "#8FC46A"), ((-46, 26), "#4C8FE0")):
        b.append(f'<line x1="{o[0]:.0f}" y1="{o[1]:.0f}" x2="{o[0]+dx:.0f}" y2="{o[1]+dy:.0f}" stroke="{c}" stroke-width="3" stroke-linecap="round"/>')
    b.append('<ellipse cx="600" cy="125" rx="120" ry="34" fill="none" stroke="#8FC46A" stroke-width="1" stroke-dasharray="4 6" opacity=".6"/>')
    return svg("".join(b), "#141A12")


def cinder(rng):
    b = ['<defs><radialGradient id="g" cx=".75" cy=".1" r=".8"><stop offset="0" stop-color="#5A4C7A"/>'
         '<stop offset="1" stop-color="#16121F"/></radialGradient></defs><rect width="800" height="240" fill="url(#g)"/>',
         stars(rng, 120, 260)]
    # film strip
    b.append('<g transform="rotate(-8 600 170)"><rect x="300" y="150" width="560" height="56" fill="#0E0B14"/>')
    for x in range(306, 860, 18):
        b.append(f'<rect x="{x}" y="155" width="9" height="7" rx="1.5" fill="#B30CD8" opacity=".9"/><rect x="{x}" y="194" width="9" height="7" rx="1.5" fill="#B30CD8" opacity=".9"/>')
    for x in range(330, 840, 74):
        b.append(f'<rect x="{x}" y="166" width="62" height="24" rx="2" fill="#2A2140"/>')
    b.append('</g>')
    return svg("".join(b), "#16121F")


def static_linux(rng):
    b = []
    for x in range(260, 800, 32):
        b.append(f'<line x1="{x}" y1="0" x2="{x}" y2="240" stroke="#151821" stroke-width="1"/>')
    for y in range(0, 240, 32):
        b.append(f'<line x1="260" y1="{y}" x2="800" y2="{y}" stroke="#151821" stroke-width="1"/>')
    # terminal window
    b.append('<rect x="470" y="34" width="300" height="172" rx="10" fill="#12141A" stroke="#262A35"/>')
    b.append('<rect x="470" y="34" width="300" height="24" rx="10" fill="#181B23"/>')
    for i, c in enumerate(("#3A3F4C", "#3A3F4C", "#00C8A0")):
        b.append(f'<circle cx="{488+i*14}" cy="46" r="4" fill="{c}"/>')
    rows = [("#00C8A0", 120), ("#8E93A0", 200), ("#8E93A0", 170), ("#F5A623", 90), ("#8E93A0", 220), ("#00C8A0", 60)]
    for i, (c, w) in enumerate(rows):
        b.append(f'<rect x="488" y="{72+i*20}" width="{w}" height="7" rx="3.5" fill="{c}" opacity=".85"/>')
    b.append('<rect x="560" y="172" width="9" height="14" fill="#00C8A0"/>')
    return svg("".join(b), "#0B0C10")


def forge_os(rng):
    b = ['<defs><radialGradient id="g" cx=".82" cy="1" r=".7"><stop offset="0" stop-color="#C2451E"/>'
         '<stop offset=".5" stop-color="#4A1A10"/><stop offset="1" stop-color="#160D0A"/></radialGradient></defs>'
         '<rect width="800" height="240" fill="url(#g)"/>']
    for _ in range(70):  # rising sparks
        x, y = rng.uniform(420, 800), rng.uniform(0, 240)
        l = rng.uniform(4, 14)
        b.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x - l*.3:.0f}" y2="{y + l:.0f}" stroke="{rng.choice(["#FFB347","#FF7A2F","#FFD27A"])}" '
                 f'stroke-width="{rng.uniform(1,2.4):.1f}" stroke-linecap="round" opacity="{rng.uniform(.4,1):.2f}"/>')
    # anvil silhouette
    b.append('<path d="M540 140H750V160C730 168 712 170 700 172L680 176L676 196H702L712 214H568L578 196H604L600 176L580 172C560 170 548 166 540 160C520 160 498 154 486 146C500 142 520 140 540 140Z" fill="#0F0A09"/>')
    return svg("".join(b), "#160D0A")


def anvil_client(rng):
    b = []
    px = 20
    for y in range(0, H, px):
        for x in range(300, W, px):
            depth = (y - 120) / px
            if y < 120:
                continue
            if y < 140:
                c = rng.choice(["#5DA03A", "#4E8E31", "#6BB244"])
            elif depth < 4:
                c = rng.choice(["#7A5534", "#6A4A2D", "#86603B"])
            else:
                c = rng.choice(["#7D7D7D", "#6E6E6E", "#8A8A8A"] + (["#3FC3D8"] if rng.random() < .05 else []))
            b.append(f'<rect x="{x}" y="{y}" width="{px}" height="{px}" fill="{c}"/>')
    for cx, cy, w in ((420, 20, 5), (600, 40, 7), (720, 10, 4)):  # blocky clouds
        b.append(f'<rect x="{cx}" y="{cy}" width="{w*px}" height="{px}" fill="#F2F7FF"/>')
        b.append(f'<rect x="{cx+px}" y="{cy+px}" width="{(w+1)*px}" height="{px}" fill="#F2F7FF"/>')
    return svg("".join(b), "#7FB2E6")


MAKERS = {"fnaf-as": fnaf_as, "lada": lada, "x-usb": xusb, "rck": rck, "kc-downloader": kc_downloader,
          "winforge": winforge, "iron3d": iron3d, "cinder": cinder, "static-linux": static_linux,
          "forge-os": forge_os, "anvil-client": anvil_client}

if __name__ == "__main__":
    for name, fn in MAKERS.items():
        out = HERE / f"{name}.svg"
        out.write_text(fn(random.Random(7)), encoding="utf-8")
        print(f"{out.name} {out.stat().st_size // 1024} KB")
