# -*- coding: utf-8 -*-
# BARCELONA — getting-around guide, extending barcelona.py's hub. No CITY
# block here (barcelona.py already owns the hub). All specifics from
# research/city-barcelona.md, Section B5 (July 2026 pass) — same honesty
# rules as the rest of the network: no invented prices, times or numbers
# beyond what the research brief actually states, and nothing from the
# brief's Low-confidence items (the exact current T-casual card price).

PAGES = [

{
 "city":"barcelona", "slug":"getting-around-barcelona", "order":6,
 "title":"Getting Around Barcelona: Airport, Metro & What to Skip",
 "kicker":"Barcelona · Getting around",
 "dek":"From El Prat into town, the metro card that covers almost everything, and why you don't want a rental car anywhere near the old town.",
 "description":"How to get around Barcelona: airport transfer options (Aerobus vs. train), the metro and T-casual card, walkability of the old town, and why to skip renting a car.",
 "read":"6 min", "updated":"September 2026",
 "related":["where-to-stay-in-barcelona","best-things-to-do-in-barcelona","3-days-in-barcelona"],
 "blocks":[
  {"t":"lead","html":"Barcelona is one of the easier big European cities to move around in: a flat, walkable old core, a fast metro for everything else, and a well-connected airport. The only real mistake is renting a car for the city itself."},
  {"t":"h2","text":"From the airport into town"},
  {"t":"p","html":"You'll land at <strong>Josep Tarradellas Barcelona–El Prat</strong>, about 15km southwest of the center and one of Europe's busiest airports — Terminal 1 handles roughly 70% of flights. Two ways in are worth knowing:"},
  {"t":"compare","head":["Option","Time","Price","Best for"],
   "rows":[
     ["<strong class='best'>Aerobus</strong>","~35–40 min","~&euro;6&ndash;7 one-way","Most travelers — direct express bus straight to Plaça Catalunya, runs every 5–20 minutes depending on time of day"],
     ["R2 Nord rail","Similar journey time","A few euros less than Aerobus","Budget travelers — connects the airport to Barcelona-Sants and Passeig de Gràcia, but runs less frequently"],
   ],
   "cap":"Aerobus fares move with demand — check the current price at aerobusbcn.com before you land."},
  {"t":"p","html":"A metered taxi is the third option — pricier than either, but the easiest choice late at night or with luggage and a group, straight to your hotel door with no transfers."},
  {"t":"h2","text":"Getting around once you're here"},
  {"t":"p","html":"The tourist core — <strong>Barri Gòtic, El Born, El Raval and the Eixample's Dreta side</strong> — is flat and genuinely walkable; most of what's in our <a class='inline' href='/barcelona/best-things-to-do-in-barcelona/'>things-to-do guide</a> is reachable on foot from any of those neighborhoods. For longer hops, the metro is fast and dense, and the <strong>T-casual</strong> multi-trip card (the current successor to the old T-10) is the one to buy — ten journeys, shareable between however many people you're traveling with, and zone 1 covers essentially every central sight."},
  {"t":"tip","head":"The best food is a short ride away","html":"Worth knowing: a lot of Barcelona's best eating — several of the places in our <a class='inline' href='/barcelona/where-to-eat-in-barcelona/'>food guide</a> — sits in neighborhoods like Sant Andreu, Horta-Guinardó, Sants and Gràcia, just outside the tourist core. A short metro ride buys you real neighborhood food and Rambla-adjacent prices you won't pay a few stops out."},
  {"t":"h2","text":"What to skip: renting a car"},
  {"t":"warn","head":"Don't rent a car for the city itself","html":"Barcelona's old-town streets are narrow, medieval and largely off-limits or awkward for private cars, parking is scarce and expensive, and the metro plus walking covers the entire tourist core more easily than driving ever would. A car only makes sense if you're planning to leave the city entirely — for the coast or the mountains beyond a day trip's reach — and even then, most people rent for just those days rather than the whole stay."},
  {"t":"h2","text":"Day trips out of the city"},
  {"t":"p","html":"For trips like Montserrat, you're looking at train plus rack railway or cable car rather than a car — see our <a class='inline' href='/barcelona/best-things-to-do-in-barcelona/'>things-to-do guide</a> for the specifics. It's simpler to book as a single guided day trip than to piece together the connections yourself on a first visit."},
  {"t":"book","head":"Compare hotels near the transit you'll actually use","html":"If you haven't picked a neighborhood yet, Booking.com lets you filter by area and see today's prices side by side — useful for weighing walkability against how far you'll be riding the metro each day.","program":"booking","query":"Barcelona","label":"See Barcelona hotels on Booking"},
 ],
 "faq":[
   ("How do I get from Barcelona airport to the city center?",
    "Take the Aerobus express bus (about 35–40 minutes to Plaça Catalunya, roughly €6–7 one-way, running every 5–20 minutes) or the R2 Nord rail line, which is a little cheaper but less frequent and serves Barcelona-Sants and Passeig de Gràcia. A metered taxi costs more but goes door-to-door."),
   ("Do you need a car in Barcelona?",
    "No — and you shouldn't rent one for the city itself. The old town's streets are narrow and largely unsuited to private cars, parking is scarce, and the metro plus walking cover the entire tourist core more easily. Only consider a car if you're heading well beyond the city for a few days."),
   ("What's the easiest way to get around Barcelona day to day?",
    "Walk the flat, compact tourist core — Barri Gòtic, El Born, El Raval and Eixample's Dreta side are all close together — and use the metro with a T-casual multi-trip card for anything farther, including the neighborhoods outside the center where a lot of the best food is."),
 ],
},

]
