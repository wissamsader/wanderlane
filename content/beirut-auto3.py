# -*- coding: utf-8 -*-
# BEIRUT — getting-around guide, extending beirut.py's hub. No CITY block
# here (beirut.py already owns the hub). All specifics from
# research/city-beirut.md, Section B5 (July 2026 pass) — same honesty
# rules as the rest of the network: no invented prices, times or numbers
# beyond what the research brief actually states, and nothing from the
# brief's Low-confidence items.

PAGES = [

{
 "city":"beirut", "slug":"getting-around-beirut", "order":6,
 "title":"Getting Around Beirut: Airport, Taxis & What to Skip",
 "kicker":"Beirut · Getting around",
 "dek":"From Rafic Hariri airport into town, why a short taxi hop between neighborhoods is normal even in a walkable city, and the honest cash-and-Bolt facts nobody puts in the brochure.",
 "description":"How to get around Beirut: airport transfer options, taxis vs. Bolt, walkability within neighborhoods, and the cash-only reality that shapes how you'll actually pay for it all.",
 "read":"6 min", "updated":"September 2026",
 "related":["where-to-stay-in-beirut","best-things-to-do-in-beirut","3-days-in-beirut"],
 "blocks":[
  {"t":"lead","html":"Beirut isn't a city with a metro or a rail line to learn — it runs on foot within a neighborhood and on taxis between them. That's a simpler system than it sounds, once you know the two things that trip people up: how you'll pay, and what to expect right at the airport."},
  {"t":"h2","text":"From the airport into town"},
  {"t":"p","html":"You'll land at <strong>Beirut–Rafic Hariri International Airport (BEY)</strong>, Lebanon's only airport, south of the city near the southern suburbs — roughly 15 to 25 minutes to Hamra, Downtown or Achrafieh depending on traffic."},
  {"t":"compare","head":["Option","What to know","Best for"],
   "rows":[
     ["<strong class='best'>Official taxi counters</strong>","Inside arrivals — agree the fare before you get in.","Most first-timers; the simplest, most predictable option."],
     ["Bolt","Metered in-app fare, no haggling — but airport security has reportedly turned away some Bolt pickups that arrive without an already-matched passenger, so it can be hit-or-miss right at arrivals.","Travelers comfortable troubleshooting a ride-share pickup, or anywhere else in the city once you've landed."],
   ],
   "cap":"If Bolt gives you trouble at the curb, the taxi counter inside arrivals is the fallback, not the other way around."},
  {"t":"h2","text":"Getting around once you're here"},
  {"t":"p","html":"Beirut's neighborhoods — <strong>Hamra, Mar Mikhael, Gemmayzeh, Achrafieh, Badaro, Downtown</strong> — are each walkable internally. But sidewalks between districts are patchy or absent, and distances that look short on a map can be deceptive on foot. A short Bolt or taxi hop between neighborhoods (Hamra to Mar Mikhael, say) is normal, cheap and genuinely expected here — it isn't a sign you've done something wrong."},
  {"t":"tip","head":"Gemmayzeh to Mar Mikhael is the one walk worth doing","html":"The Saint Nicolas Stairs connect Gemmayzeh to Mar Mikhael on foot — the one inter-neighborhood walk that's both scenic and genuinely short, if you're moving between an evening in one and a nightcap in the other."},
  {"t":"h2","text":"Cash rules almost everything"},
  {"t":"warn","head":"Bring more small-denomination USD than you think you need","html":"Beirut has run on a cash-and-USD basis since the 2019–2020 banking crisis, and that shapes how you'll pay for taxis and Bolt rides as much as meals: crisp, newer US bills are the practical currency, card acceptance is inconsistent outside upscale venues, and ATM withdrawals (especially in USD, especially on foreign cards) can be unreliable. Carry enough small bills to cover a day's taxis and tips without needing to break a large one."},
  {"t":"h2","text":"What to skip"},
  {"t":"p","html":"Skip trying to plan around a public transit map — there isn't one to speak of here, and the taxi-and-walking rhythm above is genuinely how residents get around, not a workaround. And don't count on a ride-share pickup landing smoothly right at the airport curb on your first try; that's the one spot where the official taxi counter is the more reliable default, not the backup plan."},
  {"t":"book","head":"Once you've picked a neighborhood to base yourself in","html":"Booking.com lets you compare Beirut hotel prices by area, which is worth doing alongside this guide — a place in Hamra or Gemmayzeh cuts down on how many taxi hops you'll need each day.","program":"booking","query":"Beirut","label":"See Beirut hotels on Booking"},
 ],
 "faq":[
   ("How do I get from Beirut airport to the city center?",
    "Use the official taxi counters inside arrivals and agree the fare before you get in — it's the simplest, most predictable option. Bolt also operates in Beirut with a metered in-app fare, but airport security has reportedly turned away some Bolt pickups that arrive without an already-matched passenger, so it can be hit-or-miss right at the curb."),
   ("Is Beirut walkable?",
    "Within a neighborhood, yes — Hamra, Mar Mikhael, Gemmayzeh, Achrafieh, Badaro and Downtown are each walkable internally. Between neighborhoods, sidewalks are patchy and distances can be deceptive, so a short taxi or Bolt hop is the normal way to move around, not a sign you've planned poorly."),
   ("Can I pay for taxis and Bolt rides with a card in Beirut?",
    "Don't count on it. Beirut has run largely on cash and USD since the 2019–2020 banking crisis — card acceptance is inconsistent outside upscale venues and foreign-card ATM withdrawals can be unreliable. Carry more small-denomination US bills than you think you'll need."),
 ],
},

]
