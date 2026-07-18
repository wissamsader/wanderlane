# -*- coding: utf-8 -*-
"""Assemble a self-contained visual tour of Wanderlane (screenshots as data URIs)."""
import base64, io, os
from PIL import Image

SS = "/private/tmp/claude-501/-Users-w/01fbaf4a-baae-46df-90b7-3992be7a2b23/scratchpad"
PINS = os.path.expanduser("~/CLAUDE-DEEPSEEK/wanderlane/pins")
OUT = os.path.join(SS, "wanderlane-tour.html")

def datauri(path, width, top_crop_ratio=None, q=80):
    im = Image.open(path).convert("RGB")
    if top_crop_ratio:
        w, h = im.size
        im = im.crop((0, 0, w, min(h, int(w * top_crop_ratio))))
    w, h = im.size
    nh = int(h * width / w)
    im = im.resize((width, nh), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

shots = {
 "home": datauri(f"{SS}/live-home.png", 860, 1.02),
 "berlin": datauri(f"{SS}/wl-berlin.png", 860, 1.05),
 "beirut": datauri(f"{SS}/wl-beirut.png", 860, 1.05),
 "barca": datauri(f"{SS}/live-barca-itin.png", 860, 1.05),
 "damascus": datauri(f"{SS}/wl-damascus.png", 860, 1.05),
 "phone": datauri(f"{SS}/wl-m2.png", 300),
 "pin1": datauri(f"{PINS}/pin-beirut-eat.png", 360),
 "pin2": datauri(f"{PINS}/pin-berlin-eat.png", 360),
 "pin3": datauri(f"{PINS}/pin-damascus.png", 360),
 "pin4": datauri(f"{PINS}/pin-barcelona-itin.png", 360),
}

def frame(img, url):
    return (f'<figure class="frame"><div class="bar"><span class="dot"></span><span class="dot"></span>'
            f'<span class="dot"></span><span class="url">{url}</span></div>'
            f'<div class="shot"><img src="{img}" alt="" loading="lazy"></div></figure>')

SECTIONS = [
 ("The front door", "One brand, seven cities",
  "The homepage points readers to wherever they're headed — Chiang Mai, Beirut, Barcelona, Palermo, Berlin, Da Nang &amp; Hoi An, Damascus. Every guide is built from real places, many of them businesses we already made websites for, using photos we own.",
  frame(shots["home"], "wanderlane · home")),
 ("A guide, up close", "Berlin's &lsquo;Arab Street&rsquo; &mdash; which no other guide covers",
  "Every featured spot sits on Sonnenallee in Neuk&ouml;lln, shown with our own photos, and links back to its Wanderlane page &mdash; free promotion, and a sweetener when a friend sells that business a website. Below the food: where to stay, monetized.",
  frame(shots["berlin"], "wanderlane/berlin")),
 ("The moat", "Real photos, not stock",
  "Fifteen Beirut tables, ranked, each with a photo taken on the ground &mdash; LMATBAKH&rsquo;s candlelit terrace, a wood-fired oven mid-flame, a 60-year falafel counter. This is the one thing an AI travel site can&rsquo;t fake, and it&rsquo;s ours already.",
  frame(shots["beirut"], "wanderlane/beirut/where-to-eat-in-beirut")),
 ("Where the money is", "Boarding-pass hotel cards",
  "Every &lsquo;where to stay&rsquo; guide now sells with designed boarding-pass cards &mdash; airport-code tab, perforation, barcode, price, and a booking button that earns a commission on every stay. No borrowed hotel photos needed; the design carries it.",
  frame(shots["barca"], "wanderlane/chiangmai/where-to-stay-in-chiang-mai")),
 ("Handled with care", "A love letter, done responsibly",
  "Damascus is a food-and-heritage guide, not a booking pitch: real photos of Bakdash and the old-city caf&eacute;s, an honest travel-advisory note, and no hotel CTAs. Some cities earn trust instead of commission &mdash; that&rsquo;s the right call.",
  frame(shots["damascus"], "wanderlane/damascus")),
]

pins_html = "".join(f'<img class="pin" src="{shots[k]}" alt="Pinterest pin" loading="lazy">'
                    for k in ("pin1", "pin2", "pin3", "pin4"))

STEPS = [
 ("A reader clicks", "Someone reads a guide and taps a hotel, tour, eSIM or insurance link."),
 ("The platform pays us", "Booking, GetYourGuide, 12Go and the rest pay a commission &mdash; the reader pays the exact same price."),
 ("It compounds", "The catalogue keeps earning while you sleep. One marker in the config switches all of it on at once."),
]
steps_html = "".join(
 f'<li><span class="n">{i+1}</span><div><h4>{t}</h4><p>{d}</p></div></li>'
 for i, (t, d) in enumerate(STEPS))

sections_html = "".join(
 f'<section class="tour"><div class="cap"><p class="eyebrow">{e}</p><h2>{t}</h2><p>{c}</p></div>{f}</section>'
 for e, t, c, f in SECTIONS)

COMPASS = ('<svg viewBox="0 0 32 32" width="34" height="34" fill="none" aria-hidden="true">'
 '<circle cx="16" cy="16" r="14" stroke="currentColor" stroke-width="1.5" opacity=".55"/>'
 '<circle cx="16" cy="2.7" r="1.1" fill="currentColor"/>'
 '<path d="M16 6 L19 16 L16 26 L13 16 Z" fill="currentColor"/>'
 '<circle cx="16" cy="16" r="1.9" fill="var(--paper)" stroke="currentColor" stroke-width="1.3"/></svg>')

HTML = """<div class="wrap">
<header class="hero">
  <div class="mark">__COMPASS__<span>Wanderlane</span></div>
  <p class="eyebrow">Build report &middot; redesigned 18 July 2026</p>
  <h1>Wanderlane, rebuilt<br>to our real standard.</h1>
  <p class="lede">A travel-guide network across all seven cities we&rsquo;ve worked in &mdash; now with the
  &ldquo;field journal&rdquo; design: film-grain heroes, passport stamps, postcard city cards, boarding-pass
  hotel cards, and a photo pass that swapped every weak image for a real, appetizing one.</p>
  <div class="stats">
    <div><b>7</b><span>cities</span></div>
    <div><b>26</b><span>guides</span></div>
    <div><b>37</b><span>pages</span></div>
    <div><b class="live">Live</b><span>&amp; verified</span></div>
  </div>
  <a class="btn" href="https://wissamsader.github.io/wanderlane/" target="_blank" rel="noopener">Open the live site &rarr;</a>
</header>

__SECTIONS__

<section class="pins">
  <div class="cap center"><p class="eyebrow">The traffic engine</p><h2>21 Pinterest pins, ready to post</h2>
  <p>Travel is Pinterest&rsquo;s biggest category and new accounts get reach in weeks. These are made from our own
  photos &mdash; upload them and they pull readers straight into the guides.</p></div>
  <div class="pinrow">__PINS__</div>
</section>

<section class="earn">
  <div class="cap center"><p class="eyebrow">How it makes money</p><h2>No clients, no pitching &mdash; just links</h2></div>
  <ol class="steps">__STEPS__</ol>
</section>

<footer class="foot">
  <div class="mark">__COMPASS__<span>Wanderlane</span></div>
  <h2>It&rsquo;s live right now.</h2>
  <p>Everything above is built, deployed and working. The one thing that has to be you: sign up at Travelpayouts and
  paste a single marker into the config &mdash; that switches earning on across all seven cities. About 15 minutes.</p>
  <a class="btn" href="https://wissamsader.github.io/wanderlane/" target="_blank" rel="noopener">wissamsader.github.io/wanderlane &rarr;</a>
</footer>
</div>
"""

HTML = (HTML.replace("__COMPASS__", COMPASS).replace("__SECTIONS__", sections_html)
            .replace("__PINS__", pins_html).replace("__STEPS__", steps_html))

STYLE = """<style>
:root{--paper:#FAF6EF;--paper2:#F1E9DB;--card:#fff;--ink:#211D18;--ink-soft:#5C5348;--faint:#8A8073;
--clay:#C0552F;--clay-deep:#9E3F1F;--forest:#1F4D3F;--line:rgba(33,29,24,.13);--shadow:0 22px 50px -24px rgba(33,29,24,.42);
--display:Georgia,"Times New Roman",serif;--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,sans-serif;}
@media (prefers-color-scheme:dark){:root{--paper:#16130E;--paper2:#201B14;--card:#221C15;--ink:#F3ECE0;--ink-soft:#C6BBA9;
--faint:#93897A;--clay:#E5825A;--clay-deep:#E5825A;--forest:#7FC9AA;--line:rgba(255,255,255,.12);--shadow:0 26px 60px -26px rgba(0,0,0,.72);}}
:root[data-theme="light"]{--paper:#FAF6EF;--paper2:#F1E9DB;--card:#fff;--ink:#211D18;--ink-soft:#5C5348;--faint:#8A8073;
--clay:#C0552F;--clay-deep:#9E3F1F;--forest:#1F4D3F;--line:rgba(33,29,24,.13);--shadow:0 22px 50px -24px rgba(33,29,24,.42);}
:root[data-theme="dark"]{--paper:#16130E;--paper2:#201B14;--card:#221C15;--ink:#F3ECE0;--ink-soft:#C6BBA9;--faint:#93897A;
--clay:#E5825A;--clay-deep:#E5825A;--forest:#7FC9AA;--line:rgba(255,255,255,.12);--shadow:0 26px 60px -26px rgba(0,0,0,.72);}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:1000px;margin:0 auto;padding:0 22px}
.eyebrow{font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--clay);font-weight:700;margin:0 0 .6em}
h1{font-family:var(--display);font-weight:600;font-size:clamp(2.4rem,6vw,4rem);line-height:1.05;letter-spacing:-.01em;text-wrap:balance;margin:.1em 0 .35em}
h2{font-family:var(--display);font-weight:600;font-size:clamp(1.5rem,3.4vw,2.1rem);line-height:1.14;text-wrap:balance;margin:0 0 .4em}
h4{font-family:var(--display);font-weight:600;font-size:1.12rem;margin:0 0 .25em;color:var(--ink)}
p{margin:0 0 1em;color:var(--ink-soft)}
.mark{display:flex;align-items:center;gap:10px;color:var(--clay);font-family:var(--display);font-weight:600;font-size:1.25rem}
.mark span{color:var(--ink)}
.hero{padding:clamp(46px,9vw,104px) 0 36px;text-align:center;max-width:760px;margin:0 auto}
.hero .eyebrow{color:var(--faint)}
.hero .mark{justify-content:center;margin-bottom:26px}
.lede{font-size:1.18rem;color:var(--ink-soft);max-width:58ch;margin:.4em auto 0}
.stats{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin:34px 0 30px}
.stats div{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:15px 24px;min-width:94px}
.stats b{display:block;font-family:var(--display);font-size:2rem;color:var(--clay);font-variant-numeric:tabular-nums;line-height:1}
.stats b.live{font-size:1.5rem;color:var(--forest)}
.stats span{font-size:.78rem;color:var(--faint);letter-spacing:.03em}
.btn{display:inline-block;background:var(--clay);color:#fff;font-weight:600;font-size:1rem;padding:.85em 1.5em;border-radius:100px;text-decoration:none;transition:transform .18s,background .2s}
.btn:hover{background:var(--clay-deep);transform:translateY(-2px)}
.btn:focus-visible{outline:3px solid var(--forest);outline-offset:3px}
.tour{padding:clamp(34px,6vw,60px) 0;border-top:1px solid var(--line)}
.tour .cap{max-width:64ch;margin:0 0 24px}
.frame{margin:0;background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:var(--shadow)}
.bar{display:flex;align-items:center;gap:7px;padding:11px 15px;background:var(--paper2);border-bottom:1px solid var(--line)}
.dot{width:11px;height:11px;border-radius:50%;background:var(--faint);opacity:.5}
.url{margin-left:12px;font-size:.78rem;color:var(--faint);font-family:ui-monospace,Menlo,monospace;letter-spacing:.02em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.shot{max-height:600px;overflow:hidden}
.shot img{width:100%;display:block}
.pins{padding:clamp(40px,7vw,68px) 0;border-top:1px solid var(--line)}
.center{text-align:center;margin-inline:auto}
.pinrow{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:28px}
.pin{width:210px;border-radius:12px;box-shadow:var(--shadow)}
.earn{padding:clamp(40px,7vw,68px) 0;border-top:1px solid var(--line)}
.steps{list-style:none;padding:0;margin:26px 0 0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.steps li{display:flex;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px}
.steps .n{flex:0 0 auto;width:34px;height:34px;border-radius:50%;background:var(--clay);color:#fff;font-family:var(--display);font-weight:600;display:grid;place-items:center}
.steps p{margin:0;font-size:.95rem}
.foot{text-align:center;padding:clamp(50px,9vw,96px) 0 84px;border-top:1px solid var(--line);margin-top:18px}
.foot .mark{justify-content:center;margin-bottom:18px}
.foot p{max-width:56ch;margin-inline:auto}
.foot .btn{margin-top:22px}
@media(max-width:720px){.steps{grid-template-columns:1fr}.pin{width:45%}.shot{max-height:460px}}
.reveal{opacity:0;transform:translateY(16px);transition:opacity .6s ease,transform .6s ease}
.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}.btn{transition:none}}
</style>"""

SCRIPT = """<script>
(function(){var els=document.querySelectorAll('.tour,.pins,.earn,.foot');
if(!('IntersectionObserver' in window))return;
els.forEach(function(e){e.classList.add('reveal')});
var o=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');o.unobserve(x.target)}})},{rootMargin:'0px 0px -8% 0px'});
els.forEach(function(e){o.observe(e)});})();
</script>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(STYLE + HTML + SCRIPT)
print("wrote", OUT, round(os.path.getsize(OUT) / 1024), "KB")
