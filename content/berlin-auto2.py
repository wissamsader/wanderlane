# -*- coding: utf-8 -*-
# BERLIN — getting-around guide, extending berlin.py's hub. No CITY block
# here (berlin.py already owns the hub). All specifics from
# research/city-berlin.md, Section B ("Getting there / around", July 2026
# pass) — same honesty rules as the rest of the network: no invented
# prices, times or numbers beyond what the research brief actually states.

PAGES = [

{
 "city":"berlin", "slug":"getting-around-berlin", "order":6,
 "title":"Getting Around Berlin: Airport, Transit & What to Skip",
 "kicker":"Berlin · Getting around",
 "dek":"From BER airport into the city on the Airport Express, how the BVG network and a bike cover everything else, and the one pass worth pricing before you buy it.",
 "description":"How to get around Berlin: BER airport transfer options, the BVG U-Bahn/S-Bahn/tram/bus network, biking, and whether the Berlin WelcomeCard is worth it.",
 "read":"6 min", "updated":"October 2026",
 "related":["where-to-stay-in-berlin","best-things-to-do-in-berlin","3-days-in-berlin"],
 "blocks":[
  {"t":"lead","html":"Berlin is flat, well-signed and covered end to end by one integrated transit network, which makes it one of the easier European capitals to move around in. Here's the airport transfer, the network that does the rest, and the one pass worth doing the math on before you buy it."},
  {"t":"h2","text":"From BER airport into town"},
  {"t":"p","html":"<strong>Berlin Brandenburg Airport (BER)</strong> sits about 18km southeast of the city center, with its own station open 24/7."},
  {"t":"compare","head":["Option","What to know","Best for"],
   "rows":[
     ["<strong class='best'>Airport Express (FEX)</strong>","Every 15 minutes to Berlin Hauptbahnhof (via Südkreuz, Potsdamer Platz), about 22 minutes.","Most arrivals — it's the fastest, most frequent link into the center."],
     ["S-Bahn S9 / S45","S9 runs to Alexanderplatz and Friedrichstraße/Hbf; S45 runs via Neukölln and Tempelhof.","Landing outside the center, or heading straight to Neukölln for Sonnenallee."],
     ["Regional trains (RE7, RB14, RE20 etc.)","Also call at the airport station.","Travelers already routing through the wider regional rail network."],
   ],
   "cap":"All of these use the same airport station, so you're choosing a line, not a separate transfer system."},
  {"t":"h2","text":"Getting around once you're here"},
  {"t":"p","html":"The <strong>BVG</strong> network — U-Bahn, S-Bahn, trams and buses all on one system — covers the city thoroughly, and central Mitte, Kreuzberg and Neukölln are all highly walkable once you're in them. Berlin is also flat and genuinely bikeable, with extensive bike lanes and rental schemes like Nextbike and Lime if you'd rather pedal than wait for a train."},
  {"t":"tip","head":"Heading to Sonnenallee specifically","html":"Sonnenallee has its own S-Bahn station, or take the U7 to Karl-Marx-Straße or Rathaus Neukölln and walk in — see our <a class='inline' href='/berlin/where-to-eat-in-berlin/'>Sonnenallee food crawl</a> for the full walking order."},
  {"t":"h2","text":"Is the Berlin WelcomeCard worth it?"},
  {"t":"p","html":"The <strong>Berlin WelcomeCard</strong> bundles unlimited public transport with discounts (historically up to 50%) on museums, attractions and tours, sold in 48h/72h/5-day/6-day options. If you're sightseeing hard across several days and plan to use the transit a lot anyway, it can pencil out — but price it against single tickets for your actual itinerary first rather than assuming it's a win. Note that zone AB doesn't reach BER airport; you need the pricier zone ABC version to cover that transfer too."},
  {"t":"warn","head":"Confirm current pricing before you buy","html":"WelcomeCard pricing changes, so check the live price against what you'd actually spend on single BVG tickets for your trip length before committing — for a short stay with light sightseeing, separate tickets are sometimes the cheaper call."},
  {"t":"h2","text":"What to skip"},
  {"t":"p","html":"Skip booking a private airport transfer by default — the Airport Express gets you to Hauptbahnhof in about 22 minutes on a schedule that runs every 15 minutes, which is hard to beat on time or price. And don't buy a multi-day transit pass on reflex: if your days are light on sightseeing or you're mostly walking within one neighborhood, single tickets can genuinely cost less than the WelcomeCard."},
  {"t":"book","head":"Once you've picked a neighborhood to base yourself in","html":"Booking.com lets you compare Berlin hotel prices by area — worth doing alongside this guide, since a stay near a U-Bahn or S-Bahn stop makes the whole network easier to use.","program":"booking","query":"Berlin","label":"See Berlin hotels on Booking"},
 ],
 "faq":[
   ("How do I get from Berlin Brandenburg Airport (BER) to the city center?",
    "The Airport Express (FEX) is the fastest option — it runs every 15 minutes to Berlin Hauptbahnhof in about 22 minutes. S-Bahn lines S9 and S45 also serve the airport and run into the center, with S45 passing through Neukölln and Tempelhof along the way."),
   ("Is Berlin easy to get around without a car?",
    "Yes — the BVG network (U-Bahn, S-Bahn, trams and buses) covers the city thoroughly, and Berlin is flat enough that biking is a genuine alternative, with rental schemes like Nextbike and Lime widely available. Central districts like Mitte, Kreuzberg and Neukölln are also highly walkable."),
   ("Is the Berlin WelcomeCard worth buying?",
    "It depends on your itinerary. The card bundles unlimited transit with museum and attraction discounts, which can pay off if you're sightseeing hard across several days — but price it against single BVG tickets for your actual trip first, and remember you need the pricier zone ABC version if you want it to cover the BER airport transfer too."),
 ],
},

]
