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
from config import BRAND, BASE_URL, TAGLINE, CITIES, AFF, SOCIAL, CONTACT, TP_MARKER, USE_TP, BASE_PATH

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
    tp = a.get("tp")
    if USE_TP and tp and tp.get("promo_id") and TP_MARKER and not TP_MARKER.startswith("REPLACE"):
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
    href = aff_link(program, target, query)
    lab = label or aff_label(program)
    cls = "btn " + style + (" btn-sm" if small else "")
    return (f'<a class="{cls}" href="{esc(href)}" target="_blank" '
            f'rel="sponsored nofollow noopener">{esc(lab)} <span class="arr">→</span></a>')

# ---------- business photo bridge (our own owned photos) --------------
def eat_photo(city_id, slug):
    """Copy a featured business's real hero photo into site assets; return rel path or None."""
    repo = os.path.join(BIZ_REPOS, f"{city_id}-github", slug, "img")
    if not os.path.isdir(repo):
        return None
    cands = sorted(glob.glob(os.path.join(repo, "*")))
    imgs = [c for c in cands if c.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]
    if not imgs:
        return None
    # prefer 01.*
    hero = next((i for i in imgs if re.search(r"01\.", os.path.basename(i))), imgs[0])
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
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/wanderlane.css">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
{ld}
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
    cards = ""
    for it in b["items"]:
        cid = it.get("city", city_id)
        slug = it.get("slug")
        photo = it.get("photo")
        if slug and not photo:
            photo = eat_photo(cid, slug)
        img = (f'<img class="card-photo" src="{esc(photo)}" alt="{esc(it["name"])}" loading="lazy">'
               if photo else '<div class="card-photo" style="display:grid;place-items:center;'
               'background:linear-gradient(135deg,var(--paper-2),#e8ddc9)">'
               '<span style="font-family:var(--display);font-size:2rem;color:var(--clay);opacity:.5">&#127860;</span></div>')
        tag = f'<span class="card-tag">{esc(it["area"])}</span>' if it.get("area") else ""
        ours = ""
        link = ""
        if slug:
            ours = '<span class="ours">Featured &middot; has a Wanderlane page</span>'
            link = (f'<a class="link-arrow" href="{esc(biz_url(cid,slug))}" target="_blank" '
                    f'rel="noopener">Visit &amp; details <span class="arr">→</span></a>')
        cards += (f'<div class="card">{img}<div class="card-body">{tag}'
                  f'<h3>{esc(it["name"])}</h3>'
                  f'<p class="card-blurb">{it["blurb"]}</p>'
                  f'<div class="card-foot">{ours}{link}</div></div></div>')
    cls = "cards c3" + (" ranked" if ranked else "")
    return f'<div class="{cls}">{cards}</div>'

def render_stays(b):
    cards = ""
    for it in b["items"]:
        tag = f'<span class="card-tag">{esc(it["area"])}</span>' if it.get("area") else ""
        price = f'<span class="price">{esc(it["band"])} <small>/ night</small></span>' if it.get("band") else ""
        btn = aff_button(it.get("program", "booking"), it.get("target"), it.get("query"),
                         it.get("label", "Check prices"), "btn-book btn-sm", small=True)
        cards += (f'<div class="card"><div class="card-body">{tag}'
                  f'<h3>{esc(it["name"])}</h3>'
                  f'<p class="card-blurb">{it["blurb"]}</p>'
                  f'<div class="card-foot">{price}{btn}</div></div></div>')
    return f'<div class="cards c3">{cards}</div>'

def render_do(b):
    cards = ""
    for it in b["items"]:
        tag = f'<span class="card-tag">{esc(it["tag"])}</span>' if it.get("tag") else ""
        btn = aff_button(it.get("program", "gyg"), it.get("target"), it.get("query"),
                         it.get("label"), "btn-forest btn-sm", small=True) if it.get("program") else ""
        cards += (f'<div class="card"><div class="card-body">{tag}'
                  f'<h3>{esc(it["name"])}</h3>'
                  f'<p class="card-blurb">{it["blurb"]}</p>'
                  f'<div class="card-foot">{btn}</div></div></div>')
    return f'<div class="cards c3">{cards}</div>'

