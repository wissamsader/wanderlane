# -*- coding: utf-8 -*-
# PALERMO — getting-around guide, extending palermo.py's hub. No CITY block
# here (palermo.py already owns the hub). All specifics from
# research/city-palermo.md, Section B5 ("Getting there / around") plus the
# B1 note on the historic-core quarters — same honesty rules as the rest of
# the network: no invented prices, times or numbers beyond what the
# research brief actually states.

PAGES = [

{
 "city":"palermo", "slug":"getting-around-palermo", "order":6,
 "title":"Getting Around Palermo: Airport, Transit & What to Skip",
 "kicker":"Palermo · Getting around",
 "dek":"From Falcone–Borsellino airport into the city by train or shuttle bus, why the historic core is a walking city, and the one thing Wikivoyage itself warns you off.",
 "description":"How to get around Palermo: the Falcone–Borsellino airport transfer by train or bus, walking the historic core, the AMAT bus ticket, and why driving in the center is a bad idea.",
 "read":"6 min", "updated":"October 2026",
 "related":["where-to-stay-in-palermo","best-things-to-do-in-palermo","3-days-in-palermo"],
 "blocks":[
  {"t":"lead","html":"Palermo's historic core is compact enough to see mostly on foot, which takes the pressure off getting the transit right. Here's the airport transfer, how the center itself works once you're in it, and the one thing the city's own guides tell you flat out to skip."},
  {"t":"h2","text":"From Falcone–Borsellino airport into town"},
  {"t":"p","html":"<strong>Falcone–Borsellino Airport</strong> (Punta Raisi) sits about 35km from the city center."},
  {"t":"compare","head":["Option","What to know","Best for"],
   "rows":[
     ["<strong class='best'>Train</strong>","Punta Raisi station is the terminus of the Palermo metropolitan line, running direct to Palermo Centrale roughly every 30 minutes from early morning to around 22:00.","Most arrivals — frequent, direct to the main station, no traffic to sit in."],
     ["Airport shuttle bus","Prestia e Comandè runs a dedicated shuttle to the city center every 30 minutes.","Landing outside train hours, or heading somewhere a bus stop suits better than Palermo Centrale."],
     ["Taxi","Available at the arrivals rank; figure roughly 45–60 minutes depending on traffic. Agree the fare before you set off.","Late arrivals, luggage-heavy trips, or a direct drop at your door."],
   ],
   "cap":"Confirm the current Prestia e Comandè fare and train timetable before you fly — exact current pricing wasn't verified for this guide."},
  {"t":"h2","text":"Getting around the historic core"},
  {"t":"p","html":"The old city — Kalsa, Vucciria, Ballarò, Capo and the Quattro Canti crossroads where they all meet — is compact and genuinely walkable; most of what you came to see is reachable on foot. A free “Centro Storico” tourist bus loop covers the rest, and a 24-hour AMAT bus ticket runs about €4 if you want the wider city on transit."},
  {"t":"tip","head":"Basing yourself to walk more, taxi less","html":"Staying centrally — around Piazza Ruggero Settimo, Fontana della Ninfa or Piazza Giuseppe Verdi — puts you in walking range of the historic core, which is the general lodging advice for the city. See our <a class='inline' href='/palermo/where-to-stay-in-palermo/'>where-to-stay guide</a> for specific picks in that area and in Kalsa."},
  {"t":"h2","text":"What to skip"},
  {"t":"warn","head":"Don't rent a car for the city itself","html":"Palermo's own travel guides flag driving here directly as dangerous, because the rules of the road aren't reliably followed. Narrow one-way streets in the historic center, aggressive scooter traffic and chaotic parking make a rental car more trouble than it's worth inside the city. Walk or bus centrally, and only rent a car for day trips outside town — Cefalù or Segesta, for instance — where you actually need the range a car gives you."},
  {"t":"p","html":"Skip booking a private airport transfer by default, too: the direct train to Palermo Centrale runs every 30 minutes and gets you to the main station without the traffic a private car or taxi has to sit in."},
  {"t":"book","head":"Once you've picked a neighborhood to base yourself in","html":"Booking.com lets you compare Palermo hotel and B&B prices by area &mdash; worth doing alongside this guide, since a stay near the historic core means less time spent getting to it.","program":"booking","query":"Palermo","label":"See Palermo stays on Booking"},
 ],
 "faq":[
   ("How do I get from Palermo airport to the city center?",
    "The train from Punta Raisi station is the easiest option — it's the terminus of the Palermo metropolitan line and runs direct to Palermo Centrale roughly every 30 minutes from early morning to around 22:00. A Prestia e Comandè shuttle bus also runs every 30 minutes, and taxis are available at the arrivals rank for around 45–60 minutes depending on traffic."),
   ("Is Palermo's historic center walkable?",
    "Yes — Kalsa, Vucciria, Ballarò, Capo and the Quattro Canti crossroads are compact and genuinely walkable, and most sights are reachable on foot. A free Centro Storico tourist bus loop and a roughly €4 24-hour AMAT bus ticket cover anything further out."),
   ("Should I rent a car in Palermo?",
    "Not for the city itself — Palermo's own travel guides describe driving in the center as dangerous, with narrow one-way streets, heavy scooter traffic and difficult parking. Walk or use buses in the historic core, and save a rental car for day trips outside town, like Cefalù or Segesta."),
 ],
},

]
