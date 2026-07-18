# -*- coding: utf-8 -*-
"""WANDERLANE config — brand, cities, and the affiliate money-plumbing.

ACTIVATION (see ops/ACCOUNTS.md for the 15-minute walkthrough):
  1. Sign up at travelpayouts.com  ->  paste your marker into TP_MARKER below.
     That single marker monetizes Booking, Agoda, Hostelworld, Klook,
     GetYourGuide, 12Go, Airalo & Tripadvisor across the WHOLE network.
  2. Sign up at safetywing.com/ambassador -> paste referenceID into AFF["safetywing"].
  3. (optional) Amazon Associates -> AMAZON_TAG.
Links already point to the correct real pages; adding the ids just switches
tracking on. Re-run build.py and the entire network is monetized."""

BRAND   = "Wanderlane"
TAGLINE = "The good streets, found."
BASE_URL = "https://wissamsader.github.io/wanderlane"   # -> https://wanderlane.co once the domain is live
BASE_PATH = "/wanderlane"   # GitHub Pages project subpath. Set to "" when a custom domain serves at root.

CONTACT = "hello@wanderlane.co"        # create this inbox (or point to your own)

# Optional, paste-and-rebuild (see ops/ROADMAP.md):
# Travelpayouts Drive (their auto-monetization layer; snippet from the TP dashboard, installed 2026-07-18).
# Injected into every page head. A privacy-friendly analytics snippet can be appended here too.
ANALYTICS = """<script nowprocket data-noptimize="1" data-cfasync="false" data-wpfc-render="false" seraph-accel-crit="1" data-no-defer="1">
(function () {
  var script = document.createElement("script");
  script.async = 1;
  script.src = 'https://emrld.ltd/NTUyMDcx.js?t=552071';
  document.head.appendChild(script);
})();
</script>"""
GSC_VERIFY = ""      # Google Search Console verification token -> <meta google-site-verification> for indexing
SOCIAL = {
    "pinterest": "https://www.pinterest.com/wanderlaneguides/",   # create (see ops/PINTEREST.md)
    "instagram": "https://www.instagram.com/wanderlane.guides/",
}

# ---------------------------------------------------------------- AFFILIATES
# One Travelpayouts marker drives 8 of the brands via the verified deep-link
# format:  https://<sub>.travelpayouts.com/click?shmarker=<MARKER>&promo_id=<ID>
#          &source_type=customlink&type=click&custom_url=<ENCODED DEST>
TP_MARKER = "552071"              # Wissam's Travelpayouts marker (activated 2026-07-18)
USE_TP    = True                  # route through Travelpayouts when a promo_id is known
AMAZON_TAG = ""                   # optional: your-amazon-tag-20

# per-brand: dest = real destination ({q}=search term); tp = Travelpayouts routing
# (sub-domain + promo_id, both confirmed for booking/12go, fill the rest from the
# TP dashboard link builder — 10 sec each); direct_* = optional direct-signup fallback.
AFF = {
    "booking": {
        "dest": "https://www.booking.com/searchresults.html?ss={q}",
        "tp": {"sub": "c84", "promo_id": "3650"},
        "direct_param": "aid", "direct_id": "",
        "label": "Check prices on Booking", "qspace": "+",
    },
    "agoda": {
        "dest": "https://www.agoda.com/search?city={q}",
        "tp": {"sub": "c104", "promo_id": "2854"},    # verified public promo_id
        "direct_param": "cid", "direct_id": "",
        "label": "Check prices on Agoda", "qspace": "%20",
    },
    "hostelworld": {
        "dest": "https://www.hostelworld.com/s?q={q}",
        "tp": {"sub": "c93", "promo_id": "3518"},     # verified public promo_id
        "direct_param": "clickref", "direct_id": "",
        "label": "Find hostels", "qspace": "+",
    },
    "gyg": {   # GetYourGuide
        "dest": "https://www.getyourguide.com/s/?q={q}",
        "tp": {"sub": "c108", "promo_id": "3965"},    # verified public promo_id
        "direct_param": "partner_id", "direct_id": "",
        "label": "See tours on GetYourGuide", "qspace": "+",
    },
    "klook": {
        "dest": "https://www.klook.com/en-US/search/?query={q}",
        "tp": {"sub": None, "promo_id": None},
        "direct_param": "aid", "direct_id": "",
        "label": "Book on Klook", "qspace": "%20",
    },
    "12go": {  # SE-Asia trains/buses/ferries — promo_id confirmed
        "dest": "https://12go.asia/en/travel/{q}",
        "tp": {"sub": "c44", "promo_id": "1764"},
        "direct_param": None, "direct_id": "",
        "label": "Check times & prices on 12Go", "qspace": "-",
    },
    "airalo": {  # eSIM
        "dest": "https://www.airalo.com/{q}-esim",
        "tp": {"sub": None, "promo_id": None},
        "direct_param": None, "direct_id": "",
        "label": "Get an eSIM (Airalo)", "qspace": "-",
    },
    "tripadvisor": {
        "dest": "https://www.tripadvisor.com/Search?q={q}",
        "tp": {"sub": None, "promo_id": None},
        "direct_param": None, "direct_id": "",
        "label": "See reviews on Tripadvisor", "qspace": "%20",
    },
    "safetywing": {  # NOT on Travelpayouts — direct only; recurring 10% commission
        "dest": "https://safetywing.com/nomad-insurance/",
        "tp": None,
        "direct_param": "referenceID", "direct_id": "",
        "label": "Get nomad insurance (SafetyWing)", "qspace": "%20",
    },
}