def render_compare(b):
    thead = "".join(f"<th>{esc(h)}</th>" for h in b["head"])
    rows = ""
    for r in b["rows"]:
        cells = "".join(f"<td>{c}</td>" for c in r)
        rows += f"<tr>{cells}</tr>"
    cap = f'<p class="muted" style="font-size:.85rem;margin:.4em 0 0">{b["cap"]}</p>' if b.get("cap") else ""
    return f'<div class="table-wrap"><table class="compare"><thead><tr>{thead}</tr></thead><tbody>{rows}</tbody></table></div>{cap}'

# ---------------------------------------------------------------- hero
def hero(page, city):
    img = page.get("hero")
    accent = (city or {}).get("accent", "var(--forest-deep)")
    if img:
        bg = f'<img class="hero-img" src="{esc(img)}" alt="" fetchpriority="high">'
        style = ""
    else:
        bg = ""
        style = (f' style="background:'
                 f'radial-gradient(120% 120% at 15% 10%,color-mix(in srgb,{accent} 78%,#000) 0%,{accent} 55%,color-mix(in srgb,{accent} 60%,#000) 100%)"')
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
    return f"""<section class="hero"{style}>{bg}<div class="hero-inner"><div class="wrap">
{kicker}<h1>{esc(page.get("h1") or page["title"])}</h1>{dek}{meta}</div></div></section>"""

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
    ld = {"@context": "https://schema.org", "@type": "Article",
          "headline": page["title"], "description": page.get("description", ""),
          "author": {"@type": "Organization", "name": BRAND},
          "publisher": {"@type": "Organization", "name": BRAND},
          "mainEntityOfPage": wl_url(path)}
    graph = {"@context": "https://schema.org", "@graph": [ld] + ([faq_ld] if faq_ld else [])}
    doc = (head(f'{page["title"]} | {BRAND}', page.get("description", page.get("dek", "")), path,
                image=page.get("hero"), jsonld=graph, article=True)
           + header(active=page["city"]) + disclosure_strip() + hero(page, city)
           + crumb
           + '<div class="article"><div class="wrap"><div class="article-grid">'
           + toc_html
           + f'<article class="prose">{body}{faq_html}{rel_html}</article>'
           + '</div></div></div>'
           + footer())
    write(path, doc)

