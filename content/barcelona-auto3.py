# -*- coding: utf-8 -*-
# BARCELONA — on-a-budget guide, extending barcelona.py's hub. No CITY
# block here (barcelona.py already owns the hub). All specifics from
# research/city-barcelona.md (July 2026 pass) — same honesty rules as the
# rest of the network: no invented prices, and the one low-confidence price
# in the brief (the exact current T-casual metro card cost) is left out
# rather than guessed.

PAGES = [

{
 "city":"barcelona", "slug":"barcelona-on-a-budget", "order":7,
 "title":"Barcelona on a Budget: What It Actually Costs",
 "kicker":"Barcelona · Budget",
 "dek":"Real prices for lunch, a bed and the airport bus — plus the honest gaps where we won't invent a number — so you know roughly where your money goes.",
 "description":"What things actually cost in Barcelona: menú del día lunch prices, real hotel bands from hostel to luxury, the airport bus fare, and how to spend less without feeling cheap.",
 "read":"7 min", "updated":"October 2026",
 "related":["where-to-stay-in-barcelona","where-to-eat-in-barcelona","getting-around-barcelona"],
 "blocks":[
  {"t":"lead","html":"Barcelona isn't a cheap city, but it's a lot more affordable than its postcard reputation suggests — if you know which prices are real and which neighborhoods are worth the short metro ride. Here's what things actually cost, with the gaps left honest rather than guessed."},
  {"t":"h2","text":"The real numbers"},
  {"t":"compare","head":["What","Price","Note"],
   "rows":[
     ["Lunch menú del día","&euro;12.90&ndash;18","Two-plus courses and a drink, weekday lunch — our food guide's own picks"],
     ["Airport bus (Aerobus), one-way","~&euro;6&ndash;7","~35&ndash;40 min, straight to Pla&ccedil;a Catalunya"],
     ["Budget hostel bed","<em>not verified this pass</em>","Hostal Santa Ana &amp; Somnio Hostels are solid, well-rated picks &mdash; check current rates direct"],
     ["Mid-range hotel, double","from ~$157/night","Design hotel or a 10-min walk to the beach, below"],
     ["Boutique hotel, double","from ~$305/night","Pool and spa in the old-town center"],
     ["Luxury splurge, double","from ~$938/night","If the budget is genuinely open"],
   ],
   "cap":"Prices are a snapshot from our July 2026 research pass and move with season and demand — check live rates before booking. We won't put a number on a budget hostel bed or the metro card price here; neither was confirmed to a standard we're comfortable publishing."},
  {"t":"h2","text":"Eat well for less: menú del día and vermut hour"},
  {"t":"p","html":"The single best budget move in this city is eating lunch, not dinner. Most sit-down restaurants outside the Rambla run a weekday <strong>menú del día</strong> — a fixed, multi-course lunch that costs a fraction of ordering the same food à la carte at night."},
  {"t":"eats","items":[
    {"name":"Chez Lola","slug":"chez-lola","area":"Sant Andreu","blurb":"A &euro;12.90 weekday menú del día at a proper French bistro &mdash; the mustard chicken and homemade banana-chocolate cake are the two dishes people come back for."},
    {"name":"Restaurant l'Andreuenc","slug":"restaurant-landreuenc","area":"Sant Andreu","blurb":"Traditional Catalan cooking from two brothers, menú del día around &euro;18. Reserve ahead &mdash; word's out."},
  ]},
  {"t":"p","html":"For the other great budget ritual, find a <strong>vermut hour</strong> — house vermouth on tap with olives and anchovies, classically a Saturday or Sunday midday thing. Vermuteria Oxiterraneo (Sant Andreu), Vermuteria Puigmart&iacute; and the rest of our <a class='inline' href='/barcelona/where-to-eat-in-barcelona/'>food guide</a>'s Gr&agrave;cia picks are built entirely around it."},
  {"t":"tip","head":"August closures","html":"Many of the small, family-run bodegas and restaurants that make this city's food scene worth the trip — several of them in our own food guide — close for a few weeks of summer holiday in August. Check hours before a summer visit."},
  {"t":"h2","text":"Where to sleep without overpaying"},
  {"t":"stays","items":[
    {"name":"Hostal Santa Ana","area":"Barri G&ograve;tic","blurb":"Central, historic-core location with good value and free wifi (7.6/10). The cheapest tier we can point to with confidence on name alone — check the current nightly rate direct.","program":"booking","query":"Hostal Santa Ana Barcelona"},
    {"name":"Somnio Hostels","area":"Eixample","blurb":"Renovated 2023, a short walk to Las Ramblas (7.7/10). Same honest note on price as above.","program":"booking","query":"Somnio Hostels Barcelona"},
    {"name":"Praktik &Egrave;ssens","area":"Eixample (Passeig de Gr&agrave;cia)","band":"from ~$157","blurb":"Design-hotel feel right by the Gaud&iacute; landmarks, without the Gaud&iacute;-adjacent markup.","program":"booking","query":"Praktik Essens Barcelona"},
    {"name":"Acta Voraport","area":"Sant Mart&iacute; / Poblenou","band":"from ~$157","blurb":"A 10-minute walk to Bogatell Beach, with a terrace and parking &mdash; good if you want beach over G&ograve;tic-core.","program":"booking","query":"Acta Voraport Barcelona"},
    {"name":"Yurbban Passage Hotel & Spa","area":"Ciutat Vella","band":"from ~$305","blurb":"Outdoor pool and spa, still in the old-town center, if you want to stretch the budget a little.","program":"booking","query":"Yurbban Passage Hotel Barcelona"},
  ]},
  {"t":"book","head":"Compare live rates before you book","html":"Booking.com's own current prices for these and every other property move with season and demand &mdash; worth a quick check against the bands above.","program":"booking","query":"Barcelona","label":"See Barcelona hotels on Booking"},
  {"t":"h2","text":"Getting around without wasting money"},
  {"t":"p","html":"The tourist core &mdash; Barri G&ograve;tic, El Born, El Raval and Eixample's Dreta side &mdash; is flat and genuinely walkable, so you can skip transit costs for most of a day's sightseeing. For the airport, the Aerobus (~&euro;6&ndash;7 one-way) beats a taxi on price; the R2 Nord rail line is a few euros cheaper still but runs less often. Full detail in our <a class='inline' href='/barcelona/getting-around-barcelona/'>getting around guide</a>."},
  {"t":"tip","head":"Ride a few stops for better, cheaper food","html":"A lot of this city's best eating sits outside the tourist core &mdash; Sant Andreu, Horta-Guinard&oacute;, Sants and Gr&agrave;cia, all in our food guide &mdash; and a short metro ride there buys real neighborhood prices instead of Rambla-adjacent markups."},
  {"t":"h2","text":"Free (or nearly free) things to do"},
  {"t":"ul","items":[
    "<strong>Walk the Gothic Quarter yourself.</strong> The medieval core is free to wander &mdash; the cathedral exterior, Pla&ccedil;a Reial, the tangled lanes &mdash; and best early morning or after dinner once the day-tour crowds thin out.",
    "<strong>La Boqueria market</strong>, early morning, is free to browse and a far better experience before it turns into a photo-op.",
    "<strong>Barceloneta beach</strong> costs nothing beyond whatever you spend at a chiringuito.",
  ]},
  {"t":"warn","head":"Book the paid sights ahead","html":"Sagrada Fam&iacute;lia and Park G&uuml;ell's monumental zone both run timed entry that sells out days ahead in season. We don't have a verified current ticket price for this guide &mdash; see our <a class='inline' href='/barcelona/best-things-to-do-in-barcelona/'>things-to-do guide</a> and book direct before you travel rather than assume you can walk up."},
  {"t":"h2","text":"When to go to spend less"},
  {"t":"p","html":"Winters are mild here, with the lowest crowds <em>and</em> the lowest prices of the year. May&ndash;June and September&ndash;October are the shoulder-season sweet spot &mdash; warm without August's peak heat, crowds or prices. Full seasonal detail in our <a class='inline' href='/barcelona/best-time-to-visit-barcelona/'>best time to visit guide</a>."},
  {"t":"h2","text":"Spend it like a local"},
  {"t":"p","html":"Barcelona is one of Europe's most visible overtourism flashpoints, and short-term rentals are currently the most politically charged accommodation choice in the city — the mayor has announced a plan to phase out short-term tourist-apartment licenses. A hotel (see above) is the lower-friction, more locally accepted option right now, and it happens to point you toward exactly the kind of neighborhood spending that keeps this guide's own picks in business: a meal in Sant Andreu or Gr&agrave;cia costs less and lands better than the same meal a block off the Rambla."},
 ],
 "faq":[
   ("Is Barcelona an expensive city to visit?",
    "Not especially, if you eat lunch at a menú del día instead of dinner à la carte, walk the flat tourist core instead of taxiing everywhere, and pick a hotel over a short-term rental. It's pricier than it looks the moment you add paid attraction tickets and a boutique hotel, though — those are where costs climb fastest."),
   ("What's the cheapest way to eat well in Barcelona?",
    "A weekday menú del día — a fixed lunch menu — at a neighborhood restaurant rather than a tourist-zone dinner. Chez Lola (€12.90) and Restaurant l'Andreuenc (around €18) in Sant Andreu are two confirmed examples; vermut hour on a Saturday or Sunday is the other great low-cost local ritual."),
   ("How much does a hotel cost in Barcelona?",
    "Verified mid-range doubles start around $157–188 a night, boutique hotels around $305, and genuine luxury around $938 — all snapshot prices that move with season. We don't have a confirmed current price for the cheapest hostel beds, so check live listings directly before you book."),
 ],
},

]
