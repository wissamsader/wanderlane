#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WANDERLANE static-site generator.
Reads content modules from content/ and renders a premium, SEO-clean,
affiliate-monetized travel-guide network into site/.

Run:  python3 build.py
Add a city/article: drop a dict into content/*.py -> rebuild -> push.
"""
import os, re, shutil, html, importlib.util, datetime, glob, urllib.parse
from config import BRAND, BASE_URL, TAGLINE, CITIES, AFF, SOCIAL, CONTACT, TP_MARKER, USE_TP, BASE_PATH, AGODA_PAGES, HW_STAYS, HW_CITY_PAGES
try:
    from config import ANALYTICS, GSC_VERIFY
except ImportError:
    ANALYTICS, GSC_VERIFY = "", ""
try:
    from config import CITY_WORDS
except ImportError:
    CITY_WORDS = {}

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "docs")   # GitHub Pages serves /docs at the repo subpath
CONTENT = os.path.join(ROOT, "content")
BIZ_REPOS = os.path.expanduser("~/CLAUDE-DEEPSEEK/business website github")

# ---------------------------------------------------------------- helpers
def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s.lower()).strip()
    return re.sub(r"[\s_]+", "-", s)

def esc(s):
    return html.escape(s, quote=True) if s else ""

def city_by_id(cid):
    for c in CITIES:
        if c["id"] == cid:
            return c
    return None

# ---------- affiliate link engine -------------------------------------
def aff_link(program, target=None, query=None, subid=None):
    """Build an affiliate URL. Points to the real destination always; adds
    Travelpayouts (or direct) tracking once ids are set in config."""
    a = AFF.get(program)
    if not a:
        return target or "#"
    if target and str(target).startswith("http"):
        dest = target
    else:
        q = (query or "").replace(" ", a.get("qspace", "+"))
        dest = a["dest"].format(q=q) if "{q}" in a["dest"] else a["dest"]
    if a.get("wrap"):  # dashboard-verified deep-link (program active for our marker)
        return a["wrap"].format(dest=urllib.parse.quote(dest, safe=""))
    tp = a.get("tp")
    if USE_TP and tp and tp.get("joined") and tp.get("promo_id") and TP_MARKER and not TP_MARKER.startswith("REPLACE"):
        marker = TP_MARKER + (("." + re.sub(r"[^A-Za-z0-9_]", "", subid)) if subid else "")
        sub = tp.get("sub") or "tp"
        return (f"https://{sub}.travelpayouts.com/click?shmarker={marker}"
                f"&promo_id={tp['promo_id']}&source_type=customlink&type=click"
                f"&custom_url={urllib.parse.quote(dest, safe='')}")
    dp, di = a.get("direct_param"), a.get("direct_id")
    if dp and di:
        dest += ("&" if "?" in dest else "?") + f"{dp}={di}"
    return dest

def aff_label(program, fallback="Check prices"):
    a = AFF.get(program) or {}
    return a.get("label", fallback)

def aff_button(program, target=None, query=None, label=None, style="btn-book", small=False):
    if not program:
        return ""
    if program == "agoda" and not (target and str(target).startswith("http")):
        mapped = AGODA_PAGES.get((query or "").strip())
        if mapped:
            target = mapped
        else:  # Agoda text-search is broken (bounces to homepage) — honest fallback
            program = "booking"
    if program == "hostelworld" and not (target and str(target).startswith("http")):
        q = (query or "").strip()
        mapped = HW_STAYS.get(q) or HW_CITY_PAGES.get(q)
        if mapped:
            target = mapped
        else:  # HW has no working text-search GET; unmapped = broken promise, flag it
            print(f"WARN: unmapped hostelworld query {q!r} — add to HW_STAYS/HW_CITY_PAGES; using Booking fallback")
            program = "booking"
    href = aff_link(program, target, query)
    lab = label or aff_label(program)
    cls = "btn " + style + (" btn-sm" if small else "")
    return (f'<a class="{cls}" href="{esc(href)}" target="_blank" '
            f'rel="sponsored nofollow noopener">{esc(lab)} <span class="arr">→</span></a>')

ESIM_COUNTRY = {"chiangmai": "thailand", "beirut": "lebanon", "barcelona": "spain",
                "palermo": "italy", "berlin": "germany", "vietnam": "vietnam"}

def essentials_block(city):
    """Universal 'before you go' money surface: eSIM + insurance. Skipped for Damascus (sensitive)."""
    if not city or city["id"] == "damascus":
        return ""
    ctry = ESIM_COUNTRY.get(city["id"], "")
    esim = aff_button("airalo", query=ctry, label=f'Get a {city["name"]} eSIM', style="btn-book")
    ins = aff_button("safetywing", label="Compare travel insurance", style="btn-forest")
    return ('<div class="callout" style="margin-top:44px">'
            '<div class="c-head">&#9992; Two things worth sorting before you go</div>'
            '<p>Land already connected with an <strong>eSIM</strong> instead of hunting for a SIM at the airport, '
            'and don\'t travel uninsured — one medical bill abroad costs many times the premium.</p>'
            f'<p style="display:flex;gap:12px;flex-wrap:wrap;margin:.2em 0 0">{esim}{ins}</p></div>')

# ---------- business photo bridge (our own owned photos) --------------
# Eyeballed photo picks (photo-gate pass 2026-07-18): swap menu boards, promo
# posters, faces and grim storefronts for appetizing frames. None = use the
# designed no-photo panel instead.
PHOTO_PICKS = {
    ("beirut", "falafel-tabbara"): 8,
    ("beirut", "al-daouk"): 6,
    ("beirut", "malek-al-foul"): 2,
    ("berlin", "abu-haija-fleischerei"): 2,
    ("berlin", "atscham-markt"): None,
    ("berlin", "ali-lobany-fleischerei"): 5,
    ("berlin", "al-amana-fleischerei"): 5,
    ("palermo", "no-zu-toto"): 4,
    ("palermo", "odori-e-sapori"): 5,
    ("palermo", "trattoria-da-pino"): 7,
    ("barcelona", "chez-lola"): 5,
    ("barcelona", "celler-cal-marino"): 7,
    ("damascus", "elburj"): 5,
}

def eat_photo(city_id, slug):
    """Copy a featured business's real photo into site assets; return rel path or None."""
    pick = PHOTO_PICKS.get((city_id, slug), 1)
    if pick is None:
        return None
    repo = os.path.join(BIZ_REPOS, f"{city_id}-github", slug, "img")
    if not os.path.isdir(repo):
        return None
    cands = sorted(glob.glob(os.path.join(repo, "*")))
    imgs = [c for c in cands if c.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]
    if not imgs:
        return None
    pat = re.compile(rf"{pick:02d}\.")
    hero = next((i for i in imgs if pat.search(os.path.basename(i))), imgs[0])
    outdir = os.path.join(SITE, "assets", "eats")
    os.makedirs(outdir, exist_ok=True)
    ext = os.path.splitext(hero)[1].lower()
    outname = f"{city_id}-{slug}{ext}"
    try:
        shutil.copy2(hero, os.path.join(outdir, outname))
        return f"/assets/eats/{outname}"
    except Exception:
        return None

def biz_url(city_id, slug):
    return f"https://wissamsader.github.io/{city_id}/{slug}/"

# Decorative dish still-lifes for slugless DISH cards (no venue claim; alt marks them
# illustrative). Generated 07-18, eyeballed: no text/logos/people, palette-matched.
DISH_STILLS = {
    ("vietnam", "cao-lau"): "/assets/stills/vietnam-cao-lau.jpg",
    ("vietnam", "white-rose-dumplings"): "/assets/stills/vietnam-white-rose.jpg",
    ("vietnam", "banh-mi-phuong"): "/assets/stills/vietnam-banh-mi.jpg",
}

def dish_still(city_id, name):
    key = slugify(re.sub(r"[àáảãạâầấẩẫậăằắẳẵặ]", "a",
          re.sub(r"[èéẻẽẹêềếểễệ]", "e",
          re.sub(r"[ìíỉĩị]", "i",
          re.sub(r"[òóỏõọôồốổỗộơờớởỡợ]", "o",
          re.sub(r"[ùúủũụưừứửữự]", "u", name.lower()))))))
    return DISH_STILLS.get((city_id, key))

# ---------------------------------------------------------------- SVG mark
COMPASS = ('<svg class="wl-mark" viewBox="0 0 32 32" fill="none" aria-hidden="true">'
  '<g class="ring"><circle cx="16" cy="16" r="14" stroke="currentColor" stroke-width="1.6" opacity=".5"/>'
  '<circle cx="16" cy="2.6" r="1.1" fill="currentColor"/></g>'
  '<path class="needle" d="M16 6 L19 16 L16 26 L13 16 Z" fill="currentColor"/>'
  '<circle cx="16" cy="16" r="2" fill="var(--paper)" stroke="currentColor" stroke-width="1.4"/></svg>')

def wl_url(path=""):
    return (BASE_URL.rstrip("/") + "/" + path.lstrip("/")).rstrip("/") if path else BASE_URL

# ---------------------------------------------------------------- chrome
def head(title, desc, path, image=None, jsonld=None, article=False):
    canonical = wl_url(path)
    img = image or f"{BASE_URL}/assets/og-default.png"
    if img.startswith("/"):
        img = BASE_URL.rstrip("/") + img
    ld = ""
    if jsonld:
        import json
        ld = '<script type="application/ld+json">' + json.dumps(jsonld, ensure_ascii=False) + '</script>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(canonical)}">
<meta property="og:type" content="{'article' if article else 'website'}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:image" content="{esc(img)}">
<meta property="og:site_name" content="{esc(BRAND)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FAF6EF">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/wanderlane.css">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
{('<meta name="google-site-verification" content="' + GSC_VERIFY + '">') if GSC_VERIFY else ''}
{ld}
{ANALYTICS}
</head>
<body>
"""

def header(active=None):
    links = ""
    for c in CITIES:
        cls = ' style="color:var(--clay)"' if active == c["id"] else ""
        links += f'<a href="/{c["id"]}/"{cls}>{esc(c["short"])}</a>'
    return f"""<header class="site-head" id="siteHead">
<nav class="nav wrap">
<a class="brand" href="/">{COMPASS}<span>{esc(BRAND)}</span></a>
<button class="nav-toggle" id="navToggle" aria-label="Menu"><span></span><span></span><span></span></button>
<div class="nav-links" id="navLinks">
<div class="nav-cities">{links}</div>
<a href="/about/">About</a>
</div>
</nav>
</header>"""

def disclosure_strip():
    return ('<div class="disclosure"><div class="wrap">'
      '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 100 20 10 10 0 000-20zm1 15h-2v-6h2zm0-8h-2V7h2z"/></svg>'
      '<span>Some links are affiliate links. If you book through them, we may earn a small commission '
      '&mdash; at no extra cost to you. It keeps these guides free. '
      '<a href="/disclosure/">How this works</a>.</span></div></div>')

def footer():
    city_links = "".join(f'<a href="/{c["id"]}/">{esc(c["name"])}</a>' for c in CITIES)
    yr = 2026
    return f"""<footer class="site-foot">
<div class="wrap">
<div>
<div class="foot-brand">{COMPASS}{esc(BRAND)}</div>
<p class="foot-note">{esc(TAGLINE)} Honest, on-the-ground city guides &mdash; real places, written by people who go.</p>
</div>
<div><h4>Cities</h4>{city_links}</div>
<div><h4>Wanderlane</h4>
<a href="/about/">About us</a>
<a href="/disclosure/">Affiliate disclosure</a>
<a href="/privacy/">Privacy</a>
<a href="{esc(SOCIAL.get('pinterest','#'))}" target="_blank" rel="noopener">Pinterest</a>
</div>
</div>
<div class="wrap foot-bottom">
<span>&copy; {yr} {esc(BRAND)}. Written from the road.</span>
<span>Made with care, not by a content farm.</span>
</div>
</footer>
<script src="/assets/wanderlane.js" defer></script>
</body></html>"""

# ---------------------------------------------------------------- blocks
def anchor_id(text):
    return slugify(text)[:50]

def render_block(b, city_id=None):
    t = b.get("t")
    if t == "lead":
        return f'<p class="lead">{b["html"]}</p>'
    if t == "p":
        return f'<p>{b["html"]}</p>'
    if t == "h2":
        i = b.get("id") or anchor_id(b["text"])
        return f'<h2 id="{i}">{esc(b["text"])}</h2>'
    if t == "h3":
        return f'<h3>{esc(b["text"])}</h3>'
    if t == "ul":
        return "<ul>" + "".join(f"<li>{it}</li>" for it in b["items"]) + "</ul>"
    if t == "ol":
        return "<ol>" + "".join(f"<li>{it}</li>" for it in b["items"]) + "</ol>"
    if t == "quote":
        return f'<blockquote>{b["html"]}</blockquote>'
    if t == "figure":
        cap = f'<figcaption>{esc(b["cap"])}</figcaption>' if b.get("cap") else ""
        return f'<figure><img src="{esc(b["img"])}" alt="{esc(b.get("alt",b.get("cap","")))}" loading="lazy">{cap}</figure>'
    if t in ("tip", "warn", "callout"):
        cls = {"tip": "tip", "warn": "warn", "callout": ""}[t]
        head_txt = b.get("head", {"tip": "Local tip", "warn": "Heads up", "callout": ""}[t])
        icon = {"tip": "&#9788;", "warn": "&#9888;", "callout": "&#9432;"}[t]
        hd = f'<div class="c-head">{icon} {esc(head_txt)}</div>' if head_txt else ""
        return f'<div class="callout {cls}">{hd}<p>{b["html"]}</p></div>'
    if t == "book":
        btn = aff_button(b["program"], b.get("target"), b.get("query"), b.get("label"))
        return (f'<div class="callout book"><div class="bk-txt">'
                f'<div class="c-head">&#9992; {esc(b.get("head","Book it"))}</div>'
                f'<p>{b["html"]}</p></div>{btn}</div>')
    if t == "btnrow":
        btns = "".join(aff_button(x["program"], x.get("target"), x.get("query"),
                                  x.get("label"), x.get("style", "btn-book")) for x in b["btns"])
        return f'<p class="btnrow" style="display:flex;gap:12px;flex-wrap:wrap;margin:1.4em 0">{btns}</p>'
    if t == "eats":
        return render_eats(b, city_id)
    if t == "stays":
        return render_stays(b)
    if t == "do":
        return render_do(b)
    if t == "compare":
        return render_compare(b)
    return ""

def render_eats(b, city_id):
    ranked = b.get("ranked")
    items = list(b["items"])
    feature_html = ""
    if b.get("_feature") and items:
        it = items.pop(0)
        cid = it.get("city", city_id)
        slug = it.get("slug")
        photo = it.get("photo") or (eat_photo(cid, slug) if slug else None)
        if photo:
            link = (f'<a class="link-arrow" href="{esc(biz_url(cid,slug))}" target="_blank" rel="noopener">'
                    f'Visit &amp; details <span class="arr">→</span></a>') if slug else ""
            tag = f'<span class="card-tag">{esc(it["area"])}</span>' if it.get("area") else ""
            feature_html = (f'<div class="feature rv"><div class="f-ph">'
                            f'<span class="f-no">No. 01 — the one to start with</span>'
                            f'<img src="{esc(photo)}" alt="{esc(it["name"])}" loading="lazy"></div>'
                            f'<div class="f-body">{tag}<h3>{esc(it["name"])}</h3>'
                            f'<p class="card-blurb">{it["blurb"]}</p>'
                            f'<div class="card-foot"><span class="ours">Featured</span>{link}</div></div></div>')
        else:
            items.insert(0, it)
    cards = ""
    for it in items:
        cid = it.get("city", city_id)
        slug = it.get("slug")
        photo = it.get("photo")
        if slug and not photo:
            photo = eat_photo(cid, slug)
        still = None if photo else dish_still(cid, it["name"])
        if photo:
            img = (f'<div class="frame"><div class="ph">'
                   f'<img src="{esc(photo)}" alt="{esc(it["name"])}" loading="lazy"></div></div>')
        elif still:
            img = (f'<div class="frame"><div class="ph">'
                   f'<img src="{esc(still)}" alt="{esc(it["name"])} — dish still life (illustrative)" loading="lazy"></div></div>')
        else:
            img = ('<div class="frame"><div class="nopic">'
                   '<span class="np-stamp">Wander<br>lane<br>pick</span></div></div>')
        tag = f'<span class="card-tag">{esc(it["area"])}</span>' if it.get("area") else ""
        ours = ""
        link = ""
        if slug:
            ours = '<span class="ours">Featured</span>'
            link = (f'<a class="link-arrow" href="{esc(biz_url(cid,slug))}" target="_blank" '
                    f'rel="noopener">Visit &amp; details <span class="arr">→</span></a>')
        cards += (f'<div class="card">{img}<div class="card-body">{tag}'
                  f'<h3>{esc(it["name"])}</h3>'
                  f'<p class="card-blurb">{it["blurb"]}</p>'
                  f'<div class="card-foot">{ours}{link}</div></div></div>')
    cls = "cards c3" + (" ranked" if ranked else "") + (" ranked-off" if (ranked and feature_html) else "")
    return f'{feature_html}<div class="{cls}">{cards}</div>'

AREA_CODE_DROP = {"the", "a", "an", "of", "de", "el", "la"}
def area_code(area, name):
    """Airport-style 3-letter code from the area (or name) for boarding-pass tabs."""
    src = (area or name or "STA")
    words = [w for w in re.split(r"[^A-Za-z]+", src) if w and w.lower() not in AREA_CODE_DROP]
    if not words:
        return "STA"
    if len(words) >= 2:
        return (words[0][0] + words[1][0] + (words[0][1] if len(words[0]) > 1 else "X")).upper()
    return words[0][:3].upper()

PLANE_SVG = ('<svg class="plane" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">'
             '<path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z"/></svg>')

def render_stays(b):
    cards = ""
    for it in b["items"]:
        code = area_code(it.get("area"), it.get("name"))
        area = f'<span class="pass-area">{esc(it["area"])}</span>' if it.get("area") else ""
        price = f'<span class="price">{esc(it["band"])} <small>/ night</small></span>' if it.get("band") else ""
        btn = aff_button(it.get("program", "booking"), it.get("target"), it.get("query"),
                         it.get("label", "Check prices"), "btn-book btn-sm", small=True)
        cards += (f'<div class="pass"><div class="tab"><span class="code">{esc(code)}</span>'
                  f'{PLANE_SVG}<span class="lbl">Boarding</span></div><div class="perf"></div>'
                  f'<div class="pass-body"><span class="barcode"></span>{area}'
                  f'<h3>{esc(it["name"])}</h3>'
                  f'<p class="card-blurb">{it["blurb"]}</p>'
                  f'<div class="pass-foot">{price}{btn}</div></div></div>')
    return f'<div class="passes">{cards}</div>'

def render_do(b):
    """Things-to-do as an elegant numbered index (hairline rows, Idyllic pattern)."""
    rows = ""
    for it in b["items"]:
        tag = f'<span class="ix-tag">{esc(it["tag"])}</span>' if it.get("tag") else ""
        btn = aff_button(it.get("program", "gyg"), it.get("target"), it.get("query"),
                         it.get("label", "Book"), "btn-forest btn-sm", small=True) if it.get("program") else ""
        rows += (f'<div class="ix-row"><span class="ix-no"></span>'
                 f'<h3>{esc(it["name"])} {tag}</h3>'
                 f'<p class="ix-blurb">{it["blurb"]}</p>'
                 f'<span class="ix-act">{btn}</span></div>')
    return f'<div class="index">{rows}</div>'

def render_compare(b):
    thead = "".join(f"<th>{esc(h)}</th>" for h in b["head"])
    rows = ""
    for r in b["rows"]:
        cells = "".join(f"<td>{c}</td>" for c in r)
        rows += f"<tr>{cells}</tr>"
    cap = f'<p class="muted" style="font-size:.85rem;margin:.4em 0 0">{b["cap"]}</p>' if b.get("cap") else ""
    return f'<div class="table-wrap"><table class="compare"><thead><tr>{thead}</tr></thead><tbody>{rows}</tbody></table></div>{cap}'

# ---------------------------------------------------------------- hero
ROSE_SVG = ('<svg class="rose" viewBox="0 0 200 200" fill="none" stroke="currentColor" aria-hidden="true">'
  '<circle cx="100" cy="100" r="86" stroke-width="1"/><circle cx="100" cy="100" r="62" stroke-width=".6" stroke-dasharray="3 7"/>'
  '<path d="M100 10 L108 92 L100 100 L92 92 Z M100 190 L108 108 L100 100 L92 108 Z '
  'M10 100 L92 92 L100 100 L92 108 Z M190 100 L108 92 L100 100 L108 108 Z" stroke-width="1"/>'
  '<path d="M36 36 L96 96 M164 36 L104 96 M36 164 L96 104 M164 164 L104 104" stroke-width=".5" stroke-dasharray="2 6"/></svg>')

def hero_stamp(city):
    if not city:
        return ""
    return (f'<div class="stamp spin" style="width:120px;height:120px;right:8%;bottom:20%;font-size:.6rem;transform:rotate(10deg)">'
            f'<span>{esc(city["short"]).upper()}<small>WANDERLANE &middot; VERIFIED</small></span></div>')

def hero(page, city):
    img = page.get("hero")
    accent = (city or {}).get("accent", "#1F4D3F")
    if img:
        bg = f'<img class="hero-img" src="{esc(img)}" alt="" fetchpriority="high">'
        cls = "hero has-img"
        style = ""
        deco = ""
    else:
        bg = ""
        cls = "hero"
        style = (f' style="background:radial-gradient(120% 135% at 16% 4%,'
                 f'color-mix(in srgb,{accent} 44%,var(--espresso)) 0%,var(--espresso) 58%)"')
        deco = ROSE_SVG + hero_stamp(city)
    kicker = f'<div class="kicker">{esc(page["kicker"])}</div>' if page.get("kicker") else ""
    dek = f'<p class="dek">{esc(page["dek"])}</p>' if page.get("dek") else ""
    meta = ""
    mparts = []
    if page.get("updated"):
        mparts.append(f'<span>Updated {esc(page["updated"])}</span>')
    if page.get("read"):
        mparts.append(f'<span>{esc(page["read"])} read</span>')
    if mparts:
        meta = '<div class="hero-meta">' + '<span class="dot"></span>'.join(mparts) + '</div>'
    return f"""<section class="{cls}"{style}>{bg}{deco}<div class="hero-inner"><div class="wrap">
{kicker}<h1>{esc(page.get("h1") or page["title"])}</h1>{dek}{meta}</div></div></section>"""

def route_divider():
    return ('<div class="route" aria-hidden="true">'
            '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">'
            '<path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z"/></svg></div>')

# ---------------------------------------------------------------- pages
def build_article(page):
    city = city_by_id(page["city"])
    path = f'{page["city"]}/{page["slug"]}/'
    # toc
    heads = [b for b in page["blocks"] if b.get("t") == "h2"]
    toc_html = ""
    if page.get("toc", True) and len(heads) >= 3:
        items = "".join(f'<a href="#{b.get("id") or anchor_id(b["text"])}">{esc(b["text"])}</a>' for b in heads)
        toc_html = f'<aside class="toc-col"><nav class="toc"><div class="toc-title">In this guide</div>{items}</nav></aside>'
    body = "".join(render_block(b, page["city"]) for b in page["blocks"])
    # faq
    faq_html = ""
    faq_ld = None
    if page.get("faq"):
        qs = "".join(f'<details><summary>{esc(q)}</summary><p>{a}</p></details>' for q, a in page["faq"])
        faq_html = f'<section class="faq"><h2 id="faq">Frequently asked questions</h2>{qs}</section>'
        faq_ld = {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
            for q, a in page["faq"]]}
    # related
    rel_html = ""
    if page.get("related"):
        cards = ""
        for rid in page["related"]:
            rp = PAGE_INDEX.get(rid)
            if rp:
                cards += (f'<a class="guide-card" href="/{rp["city"]}/{rp["slug"]}/">'
                          f'<div class="gc-body"><h3>{esc(rp["title"])}</h3>'
                          f'<p>{esc(rp.get("dek","")[:90])}</p></div></a>')
        if cards:
            rel_html = f'<div class="related"><h2>Keep reading</h2><div class="guide-list">{cards}</div></div>'
    crumb = (f'<div class="crumb wrap"><a href="/">Home</a><span class="sep">/</span>'
             f'<a href="/{city["id"]}/">{esc(city["name"])}</a><span class="sep">/</span>{esc(page["title"])}</div>')
    # light editorial article hero (outlined giant initial, mono meta)
    meta_parts = []
    if page.get("updated"):
        meta_parts.append(f'<span>Updated {esc(page["updated"])}</span>')
    if page.get("read"):
        meta_parts.append(f'<span>{esc(page["read"])} read</span>')
    meta = ('<div class="hero-meta">' + '<span class="dot"></span>'.join(meta_parts) + '</div>') if meta_parts else ""
    art_hero = (f'<section class="art-hero"><div class="wrap">'
                f'<span class="initial" aria-hidden="true">{esc(city["name"][0])}.</span>'
                f'<div class="kicker">{esc(page.get("kicker",""))}</div>'
                f'<h1>{esc(page.get("h1") or page["title"])}</h1>'
                f'<p class="dek">{esc(page.get("dek",""))}</p>{meta}'
                f'</div></section>')
    ld = {"@context": "https://schema.org", "@type": "Article",
          "headline": page["title"], "description": page.get("description", ""),
          "author": {"@type": "Organization", "name": BRAND},
          "publisher": {"@type": "Organization", "name": BRAND},
          "mainEntityOfPage": wl_url(path)}
    graph = {"@context": "https://schema.org", "@graph": [ld] + ([faq_ld] if faq_ld else [])}
    doc = (head(f'{page["title"]} | {BRAND}', page.get("description", page.get("dek", "")), path,
                image=page.get("hero") or f"/assets/og-{page['city']}.png", jsonld=graph, article=True)
           + header(active=page["city"]) + disclosure_strip() + art_hero
           + crumb
           + '<div class="article"><div class="wrap"><div class="article-grid">'
           + toc_html
           + f'<article class="prose">{body}{faq_html}{essentials_block(city)}{rel_html}</article>'
           + '</div></div></div>'
           + footer())
    write(path, doc)

def city_slugs(city):
    """All featured-business slugs used anywhere in this city's content (for photo strips)."""
    slugs, seen = [], set()
    def harvest(blocks):
        for b in blocks or []:
            if b.get("t") == "eats":
                for it in b["items"]:
                    s = it.get("slug")
                    if s and s not in seen:
                        seen.add(s); slugs.append(s)
    harvest(city.get("intro_blocks"))
    for p in ALL_PAGES:
        if p["city"] == city["id"]:
            harvest(p.get("blocks"))
    return slugs

STRIP_FALLBACK = {   # cities with few featured-eats photos still get a real-photo band
    "vietnam": ["banh-xeo-ba-duong", "bun-cha-ca-109", "kon-tiki-hostel", "nha-bo-homestay", "may-spa", "harmony-haven-spa"],
}

def photo_strip(city, count=6, skip=1):
    """A band of real, vetted photos from this city's featured businesses."""
    figs, n, used = "", 0, set()
    def add(ph, label):
        nonlocal figs, n
        if not ph or ph in used:
            return
        used.add(ph)
        figs += (f'<figure><img src="{esc(ph)}" alt="{esc(label)}" loading="lazy">'
                 f'<figcaption>{esc(label)}</figcaption></figure>')
        n += 1
    for s in city_slugs(city)[skip:]:
        if n >= count:
            break
        add(eat_photo(city["id"], s), s.replace("-", " "))
    if n < count:
        for s in STRIP_FALLBACK.get(city["id"], []):
            if n >= count:
                break
            add(eat_photo(city["id"], s), s.replace("-", " "))
    if n < count and city["id"] == "chiangmai":
        for ph in thumb_pool("chiangmai")[1:]:      # guesthouse photos (skip the hero itself)
            if n >= count:
                break
            label = os.path.basename(ph).replace("chiangmai-", "").rsplit(".", 1)[0].replace("-", " ")
            add(ph, label)
    return f'<div class="strip rv">{figs}</div>' if n >= 4 else ""

def dotline(city_id, dark=False):
    words = CITY_WORDS.get(city_id)
    if not words:
        return ""
    seq = "".join(f"<span>{esc(w)}</span>" for w in words)
    cls = "dotline on-dark" if dark else "dotline"
    return f'<div class="{cls}" aria-hidden="true"><div class="ticker-track">{seq}{seq}</div></div>'

def city_hero(city):
    n_guides = len([p for p in ALL_PAGES if p["city"] == city["id"]]) + 1
    n_places = len(city_slugs(city))
    img = city.get("hero")
    photo = (f'<img src="{esc(img)}" alt="{esc(city["name"])}" fetchpriority="high">'
             if img else "")
    cap = f'<span class="ch-cap">Photographed on the ground &middot; {esc(city["name"])}</span>'
    initial = esc(city["name"][0]) + "."
    stat_places = f'<div><b>{n_places or "—"}</b>places we vouch for</div>' if n_places else ""
    return f"""<section class="city-hero">
<div class="ch-left"><span class="initial" aria-hidden="true">{initial}</span>
<div class="kicker">{esc(city.get("region_label",""))}</div>
<h1>{esc(city["name"])}</h1>
<p class="dek">{esc(city.get("dek",""))}</p>
<div class="ch-meta"><div><b>{n_guides}</b>guides</div>{stat_places}<div><b>July&nbsp;2026</b>last walked</div></div>
</div>
<div class="ch-right">{photo}{cap}</div>
</section>"""

def build_hub(city):
    path = f'{city["id"]}/'
    pages = [p for p in ALL_PAGES if p["city"] == city["id"]]
    pages.sort(key=lambda p: p.get("order", 99))
    # transform intro blocks: number the h2s as chapters, feature the first eats
    blocks = [dict(b) for b in city.get("intro_blocks", [])]
    ch = 0
    first_eats = True
    parts = []
    for b in blocks:
        if b.get("t") == "h2":
            ch += 1
            parts.append(f'<div class="chapter rv"><span class="no">CH. {ch:02d}</span><h2 id="{anchor_id(b["text"])}">{esc(b["text"])}</h2></div>')
            continue
        if b.get("t") == "eats" and first_eats:
            b["_feature"] = True
            first_eats = False
        parts.append(render_block(b, city["id"]))
    intro = "".join(parts)
    # go-deeper cards for the city's articles
    guide_cards = ""
    for i, p in enumerate(pages):
        kick = (p.get("kicker") or "").split("·")[-1].strip() or "Guide"
        guide_cards += (f'<a class="guide-card rv rv-d{i%3}" href="/{city["id"]}/{p["slug"]}/">'
                        f'{guide_thumb(p, i+1)}'
                        f'<div class="gc-body"><span class="gc-kicker">{esc(kick)}</span><h3>{esc(p["title"])}</h3>'
                        f'<p>{esc(p.get("dek","")[:100])}</p></div></a>')
    deeper = ""
    if guide_cards:
        deeper = ('<section class="sec sec-alt"><div class="wrap">'
                  f'<div class="sec-head rv"><div class="kicker">Go deeper</div><h2>More {esc(city["name"])} guides</h2></div>'
                  f'<div class="guide-list">{guide_cards}</div></div></section>')
    # faq
    faq_html, faq_ld = "", None
    if city.get("faq"):
        qs = "".join(f'<details><summary>{esc(q)}</summary><p>{a}</p></details>' for q, a in city["faq"])
        faq_html = ('<section class="sec"><div class="wrap"><div class="prose" style="margin-inline:auto">'
                    f'<div class="faq"><h2 id="faq">{esc(city["name"])} FAQ</h2>{qs}</div></div></div></section>')
        faq_ld = {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
            for q, a in city["faq"]]}
    coll = {"@context": "https://schema.org", "@type": "CollectionPage",
            "name": f'{city["name"]} Travel Guide', "description": city.get("dek", ""), "url": wl_url(path)}
    graph = {"@context": "https://schema.org", "@graph": [coll] + ([faq_ld] if faq_ld else [])}
    doc = (head(f'{city["name"]} Travel Guide: Where to Eat, Stay & What to Do | {BRAND}',
                city.get("dek", ""), path, image=city.get("hero") or f"/assets/og-{city['id']}.png", jsonld=graph)
           + header(active=city["id"]) + disclosure_strip()
           + city_hero(city)
           + dotline(city["id"])
           + f'<section class="sec"><div class="wrap">{photo_strip(city)}<div class="prose" style="max-width:960px;margin-inline:auto">{intro}</div></div></section>'
           + deeper + faq_html
           + (f'<section class="sec"><div class="wrap"><div class="prose" style="max-width:960px;margin-inline:auto">{essentials_block(city)}</div></div></section>' if essentials_block(city) else "")
           + footer())
    write(path, doc)

def build_home():
    cards = ""
    for i, c in enumerate(CITIES):
        ph = c.get("hero")
        img = (f'<img src="{esc(ph)}" alt="{esc(c["name"])}" loading="lazy">' if ph else "")
        n = len([p for p in ALL_PAGES if p["city"] == c["id"]])
        cnt = "Guide" if n == 0 else f'{n+1}<br>guides'
        cards += (f'<a class="postcard rv rv-d{i%3}" href="/{c["id"]}/">'
                  f'<span class="pc-air"></span><div class="ph">{img}</div>'
                  f'<div class="pc-body"><div><h3>{esc(c["name"])}</h3>'
                  f'<div class="pc-sub">{esc(c.get("region_label",""))} &middot; {esc(c.get("tagline",""))}</div></div>'
                  f'<span class="pc-count">{cnt}</span></div></a>')
    ticker_cities = "".join(f"<span>{esc(c['name'])}</span>" for c in CITIES)
    ticker = (f'<div class="dotline on-dark" aria-hidden="true"><div class="ticker-track">'
              f'{ticker_cities}{ticker_cities}</div></div>')
    hero_img = ""
    hp = os.path.join(SITE, "assets/heroes/beirut.jpg")
    if os.path.exists(hp):
        hero_img = '<img class="hero-img" src="/assets/heroes/beirut.jpg" alt="" fetchpriority="high">'
    home_hero = f"""<section class="hero home-hero has-img">
{hero_img}{ROSE_SVG}
<div class="stamp spin" style="width:126px;height:126px;left:7%;top:16%;font-size:.6rem;color:var(--cream);transform:rotate(-12deg)"><span>EST. 2026<small>FIELD NOTES</small></span></div>
<div class="stamp" style="width:98px;height:98px;right:9%;top:24%;font-size:.54rem;color:var(--ochre);transform:rotate(9deg)"><span>7 CITIES<small>ON FOOT</small></span></div>
<div class="hero-inner"><div class="wrap">
<div class="kicker" style="justify-content:center">{esc(BRAND)} &middot; honest city guides</div>
<h1>The good streets, <em>found</em> for you.</h1>
<p class="dek">Where to eat, where to stay, and what's actually worth your time &mdash; in the cities we know by foot, not by algorithm.</p>
<div class="hero-cta"><a class="btn btn-book btn-lg" href="#cities">Pick a city <span class="arr">↓</span></a></div>
</div></div>{ticker}</section>"""
    ld = {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND,
          "url": BASE_URL, "description": TAGLINE}
    doc = (head(f'{BRAND} — Honest City Guides for Food, Stays & Real Experiences',
                "Independent, on-the-ground travel guides to Chiang Mai, Beirut, Barcelona, Palermo, Berlin, Da Nang & Hoi An, and Damascus. Where to eat, where to stay, what to do.",
                "", image=HOME_HERO, jsonld=ld)
           + header() + home_hero
           + '<section class="sec" id="cities"><div class="wrap"><div class="sec-head center rv"><div class="kicker">Pick a city</div>'
           + '<h2>Where are you going?</h2><p class="muted">Every guide is built from real places we\'ve walked into — not a scraped list.</p></div>'
           + f'<div class="city-grid">{cards}</div></div></section>'
           + route_divider()
           + home_popular()
           + home_manifesto()
           + footer())
    write("", doc)

POPULAR = ["where-to-eat-in-chiang-mai", "3-days-in-barcelona", "where-to-eat-in-berlin",
           "chiang-mai-scooter-rental", "where-to-eat-in-palermo", "da-nang-hoi-an-itinerary"]

# Chiang Mai guesthouse photos (its repo layout is <slug>/photos/); vetted picks.
CM_THUMBS = [("hoh-guesthouse", 1), ("little-siri", 4), ("baan-thalang", 1), ("tangmo-house", 1), ("chinda-boutique", 2)]
_THUMB_POOLS = {}

def thumb_pool(city_id):
    """Per-city pool of distinct real photos for guide-card thumbs."""
    if city_id in _THUMB_POOLS:
        return _THUMB_POOLS[city_id]
    pool = []
    hp = os.path.join(SITE, f"assets/heroes/{city_id}.jpg")
    if os.path.exists(hp):
        pool.append(f"/assets/heroes/{city_id}.jpg")
    if city_id == "chiangmai":
        outdir = os.path.join(SITE, "assets", "thumbs")
        os.makedirs(outdir, exist_ok=True)
        for slug, n in CM_THUMBS:
            for ext in (".jpg", ".jpeg", ".png"):
                src = os.path.join(BIZ_REPOS, "chiangmai-github", slug, "photos", f"{n:02d}{ext}")
                if os.path.exists(src):
                    out = f"chiangmai-{slug}.jpg"
                    shutil.copy2(src, os.path.join(outdir, out))
                    pool.append(f"/assets/thumbs/{out}")
                    break
    else:
        c = city_by_id(city_id)
        if c:
            for s in city_slugs(c):
                ph = eat_photo(city_id, s)
                if ph and ph not in pool:
                    pool.append(ph)
                if len(pool) >= 7:
                    break
    _THUMB_POOLS[city_id] = pool
    return pool

def guide_thumb(p, i=0):
    """Photo thumb for a guide card — a different real photo per card."""
    pool = thumb_pool(p["city"])
    if pool:
        ph = pool[i % len(pool)]
        return f'<img src="{esc(ph)}" alt="" loading="lazy">'
    return ('<div class="gc-side">'
            '<svg width="54" height="54" viewBox="0 0 32 32" fill="none" stroke="currentColor">'
            '<circle cx="16" cy="16" r="13" stroke-width="1.2"/>'
            '<path d="M16 6 L19 16 L16 26 L13 16 Z" fill="currentColor" stroke="none"/></svg></div>')

def home_popular():
    cards = ""
    for i, slug in enumerate(POPULAR):
        p = PAGE_INDEX.get(slug)
        if not p:
            continue
        c = city_by_id(p["city"])
        cards += (f'<a class="guide-card rv rv-d{i%3}" href="/{p["city"]}/{p["slug"]}/">'
                  f'{guide_thumb(p, i)}'
                  f'<div class="gc-body"><span class="gc-kicker">{esc(c["name"])}</span>'
                  f'<h3>{esc(p["title"])}</h3><p>{esc(p.get("dek","")[:88])}</p></div></a>')
    if not cards:
        return ""
    return ('<section class="sec"><div class="wrap">'
            '<div class="sec-head center rv"><div class="kicker">Reader favourites</div>'
            '<h2>Popular guides</h2></div>'
            f'<div class="guide-list">{cards}</div></div></section>')

def home_manifesto():
    return ('<section class="sec sec-dark"><div class="wrap"><div class="prose center rv" style="margin-inline:auto;position:relative">'
      '<div class="kicker" style="justify-content:center;color:var(--cream)">Why Wanderlane</div>'
      '<h2>The internet is full of fake travel advice.<br><em style="color:var(--clay-soft)">This isn&rsquo;t.</em></h2>'
      '<p>Most &ldquo;best of&rdquo; travel lists are written by people who have never been there — the same fifteen places, reworded by a machine. '
      'Our guides start from restaurants, caf&eacute;s and stays we actually feature and photograph on the ground, then fill in the practical stuff you really need: '
      'how to get there, what to book ahead, what to skip. No fluff, no invented five-star everything. Just the good streets.</p>'
      '</div></div></section>')

# ---------------------------------------------------------------- simple pages
def build_simple(slug, title, desc, body_html):
    path = f'{slug}/'
    doc = (head(f'{title} | {BRAND}', desc, path)
           + header()
           + f'<section class="article"><div class="wrap"><article class="prose">'
           + f'<div class="kicker">{esc(BRAND)}</div><h1 style="font-size:clamp(2rem,5vw,3rem);margin-bottom:.5em">{esc(title)}</h1>'
           + body_html + '</article></div></section>'
           + footer())
    write(path, doc)

# ---------------------------------------------------------------- io
def write(path, doc):
    if BASE_PATH:   # prefix root-absolute internal links/assets for GitHub Pages subpath hosting
        doc = (doc.replace('href="/', f'href="{BASE_PATH}/').replace('src="/', f'src="{BASE_PATH}/')
                  .replace("href='/", f"href='{BASE_PATH}/").replace("src='/", f"src='{BASE_PATH}/"))
    out = os.path.join(SITE, path, "index.html") if path else os.path.join(SITE, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)

def load_content():
    pages = []
    for fp in sorted(glob.glob(os.path.join(CONTENT, "*.py"))):
        name = os.path.splitext(os.path.basename(fp))[0]
        if name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"content_{name}", fp)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "PAGES"):
            pages.extend(mod.PAGES)
        if hasattr(mod, "CITY"):        # augment the matching config city (intro_blocks, faq)
            c = city_by_id(mod.CITY.get("id"))
            if c:
                c.update({k: v for k, v in mod.CITY.items() if k != "id"})
    return pages

def sitemap():
    urls = [""] + [f'{c["id"]}/' for c in CITIES] + [f'{p["city"]}/{p["slug"]}/' for p in ALL_PAGES] \
           + ["about/", "disclosure/", "privacy/"]
    today = "2026-07-18"
    body = "".join(f'<url><loc>{wl_url(u)}</loc><lastmod>{today}</lastmod>'
                   f'<priority>{"1.0" if u=="" else "0.8" if u.count("/")<=1 else "0.7"}</priority></url>' for u in urls)
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">{body}</urlset>'
    with open(os.path.join(SITE, "sitemap.xml"), "w") as f:
        f.write(xml.replace("sitemap.org/schemas/sitemap", "sitemaps.org/schemas/sitemap"))

def copy_static():
    """Copy the design system + assets (css/js/favicon/og/heroes) from static/ into docs/assets/."""
    src = os.path.join(ROOT, "static")
    dst = os.path.join(SITE, "assets")
    shutil.copytree(src, dst, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".*"))

def static_files():
    copy_static()
    with open(os.path.join(SITE, "CNAME"), "w") as f:      # GitHub Pages custom domain
        f.write("wanderlane.space\n")
    with open(os.path.join(SITE, "wanderlane2026seed.txt"), "w") as f:   # IndexNow key file
        f.write("wanderlane2026seed")
    with open(os.path.join(SITE, ".nojekyll"), "w") as f:
        f.write("")
    with open(os.path.join(SITE, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n")

# ---------------------------------------------------------------- run
HOME_HERO = "/assets/heroes/home.jpg" if os.path.exists(os.path.join(SITE, "assets/heroes/home.jpg")) else None
ALL_PAGES = []
PAGE_INDEX = {}

def main():
    global ALL_PAGES, PAGE_INDEX, HOME_HERO
    copy_static()   # bring css/js/heroes into docs/assets BEFORE hero paths are resolved
    ALL_PAGES = load_content()
    PAGE_INDEX = {p["slug"]: p for p in ALL_PAGES}
    # resolve hero images if present on disk
    for c in CITIES:
        hp = os.path.join(SITE, f'assets/heroes/{c["id"]}.jpg')
        if os.path.exists(hp):
            c["hero"] = f'/assets/heroes/{c["id"]}.jpg'
    hh = os.path.join(SITE, "assets/heroes/home.jpg")
    HOME_HERO = "/assets/heroes/home.jpg" if os.path.exists(hh) else None
    for p in ALL_PAGES:
        build_article(p)
    for c in CITIES:
        build_hub(c)
    build_home()
    # simple pages built by content/_pages via SIMPLE if present
    try:
        import importlib.util as _il
        sp = os.path.join(CONTENT, "_pages.py")
        if os.path.exists(sp):
            spec = _il.spec_from_file_location("content_pages", sp)
            mod = _il.module_from_spec(spec); spec.loader.exec_module(mod)
            for s in mod.SIMPLE:
                build_simple(s["slug"], s["title"], s["desc"], s["html"])
    except Exception as e:
        print("simple pages:", e)
    sitemap(); static_files()
    print(f"Built {len(ALL_PAGES)} articles + {len(CITIES)} city hubs + home. -> {SITE}")

if __name__ == "__main__":
    main()