def build_hub(city):
    path = f'{city["id"]}/'
    pages = [p for p in ALL_PAGES if p["city"] == city["id"]]
    pages.sort(key=lambda p: p.get("order", 99))
    intro = "".join(render_block(b, city["id"]) for b in city.get("intro_blocks", []))
    # go-deeper cards for the city's articles
    guide_cards = ""
    for p in pages:
        ph = p.get("hero")
        img = (f'<img src="{esc(ph)}" alt="{esc(p["title"])}" loading="lazy">'
               if ph else f'<div style="width:38%;flex:0 0 auto;background:linear-gradient(135deg,{city.get("accent","var(--forest)")},#000)"></div>')
        guide_cards += (f'<a class="guide-card" href="/{city["id"]}/{p["slug"]}/">{img}'
                        f'<div class="gc-body"><h3>{esc(p["title"])}</h3>'
                        f'<p>{esc(p.get("dek","")[:100])}</p></div></a>')
    deeper = ""
    if guide_cards:
        deeper = ('<section class="sec sec-alt"><div class="wrap">'
                  f'<div class="sec-head"><div class="kicker">Go deeper</div><h2>More {esc(city["name"])} guides</h2></div>'
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
    hub_page = {"title": f'{city["name"]} Travel Guide', "h1": city.get("hub_h1", city["name"]),
                "kicker": city.get("region_label", "City guide"),
                "dek": city.get("dek", ""), "hero": city.get("hero"), "updated": "July 2026"}
    coll = {"@context": "https://schema.org", "@type": "CollectionPage",
            "name": f'{city["name"]} Travel Guide', "description": city.get("dek", ""), "url": wl_url(path)}
    graph = {"@context": "https://schema.org", "@graph": [coll] + ([faq_ld] if faq_ld else [])}
    crumb = (f'<div class="crumb wrap"><a href="/">Home</a><span class="sep">/</span>{esc(city["name"])}</div>')
    doc = (head(f'{city["name"]} Travel Guide: Where to Eat, Stay & What to Do | {BRAND}',
                city.get("dek", ""), path, image=city.get("hero"), jsonld=graph)
           + header(active=city["id"]) + disclosure_strip() + hero(hub_page, city) + crumb
           + f'<section class="sec"><div class="wrap"><div class="prose" style="max-width:920px;margin-inline:auto">{intro}</div></div></section>'
           + deeper + faq_html + footer())
    write(path, doc)

def build_home():
    cards = ""
    for c in CITIES:
        ph = c.get("hero")
        img = (f'<img src="{esc(ph)}" alt="{esc(c["name"])}">' if ph
               else f'<div style="position:absolute;inset:0;z-index:-2;background:linear-gradient(160deg,{c.get("accent","var(--forest)")},#000)"></div>')
        n = len([p for p in ALL_PAGES if p["city"] == c["id"]])
        cnt = "Full guide" if n == 0 else (f'{n+1} guides')
        cards += (f'<a class="city-card" href="/{c["id"]}/">{img}<div class="cc-body">'
                  f'<div class="cc-count">{esc(c.get("region_label",""))} &middot; {cnt}</div>'
                  f'<h3>{esc(c["name"])}</h3><p>{esc(c.get("tagline",""))}</p></div></a>')
    hero_page = {"title": "Honest city guides, written from the road",
                 "h1": "The good streets, found for you.",
                 "kicker": BRAND,
                 "dek": "Where to eat, where to stay, and what's actually worth your time — in the cities we know by foot, not by algorithm.",
                 "hero": HOME_HERO}
    home_hero = hero(hero_page, None).replace('class="hero"', 'class="hero home-hero"')
    ld = {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND,
          "url": BASE_URL, "description": TAGLINE}
    doc = (head(f'{BRAND} — Honest City Guides for Food, Stays & Real Experiences',
                "Independent, on-the-ground travel guides to Chiang Mai, Beirut, Barcelona, Palermo, Berlin, Da Nang & Hoi An, and Damascus. Where to eat, where to stay, what to do.",
                "", image=HOME_HERO, jsonld=ld)
           + header() + home_hero
           + '<section class="sec"><div class="wrap"><div class="sec-head center"><div class="kicker">Pick a city</div>'
           + '<h2>Where are you going?</h2><p class="muted">Every guide is built from real places we\'ve walked into — not a scraped list.</p></div>'
           + f'<div class="city-grid">{cards}</div></div></section>'
           + home_manifesto()
           + footer())
    write("", doc)

def home_manifesto():
    return ('<section class="sec sec-alt"><div class="wrap"><div class="prose center" style="margin-inline:auto">'
      '<div class="kicker" style="text-align:center">Why Wanderlane</div>'
      '<h2>The internet is full of fake travel advice. This isn\'t.</h2>'
      '<p class="muted">Most "best of" travel lists are written by people who have never been there — the same fifteen places, reworded by a machine. '
      'Our guides start from restaurants, cafes and stays we actually feature and photograph on the ground, then fill in the practical stuff you really need: '
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
        doc = doc.replace('href="/', f'href="{BASE_PATH}/').replace('src="/', f'src="{BASE_PATH}/')
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
    """Copy the design system (css/js/favicon) from static/ into docs/assets/."""
    src = os.path.join(ROOT, "static")
    dst = os.path.join(SITE, "assets")
    os.makedirs(dst, exist_ok=True)
    for f in os.listdir(src):
        if f.startswith("."):
            continue
        shutil.copy2(os.path.join(src, f), os.path.join(dst, f))

def static_files():
    copy_static()
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
