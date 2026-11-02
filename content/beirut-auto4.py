# -*- coding: utf-8 -*-
# BEIRUT — on-a-budget guide, extending beirut.py's hub. No CITY block
# here (beirut.py already owns the hub). All specifics from
# research/city-beirut.md (July 2026 pass) — same honesty rules as the
# rest of the network: no invented prices, fares or numbers beyond what
# the research brief actually states, and nothing from Low-confidence items.

PAGES = [

{
 "city":"beirut", "slug":"beirut-on-a-budget", "order":7,
 "title":"Beirut on a Budget: What It Actually Costs",
 "kicker":"Beirut · Budget",
 "dek":"Real hotel price bands, why cash is the actual currency here, and the honest gaps where we won't invent a number — so you know roughly where your money goes.",
 "description":"What things actually cost in Beirut: real hotel price bands from budget to heritage-luxury, why USD cash runs this city, free things to do, and how to spend less.",
 "read":"7 min", "updated":"November 2026",
 "related":["where-to-stay-in-beirut","where-to-eat-in-beirut","getting-around-beirut"],
 "blocks":[
  {"t":"lead","html":"Beirut isn't cheap in the way some of its neighbors are, but it's a lot more affordable than a few heritage-luxury hotel names suggest — if you know which numbers are real and which ones we won't guess at. Here's what things actually cost, with the gaps left honest rather than invented."},
  {"t":"h2","text":"The real numbers"},
  {"t":"compare","head":["What","Price","Note"],
   "rows":[
     ["Budget hotel, Hamra","<em>no confirmed nightly rate</em>","Hamra Urban Gardens is well-run and well-located — check the current rate direct before you book"],
     ["Serviced suite, Hamra","$70&ndash;90","Queens Suite Hotel — a step up from a hostel without boutique pricing"],
     ["Design hotel, Badaro","~$200","The Smallville Hotel — rooftop pool and bar, steps from the National Museum"],
     ["Downtown boutique suite","~&pound;137","Saifi Suites Hotel — a short walk to the Souks and Gemmayzeh"],
     ["Heritage-luxury splurge","~&pound;220&ndash;380","InterContinental Phoenicia or Hotel Albergo — the two known-name splurges"],
   ],
   "cap":"Prices are a snapshot from our July 2026 research pass and move with season and demand — reconfirm before booking. We won't put a number on a specific meal, a taxi fare, or the budget hostel tier here; none of those were confirmed to a standard we're comfortable publishing — see below for what we do know."},
  {"t":"h2","text":"Cash is the real currency, not the dollar sign on a menu"},
  {"t":"warn","head":"This is the one budget fact that matters most here","html":"Beirut has run largely on cash and USD since the 2019&ndash;2020 banking crisis. Crisp, newer US bills are the practical currency for hotels, restaurants, taxis and tours; card acceptance is inconsistent outside upscale venues; and ATM withdrawals &mdash; especially in USD, especially on foreign cards &mdash; can be unreliable. The real budgeting move in Beirut isn't finding the cheapest menu, it's landing with enough small-denomination cash that you're never stuck negotiating a bad rate or a broken ATM mid-trip."},
  {"t":"h2","text":"Eating without a fixed price list"},
  {"t":"p","html":"We don't have confirmed per-dish or per-meal prices from this research pass, so we won't invent one here — but the honest shape of it is this: almost everything in our <a class='inline' href='/beirut/where-to-eat-in-beirut/'>food guide</a> is a cash-only, family-run counter, not a tourist-menu restaurant, and that's exactly the kind of place that tends to run cheap. <strong>Hamdi Al Zahabi Sweets</strong> is known locally for \"generous staff and fair prices\"; places like <strong>Abu Hassan</strong>, <strong>Malek al Foul</strong> and <strong>Falafel Tabbara</strong> have fed the same neighborhoods for 60-plus years on foul, hummus and falafel &mdash; not exactly luxury-margin food. The practical move is the same one locals make: eat where the queue is Lebanese, not where the menu has photos."},
  {"t":"h2","text":"Where to sleep without overpaying"},
  {"t":"stays","items":[
    {"name":"Hamra Urban Gardens","area":"Hamra","band":"Budget","program":"booking","query":"Hamra Urban Gardens Beirut",
     "blurb":"A small, no-frills budget stay in Hamra's café-and-bookshop strip. No confirmed nightly rate this pass — check direct before you book."},
    {"name":"Queens Suite Hotel","area":"Hamra","band":"$70–90","program":"booking","query":"Queens Suite Hotel Beirut",
     "blurb":"Serviced suites in the same Hamra strip, a genuine step up without boutique pricing — walking distance to half our food guide's picks."},
  ]},
  {"t":"book","head":"Compare live rates before you book","html":"Booking.com's own current prices for these and every other Beirut property move with season and demand &mdash; worth a quick check against the bands above, and against the fuller spread in our <a class='inline' href='/beirut/where-to-stay-in-beirut/'>where-to-stay guide</a>.","program":"booking","query":"Beirut","label":"See Beirut hotels on Booking"},
  {"t":"h2","text":"Getting around without wasting money"},
  {"t":"p","html":"Each neighborhood &mdash; Hamra, Mar Mikhael, Gemmayzeh, Achrafieh, Badaro, Downtown &mdash; is walkable in itself, so you can skip transport costs for most of a single day in one place. Between neighborhoods, a short Bolt or taxi hop is normal, cheap and genuinely how residents get around, not a sign you've planned badly. We don't have a confirmed current fare for either, so budget for &ldquo;a few short rides a day&rdquo; rather than a specific number &mdash; full detail in our <a class='inline' href='/beirut/getting-around-beirut/'>getting around guide</a>."},
  {"t":"tip","head":"Agree the fare, every time","html":"Official taxi counters inside the airport want you to agree the fare before you get in &mdash; and that habit is worth keeping for any unmetered ride anywhere in the city. Bolt's in-app meter sidesteps the need to haggle at all."},
  {"t":"h2","text":"Free (or nearly free) things to do"},
  {"t":"ul","items":[
    "<strong>The Corniche &amp; Pigeon Rocks.</strong> A free 4.8km seafront walk out toward Raouch&eacute; for a clifftop view of Beirut's only natural sea arches &mdash; best at golden hour.",
    "<strong>Beirut Souks &amp; Downtown.</strong> Free to walk the rebuilt streetscape around Martyrs' Square, next to the Mohammad Al-Amin Mosque.",
    "<strong>The Bourj Hammoud food walk.</strong> Wandering the Armenian quarter's market streets costs nothing &mdash; you only spend when you sit down to eat.",
    "<strong>Horsh Beirut.</strong> The city's largest green space, next to Badaro &mdash; free, though access and opening hours have historically been restricted at times, so check current status before counting on it.",
  ]},
  {"t":"warn","head":"Museums are self-ticketed, not free","html":"The National Museum and Sursock Museum are both self-ticketed at the door rather than bookable online, and we don't have a confirmed current entry price for either from this research pass &mdash; see our <a class='inline' href='/beirut/best-things-to-do-in-beirut/'>things-to-do guide</a> and budget a small cash amount for each rather than assuming they're free."},
  {"t":"h2","text":"When to go to spend less"},
  {"t":"p","html":"Winter is mild by regional standards and runs the cheapest hotel rates of the year alongside November and March. <strong>July&ndash;August</strong> is the opposite: the busiest and priciest season, as the diaspora comes home for summer and demand pushes hotel rates up across the board. <strong>April&ndash;June</strong> and <strong>September&ndash;October</strong> split the difference &mdash; warm and comfortable without summer's premium. Full seasonal detail in our <a class='inline' href='/beirut/best-time-to-visit-beirut/'>best time to visit guide</a>."},
  {"t":"h2","text":"Spend it like a Beirut local"},
  {"t":"p","html":"The cheapest version of this trip and the most authentic one are the same trip: a cash-only counter in Hamra or Bourj Hammoud instead of a Downtown tourist menu, a Bolt hop instead of a hired car and driver, and a self-guided wander down the Corniche instead of a paid tour. Landing with enough small, crisp USD bills does more for your budget here than any single discount &mdash; it's the one piece of prep that actually changes how every other price in this guide plays out."},
 ],
 "faq":[
   ("Is Beirut an expensive city to visit?",
    "Not inherently — most of its best food is cash-only counter food that's run cheap for decades, and hotel options span from a simple Hamra budget stay to heritage-luxury addresses at £220–380. The real cost driver is timing: July–August pushes hotel prices up across the board, while winter, November and March are the cheapest."),
   ("What's the cheapest way to eat well in Beirut?",
    "Eat where locals eat: cash-only, family-run counters like Abu Hassan, Malek al Foul or Falafel Tabbara rather than tourist-menu restaurants in Downtown. We don't have confirmed per-dish prices to quote, but these are decades-old neighborhood institutions, not high-margin restaurants — see our food guide for the full list."),
   ("How much does a hotel cost in Beirut?",
    "A serviced suite in Hamra runs $70–90, a design hotel like The Smallville around $200, and heritage-luxury addresses like Hotel Albergo or the InterContinental Phoenicia run £220–380. We don't have a confirmed current rate for the cheapest budget tier (Hamra Urban Gardens) — check live listings directly before you book."),
 ],
},

]