# Dot-marquee vocabulary per city (renders as the italic ticker strip on hubs)
CITY_WORDS = {
    "chiangmai": ["Khao soi", "The Old City moat", "Doi Suthep at dawn", "Night markets", "Nimman cafés", "Sticky Waterfalls", "Sai ua"],
    "beirut":    ["Manoushe at 6am", "Hamra", "The Corniche", "Mezze for the table", "Mar Mikhael", "Knefeh", "Fairuz on the radio"],
    "barcelona": ["Vermut hour", "El Born", "Gaudí", "Pa amb tomàquet", "Gràcia squares", "La Boqueria", "Absenta"],
    "palermo":   ["Arancine", "Ballarò", "The Kalsa", "Cannoli", "Mondello", "Vucciria at night", "Pane e panelle"],
    "berlin":    ["Sonnenallee", "Kunafa", "Museum Island", "Neukölln", "Döner", "The Wall", "Späti culture"],
    "vietnam":   ["Bánh xèo", "My Khe beach", "Lantern night", "Hoi An old town", "Mì Quảng", "An Bàng", "Basket boats"],
    "damascus":  ["Booza at Bakdash", "The old souq", "Courtyard houses", "Knafeh", "Straight Street", "Jasmine", "Arabic coffee"],
}

# ---------------------------------------------------------------- CITIES
# id MUST match the business repo slug (wissamsader.github.io/<id>/) so featured
# restaurants link to their real pages and reuse their real photos.
CITIES = [
    {
        "id": "chiangmai", "name": "Chiang Mai", "short": "Chiang Mai",
        "region_label": "Northern Thailand", "region": "asia", "accent": "#A85D2A",
        "tagline": "Temples, night markets, and the best khao soi of your life.",
        "dek": "Northern Thailand's slow, green, temple-strewn capital — and a genuine food city. "
               "Where to stay by neighborhood, what to eat, and how to actually get here.",
        "hub_h1": "Chiang Mai, on foot",
    },
    {
        "id": "beirut", "name": "Beirut", "short": "Beirut",
        "region_label": "Lebanon", "region": "mideast", "accent": "#1E6A73",
        "tagline": "Mezze, sea, and a city that refuses to sit still.",
        "dek": "Loud, warm, and one of the great eating cities of the Mediterranean. "
               "The neighborhoods, the tables worth crossing town for, and how to visit thoughtfully.",
        "hub_h1": "Beirut, at the table",
    },
    {
        "id": "barcelona", "name": "Barcelona", "short": "Barcelona",
        "region_label": "Catalonia, Spain", "region": "europe", "accent": "#A5302A",
        "tagline": "Tapas, Gaudí, and long Mediterranean evenings.",
        "dek": "Beyond the Sagrada Família queues — where locals actually eat and drink, "
               "which neighborhood to sleep in, and the tickets worth booking ahead.",
        "hub_h1": "Barcelona, the good streets",
    },
    {
        "id": "palermo", "name": "Palermo", "short": "Palermo",
        "region_label": "Sicily, Italy", "region": "europe", "accent": "#245C7A",
        "tagline": "Sicily's loud, delicious, baroque heart.",
        "dek": "A street-food capital wrapped in Arab-Norman history. The markets, the fried things "
               "worth queuing for, and where to base yourself.",
        "hub_h1": "Palermo, market to table",
    },
    {
        "id": "berlin", "name": "Berlin", "short": "Berlin",
        "region_label": "Germany", "region": "europe", "accent": "#3B4A54",
        "tagline": "History, techno, and the best Arab food outside the Levant.",
        "dek": "The big sights, done efficiently — plus the thing most Berlin guides miss entirely: "
               "Sonnenallee, the Levantine food street in the heart of Neukölln.",
        "hub_h1": "Berlin, beyond the wall",
    },
    {
        "id": "vietnam", "name": "Da Nang & Hoi An", "short": "Vietnam",
        "region_label": "Central Vietnam", "region": "asia", "accent": "#15795A",
        "tagline": "Lanterns in Hoi An, beaches and banh xeo in Da Nang.",
        "dek": "Central Vietnam's golden pair — a UNESCO lantern town and a beach-and-food city 45 minutes apart. "
               "Where to stay, what to eat, and how to move between them.",
        "hub_h1": "Da Nang & Hoi An",
    },
    {
        "id": "damascus", "name": "Damascus", "short": "Damascus",
        "region_label": "Syria", "region": "mideast", "accent": "#6E5A34",
        "tagline": "One of the oldest cities on earth — and its table.",
        "dek": "A respectful food-and-heritage guide to the old city's kitchens, sweets and coffeehouses. "
               "Here for the culture, and the day the doors open wider.",
        "hub_h1": "Damascus, the oldest table",
    },
]
