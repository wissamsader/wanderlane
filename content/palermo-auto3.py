# -*- coding: utf-8 -*-
# PALERMO — on-a-budget guide, extending palermo.py's hub. No CITY block
# here (palermo.py already owns the hub). All specifics from
# research/city-palermo.md (July 2026 pass, Sections A2/B2/B5/B6) — same
# honesty rules as the rest of the network: no invented prices, fares or
# numbers beyond what the research brief actually states.

PAGES = [

{
 "city":"palermo", "slug":"palermo-on-a-budget", "order":7,
 "title":"Palermo on a Budget: What It Actually Costs",
 "kicker":"Palermo · Budget",
 "dek":"Real street-food prices from €1.50 arancine to a €27 seafood platter, hotel bands from hostel to boutique, the €4 bus ticket, and the gaps we won't invent.",
 "description":"What Palermo actually costs: real street-food prices, hotel bands by neighborhood, the AMAT bus ticket, and the numbers our research pass couldn't confirm — left honest, not guessed.",
 "read":"7 min", "updated":"November 2026",
 "related":["where-to-stay-in-palermo","where-to-eat-in-palermo","getting-around-palermo"],
 "blocks":[
  {"t":"lead","html":"Palermo might be the best-value food city in Italy — most of what's worth eating here was built to be cheap, fast and eaten standing up, not plated for tourists. Here's what things actually cost, with the gaps left honest instead of invented."},
  {"t":"h2","text":"The real numbers: street food prices"},
  {"t":"p","html":"These are transcribed from each business's own menu board or listing, not estimated averages — see our <a class='inline' href='/palermo/where-to-eat-in-palermo/'>food guide</a> for the full 15-place list."},
  {"t":"compare","head":["What","Price","Where"],
   "rows":[
     ["<strong class='best'>Arancina</strong> (fried rice ball)","€1.50","Antonello Street Food, Il Rosticciere"],
     ["Pane e panelle, full board","€1.50&ndash;€3","Friggitoria Chiluzzo"],
     ["Sfincione (Palermo focaccia-pizza)","€7","Villena"],
     ["Pasta con le cozze","€14","Sicily Street Food"],
     ["Grilled calamaro / caponata starter","€9 / €3","Trattoria Al Sorriso"],
     ["“Pranzo Operaio” workers' lunch, primi / agnello","€3&ndash;5 / €10","Trattoria da Pino"],
     ["Boxed seafood platter (“Acquario”)","€27","Carizzi d'amuri"],
   ],
   "cap":"We don't have a confirmed current price for pani ca meusa, cannoli or granita con brioche from this research pass, so none of those get a number here."},
  {"t":"h2","text":"Where to sleep without overpaying"},
  {"t":"p","html":"The budget end of our <a class='inline' href='/palermo/where-to-stay-in-palermo/'>stays guide</a> isn't a tourist-trap tier — it's a well-reviewed hostel and a straightforward boutique hotel, both in the same walkable Politeama/Libertà area as our flagship restaurant."},
  {"t":"stays","items":[
    {"name":"A Casa di Amici","area":"Libertà/Politeama","band":"€25–90","program":"booking","query":"A Casa di Amici Palermo",
     "blurb":"A boutique hostel with 7 private themed rooms plus dorms (one women-only), steps from Teatro Politeama. Breakfast included."},
    {"name":"Skyline Boutique Hotel","area":"Ruggero Settimo","band":"€60–100","program":"booking","query":"Skyline Boutique Hotel Palermo",
     "blurb":"9.0/10 on Booking — near the Via della Libertà shopping strip, a budget step up from a hostel without boutique pricing."},
  ]},
  {"t":"p","html":"Once you're past €100 a night you're into Massimo Plaza (€110–170) or Palazzo Cartari in Kalsa (€100–160) — both genuinely nice, neither necessary if the budget is tight."},
  {"t":"book","head":"Compare live rates before you book","html":"Booking.com's current prices for these and every other Palermo property move with season and demand &mdash; worth checking against the bands above before you commit.","program":"booking","query":"Palermo","label":"See Palermo hotels on Booking"},
  {"t":"h2","text":"Getting around without wasting money"},
  {"t":"p","html":"The historic core — Kalsa, Vucciria, Ballarò, Capo and the Quattro Canti crossroads where they all meet — is compact and genuinely walkable, so most days here cost nothing in transport at all. If you want the wider city, a 24-hour AMAT bus ticket runs about €4, and a free “Centro Storico” tourist loop bus covers some of the rest. We don't have a confirmed current fare for the Prestia e Comandè airport shuttle or the Punta Raisi airport train, so check those live before you fly — full detail in our <a class='inline' href='/palermo/getting-around-palermo/'>getting around guide</a>."},
  {"t":"warn","head":"Don't rent a car for the city itself","html":"Palermo's own travel guides flag driving here directly as dangerous, with narrow one-way streets and rules that aren't reliably followed. A rental car is more trouble than it's worth inside the historic core — walk or bus centrally, and only rent one for day trips outside town, like Cefalù or Monreale."},
  {"t":"h2","text":"Free (or nearly free) things to do"},
  {"t":"ul","items":[
    "<strong>Walk the three markets.</strong> Ballarò, Vucciria and Capo cost nothing to wander — you only spend when you stop to eat.",
    "<strong>Quattro Canti.</strong> Palermo's Baroque crossroads, free to stand in and look up at any hour.",
    "<strong>Mondello beach.</strong> The Belle Époque seaside bay is a free sandy stretch, reached through La Favorita park — you just pay for however you get there.",
    "<strong>The Kalsa's palazzi streets.</strong> Free to walk even if you don't book inside Palazzo Abatellis or Palazzo Chiaramonte-Steri.",
  ]},
  {"t":"tip","head":"Budget cash for tickets, not just food","html":"We don't have confirmed current ticket prices for the Cathedral, the Palatine Chapel, Teatro Massimo or the Capuchin Catacombs from this research pass, so none of those get a number here either — budget some cash for entry and check current prices before you go. See our <a class='inline' href='/palermo/best-things-to-do-in-palermo/'>things-to-do guide</a> for what each one actually is."},
  {"t":"h2","text":"When to go to spend less"},
  {"t":"p","html":"We don't have confirmed seasonal hotel-pricing data for Palermo from this research pass, so we won't claim a literal cheapest month. What we do know: spring (April&ndash;June) and early autumn (September&ndash;October) avoid both August's peak heat and its cruise-ship crowds, which at minimum buys you shorter queues and a calmer, less squeezed version of the same free sights. A few family-run spots on our eats list close one day a week or take a summer break &mdash; check before a trip built around one restaurant."},
  {"t":"h2","text":"Spend it like a Palermo local"},
  {"t":"p","html":"The cheapest version of this trip and the most authentic one are the same trip: an arancina eaten standing at a street cart instead of a sit-down restaurant, the historic core on foot instead of a taxi, and the markets themselves instead of a paid tour through them. None of that is a compromise here &mdash; it's genuinely how the city eats and moves."},
 ],
 "faq":[
   ("Is Palermo an expensive city to visit?",
    "Not inherently — its best food is market and street food built to be cheap (arancine at €1.50, a full pane e panelle board for €1.50–3), and a budget hostel like A Casa di Amici runs €25–90 a night. We don't have a confirmed overall daily-budget figure from this research pass, so we won't invent one, but the building blocks are genuinely low-cost."),
   ("What does street food actually cost in Palermo?",
    "An arancina runs €1.50 at Antonello Street Food or Il Rosticciere, a full pane e panelle board at Friggitoria Chiluzzo runs €1.50–3, and sfincione at Villena is €7. A sit-down seafood lunch like Sicily Street Food's pasta con le cozze is €14 — still well below fine-dining prices."),
   ("Do I need much money for transport in Palermo?",
    "Very little. The historic core is compact and walkable, so most days cost nothing in transport. A 24-hour AMAT bus ticket is about €4 if you want the wider city, and a free Centro Storico loop bus covers some of that ground too — just skip renting a car for the city itself."),
 ],
},

]
