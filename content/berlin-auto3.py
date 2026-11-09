# -*- coding: utf-8 -*-
# BERLIN — on-a-budget guide, extending berlin.py's hub. No CITY block
# here (berlin.py already owns the hub). All specifics from
# research/city-berlin.md (July 2026 pass) — same honesty rules as the
# rest of the network: no invented prices, fares or numbers beyond what
# the research brief actually states, and nothing from Low-confidence items.

PAGES = [

{
 "city":"berlin", "slug":"berlin-on-a-budget", "order":7,
 "title":"Berlin on a Budget: What It Actually Costs",
 "kicker":"Berlin · Budget",
 "dek":"Real neighborhood hotel price bands, why Sonnenallee is the best-value eating in the city, what's genuinely free, and the numbers we won't invent.",
 "description":"What things actually cost in Berlin: hotel price bands by neighborhood, the Sonnenallee food crawl's real value, free sights, and the gaps we won't guess at.",
 "read":"7 min", "updated":"November 2026",
 "related":["where-to-stay-in-berlin","where-to-eat-in-berlin","getting-around-berlin"],
 "blocks":[
  {"t":"lead","html":"Berlin isn't a cheap European capital, but it's a lot more forgiving than Mitte's hotel prices make it look — if you know which neighborhood to sleep in and which street to eat on. Here's what things actually cost, with the gaps left honest instead of invented."},
  {"t":"h2","text":"The real numbers: hotels by neighborhood"},
  {"t":"compare","head":["Area","Nightly band","Note"],
   "rows":[
     ["<strong class='best'>Friedrichshain</strong>","Hostel dorms from ~&euro;24","Berlin's cheapest hostel beds, right by the East Side Gallery and the club scene."],
     ["Kreuzberg","~&euro;70&ndash;150","Counterculture heart, multicultural food, late-night bars."],
     ["Prenzlauer Berg","~&euro;90&ndash;170","Leafy, family-friendly, a slower pace."],
     ["Mitte","~&euro;80&ndash;450","Walk to Brandenburg Gate and Museum Island — the widest range, and the priciest floor."],
     ["Charlottenburg","~&euro;150&ndash;400+","West Berlin elegance, furthest from the Mitte sights."],
     ["Neukölln","<em>no confirmed band</em>","Our featured Sonnenallee food ground, and the best-value district for eating — we just don't have a hotel price range for it from this research pass."],
   ],
   "cap":"Bands are aggregated from multiple current travel-guide sources, not a live quote — treat them as a planning range, not a booking price. We also don't have a confirmed current price for a single BVG transit ticket, the Berlin WelcomeCard, or any specific döner/currywurst price, so none of those get a number here."},
  {"t":"h2","text":"Where to sleep cheap, and still in Mitte"},
  {"t":"p","html":"The two genuinely budget-tier options in our <a class='inline' href='/berlin/where-to-stay-in-berlin/'>stays guide</a> both sit in Mitte itself, so you're not trading price for location the way you might expect."},
  {"t":"stays","items":[
    {"name":"Heart of Gold Hostel & Capsules Berlin","area":"Mitte","band":"Budget/hostel","program":"booking","query":"Heart of Gold Hostel Berlin",
     "blurb":"Capsule-hotel-style bunks dead in the center of Mitte — the cheapest tier that still feels designed, not just cheap."},
    {"name":"ibis Berlin Hauptbahnhof","area":"Mitte","band":"Budget","program":"booking","query":"ibis Berlin Hauptbahnhof",
     "blurb":"A reliable chain hotel steps from the main train station — the unglamorous, always-works option if you land late or leave early."},
  ]},
  {"t":"book","head":"Compare live rates before you book","html":"Booking.com's current prices for these and every other Berlin property move with season and demand &mdash; worth checking against the bands above before you commit.","program":"booking","query":"Berlin","label":"See Berlin hotels on Booking"},
  {"t":"h2","text":"Eating without a fixed price list"},
  {"t":"p","html":"We don't have confirmed per-dish prices from this research pass, so we won't invent one here — but the honest shape of it is this: our own data on the <a class='inline' href='/berlin/where-to-eat-in-berlin/'>Sonnenallee food crawl</a> is itself the budget tip. Neukölln, and Sonnenallee specifically, is described in our research as the single best-value district for authentic eating in the city — a dense strip of falafel counters, shawarma shops, halal butchers and Levantine grocers, not tourist-menu restaurants. Berlin's two most iconic street foods, currywurst and döner, are famously cheap by reputation across the city generally, though we don't have a specific current price for either to quote honestly."},
  {"t":"tip","head":"Self-catering option","html":"Maybachufer's canal-side Turkish market (the &ldquo;T&uuml;rkenmarkt&rdquo;) in Neukölln is the classic spot for cheap produce, cheese, bread and fabric — historically open Tuesday and Friday afternoons, though confirm the current schedule before you plan a trip around it."},
  {"t":"h2","text":"Free things to do"},
  {"t":"ul","items":[
    "<strong>Brandenburg Gate.</strong> Free, floodlit at night, open whenever you show up.",
    "<strong>East Side Gallery.</strong> 1.3km of the Berlin Wall repainted by international artists, along the river in Friedrichshain — always open, no ticket.",
    "<strong>Holocaust Memorial.</strong> The Memorial to the Murdered Jews of Europe, free and open at all times, right by the Brandenburg Gate and Tiergarten.",
    "<strong>Tiergarten.</strong> Berlin's big central park — a free walk between Brandenburg Gate and Charlottenburg rather than a transit hop.",
  ]},
  {"t":"tip","head":"The Reichstag dome is free, but book the slot","html":"Entry to the Reichstag's glass dome costs nothing, but you need a reserved time slot and those fill up — some 2026 dates close the dome to visitors entirely. It's the one free sight on this list worth planning around in advance."},
  {"t":"h2","text":"Getting around without wasting money"},
  {"t":"p","html":"The BVG network (U-Bahn, S-Bahn, trams and buses) covers the whole city, and central Mitte, Kreuzberg and Neukölln are all genuinely walkable once you're in them — easy days where you spend nothing on transport at all. Berlin is also flat and bikeable, with rental schemes like Nextbike and Lime if you'd rather pedal, though we don't have current rental pricing for either to quote."},
  {"t":"warn","head":"Price the WelcomeCard before you buy it","html":"The Berlin WelcomeCard bundles unlimited transit with museum and attraction discounts, sold in multi-day options — but its pricing changes and we don't have a confirmed current rate. Check the live price against what you'd actually spend on single BVG tickets for your trip length before committing; for a short stay with light sightseeing, separate tickets sometimes cost less."},
  {"t":"h2","text":"When to go to spend less"},
  {"t":"p","html":"Winter (December&ndash;February) is the quietest, lowest-demand season — genuinely cold, with highs around 3&deg;C, but the thinnest crowds and presumably the softest hotel rates of the year, aside from the separate demand spike Christmas markets bring in late November and December. Peak summer (June&ndash;August) is the busiest and priciest window, and late September's Berlin Marathon fills hotels citywide even though it falls inside the otherwise-quieter shoulder season — check that date specifically before you book."},
  {"t":"h2","text":"Spend it like a Berlin local"},
  {"t":"p","html":"The cheapest version of this trip and the most authentic one overlap almost completely: a Sonnenallee counter instead of a Mitte tourist menu, a bike or the BVG instead of taxis, and the free monuments done properly on foot instead of a paid bus tour past them. Picking Friedrichshain, Kreuzberg or Neukölln over Mitte for your bed does more for the budget than any single discount — it's the one choice in this guide that changes every other price that follows from it."},
 ],
 "faq":[
   ("Is Berlin an expensive city to visit?",
    "It can be, in Mitte's priciest hotels, but it doesn't have to be — Friedrichshain has the city's cheapest hostel beds (dorms from around €24), Kreuzberg and Prenzlauer Berg run roughly €70–170 a night, and the best-value eating (Neukölln's Sonnenallee) is also some of the most authentic food in the city."),
   ("What's the cheapest way to eat well in Berlin?",
    "Head to Sonnenallee in Neukölln — our research identifies it as the city's single best-value eating district, dense with falafel counters, shawarma shops and Levantine bakeries rather than tourist-menu restaurants. We don't have confirmed per-dish prices to quote, but it's built on counter food, not fine dining."),
   ("Is the Berlin WelcomeCard worth buying to save money?",
    "It depends on your itinerary — the card bundles unlimited transit with attraction discounts, which can pay off on a sightseeing-heavy multi-day trip. We don't have a confirmed current price for it, so check it against what single BVG tickets would cost for your actual trip before buying."),
 ],
},

]
