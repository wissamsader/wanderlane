# -*- coding: utf-8 -*-
# PALERMO — depth pack: stays, essential sights, and a 3-day itinerary.
# Facts sourced from research/city-palermo.md + well-known Palermo/Sicily
# general knowledge (July 2026). No CITY block here — palermo.py owns that;
# this file only adds three more articles to the same city.

PAGES = [

# ============================================================ WHERE TO STAY
{
 "city":"palermo", "slug":"where-to-stay-in-palermo", "order":2,
 "title":"Where to Stay in Palermo: Best Areas & Hotels",
 "kicker":"Palermo · Where to stay",
 "dek":"Four very different neighborhoods, one clear answer for who each suits — plus the real hostels and hotels worth booking in every price band.",
 "description":"An honest, area-by-area guide to where to stay in Palermo — Kalsa, Vucciria, Ballarò and Politeama/Libertà — with real hostels and hotels for every budget.",
 "read":"9 min", "updated":"July 2026",
 "related":["where-to-eat-in-palermo","best-things-to-do-in-palermo","3-days-in-palermo"],
 "blocks":[
  {"t":"lead","html":"Palermo's centro storico is really four neighborhoods wearing one name — a gallery-and-palazzo quarter, a market-by-day-bar-by-night quarter, the city's biggest street market, and a polished 19th-century boulevard just outside it all. Picking the right one changes your trip more than the hotel itself does."},
  {"t":"h2","text":"The four areas, honestly"},
  {"t":"compare","head":["Area","Best for","The trade-off"],
   "rows":[
     ["<strong>Kalsa</strong>","Galleries, palazzi, boutique stays, a seafront walk on the Foro Italico","Restored only since the mid-1990s — some backstreets away from the main piazze still feel quiet after dark"],
     ["<strong>Vucciria</strong>","The market-by-day, bar-crawl-by-night atmosphere, cheap eats on your doorstep","Genuinely loud on Friday and Saturday nights; thin on actual hotels, mostly short-let apartments"],
     ["<strong>Ballarò</strong>","Being inside the city's biggest daily market, the cheapest street food, real local life","Chaotic and crowded by day, and there's almost nowhere to sleep — a food base, not a bed base"],
     ["<strong>Politeama/Libertà</strong>","First-timers who want an easy, walkable, polished base; Via della Libertà shopping","Not 'old Palermo' — you'll walk or bus 15–20 minutes to reach the Cathedral and Quattro Canti"],
   ],
   "cap":"Short version: sleep in Kalsa or Politeama/Libertà, eat and wander in Ballarò and Vucciria."},
  {"t":"p","html":"Wikivoyage's own advice lands in the same place: stick to the city centre around Piazza Ruggero Settimo, Fontana della Ninfa and Piazza Giuseppe Verdi — Politeama/Libertà and the streets leading into the old town — for the easiest mix of safety and walkability."},
  {"t":"h2","text":"Best budget stay"},
  {"t":"p","html":"Palermo isn't a big hostel city the way some destinations are — most budget travelers land on one address, and it's a genuinely good one:"},
  {"t":"stays","items":[
    {"name":"A Casa di Amici","area":"Libertà/Politeama, Via Dante 57","band":"€25–90","program":"booking","query":"A Casa di Amici Palermo",
     "blurb":"Seven private themed rooms plus dorms (one women-only), steps from Teatro Politeama. Breakfast included, and it's an officially registered guesthouse (CIR/CIN) — worth checking any listing for that code before you book."},
  ]},
  {"t":"h2","text":"Mid-range & boutique hotels"},
  {"t":"stays","items":[
    {"name":"Skyline Boutique Hotel","area":"Ruggero Settimo","band":"€60–100","program":"booking","query":"Skyline Boutique Hotel Palermo",
     "blurb":"9.0/10 on Booking — near the Via della Libertà shopping strip and Teatro Politeama, an easy walkable base."},
    {"name":"Hotel Trinacria","area":"Borgo Vecchio","band":"€70–110","program":"booking","query":"Hotel Trinacria Palermo",
     "blurb":"9.1/10 on Booking — central, close to the port side of the old town, a level up from the budget guesthouses without hitting boutique prices."},
    {"name":"Massimo Plaza Hotel","area":"Via Maqueda 437, opposite Teatro Massimo","band":"€110–170","program":"booking","query":"Massimo Plaza Hotel Palermo",
     "blurb":"11 soundproofed rooms marketed as 'a window on Teatro Massimo' — genuinely across the street from the opera house, and about as central as Palermo gets."},
    {"name":"Palazzo Cartari","area":"La Kalsa","band":"€100–160","program":"booking","query":"Palazzo Cartari Palermo",
     "blurb":"9.3/10 on Booking — a historic palazzo conversion inside Kalsa's gallery-and-palazzo streets, an easy walk from the Foro Italico."},
  ]},
  {"t":"h2","text":"If you're splurging"},
  {"t":"p","html":"<strong>Palazzo Lanza Tomasi (Butera 28 Apartments)</strong> is the one to know about. It's the 18th-century palazzo that was the last home of Giuseppe Tomasi di Lampedusa, author of <em>The Leopard</em> — his manuscript, library and furnishings are still on site. The self-catering apartments are 5-star/ADSI-certified, sit right on the Kalsa/Foro Italico seafront, and are about as close as a hotel booking gets to sleeping inside Sicilian literary history."},
  {"t":"stays","items":[
    {"name":"Palazzo Lanza Tomasi (Butera 28)","area":"Kalsa/Foro Italico seafront","band":"€180–320","program":"booking","query":"Butera 28 Palazzo Lanza Tomasi Palermo",
     "blurb":"Self-catering apartments inside Lampedusa's own 18th-century palazzo — his library and manuscripts are still on site. Kalsa's most memorable splurge."},
  ]},
  {"t":"book","head":"Compare prices before you commit","html":"All six of these are real, bookable listings — but rates move with the season. Compare current prices on Booking before you decide.","program":"booking","query":"Palermo","label":"See Palermo stays on Booking"},
  {"t":"tip","head":"When to book","html":"April–June and September–October are peak season, and the boutique palazzo conversions (Palazzo Cartari, Butera 28) have very few rooms — book those a few weeks ahead. A Casa di Amici and the mid-range hotels are more flexible, even in summer."},
 ],
 "faq":[
   ("Which area is best to stay in for a first visit to Palermo?",
    "Politeama/Libertà if you want an easy, polished, walkable base with shopping on Via della Libertà. Kalsa if you'd rather be inside the old town's gallery-and-palazzo quarter, with the Foro Italico seafront on your doorstep and a boutique or luxury stay in mind."),
   ("Is Ballarò or Vucciria a good place to actually sleep?",
    "Not really — they're better for eating and atmosphere than sleeping. Ballarò is chaotic by day and has almost no hotels; Vucciria gets genuinely loud after dark on weekends. Visit both, but book your bed in Kalsa or Politeama/Libertà, a short walk away."),
   ("How much does a hotel in Palermo cost?",
    "A hostel room or dorm bed at A Casa di Amici runs roughly €25–90. Mid-range and boutique hotels — Skyline, Hotel Trinacria, Massimo Plaza, Palazzo Cartari — land between about €60 and €170. A palazzo splurge like Butera 28 runs €180–320."),
 ],
},

# ============================================================ THINGS TO DO
{
 "city":"palermo", "slug":"best-things-to-do-in-palermo", "order":3,
 "title":"Best Things to Do in Palermo",
 "kicker":"Palermo · Do",
 "dek":"The Arab-Norman monuments that earned Palermo a UNESCO listing, the markets that built its street-food reputation, and the day trips worth leaving the city for.",
 "description":"What to do in Palermo: the Cathedral, Palatine Chapel, Quattro Canti, Teatro Massimo, the markets, the Catacombs, and day trips to Monreale and Cefalù.",
 "read":"11 min", "updated":"July 2026",
 "related":["where-to-eat-in-palermo","where-to-stay-in-palermo","3-days-in-palermo"],
 "blocks":[
  {"t":"lead","html":"Between the Arab-Norman monuments and the street markets, Palermo could fill a week without repeating itself. This is the shortlist that earns its place, plus what's worth booking ahead and what you can just turn up for."},
  {"t":"h2","text":"The Arab-Norman core"},
  {"t":"p","html":"Norman kings ruling a mostly Arab and Byzantine population built a genuinely hybrid architecture here — Latin, Byzantine and Islamic craftsmen working the same buildings. It's rare enough that UNESCO listed it as a single site. Start with these four:"},
  {"t":"do","items":[
    {"name":"Palermo Cathedral","tag":"UNESCO Arab-Norman","program":None,
     "blurb":"A Norman-Arab-Gothic-Baroque-Neoclassical mashup that somehow works as one building. Inside: royal tombs including Frederick II, an 1801 astronomical meridian line set into the floor, and a treasury holding the golden Crown of Constance of Sicily."},
    {"name":"Palatine Chapel, Norman Palace","tag":"Byzantine gold mosaics","program":"gyg","query":"Palermo Royal Palace Palatine Chapel","label":"See tickets",
     "blurb":"The royal chapel (Cappella Palatina) inside the Norman Palace, Palazzo dei Normanni — Byzantine gold mosaics and an Islamic muqarnas ceiling packed into one small, jaw-dropping room. Part of the same UNESCO listing as the Cathedral and a short walk from it. It's also the seat of the Sicilian regional parliament, so parts occasionally close when it's in session."},
    {"name":"Quattro Canti","tag":"Baroque crossroads","program":None,
     "blurb":"Officially Piazza Vigliena — an octagonal Baroque crossroads built 1608–1620 where Palermo's four historic quarters meet, decorated with fountains and statues of the seasons, Spanish kings and the city's patron saints. Free, always open, and the natural spot to start a walk in any direction."},
    {"name":"Teatro Massimo","tag":"Italy's largest opera house","program":"gyg","query":"Teatro Massimo Palermo tour","label":"See tours",
     "blurb":"Italy's largest opera house and one of the largest in Europe, famed for its acoustics. Guided tours run even on days with no performance — worth it just to stand on the stage."},
  ]},
  {"t":"h2","text":"The markets: Ballarò and Vucciria"},
  {"t":"p","html":"Palermo's street-food reputation was built in these two quarters, and even if you're not hungry, both are worth visiting as sights in their own right — for the full food angle, see our <a class='inline' href='/palermo/where-to-eat-in-palermo/'>Palermo food guide</a>."},
  {"t":"h3","text":"Ballarò"},
  {"t":"p","html":"The city's biggest and most authentically local daily market, running through the Albergheria quarter Monday to Saturday, roughly 07:00–20:00. It's loud, chaotic and about as unpolished as Palermo gets — go in the late morning when it's in full swing."},
  {"t":"h3","text":"Vucciria"},
  {"t":"p","html":"By day, Vucciria is a fading, half-working fish and produce market centered on Piazza San Domenico and Piazza Garraffello — genuinely atmospheric decay. By night the same alleys turn into an open-air food-and-drinks scene, with DJ sets hitting Piazza Garraffello on Fridays. Go once in daylight, once after dark; they barely feel like the same place."},
  {"t":"book","head":"See both markets with a guide","html":"A guided street-food walking tour through Ballarò and Vucciria is the easiest way to taste six or seven things in a couple of hours without gambling on which stall is good that day.","program":"gyg","query":"Palermo street food walking tour Ballaro Vucciria","label":"See street-food tours"},
  {"t":"h2","text":"Beyond the center"},
  {"t":"do","items":[
    {"name":"Capuchin Catacombs","tag":"Genuinely macabre","program":"gyg","query":"Capuchin Catacombs Palermo tickets","label":"Book tickets",
     "blurb":"Roughly 8,000 mummified bodies line the corridors, including the famously preserved child Rosalia Lombardo. It's a real, unsettling piece of history, not a haunted-house attraction — and not for everyone, or every kid."},
    {"name":"Mondello beach","tag":"Belle Époque seaside","program":None,
     "blurb":"Palermo's sandy Belle Époque bay, tucked between Monte Gallo and Monte Pellegrino and reached through La Favorita park (a tram ran out here from 1912; today it's bus or car). The easy half-day escape from the historic center's stone and heat."},
  ]},
  {"t":"warn","head":"No photos in the Catacombs","html":"Photography is officially banned inside the Capuchin Catacombs, and it's enforced. Leave the camera in your bag and just be present for it."},
  {"t":"h2","text":"Day trips worth leaving the city for"},
  {"t":"compare","head":["Trip","Distance","Best for"],
   "rows":[
     ["<strong>Monreale</strong>","~8 km, a short bus or taxi ride","A quick half-day add-on — the gold-mosaic cathedral alone is worth the trip"],
     ["<strong>Cefalù</strong>","~70 km east","A half-to-full day: a beach, a Norman cathedral, and one of Italy's prettiest old towns"],
     ["<strong>Segesta</strong>","~100 km, near Trapani","A full day for ancient-history fans — a near-perfectly preserved Doric temple and Greek theatre, best with a car or tour"],
   ],
   "cap":"Monreale is the easy yes. Cefalù or Segesta depend on whether you want a beach or ruins."},
  {"t":"callout","head":"Monreale Cathedral","html":"12th-century, Norman-built, and covered in roughly 6,500 m² of Byzantine-style gold mosaics — one of the greatest Norman monuments anywhere, and one of the best half-days you can spend outside Palermo."},
  {"t":"btnrow","btns":[
    {"program":"gyg","query":"Monreale Cathedral tour from Palermo","label":"Monreale day trip"},
    {"program":"gyg","query":"Cefalu day trip from Palermo","label":"Cefalù day trip","style":"btn-forest"},
  ]},
  {"t":"tip","head":"Book ahead in peak season","html":"Monreale and Cefalù day-trip tours, and Capuchin Catacombs tickets, can sell out on summer weekends. If your dates are fixed and it's April–October, book a day or two ahead rather than showing up."},
 ],
 "faq":[
   ("What are the must-see sights in Palermo?",
    "Palermo Cathedral, the Palatine Chapel inside the Norman Palace, Quattro Canti, and Teatro Massimo cover the Arab-Norman and Baroque essentials. Add a walk through the Ballarò and Vucciria markets, which are as much a sight as a meal."),
   ("Is the Capuchin Catacombs worth visiting?",
    "For most travelers, yes — it's a genuinely singular historical experience, not a tourist gimmick. It's also legitimately macabre (roughly 8,000 mummified bodies), photography is banned, and it's not for younger kids or anyone squeamish."),
   ("Monreale or Cefalù — which day trip should I pick?",
    "Monreale if you're short on time: it's about 8 km out and fits into a half-day without disrupting the rest of your plans. Cefalù if you want a fuller day with a beach and an old town attached. With four or five days, do both."),
 ],
},

# ============================================================ 3-DAY ITINERARY
{
 "city":"palermo", "slug":"3-days-in-palermo", "order":4,
 "title":"3 Days in Palermo: The Perfect Itinerary",
 "kicker":"Palermo · Itinerary",
 "dek":"A day-by-day plan that fits the old town, Monreale, the Cathedral, Teatro Massimo and a beach or a Cefalù day trip into three days.",
 "description":"The perfect 3-day Palermo itinerary: old-town markets and street food, Monreale and the Cathedral, then Mondello beach or a Cefalù day trip.",
 "read":"9 min", "updated":"July 2026",
 "related":["where-to-eat-in-palermo","where-to-stay-in-palermo","best-things-to-do-in-palermo"],
 "blocks":[
  {"t":"lead","html":"Three days is enough to properly do Palermo: the old town and its markets, the two big Norman set-pieces, and one day trip to close it out. Here's the plan, stop by stop."},
  {"t":"tip","head":"Where to sleep for this plan","html":"Base yourself in Kalsa or Politeama/Libertà — both keep everything on Day 1 and Day 2 within walking distance. Full breakdown, with real hotels for every budget, in our <a class='inline' href='/palermo/where-to-stay-in-palermo/'>where-to-stay guide</a>."},
  {"t":"h2","text":"Day 1 — Old town, markets & street food"},
  {"t":"p","html":"A day for wandering with no fixed reservations — orient yourself at the crossroads, then eat your way through two markets."},
  {"t":"ol","items":[
    "Start at <strong>Quattro Canti</strong> (Piazza Vigliena), the Baroque crossroads where Palermo's old quarters meet — five minutes, but it orients the rest of your trip.",
    "Walk into <strong>Ballarò market</strong> for a street-food breakfast: an arancina, pane e panelle, whatever's frying. It runs Monday–Saturday and is loudest by late morning.",
    "Spend early afternoon in <strong>Kalsa</strong> — Palazzo Abatellis, the Foro Italico seafront, the quieter gallery streets away from the market noise.",
    "Detour into <strong>Capo market</strong> behind the Cathedral for a quieter, more residential market than Ballarò — a good slow browse before dinner.",
    "Finish in <strong>Vucciria</strong> after dark: Piazza Garraffello, a drink, more street food. Friday nights bring DJ sets if your dates line up.",
  ]},
  {"t":"p","html":"For exact places and dishes — including our Michelin Guide-listed flagship — see the full <a class='inline' href='/palermo/where-to-eat-in-palermo/'>Palermo food guide</a>. For more on both markets as sights in their own right, see <a class='inline' href='/palermo/best-things-to-do-in-palermo/'>what to do in Palermo</a>."},
  {"t":"h2","text":"Day 2 — Monreale, the Cathedral & Teatro Massimo"},
  {"t":"p","html":"The big set-piece day. Go early for Monreale so you're back in the city with the whole afternoon still ahead."},
  {"t":"ol","items":[
    "Morning: bus or taxi out to <strong>Monreale Cathedral</strong>, about 8 km from the city — budget 2–3 hours there and back, more if you want the cloister too.",
    "Back in Palermo by early afternoon: lunch near the Cassaro or Quattro Canti.",
    "Spend the afternoon at <strong>Palermo Cathedral</strong> — the royal tombs, the meridian line, the treasury. The Palatine Chapel in the Norman Palace is a short walk away if you have the energy for one more UNESCO stop.",
    "End at <strong>Teatro Massimo</strong> — catch the late-afternoon light on the facade, take a guided tour, or book an evening performance if the schedule allows.",
  ]},
  {"t":"btnrow","btns":[
    {"program":"gyg","query":"Monreale Cathedral tour from Palermo","label":"Book the Monreale trip"},
    {"program":"gyg","query":"Teatro Massimo Palermo tour","label":"Book a Teatro Massimo tour","style":"btn-forest"},
  ]},
  {"t":"h2","text":"Day 3 — Mondello beach or a Cefalù day trip"},
  {"t":"p","html":"Two good, very different ways to close the trip. Pick by energy level, not guilt — both are the right answer."},
  {"t":"compare","head":["","Mondello","Cefalù"],
   "rows":[
     ["Distance","~20 minutes from central Palermo","~70 km east, about an hour by train"],
     ["Vibe","Belle Époque sandy bay, easy half-day","Norman cathedral, a beach, and one of Italy's prettiest old towns"],
     ["Pick this if...","You want to relax and be back in the city for a final dinner","You want one more real 'sight' before you leave"],
   ]},
  {"t":"p","html":"<strong>Mondello</strong> is reached through La Favorita park — bring the afternoon light and not much of a plan. <strong>Cefalù</strong> is a fuller day: its own Norman cathedral with Byzantine mosaics, a proper old town, and a beach if you save an hour for the sand."},
  {"t":"btnrow","btns":[
    {"program":"gyg","query":"Cefalu day trip from Palermo","label":"Book the Cefalù day trip"},
  ]},
  {"t":"h2","text":"Before you go"},
  {"t":"p","html":"Sort connectivity and insurance before you land, then walk or bus everywhere once you're here. See our full <a class='inline' href='/palermo/best-things-to-do-in-palermo/'>things-to-do guide</a> for more on every stop above."},
  {"t":"btnrow","btns":[
    {"program":"airalo","query":"italy","label":"Get an Italy eSIM (Airalo)"},
    {"program":"safetywing","label":"Travel insurance (SafetyWing)","style":"btn-forest"},
  ]},
  {"t":"warn","head":"Skip the rental car","html":"You won't need one for any of this — Monreale, Cefalù and Mondello are all reachable by bus, train or a booked tour, and Wikivoyage flags Palermo driving directly as \"quite dangerous as the rules of the road are not followed.\" Walk or bus centrally; only rent a car if you're extending the trip further afield."},
 ],
 "faq":[
   ("Is 3 days enough for Palermo?",
    "Yes — three days covers the full historic core, a proper market crawl through Ballarò and Vucciria, Monreale, the Cathedral, Teatro Massimo, and one more day trip or beach day. Add a fourth day if you want both Mondello and Cefalù rather than choosing."),
   ("What's the best order to see Palermo's sights in?",
    "Markets and old-town wandering first, while you're still getting oriented; Monreale and the Cathedral together on day two, since they're both morning-to-afternoon commitments; save the beach or Cefalù for last, as the natural wind-down."),
   ("Do I need a car for this itinerary?",
    "No. The historic core is walkable, Monreale and Cefalù are both reachable by bus, train or a booked tour, and Palermo's own driving conditions have a well-earned bad reputation. Save the rental car, if you want one, for trips further afield like Segesta."),
 ],
},

]
