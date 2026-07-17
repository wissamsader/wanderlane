# -*- coding: utf-8 -*-
# DA NANG & HOI AN — three deeper guides: stays, things to do, and a 4-day
# itinerary. Extends vietnam.py (which owns the CITY hub + the food guide).
# Same data-integrity rules apply: our own stays are Da Nang only
# (kon-tiki-hostel, nha-bo-homestay) — Hoi An has zero listings in our own
# network, so Hoi An content here is honest general knowledge, never an
# invented vendor name. Named hotels are limited to the [H]/[M]-confidence
# picks from research/city-vietnam.md (Furama, InterContinental Danang,
# Anantara Hoi An) — the [L]-confidence picks were dropped, not guessed at.
# (July 2026 research; see research/city-vietnam.md for source + confidence.)

PAGES = [

# ============================================================ WHERE TO STAY
{
 "city":"vietnam", "slug":"where-to-stay-da-nang-hoi-an", "order":2,
 "title":"Where to Stay in Da Nang & Hoi An",
 "kicker":"Da Nang & Hoi An · Where to stay",
 "dek":"Two cities, six real neighborhoods, and the five hostels, homestays and resorts we can actually vouch for — budget to splurge.",
 "description":"An honest guide to where to stay in Da Nang and Hoi An — the best areas in both cities, plus five real hostels, homestays and resorts worth booking.",
 "read":"8 min", "updated":"July 2026",
 "related":["where-to-eat-in-da-nang","best-things-to-do-da-nang-hoi-an"],
 "blocks":[
  {"t":"lead","html":"Da Nang and Hoi An are about 45 minutes apart by road, which makes where you sleep less a logistics question and more a choice between two different trips: a beach city with a growing nomad scene, or a UNESCO lantern town you can walk end to end. Most people do both — the only real question is which one gets your nights."},
  {"t":"h2","text":"Six areas, two cities"},
  {"t":"compare","head":["Area","City","Best for","Heads-up"],
   "rows":[
     ["<strong>My Khe Beach</strong>","Da Nang","Beach-first stays, resort towers, water sports","The busiest, most built-up strip"],
     ["<strong>An Thuong</strong>","Da Nang","Cafés, bars, coworking, the nomad crowd","A short walk inland — not beachfront itself"],
     ["<strong>City center / Han River</strong>","Da Nang","Food-focused stays near Dragon Bridge & the markets","Less beachy, more urban"],
     ["<strong>Ancient Town</strong>","Hoi An","Walkable, lantern-lit, everything on foot","Touristy, and the first area to flood Oct–Nov"],
     ["<strong>An Bang Beach</strong>","Hoi An","A quieter beach base, café strip on the sand","4–5km from the Ancient Town — taxi or cycle in"],
     ["<strong>Cam Thanh</strong>","Hoi An","Rural, coconut-village, basket boats on your doorstep","Best with your own scooter or bike"],
   ],
   "cap":"First trip and want both cities easy to reach? Base in Da Nang. Want the Ancient Town at your doorstep after dark — worth it for the lantern hours alone? Base in Hoi An itself."},
  {"t":"h2","text":"Da Nang: budget to splurge"},
  {"t":"p","html":"Our own picks are both here — a hostel and a homestay in An Hai, the residential pocket between the Han River and My Khe beach — plus two long-established beach resorts if you'd rather spend more."},
  {"t":"stays","items":[
    {"name":"Kon-Tiki Hostel","area":"An Hai, Da Nang","band":"$6–15","program":"hostelworld","query":"Kon Tiki Hostel Da Nang",
     "blurb":"The sociable budget pick: a 4.4★ hostel an easy walk from both the river and the beach. Dorms, a bar, and the easiest way to meet other travelers doing the same Da Nang–Hoi An loop."},
    {"name":"Nhà Bơ Homestay","area":"An Hai, Da Nang","band":"$15–30","program":"booking","query":"Nha Bo Homestay Da Nang",
     "blurb":"Quieter and more personal than a hostel — a 4.9★ homestay in the same pocket of An Hai, for a warm welcome over a party atmosphere, still a short walk to the sand."},
    {"name":"Furama Resort Danang","area":"My Khe Beach, Da Nang","band":"$90–160","program":"booking","query":"Furama Resort Danang",
     "blurb":"One of Vietnam's original beachfront five-stars, open on the main My Khe strip since the late 1990s — a long operating history if you want a proper resort without the top-end price."},
    {"name":"InterContinental Danang Sun Peninsula Resort","area":"Son Tra Peninsula, Da Nang","band":"$300+","program":"agoda","query":"InterContinental Danang Sun Peninsula Resort",
     "blurb":"Bill Bensley's flagship: a private-beach resort on its own peninsula, grand enough to have hosted the APEC 2017 leaders' summit. The splurge pick, and it looks the part."},
  ]},
  {"t":"book","head":"Compare Da Nang stays","html":"Agoda and Booking both have deep coverage of the My Khe and An Thuong strips — worth checking the same room on both before you commit.","program":"agoda","query":"Da Nang","label":"Check Da Nang hotels on Agoda"},
  {"t":"h2","text":"Hoi An: the one we can vouch for, and how to pick the rest"},
  {"t":"p","html":"Our own network doesn't reach into Hoi An town yet, so we're not going to invent names just to fill a list — the advice below is what we'd actually tell a friend."},
  {"t":"stays","items":[
    {"name":"Anantara Hoi An Resort","area":"Riverside, Hoi An","band":"$120–200","program":"agoda","query":"Anantara Hoi An Resort",
     "blurb":"A French-colonial-style riverside resort that's genuinely walkable to the Ancient Town — rare for something this size. The easy, reliable Hoi An choice if you'd rather not gamble on a small guesthouse."},
  ]},
  {"t":"tip","head":"For the Ancient Town, An Bang or Cam Thanh","html":"The Ancient Town has a real cluster of small courtyard boutique hotels, An Bang has beachfront guesthouses, and Cam Thanh has a handful of homestays among the rice paddies — all of them turn over too fast for us to hard-code a single 'best' pick here. Search Agoda or Booking directly for your dates, sort by rating, and skim recent reviews for any mention of flooding if you're traveling Oct–Nov."},
  {"t":"warn","head":"Booking Oct–Nov? Go for higher ground","html":"Hoi An's Ancient Town floods most years in that window — river water has reached several blocks up from the riverside in recent seasons, and ground-floor rooms are the first affected. If your dates fall here, favor upper floors or a stay just outside the immediate riverside, and keep your booking's cancellation policy flexible."},
  {"t":"p","html":"Once you've picked a base, see our <a class='inline' href='/vietnam/best-things-to-do-da-nang-hoi-an/'>things to do guide</a> for what to fill your days with, or jump straight to our <a class='inline' href='/vietnam/da-nang-hoi-an-itinerary/'>4-day itinerary</a> if you'd rather it was mapped out already."},
  {"t":"btnrow","btns":[
     {"program":"agoda","query":"Da Nang","label":"Check Da Nang on Agoda"},
     {"program":"booking","query":"Hoi An","label":"Check Hoi An on Booking","style":"btn-forest"},
  ]},
 ],
 "faq":[
   ("Should I stay in Da Nang or Hoi An?",
    "Da Nang if you want the beach, a bigger food scene, and an easy airport run — every flight into the region lands here. Hoi An if the lantern-lit Ancient Town is the whole point and you don't mind a taxi or scooter for everything else. Splitting your nights, two or three in each, is genuinely the best answer if you have the time."),
   ("Is Kon-Tiki Hostel or Nhà Bơ Homestay the better pick?",
    "Depends what you want from a stay. Kon-Tiki (4.4★) is the sociable budget option — dorms, a bar, an easy way to meet other travelers. Nhà Bơ (4.9★) is quieter and more personal, a proper homestay rather than a hostel, for a similar walk to My Khe beach. Both sit in An Hai, between the river and the sand."),
   ("Where should I stay to be close to Hoi An's Ancient Town at night?",
    "Book inside or immediately next to the Ancient Town itself — that's what buys you the motorbike-free, lantern-lit streets after dark without a taxi home. An Bang Beach is the trade-off pick: quieter and right on the sand, but 4–5km out, so you'll cycle or taxi in for the evening lantern walk."),
 ],
},

# ============================================================ THINGS TO DO
{
 "city":"vietnam", "slug":"best-things-to-do-da-nang-hoi-an", "order":3,
 "title":"Best Things to Do in Da Nang & Hoi An",
 "kicker":"Da Nang & Hoi An · Do",
 "dek":"Lantern-lit lanes, a record-length cable car, marble caves, Champa ruins and a spin around a coconut village in a basket boat.",
 "description":"The best things to do in Da Nang and Hoi An: Ancient Town lanterns, the Golden Bridge, Marble Mountains, My Son ruins and Cam Thanh's basket boats.",
 "read":"10 min", "updated":"July 2026",
 "related":["where-to-stay-da-nang-hoi-an","where-to-eat-in-da-nang"],
 "blocks":[
  {"t":"lead","html":"Da Nang and Hoi An sit 45 minutes apart and don't feel like they belong to the same trip — one's a beach city with cable cars and marble caves, the other's a UNESCO lantern town you can walk end to end. You could spend a week between them without repeating a day. This is the honest shortlist: what earns its spot, what to book ahead, and what you just turn up for."},
  {"t":"h2","text":"Hoi An's Ancient Town, the reason people come"},
  {"t":"do","items":[
    {"name":"Hoi An Ancient Town & Lantern Night","tag":"UNESCO · free to explore","program":None,
     "blurb":"Wander the 15th–19th-century shophouses by day, then come back after dark: the core goes motorbike-free and lantern-lit every evening, and it's especially vivid on the monthly Lantern Festival — the 14th day of the lunar month, when locals switch off electric lighting along the river."},
    {"name":"Japanese Covered Bridge","tag":"Hoi An's icon","program":None,
     "blurb":"A short wooden bridge built in the early 1600s to link the old Japanese and Chinese trading quarters — a small entry fee, five minutes to see, and on every Ancient Town photo you'll have seen before you arrive."},
  ]},
  {"t":"h2","text":"The three to book ahead"},
  {"t":"p","html":"These three sell out their best time slots in high season — book online rather than turning up and hoping."},
  {"t":"do","items":[
    {"name":"Ba Na Hills & the Golden Bridge","tag":"Book ahead","program":"klook","query":"Ba Na Hills Golden Bridge Da Nang","label":"Book Ba Na Hills tickets",
     "blurb":"A French colonial-era hill station at 1,500m, reached by a cable car that held the world length record. The Golden Bridge — held up by two giant stone hands — is the most photographed thing in central Vietnam, and heavily oversubscribed; a combo ticket bought ahead skips a real chunk of the queue."},
    {"name":"My Son Sanctuary","tag":"Half-day tour","program":"gyg","query":"My Son Sanctuary tour","label":"Book a My Son tour",
     "blurb":"Ruined 4th–13th-century Hindu temples of the Champa kingdom, UNESCO-listed and about 36km south of Hoi An — smaller in scale than Angkor but the same jungle-ruin atmosphere. Almost everyone goes as a guided half-day; a sunrise departure beats both the heat and the tour-bus crowds."},
    {"name":"Cam Thanh Basket Boat Tour","tag":"Coconut village","program":"klook","query":"Cam Thanh basket boat tour Hoi An","label":"Book the basket boat tour",
     "blurb":"A spin around Cam Thanh's coconut-palm water village in a round bamboo basket boat — the rower usually spins you in circles and calls it a 'basket-boat dance.' Most tours bundle it with a bike ride through the surrounding rice paddies."},
  ]},
  {"t":"h2","text":"Marble Mountains"},
  {"t":"do","items":[
    {"name":"Marble Mountains","tag":"Ngu Hanh Son","program":None,
     "blurb":"Five marble-and-limestone hills just outside Da Nang, each named for one of the five elements, honeycombed with caves holding Buddhist and Hindu shrines — Huyen Khong Cave and Tam Thai Temple are the two not to miss. It's 156 steps to the top, or take the elevator if the heat's already winning."},
  ]},
  {"t":"h2","text":"Two beaches, two moods"},
  {"t":"do","items":[
    {"name":"My Khe Beach","tag":"Da Nang","program":None,
     "blurb":"The wide, resort-lined urban beach — sun loungers, water sports, and a proper stretch of sand right inside the city."},
    {"name":"An Bang Beach","tag":"Hoi An","program":None,
     "blurb":"Smaller and slower, a few kilometers from the Ancient Town — a café strip that spills onto the sand, and the beach of choice for anyone staying more than a couple of nights."},
  ]},
  {"t":"h2","text":"Hands-on Hoi An: cooking, lanterns, tailoring"},
  {"t":"do","items":[
    {"name":"Cooking Class & Lantern-Making","tag":"Half-day, hands-on","program":"gyg","query":"Hoi An cooking class","label":"Book a cooking class",
     "blurb":"Riverside schools run half-day classes that start with a market walk and end with you cooking cao lầu and bánh xèo yourself. Many pair the same afternoon with a lantern-making workshop — ask when you book if you want both in one session."},
    {"name":"Tailoring in Hoi An","tag":"1–3 days, book early","program":None,
     "blurb":"Hoi An has 400+ tailor shops that can turn around a custom suit or dress in a day or two, roughly $49–150+ depending on garment and fabric. Get measured in your first day or two in town, not your last — a second fitting makes a real difference, and you need the days to spare."},
  ]},
  {"t":"tip","head":"Time it with the Lantern Festival if you can","html":"The Full Moon Lantern Festival falls on the 14th day of every lunar month — locals switch off electric lighting along the river in the Ancient Town and it runs on candlelit lanterns alone. Check the lunar date against your trip; it's worth shuffling a day or two to catch it."},
  {"t":"book","head":"The ones worth pre-booking","html":"Ba Na Hills, My Son, the basket boat tour and the cooking classes are the things that actually sell out — everything else here you can decide on the day.","program":"klook","query":"Da Nang Hoi An","label":"Browse Da Nang & Hoi An experiences"},
  {"t":"p","html":"Need somewhere to sleep between all this? Our <a class='inline' href='/vietnam/where-to-stay-da-nang-hoi-an/'>Da Nang & Hoi An stays guide</a> covers both cities, or follow our <a class='inline' href='/vietnam/da-nang-hoi-an-itinerary/'>4-day itinerary</a> for a day-by-day plan that fits most of this in."},
 ],
 "faq":[
   ("Is Ba Na Hills and the Golden Bridge worth it?",
    "Yes, if you book ahead and go early — it's genuinely spectacular and the cable car alone is worth the trip. The catch is crowds: it's the single most oversubscribed thing in the region, so a combo ticket bought online in advance is worth far more here than at most attractions."),
   ("What's the best thing to do in Hoi An at night?",
    "Walk the Ancient Town after dark. The streets close to motorbikes, lanterns replace streetlight, and it's at its most atmospheric during the monthly Lantern Festival — the 14th day of the lunar month, when the riverside runs on candlelight alone."),
   ("Do I need to book My Son Sanctuary or the basket boat tour in advance?",
    "Both are almost always done as guided tours rather than solo visits, and in high season the best time slots — especially My Son's sunrise departures — do sell out. Booking a day or two ahead through Klook or GetYourGuide is safer than assuming you can walk up."),
 ],
},

# ============================================================ ITINERARY
{
 "city":"vietnam", "slug":"da-nang-hoi-an-itinerary", "order":4,
 "title":"Da Nang & Hoi An: A 4-Day Itinerary",
 "kicker":"Da Nang & Hoi An · Itinerary",
 "dek":"Two nights in each city, the transfer built in rather than bolted on, and every stop pulled from what we actually recommend.",
 "description":"A 4-day Da Nang and Hoi An itinerary: beach and food, Marble Mountains and Ba Na Hills, the Ancient Town by lantern light, and My Son Sanctuary.",
 "read":"9 min", "updated":"July 2026",
 "related":["where-to-stay-da-nang-hoi-an","best-things-to-do-da-nang-hoi-an","where-to-eat-in-da-nang"],
 "blocks":[
  {"t":"lead","html":"Four days is enough to get a real feel for both cities without rushing every stop into a blur. This is the order we'd actually do it in — two nights in Da Nang, two in Hoi An, with the 45-minute transfer between them built into the plan rather than eaten as a travel day."},
  {"t":"h2","text":"Before you land"},
  {"t":"ul","items":[
    "<strong>eSIM:</strong> land already online rather than hunting for a SIM counter — set it up before you fly.",
    "<strong>Travel insurance:</strong> worth having in place before you touch a scooter or a cable car, not after.",
    "<strong>Cash:</strong> VND still rules street food and markets in both cities — don't count on cards outside hotels and bigger restaurants.",
    "<strong>Grab app:</strong> install it before you land — the easiest way to move around both cities, and the cheapest way to do the inter-city hop yourself.",
  ]},
  {"t":"btnrow","btns":[
     {"program":"airalo","query":"vietnam","label":"Get a Vietnam eSIM (Airalo)"},
     {"program":"safetywing","label":"Travel insurance (SafetyWing)","style":"btn-forest"},
  ]},
  {"t":"h2","text":"The 4 days at a glance"},
  {"t":"compare","head":["Day","Base","The plan"],
   "rows":[
     ["<strong>Day 1</strong>","Da Nang","Beach morning, Da Nang food, Han River evening"],
     ["<strong>Day 2</strong>","Da Nang","Marble Mountains, then Ba Na Hills & the Golden Bridge"],
     ["<strong>Day 3</strong>","Hoi An","Transfer in, Ancient Town by day and by lantern light"],
     ["<strong>Day 4</strong>","Hoi An","My Son Sanctuary half-day, then Cam Thanh's basket boats"],
   ],
   "cap":"Stretch this to 5–6 days by adding a slow beach day at An Bang or a cooking class — see the tip below."},
  {"t":"h2","text":"Day 1 — Da Nang: beach and food"},
  {"t":"p","html":"Start at My Khe beach while it's still cool, then walk or Grab into An Thuong for coffee. Spend the afternoon around the city center — the Dragon Bridge breathes fire and water on weekend evenings, worth timing for — before dinner at <a class='inline' href='/vietnam/where-to-eat-in-da-nang/'>Bánh Xèo Bà Dưỡng or Bún Chả Cá 109</a>, both real, both worth the walk down the alley. Sleep in An Hai or on the My Khe strip itself; see our <a class='inline' href='/vietnam/where-to-stay-da-nang-hoi-an/'>Da Nang & Hoi An stays guide</a> for specific picks."},
  {"t":"h2","text":"Day 2 — Marble Mountains and Ba Na Hills"},
  {"t":"p","html":"Morning at the Marble Mountains — climb or take the elevator up, duck into Huyen Khong Cave and Tam Thai Temple, and you're done in two to three hours. Then head up to Ba Na Hills for the record-length cable car and the Golden Bridge; go in the afternoon once the morning tour buses thin out. Full detail, plus everything else worth doing, is in our <a class='inline' href='/vietnam/best-things-to-do-da-nang-hoi-an/'>things to do guide</a>."},
  {"t":"book","head":"Book Ba Na Hills ahead","html":"It's the single most oversubscribed thing in the region — a combo ticket bought in advance skips a real chunk of the queue.","program":"klook","query":"Ba Na Hills Golden Bridge Da Nang","label":"Book Ba Na Hills tickets"},
  {"t":"h2","text":"Day 3 — Into Hoi An: the Ancient Town by lantern light"},
  {"t":"p","html":"Da Nang and Hoi An are only about 45 minutes apart along a genuinely scenic coastal route, so this isn't really a travel day — check out, transfer, and you're wandering the Ancient Town by lunchtime. Spend the afternoon on the 15th–19th-century shophouses and the Japanese Covered Bridge, get measured for anything you want tailored (do it now, not your last night — you'll want time for a second fitting), then come back out after dark, when the core goes motorbike-free and lantern-lit."},
  {"t":"book","head":"Book the Da Nang → Hoi An transfer","html":"12Go compares transfers, shuttles and private cars on this route in English, with instant e-tickets.","program":"12go","target":"https://12go.asia/en/travel/da-nang/hoi-an","label":"Check Da Nang → Hoi An transfers"},
  {"t":"h2","text":"Day 4 — My Son Sanctuary and Cam Thanh's basket boats"},
  {"t":"p","html":"Go early for My Son Sanctuary — a sunrise or morning half-day tour beats both the heat and the crowds at these 4th–13th-century Champa ruins, about 36km from Hoi An. Back in town by early afternoon for Cam Thanh: a round bamboo basket boat spin through the coconut-palm water village, usually bundled with a bike ride through the rice paddies. Spend your last evening on Hoi An's own dishes — cao lầu, white rose dumplings, bánh mì Phượng — covered in full in our <a class='inline' href='/vietnam/where-to-eat-in-da-nang/'>food guide</a>."},
  {"t":"book","head":"Book My Son ahead in high season","html":"Sunrise and early-morning departures are the ones that sell out first.","program":"gyg","query":"My Son Sanctuary tour","label":"Book a My Son tour"},
  {"t":"tip","head":"Have 5–6 days instead of 4?","html":"Add a slow day at An Bang Beach, a half-day cooking class (often paired with lantern-making), or a scooter loop back in Da Nang before you fly out. None of it needs booking weeks ahead except the cooking class in peak season."},
  {"t":"warn","head":"Traveling October–November? Read this first","html":"Hoi An floods most years in that window — river water has reached several blocks up from the riverside into the Ancient Town in recent seasons, and ground-floor rooms are the first affected. It's not a rare-disaster scenario, it's a seasonal pattern locals plan around. If your dates fall here, book accommodation on higher ground, keep the itinerary loose, and accept that a day might get rearranged around the weather."},
 ],
 "faq":[
   ("Is 4 days enough for Da Nang and Hoi An?",
    "It's enough to hit the highlights of both without feeling rushed — two nights each, with the transfer built in rather than eating a whole day. Add a day or two if you want a slow beach day, a cooking class, or want to fit in Son Tra Peninsula."),
   ("Should you visit Da Nang or Hoi An first?",
    "Da Nang first is the easier order — you'll land at Da Nang International Airport regardless, so starting there means no backtracking, and you end the trip on Hoi An's slower pace instead of rushing out of it for a flight."),
   ("How do you get from Da Nang to Hoi An?",
    "About 45 minutes by road along a scenic coastal route. Grab is the simplest option for doing it yourself, and a private transfer booked ahead on 12Go is the easiest way to arrange it in advance — see the transfer link on Day 3 above."),
 ],
},

]
