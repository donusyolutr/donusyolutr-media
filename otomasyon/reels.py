"""Dönüş Yolu reels üretici (dikey 1080x1920, seslendirme + sahneler).
Kullanım: python3 reels.py icerik/onayli/<id>.json <ses.mp3 veya ses_suresi_saniye> cikti/
(Sure verilirse sessiz video uretilir; ses Descript tarafinda eklenir.)
JSON'da "reels" alanı: {"sahneler": [{"ust": "...", "metin": "...", "ton": "yes|no|info|cover|cta"}], "seslendirme": "..."}
Sahne süreleri seslendirme süresine karakter sayısıyla orantılı bölünür.
"""
import json, sys, os, html, subprocess
import cairosvg

W, H = 1080, 1920
BG, ACC, GREEN, BLUE, WHITE, MUTED, RED = "#062018", "#9FE3C4", "#006B3C", "#00468C", "#FFFFFF", "#B7CFC4", "#FF8A80"
FONT = "Inter, DejaVu Sans, sans-serif"
M = 90


def wrap(text, size, max_w, weight=800):
    k = 0.56 if weight >= 700 else 0.52
    mx = max(6, int(max_w / (size * k)))
    lines, cur = [], ""
    for w in text.split():
        if len(cur) + len(w) + (1 if cur else 0) <= mx:
            cur = f"{cur} {w}".strip()
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines


def t(x, y, s, size, fill=WHITE, weight=400, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}">{html.escape(s)}</text>')


def scene_svg(s):
    tone = s.get("ton", "info")
    color = {"yes": ACC, "no": RED, "info": WHITE, "cover": ACC, "cta": ACC}[tone]
    size = 104 if tone == "cover" else 88
    lines = wrap(s["metin"], size, W - 2 * M)
    lh = size * 1.15
    y0 = H / 2 - (len(lines) * lh) / 2 + size * 0.8
    body = "".join(t(M, y0 + i * lh, l, size, WHITE, 800) for i, l in enumerate(lines))
    ust = t(M, y0 - size - 40, s.get("ust", ""), 44, color, 700)
    bar = (f'<rect x="0" y="0" width="{W/2}" height="18" fill="{GREEN}"/>'
           f'<rect x="{W/2}" y="0" width="{W/2}" height="18" fill="{BLUE}"/>')
    sig = t(M, H - 300, "@donusyolutr", 40, ACC, 600)  # Reels arayüzü alt ~250px'i kapatır
    btn = ""
    if tone == "cta":
        btn = (f'<rect x="{M}" y="{y0 + len(lines)*lh + 40}" rx="56" width="520" height="112" fill="{ACC}"/>'
               + t(M + 60, y0 + len(lines)*lh + 116, "DM'den yazın", 52, BG, 800))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<rect width="{W}" height="{H}" fill="{BG}"/>{bar}{ust}{body}{btn}{sig}</svg>')


def dur(path):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", path]).strip())


def render(spec_path, audio, out_dir):
    spec = json.load(open(spec_path, encoding="utf-8"))
    sc = spec["reels"]["sahneler"]
    os.makedirs(out_dir, exist_ok=True)
    tmp = os.path.join(out_dir, "_tmp"); os.makedirs(tmp, exist_ok=True)
    sessiz = not os.path.exists(audio)
    total = (float(audio) if sessiz else dur(audio)) + 0.8
    weights = [max(12, len(s["metin"])) for s in sc]
    secs = [total * w / sum(weights) for w in weights]
    parts = []
    for i, (s, d) in enumerate(zip(sc, secs)):
        png = os.path.join(tmp, f"s{i}.png")
        cairosvg.svg2png(bytestring=scene_svg(s).encode(), write_to=png)
        mp4 = os.path.join(tmp, f"s{i}.mp4")
        # hafif yakınlaşma + giriş/çıkış kararması
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png, "-t", f"{d:.2f}",
                        "-vf", f"scale=1188:2112,zoompan=z='min(zoom+0.0006,1.06)':d={int(d*30)}:s=1080x1920:fps=30,"
                               f"fade=t=in:st=0:d=0.25,fade=t=out:st={max(0,d-0.25):.2f}:d=0.25",
                        "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", mp4], check=True)
        parts.append(mp4)
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in parts))
    out = os.path.join(out_dir, f'{spec["id"]}_reels.mp4')
    ses = [] if sessiz else ["-i", audio]
    enc = ["-an"] if sessiz else ["-c:a", "aac", "-b:a", "160k", "-shortest"]
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, *ses,
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", *enc, "-movflags", "+faststart", out], check=True)
    # kapak: ilk sahne
    cover = os.path.join(out_dir, f'{spec["id"]}_kapak.jpg')
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.join(tmp, "s0.png"), cover], check=True)
    subprocess.run(["rm", "-rf", tmp])
    return out, cover


if __name__ == "__main__":
    print(*render(sys.argv[1], sys.argv[2], sys.argv[3]), sep="\n")
