# -*- coding: utf-8 -*-
"""Generate 1000x1500 Pinterest pins as HTML (screenshot to PNG after).
City-food pins use REAL photos we own (from the business repos); Chiang Mai
and home use premium accent gradients. Magazine-cover style, on brand."""
import os, glob, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
PINS = os.path.join(ROOT, "pins")
HTML = os.path.join(PINS, "html")
PHOTO = os.path.join(PINS, "photos")
BIZ = os.path.expanduser("~/CLAUDE-DEEPSEEK/business website github")
for d in (HTML, PHOTO):
    os.makedirs(d, exist_ok=True)

def biz_photo(city, slug):
    d = os.path.join(BIZ, f"{city}-github", slug, "img")
    imgs = sorted(glob.glob(os.path.join(d, "*.jpg")) + glob.glob(os.path.join(d, "*.png")))
    hero = next((i for i in imgs if "01." in os.path.basename(i)), imgs[0] if imgs else None)
    if not hero:
        return None
    out = os.path.join(PHOTO, f"{city}-{slug}.jpg")
    shutil.copy2(hero, out)
    return f"../photos/{city}-{slug}.jpg"

# pin defs: (file, kicker, title, accent, photo(city,slug) or None)
PINSET = [
 ("pin-home",           "WANDERLANE",              "The good streets, found.",            "#1F4D3F", None),
 ("pin-chiangmai-eat",  "CHIANG MAI · FOOD",       "Where to Eat in Chiang Mai",          "#A85D2A", None),
 ("pin-chiangmai-stay", "CHIANG MAI",              "Where to Stay in Chiang Mai",         "#A85D2A", None),
 ("pin-chiangmai-scooter","CHIANG MAI",            "Renting a Scooter in Chiang Mai",     "#A85D2A", None),
 ("pin-chiangmai-do",   "CHIANG MAI",              "The Best Things to Do in Chiang Mai", "#A85D2A", None),
 ("pin-berlin-eat",     "BERLIN · SONNENALLEE",    "The Best Arab Food in Berlin",        "#3B4A54", ("berlin","azzam-restaurant")),
 ("pin-palermo-eat",    "PALERMO · STREET FOOD",   "Where to Eat in Palermo",             "#245C7A", ("palermo","osteria-mercede")),
 ("pin-barcelona-eat",  "BARCELONA",               "Where to Eat in Barcelona Like a Local","#A5302A", ("barcelona","bar-marsella")),
 ("pin-beirut-eat",     "BEIRUT · FOOD",           "Where to Eat in Beirut",              "#1E6A73", ("beirut","lmatbakh")),
 ("pin-vietnam-eat",    "DA NANG · FOOD",          "Where to Eat in Da Nang",             "#15795A", ("vietnam","banh-xeo-ba-duong")),
 ("pin-damascus",       "DAMASCUS",                "The Tables of Damascus",              "#6E5A34", ("damascus","bakdash")),
]

COMPASS = ('<svg width="34" height="34" viewBox="0 0 32 32" fill="none">'
  '<circle cx="16" cy="16" r="14" stroke="#fff" stroke-width="1.6" opacity=".6"/>'
  '<circle cx="16" cy="2.6" r="1.2" fill="#fff"/>'
  '<path d="M16 6 L19 16 L16 26 L13 16 Z" fill="#fff"/>'
  '<circle cx="16" cy="16" r="2" fill="none" stroke="#fff" stroke-width="1.4"/></svg>')

def pin_html(kicker, title, accent, photo):
    if photo:
        bg = (f'<img src="{photo}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'
              f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,'
              f'rgba(20,16,12,.30) 0%,rgba(20,16,12,.20) 42%,rgba(20,16,12,.86) 100%)"></div>')
    else:
        bg = (f'<div style="position:absolute;inset:0;background:radial-gradient(120% 120% at 18% 8%,'
              f'color-mix(in srgb,{accent} 82%,#000),{accent} 55%,color-mix(in srgb,{accent} 55%,#000))"></div>'
              f'<div style="position:absolute;inset:0;background:'
              f'repeating-linear-gradient(135deg,rgba(255,255,255,.04) 0 2px,transparent 2px 26px)"></div>')
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@500;600;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;box-sizing:border-box}}
body{{width:1000px;height:1500px;overflow:hidden;font-family:'Inter',sans-serif}}
.pin{{position:relative;width:1000px;height:1500px;isolation:isolate;color:#fff;display:flex;flex-direction:column;justify-content:flex-end}}
.frame{{position:absolute;inset:34px;border:2px solid rgba(255,255,255,.5);z-index:3;pointer-events:none}}
.kicker{{font-weight:700;letter-spacing:.22em;font-size:26px;text-transform:uppercase;color:#fff;opacity:.92;margin-bottom:22px}}
h1{{font-family:'Fraunces',serif;font-weight:600;font-size:96px;line-height:1.02;letter-spacing:-.02em;text-shadow:0 2px 40px rgba(0,0,0,.4);max-width:15ch}}
.content{{position:relative;z-index:2;padding:0 78px 150px}}
.brand{{position:absolute;left:0;right:0;bottom:66px;z-index:2;display:flex;align-items:center;justify-content:center;gap:13px;font-family:'Fraunces',serif;font-size:34px;font-weight:600;letter-spacing:.01em}}
.tag{{position:absolute;top:70px;left:78px;z-index:2;font-family:'Fraunces',serif;font-style:italic;font-size:30px;opacity:.9}}
</style></head><body>
<div class="pin">{bg}<div class="frame"></div>
<div class="tag">Honest city guides</div>
<div class="content"><div class="kicker">{kicker}</div><h1>{title}</h1></div>
<div class="brand">{COMPASS}<span>Wanderlane</span></div>
</div></body></html>"""

txt = []
for name, kicker, title, accent, ph in PINSET:
    photo = biz_photo(*ph) if ph else None
    with open(os.path.join(HTML, name + ".html"), "w", encoding="utf-8") as f:
        f.write(pin_html(kicker, title, accent, photo))
    txt.append(f"{name}.png\n  {title}\n  {kicker}\n")
with open(os.path.join(PINS, "pins.txt"), "w", encoding="utf-8") as f:
    f.write("WANDERLANE PINS — titles for upload\n\n" + "\n".join(txt))
print(f"Generated {len(PINSET)} pin HTML files in {HTML}")
