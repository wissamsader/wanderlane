# -*- coding: utf-8 -*-
# DAMASCUS — one article: a dignified food & heritage guide.
# Sourced only from research/city-damascus.md (Section A eateries/slugs,
# Section B heritage/food culture, Section C travel-status note).
# This is a celebration, not a booking pitch: no hotel CTAs, no "book this
# tour" language on heritage sites, at most one soft eSIM/insurance mention,
# and a calm "check your own government's advisory" note before anything else.

CITY = {
 "id": "damascus",
 "intro_blocks": [
  {"t":"lead","html":"Damascus is one of the oldest continuously inhabited cities on earth — a claim it shares with only a handful of others, and earns as honestly as any of them. This guide is for its table: the ice cream still pounded by hand in the souq, the coffeehouse where a storyteller still reads aloud beside the Umayyad Mosque, the courtyard houses now serving fatteh instead of standing empty. It's written for the food and the culture, right now, and for the day the doors open wider."},
  {"t":"p","html":"Old Damascus is built around eating slowly and eating together. A real meal opens with mezze — small shared plates meant for a table of family and friends, not a solo diner — before kibbeh, fatteh or grilled meats arrive. Sweets are their own category: booza worked by hand, knafeh soaked in syrup, mabrouma and baklawa stacked behind glass counters that have been doing this since long before most of the world's cities looked anything like they do now. And running through nearly all of it is the coffeehouse — thick Arabic coffee, sweet tea, a nargileh, and in one particular café beside the mosque, a storyteller still reading from an old leather-bound book to a room of regulars."},
  {"t":"h2","text":"The tables to start with"},
  {"t":"eats","ranked":True,"items":[
    {"name":"Bakdash","slug":"bakdash","area":"Al-Hamidiyah Souq","blurb":"The legend of the souq, open since the 1880s — booza hand-pounded from mastic and salep until it stretches like taffy, served with clotted cream and pistachio. No delivery, no imitation."},
    {"name":"Al-Nawfara Café","slug":"nawfara","area":"Al-Qaymariyya","blurb":"Damascus's oldest café, tucked beside the Umayyad Mosque — tea or Arabic coffee with a nargileh while a hakawati storyteller reads aloud from an old leather-bound book."},
    {"name":"Beit Jabri","slug":"beit-jabri","area":"Old Damascus","blurb":"Fatteh, mezze and mixed grill inside an actual 1737 courtyard house, fountain included — one of the closest things to eating inside Old Damascus itself."},
    {"name":"Al-Beik Sweets","slug":"albeik","area":"Old Souq","blurb":"Knafeh that regulars call the best they've had anywhere, made with always-fresh bread and generous portions, tucked inside the old souq."},
    {"name":"Baron Hagop","slug":"baron-hakob","area":"Bab Touma","blurb":"An Armenian sujuk sandwich made with real patience by a family who'll tell you its history along with your order — the highest-rated table on this list."},
    {"name":"Al Qishla Café","slug":"qishla","area":"Al-Amin, Old Damascus","blurb":"Turkish coffee and nargileh inside a beautifully restored Damascene house — quiet, unshowy, entirely itself."},
    {"name":"Al-Manhal Bakery & Books","slug":"manhal","area":"Old Damascus","blurb":"Citron cake and coffee in a bakery-meets-bookshop — a modern concept with a genuinely Damascene spirit."},
    {"name":"Old Damascus Snack","slug":"old-damascus","area":"Straight Street","blurb":"Quick, honest street food eaten on the very street the Book of Acts calls 'Straight' — it's still called that today."},
  ]},
  {"t":"h2","text":"The old city"},
  {"t":"do","items":[
    {"name":"Umayyad Mosque","tag":"715 CE","blurb":"Completed by Caliph al-Walid I on the site of a Roman temple and, before that, a Byzantine cathedral — one of the oldest and largest mosques on earth, and still the city's spiritual and civic heart."},
    {"name":"Souq al-Hamidiyya","tag":"Since ~1780","blurb":"The great covered market, laid along the line of an old Roman colonnaded road straight toward the mosque — and the address for Bakdash and several more of the tables above."},
    {"name":"Straight Street","tag":"Via Recta","blurb":"The Roman-era main street named in the Book of Acts, where Saint Paul is said to have stayed — split today into Midhat Pasha Street and Bab Sharqi Street."},
    {"name":"Azem Palace","tag":"Built 1749","blurb":"An Ottoman governor's residence in banded black-and-white stone, now the Museum of Arts and Popular Traditions."},
    {"name":"Damascene courtyard houses","tag":"Old City architecture","blurb":"A plain street wall hiding a private courtyard, fountain and citrus trees — the city's signature domestic style. Some of the finest survivors, including Beit Jabri and Al Qishla Café above, now serve meals rather than standing empty."},
    {"name":"Mount Qasioun","tag":"1,151m","blurb":"The hill overlooking the whole city, lined with view restaurants and layered in local lore, including the Cave of the Seven Sleepers referenced in both early Christian sources and the Quran."},
  ]},
  {"t":"warn","head":"Before you go","html":"Official travel advisories for Syria vary by country and change over time — this guide doesn't make that call for you. Check your own government's current advisory immediately before making any plans (for example gov.uk/foreign-travel-advice/syria, travel.gc.ca, or travel.state.gov, or the equivalent for your own country). We don't offer security, entry or logistics advice here — that judgment belongs to you and your own government's current guidance, not to a food and heritage guide."},
  {"t":"p","html":"None of this is a pitch. It's a record of a real place — the mosque, the souq, the sweets counter, the courtyard fountain — kept the way it deserves to be kept, whether you're reading from Damascus itself, from a diaspora kitchen thousands of miles away, or from simple curiosity. If a trip becomes realistic for you one day, the ordinary practicalities of travel — an international eSIM, travel insurance — will exist the same as they do anywhere; this isn't the place selling them to you. For the full spread, from Bakdash's booza to the hakawati's storyteller, read <a class='inline' href='/damascus/the-tables-of-damascus/'>The Tables of Damascus</a>."},
 ],
 "faq": [
  ("What is Damascus famous for, food-wise?",
   "Damascus is one of the great food cities of the Levant: mezze culture, kibbeh, fatteh, shawarma judged by the spit and the bread, and a sweets tradition running from Bakdash's hand-pounded booza to knafeh and mabrouma on old confectionery counters — most of it centered on Souq al-Hamidiyya and the streets around the Umayyad Mosque."),
  ("Can you travel to Damascus right now?",
   "That's a question only your own government's current travel advisory can answer — it varies by country and changes over time. As of this guide's writing in mid-2026, official advisories including the UK's and Canada's caution against travel to Syria; check your own foreign ministry's page (gov.uk/foreign-travel-advice/syria, travel.gc.ca, travel.state.gov, or the equivalent) before making any plans. This guide celebrates Damascus's food and heritage — it isn't advice on whether or how to travel there."),
  ("What is Bakdash?",
   "Bakdash is Damascus's legendary ice cream house in Souq al-Hamidiyya, open since the 1880s. Its booza — mastic-and-salep ice cream hand-pounded to a stretchy, chewy texture — is served with clotted cream (ashta) and crushed pistachio, made the same way, in full view of the queue, for well over a century."),
 ],
}

