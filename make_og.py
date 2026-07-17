# -*- coding: utf-8 -*-
"""Generate per-city 1200x630 social-share (OG) cards into static/og-<city>.png,
using our own real photos where we have them. build.py copies static/* to docs/assets/."""
import os, glob, shutil, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(ROOT, "static")
TMP = os.path.join(ROOT, "pins", "og_html")
PHOTO = os.path.join(ROOT, "pins", "photos")
BIZ = os.path.expanduser("~/CLAUDE-DEEPSEEK/business website github")
os.makedirs(TMP, exist_ok=True); os.makedirs(PHOTO, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def biz_photo(city, slug):
    d = os.path.join(BIZ, f"{city}-github", slug, "img")
    imgs = sorted(glob.glob(os.path.join(d, "*.jpg")) + glob.glob(os.path.join(d, "*.png")))
    hero = next((i for i in imgs if "01." in os.path.basename(i)), imgs[0] if imgs else None)
    if not hero:
        return None
    out = os.path.join(PHOTO, f"og-{city}-{slug}.jpg")
    shutil.copy2(hero, out)
    return out

# city, region label, accent, (photo city, slug) or None
CITIES = [
 ("chiangmai","Chiang Mai","Northern Thailand","#A85D2A", None),
 ("beirut","Beirut","Lebanon","#1E6A73", ("beirut","lmatbakh")),
 ("barcelona","Barcelona","Catalonia, Spain","#A5302A", ("barcelona","bar-marsella")),
 ("palermo","Palermo","Sicily, Italy","#245C7A", ("palermo","osteria-mercede")),
 ("berlin","Berlin","Germany","#3B4A54", ("berlin","azzam-restaurant")),
 ("vietnam","Da Nang & Hoi An","Central Vietnam","#15795A", ("vietnam","banh-xeo-ba-duong")),
 ("damascus","Damascus","Syria","#6E5A34", ("damascus","bakdash")),
]

def og_html(name, region, accent, photo):
    if photo:
        bg = (f'<img src="file://{photo}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'
              f'<div style="position:absolute;inset:0;background:linear-gradient(105deg,rgba(20,16,12,.86) 0%,rgba(20,16,12,.55) 55%,rgba(20,16,12,.30) 100%)"></div>')
    else:
        bg = (f'<div style="position:absolute;inset:0;background:radial-gradient(120% 120% at 15% 10%,'
              f'color-mix(in srgb,{accent} 82%,#000),{accent} 55%,color-mix(in srgb,{accent} 55%,#000))"></div>')
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@600;700&display=swap" rel="stylesheet">
<style>*{{margin:0;box-sizing:border-box}}body{{width:1200px;height:630px;overflow:hidden;font-family:'Inter'}}
.og{{position:relative;width:1200px;height:630px;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 80px}}
.k{{position:relative;font-weight:700;letter-spacing:.2em;font-size:22px;text-transform:uppercase;color:#ffd9c2;margin-bottom:16px}}
h1{{position:relative;font-family:'Fraunces';font-weight:600;font-size:88px;line-height:1;letter-spacing:-.02em;text-shadow:0 2px 30px rgba(0,0,0,.4)}}
.sub{{position:relative;margin-top:20px;font-size:26px;color:rgba(255,255,255,.9);font-weight:600}}
.brand{{position:absolute;bottom:44px;left:80px;display:flex;align-items:center;gap:11px;font-family:'Fraunces';font-size:28px;font-weight:600}}
</style></head><body><div class="og">{bg}
<div class="k">{region}</div><h1>{name}</h1><div class="sub">Where to eat, stay &amp; what to do</div>
<div class="brand"><svg width="30" height="30" viewBox="0 0 32 32"><circle cx="16" cy="16" r="14" stroke="#fff" stroke-width="1.6" fill="none" opacity=".6"/><circle cx="16" cy="2.6" r="1.2" fill="#fff"/><path d="M16 6 L19 16 L16 26 L13 16 Z" fill="#fff"/></svg><span>Wanderlane</span></div>
</div></body></html>"""

for cid, name, region, accent, ph in CITIES:
    photo = biz_photo(*ph) if ph else None
    hp = os.path.join(TMP, f"{cid}.html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(og_html(name, region, accent, photo))
    out = os.path.join(STATIC, f"og-{cid}.png")
    subprocess.run([CHROME, "--headless=new", "--window-size=1200,630", "--virtual-time-budget=6000",
                    "--hide-scrollbars", f"--screenshot={out}", f"file://{hp}"],
                   capture_output=True)
    print("og:", cid, "ok" if os.path.exists(out) else "FAIL")
print("done")
