"""Dönüş Yolu carousel üretici.
Kullanım: python3 render.py icerik/04_kim_kullanabilir.json cikti/
JSON: {"id": "...", "slides": [{"type": "cover"|"list"|"cta", ...}]}
"""
import json, sys, os, html
import cairosvg

W, H = 1080, 1350
BG, ACC, GREEN, BLUE, WHITE = "#062018", "#9FE3C4", "#006B3C", "#00468C", "#FFFFFF"
MUTED = "#B7CFC4"
FONT = "Inter, DejaVu Sans, sans-serif"
M = 96  # kenar boşluğu


def wrap(text, size, max_w, weight=400):
    k = 0.56 if weight >= 700 else 0.52
    max_chars = max(8, int(max_w / (size * k)))
    lines, cur = [], ""
    for w in text.split():
        if len(cur) + len(w) + (1 if cur else 0) <= max_chars:
            cur = f"{cur} {w}".strip()
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines


def t(x, y, s, size, fill=WHITE, weight=400, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{html.escape(s)}</text>')


def block(text, x, y, size, max_w, fill=WHITE, weight=400, lh=1.22):
    out = []
    for i, line in enumerate(wrap(text, size, max_w, weight)):
        out.append(t(x, y + i * size * lh, line, size, fill, weight))
    return "".join(out), y + len(wrap(text, size, max_w, weight)) * size * lh


def frame(inner, idx, total, show_arrow=True):
    bar = (f'<rect x="0" y="0" width="{W/2}" height="14" fill="{GREEN}"/>'
           f'<rect x="{W/2}" y="0" width="{W/2}" height="14" fill="{BLUE}"/>')
    sig = t(M, H - 70, "@donusyolutr", 30, ACC, 600)
    page = t(W / 2, H - 70, f"{idx}/{total}", 24, MUTED, 400, "middle")
    arrow = ""
    if show_arrow:
        ax, ay = W - M, H - 80
        arrow = (f'<g fill="none" stroke="{ACC}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">'
                 f'<line x1="{ax-70}" y1="{ay}" x2="{ax}" y2="{ay}"/>'
                 f'<polyline points="{ax-26},{ay-26} {ax},{ay} {ax-26},{ay+26}"/></g>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<rect width="{W}" height="{H}" fill="{BG}"/>{bar}{inner}{sig}{page}{arrow}</svg>')


def cover(s):
    out = t(M, 230, s.get("kicker", ""), 32, ACC, 600)
    body, y = block(s["title"], M, 420, 96, W - 2 * M, WHITE, 800, 1.12)
    out += body
    out += f'<rect x="{M}" y="{y+10}" width="120" height="8" fill="{ACC}"/>'
    if s.get("sub"):
        b, _ = block(s["sub"], M, y + 110, 42, W - 2 * M, MUTED, 400, 1.3)
        out += b
    return out


def list_slide(s):
    color = {"yes": ACC, "no": "#FF8A80", "info": WHITE}.get(s.get("tone", "info"))
    out = t(M, 210, s.get("kicker", ""), 30, color, 700)
    body, y = block(s["title"], M, 300, 64, W - 2 * M, WHITE, 800, 1.15)
    out += body
    y += 50
    tone = s.get("tone", "info")
    for item in s["items"]:
        cx, cy = M + 20, y - 14
        g = f'<g fill="none" stroke="{color}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">'
        if tone == "yes":
            out += g + f'<polyline points="{cx-18},{cy} {cx-5},{cy+14} {cx+20},{cy-14}"/></g>'
        elif tone == "no":
            out += g + f'<line x1="{cx-15}" y1="{cy-15}" x2="{cx+15}" y2="{cy+15}"/><line x1="{cx+15}" y1="{cy-15}" x2="{cx-15}" y2="{cy+15}"/></g>'
        else:
            out += f'<circle cx="{cx}" cy="{cy}" r="8" fill="{color}"/>'
        b, y2 = block(item, M + 70, y, 40, W - 2 * M - 70, WHITE, 400, 1.3)
        out += b
        y = y2 + 34
    if s.get("note"):
        b, _ = block(s["note"], M, max(y + 20, H - 300), 30, W - 2 * M, MUTED, 400, 1.35)
        out += b
    return out


def cta(s):
    out = t(M, 330, s.get("kicker", ""), 32, ACC, 600)
    body, y = block(s["title"], M, 450, 80, W - 2 * M, WHITE, 800, 1.12)
    out += body
    b, y = block(s.get("sub", ""), M, y + 60, 40, W - 2 * M, MUTED, 400, 1.35)
    out += b
    btn = s.get("button", "DM · WhatsApp")
    out += (f'<rect x="{M}" y="{y+60}" rx="44" width="{len(btn)*24+120}" height="88" fill="{ACC}"/>'
            + t(M + 60, y + 118, btn, 38, BG, 800))
    return out


def render(spec_path, out_dir):
    spec = json.load(open(spec_path, encoding="utf-8"))
    os.makedirs(out_dir, exist_ok=True)
    slides, files = spec["slides"], []
    for i, s in enumerate(slides, 1):
        inner = {"cover": cover, "list": list_slide, "cta": cta}[s["type"]](s)
        svg = frame(inner, i, len(slides), show_arrow=(i < len(slides)))
        p = os.path.join(out_dir, f'{spec["id"]}_{i:02d}.png')
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=p)
        files.append(p)
    return files


if __name__ == "__main__":
    for f in render(sys.argv[1], sys.argv[2]):
        print(f)