PAGES = [

# ============================================================ THE TABLES OF DAMASCUS
{
 "city":"damascus", "slug":"the-tables-of-damascus", "order":1,
 "title":"The Tables of Damascus: A Food & Heritage Guide",
 "kicker":"Damascus · Food & heritage",
 "dek":"Booza pounded by hand since the 1880s, a storyteller still reading aloud beside the Umayyad Mosque, and old-city kitchens keeping Damascene cooking alive — a food and heritage guide, not a booking pitch.",
 "description":"A respectful Damascus food and heritage guide: Bakdash's hand-pounded booza, Old City coffeehouses, Damascene mezze, kibbeh and knafeh since the 1880s.",
 "read":"11 min", "updated":"July 2026",
 "related":[],
 "blocks":[
  {"t":"lead","html":"This is a love letter to a table, not a travel pitch. Damascus has been feeding people for longer than almost anywhere on earth, and the kitchens, sweets counters and coffeehouses below are still doing it — for locals, for a shrinking number of visitors, and for anyone reading from a diaspora kitchen far away."},
  {"t":"h2","text":"The tables, ranked"},
  {"t":"p","html":"Fifteen real Old Damascus addresses, led by the flagship, then the direct heritage-tied picks, then by how strongly reviewers and regulars vouch for them."},
  {"t":"eats","ranked":True,"items":[
    {"name":"Bakdash","slug":"bakdash","area":"Al-Hamidiyah Souq","blurb":"Open since the 1880s and still the legend of the souq — booza pounded by hand from mastic and salep until it stretches like taffy, served with clotted cream (ashta) and crushed pistachio. No delivery, no imitation, no changes to the method."},
    {"name":"Al-Nawfara Café","slug":"nawfara","area":"Al-Qaymariyya","blurb":"Damascus's oldest café, right beside the Umayyad Mosque — thick Arabic coffee or sweet tea, a nargileh, and most evenings, a hakawati reading aloud from an old leather-bound book to a room of regulars."},
    {"name":"Beit Jabri","slug":"beit-jabri","area":"Old Damascus","blurb":"Fatteh, mezze and mixed grill inside a real 1737 courtyard house, fountain and all — one of the most complete ways to actually sit inside Old Damascus rather than just walk through it."},
    {"name":"Al-Beik Sweets","slug":"albeik","area":"Old Souq","blurb":"Knafeh that regulars call the best they've had anywhere, made with always-fresh bread and no shortcuts, a short walk inside the old souq."},
    {"name":"Baron Hagop","slug":"baron-hakob","area":"Bab Touma","blurb":"The highest-rated table on this whole list: an Armenian sujuk sandwich made with real patience by a family who'll tell you the history behind it while you wait."},
    {"name":"Al Qishla Café","slug":"qishla","area":"Al-Amin, Old Damascus","blurb":"Turkish coffee and nargileh inside a beautifully restored Damascene house — reviewers say it 'screams Damascus so quietly.'"},
    {"name":"Haretna","slug":"haretna","area":"Bab Touma","blurb":"Grills, mezze and shisha in a historic Bab Touma courtyard — reviewers call it 'a true classic in Old Damascus.'"},
    {"name":"Al-Manhal Bakery & Books","slug":"manhal","area":"Old Damascus","blurb":"Citron cake and coffee in a bakery-meets-bookshop — a modern concept with a genuinely Damascene spirit, and a personal pick from our own contact in the city."},
    {"name":"Al-Burj Shawarma","slug":"elburj","area":"Qassaa","blurb":"Chicken or lamb shawarma by the sandwich or the kilo, five minutes from the Bab Touma gate — the corner locals actually send visitors to."},
    {"name":"Omaya Ice Cream","slug":"omaya-ice","area":"Old Damascus","blurb":"The Old City's other great ice cream house: a wide flavor range and fresh juice, easy to fold into a walk through the souq."},
    {"name":"Nubar Avedis Golfayan","slug":"nubar","area":"Qassaa","blurb":"Armenian sujuk and basterma cured the same way for generations — regulars describe the quality as unchanged for more than thirty years."},
    {"name":"Selena","slug":"selena","area":"Bab Touma","blurb":"Khaberniya and shish tawook beside a courtyard fountain — a relaxed, quietly romantic Old Damascus room."},
    {"name":"Old Damascus Snack","slug":"old-damascus","area":"Straight Street","blurb":"Quick, honest street food eaten on the very street the Book of Acts calls 'Straight' — it's still called that today."},
    {"name":"Al Wesam Sweets","slug":"wissam-conf","area":"Qassaa","blurb":"Knafeh nabulsiyeh, mabrouma and a full Damascene sweets counter made properly, with samneh (clarified butter) instead of shortcuts."},
    {"name":"Kahwet Almafraq","slug":"almafraq","area":"Al-Qaymariyya","blurb":"Coffee with Fairuz on the speakers, tucked into a lane in Al-Qaymariyya — small, unhurried, exactly what an Old City coffee break should feel like."},
  ]},
  {"t":"h2","text":"The dishes that define the table"},
  {"t":"ul","items":[
    "<strong>Damascene mezze</strong> — the ritual of small shared plates (hummus, mutabbal, fattoush, kibbeh nayyeh) that opens a real meal, built for a table of family and friends, not a solo diner.",
    "<strong>Kibbeh</strong> — bulgur worked with minced lamb and spices into torpedoes, patties or baked trays; Syria's most-cited signature dish, and a point of real regional pride and rivalry.",
    "<strong>Fatteh</strong> — toasted or fried flatbread layered under yogurt or tahini, chickpeas, or chicken; a Damascus breakfast or shared starter, and on the menu at Beit Jabri above.",
    "<strong>Shawarma</strong> — meat shaved from a vertical spit into fresh bread; a Damascus street-food backbone long before it became a global export, still judged locally by the spit and the bread, not the sauce.",
  ]},
  {"t":"h2","text":"Bakdash, booza and the sweets counter"},
  {"t":"p","html":"Bakdash has been doing one thing since the 1880s: booza, Damascus's own frozen dessert, made from mastic and salep (ground orchid root) and worked by hand until it stretches and resists melting — pounded to order in full view of the queue in the souq. It's the anchor of a much bigger sweets tradition. Knafeh — shredded pastry or semolina over soft cheese, soaked in syrup — sits alongside mabrouma and baklawa on old confectionery counters that were already refining this craft under the Umayyads. Even the rosewater running through half of it has the city's name on it: the damask rose, Rosa × damascena, takes its Western name directly from Damascus."},
  {"t":"compare","head":["Sweet","Where to try it","What makes it different"],
   "rows":[
     ["<strong>Booza</strong>","Bakdash, in the souq","Mastic and salep worked by hand until it stretches and resists melting — pounded to order in full view of the queue."],
     ["<strong>Knafeh</strong>","Al-Beik Sweets or Al Wesam Sweets","Shredded pastry or semolina over soft cheese, soaked in syrup — Al-Beik's is the version reviewers single out most."],
     ["<strong>Mabrouma &amp; baklawa</strong>","Al Wesam Sweets and the old confectionery counters","Layered, syrup-soaked pastries made with samneh (clarified butter) — the rest of the classic sweets counter."],
     ["<strong>Rosewater</strong>","Woven through syrups and drinks citywide","The damask rose (Rosa × damascena) takes its Western name from Damascus itself."],
   ],
   "cap":"The sweets counter is an everyday institution here, not a special-occasion trip — that's exactly why it works."},
  {"t":"h2","text":"Old-city coffeehouses & the hakawati"},
  {"t":"p","html":"Slow tea or Arabic coffee and a nargileh are their own ritual here, and no address does it better than Al-Nawfara, Damascus's oldest café, tucked beside the Umayyad Mosque. It's historically also home to the hakawati — a professional storyteller who recites serialized tales from an old leather-bound book to a room of regulars, most evenings, in what might be the most human, most alive version of the city you can sit inside. Al Qishla Café and Kahwet Almafraq keep the same spirit in quieter old-city lanes — one inside a restored Damascene house, the other with Fairuz on the speakers."},
  {"t":"h2","text":"Where all of this happens"},
  {"t":"h3","text":"Souq al-Hamidiyya"},
  {"t":"p","html":"Almost everything above sits inside or beside Souq al-Hamidiyya, Damascus's great covered market, built from around 1780 under the Ottoman sultans Abdul Hamid I and II. It runs roughly 600 meters along the line of an old Roman colonnaded road, straight toward the Umayyad Mosque — and it's the address for Bakdash and several more of the eats above."},
  {"t":"h3","text":"The Umayyad Mosque"},
  {"t":"p","html":"The mosque itself was completed in 715 CE by Caliph al-Walid I, on the site of a Roman Temple of Jupiter and, before that, a Byzantine cathedral. It's one of the oldest and largest mosques in the world, and its basilical plan and gold mosaics shaped mosque architecture across the Islamic world — it remains the spiritual and civic heart of the city today."},
  {"t":"h3","text":"Straight Street"},
  {"t":"p","html":"A few minutes' walk away is Straight Street — the Roman and Seleucid-era main street, 'the street called Straight' from the Book of Acts, where Saint Paul is said to have stayed and later escaped the city. It's split today into Midhat Pasha Street (the souq side) and Bab Sharqi Street (toward the Eastern Gate); Old Damascus Snack sits directly on it."},
  {"t":"h3","text":"Courtyard houses & Azem Palace"},
  {"t":"p","html":"Old Damascus's signature architecture is the courtyard house — a plain street wall hiding a private courtyard, fountain and citrus trees. Several of the finest survivors, including Beit Jabri and Al Qishla Café above, have been turned into restaurants and cafés rather than left empty, which is as good a way as any to actually experience one. The grandest version open to the public is Azem Palace, an Ottoman governor's residence built in 1749 in banded black-and-white stone, now the Museum of Arts and Popular Traditions."},
  {"t":"h3","text":"Mount Qasioun"},
  {"t":"p","html":"For the view over all of it, Mount Qasioun rises 1,151 meters over the city, lined with restaurants and layered in local lore — including the Cave of the Seven Sleepers, referenced in both early Christian sources and the Quran."},
  {"t":"warn","head":"Before you go","html":"Official travel advisories for Syria vary by country and change over time — this page doesn't make that call for you. Check your own government's current advisory before making any plans (gov.uk/foreign-travel-advice/syria, travel.gc.ca, travel.state.gov, or your own country's equivalent), and treat this guide as a record of Damascus's food and heritage, not as travel, entry or safety advice."},
  {"t":"callout","head":"Why this guide exists","html":"Damascus's food and heritage are real and worth documenting whether or not a given reader can visit in person right now. This is written for people with Damascene roots abroad, for cooks and researchers, for anyone who loves this city from a distance — and for the day the doors open wider. It's a record, not a pitch."},
 ],
 "faq":[
   ("What is the signature dish of Damascus?",
    "There isn't just one — a real Damascene meal opens with mezze (small shared plates like hummus, mutabbal and fattoush) before kibbeh arrives: bulgur worked with minced lamb and spices into torpedoes or patties. Kibbeh is Syria's most-cited signature dish and a genuine point of regional pride."),
   ("What is booza, and how is it different from regular ice cream?",
    "Booza is Damascus's own frozen dessert, made from mastic and salep (ground orchid root) and worked by hand until it stretches and resists melting — a much chewier, denser texture than Western ice cream. Bakdash, open since the 1880s in Souq al-Hamidiyya, is the address that made it famous, pounding it to order in full view of the queue."),
   ("What is a hakawati?",
    "A hakawati is a traditional Arab storyteller who recites serialized tales aloud from an old leather-bound book to a café full of regulars. Al-Nawfara, Damascus's oldest café beside the Umayyad Mosque, is one of the last places keeping the tradition alive, most evenings."),
 ],
},

]
