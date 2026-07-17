# -*- coding: utf-8 -*-
# DA NANG & HOI AN — Vietnam pair. 1 deep guide (food) + a portal hub.
# Da Nang eats/stays are our real, photographed business data (banh-xeo-ba-duong,
# bun-cha-ca-109, kon-tiki-hostel, nha-bo-homestay). Hoi An content is honest
# general knowledge — named by dish/reputation only, no invented vendor slugs.
# (July 2026 research; see research/city-vietnam.md for source + confidence notes)

CITY = {
 "id": "vietnam",
 "intro_blocks": [
  {"t":"lead","html":"Da Nang and Hoi An aren't really two trips — they're one, split by about 45 minutes of coastal road. Da Nang is the modern half: a genuine beach city with excellent food and a growing digital-nomad scene. Hoi An is the postcard half: a UNESCO-listed lantern town that still looks like the 18th-century trading port it was. Almost everyone visiting central Vietnam does both, and they're right to."},
  {"t":"p","html":"Everything routes through <strong>Da Nang International Airport (DAD)</strong> — there's no airport in Hoi An itself, so even a Hoi An-only trip starts here. Base in <strong>Da Nang</strong> for the beach, the seafood, and a short airport run; base in <strong>Hoi An</strong> for the Ancient Town, the tailor shops, and a slower pace, taxiing out for everything else. Plenty of people just split their nights across both — the drive between them is scenic enough to count as part of the trip, not just a commute."},
  {"t":"h2","text":"Where to eat"},
  {"t":"p","html":"Our own photographed, on-the-ground picks are both in Da Nang — that's where our local business network is. Hoi An's dishes below are the honest, well-known stuff any good local will point you to; we just don't have a specific address of our own to vouch for there yet."},
  {"t":"eats","ranked":True,"items":[
    {"name":"Bánh Xèo Bà Dưỡng","slug":"banh-xeo-ba-duong","area":"Da Nang","blurb":"Da Nang's benchmark bánh xèo — a crispy turmeric-rice pancake you wrap yourself in herbs and rice paper. Down a long, busy alley in the Hai Chau district; order the nem lụi (grilled lemongrass pork skewers) and bò né (sizzling beef) alongside it."},
    {"name":"Bún Chả Cá 109","slug":"bun-cha-ca-109","area":"Da Nang","blurb":"A genuine Da Nang specialty you won't find in most of Vietnam: fish-and-crab-cake noodle soup. Add lime, pickled onion and a spoon of fermented shrimp paste — regulars say the broth is flat without them."},
    {"name":"Cao Lầu","area":"Hoi An","blurb":"Hoi An's own noodle, found almost nowhere else — thick, chewy rice noodles under sliced roast pork and crispy croutons. Every lane in the Ancient Town has a version; there's no single 'best,' just good ones."},
    {"name":"White Rose Dumplings","area":"Hoi An","blurb":"Bánh bao vạc — translucent steamed shrimp dumplings folded to look like a flower, a Hoi An original made by a handful of family kitchens that do little else."},
    {"name":"Bánh Mì Phượng","area":"Hoi An","blurb":"Madam Khánh's stall is arguably Vietnam's most famous bánh mì stop. Expect a queue, and a sandwich stacked with more than you'd think fits in one baguette."},
  ]},
  {"t":"h2","text":"Where to stay"},
  {"t":"p","html":"Three areas do the job: <strong>My Khe / An Thuong</strong> in Da Nang for beach-and-nomad energy, the <strong>Hoi An Ancient Town</strong> for lantern-lit walkability, and <strong>An Bang Beach</strong> nearby for a quieter alternative a short ride from the old town. Our own picks — Kon-Tiki Hostel and Nhà Bơ Homestay — both sit in An Hai, Da Nang, between the river and My Khe beach."},
  {"t":"stays","items":[
    {"name":"Kon-Tiki Hostel","area":"An Hai, Da Nang","band":"$6–15","program":"hostelworld","query":"Kon Tiki Hostel Da Nang","blurb":"A 4.4★-rated budget hostel between the river and the beach — our pick for a sociable, walkable base without a resort price tag."},
    {"name":"Nhà Bơ Homestay","area":"An Hai, Da Nang","band":"$15–30","program":"booking","query":"Nha Bo Homestay Da Nang","blurb":"A 4.9★-rated homestay in the same neighborhood — warmer and quieter than a hostel, still an easy walk to the beach."},
    {"name":"Furama Resort Danang","area":"My Khe Beach, Da Nang","band":"$90–160","program":"booking","query":"Furama Resort Danang","blurb":"One of Vietnam's original beachfront five-stars, open on the main My Khe strip since the late 1990s — a long, established operating history."},
    {"name":"InterContinental Danang Sun Peninsula Resort","area":"Son Tra Peninsula, Da Nang","band":"$300+","program":"agoda","query":"InterContinental Danang Sun Peninsula Resort","blurb":"Bill Bensley's flagship: a private-beach resort on its own peninsula, grand enough to have hosted the APEC 2017 leaders' summit. The splurge pick."},
    {"name":"Anantara Hoi An Resort","area":"Riverside, Hoi An","band":"$120–200","program":"agoda","query":"Anantara Hoi An Resort","blurb":"A French-colonial-style riverside resort that's genuinely walkable to the Ancient Town — rare for something this size. The easy Hoi An choice."},
  ]},
  {"t":"book","head":"Compare Da Nang & Hoi An stays","html":"Agoda and Booking both have deep coverage here; Agoda often edges Booking on price across Vietnam, so it's worth checking both before you commit.","program":"agoda","query":"Da Nang","label":"Check Da Nang & Hoi An hotels on Agoda"},
  {"t":"h2","text":"What to do"},
  {"t":"p","html":"You could fill a week here without repeating yourself. These six earn their spot — book the oversubscribed ones ahead, and just turn up for the rest."},
  {"t":"do","items":[
    {"name":"Hoi An Ancient Town & Lantern Night","tag":"UNESCO · free to explore","blurb":"Wander the UNESCO-listed core by day for the 15th–19th-century shophouses and the early-1600s Japanese Covered Bridge, then come back after dark, when the streets go motorbike-free and lantern-lit."},
    {"name":"Marble Mountains","tag":"Ngu Hanh Son","blurb":"Five marble and limestone hills just outside Da Nang, riddled with caves holding Buddhist and Hindu shrines — Huyen Khong Cave and Tam Thai Temple are the highlights. Climb the 156 steps or take the elevator."},
    {"name":"Ba Na Hills & the Golden Bridge","tag":"Book ahead","blurb":"A French-era hill station at 1,500m, reached by a record-length cable car, with the giant stone 'hands' of the Golden Bridge that went viral worldwide. Heavily oversubscribed — book a combo ticket rather than queuing on the day.","program":"klook","query":"Ba Na Hills Golden Bridge Da Nang","label":"Book Ba Na Hills tickets"},
    {"name":"My Son Sanctuary","tag":"Half-day tour","blurb":"Ruined 4th–13th-century Hindu temples of the Champa kingdom, UNESCO-listed and about 36km south of Hoi An — a smaller-scale cousin of Angkor. Almost everyone visits as a guided half-day, sunrise options included.","program":"gyg","query":"My Son Sanctuary tour","label":"Book a My Son tour"},
    {"name":"My Khe & An Bang Beaches","tag":"Two beaches, two moods","blurb":"My Khe (Da Nang) is the wide, resort-lined urban beach with water sports on tap. An Bang (Hoi An, a few km from the Ancient Town) is smaller and slower — a café strip right on the sand."},
    {"name":"Cam Thanh Basket Boat Tour","tag":"Coconut village","blurb":"Spin around the coconut-palm water village of Cam Thanh in a round bamboo basket boat — the rower often throws in a 'basket-boat dance.' Usually bundled with a bike tour of the surrounding rice paddies.","program":"klook","query":"Cam Thanh basket boat tour Hoi An","label":"Book the basket boat tour"},
  ]},
  {"t":"h2","text":"Getting around & between"},
  {"t":"p","html":"<strong>Da Nang International Airport (DAD)</strong> — Vietnam's third-largest — is the only airport for this whole region; both cities are reached from here, with direct international links to Bangkok, Singapore, Seoul, Taipei, Hong Kong and Kuala Lumpur. There's no airport in Hoi An itself."},
  {"t":"p","html":"Da Nang to Hoi An is roughly 28–30km, 45 minutes to an hour. <strong>Grab</strong> is the easiest, most transparent option; metered taxis and shared shuttles also cover the route, and confident riders do it themselves by scooter (from around 80,000–150,000 VND/day) along a genuinely scenic coastal road — an International Driving Permit is technically required."},
  {"t":"book","head":"Book the Da Nang ↔ Hoi An hop (or onward)","html":"12Go is the standard way to compare and book transfers, buses and trains around Vietnam in English, including onward routes like Hue.","program":"12go","target":"https://12go.asia/en/travel/da-nang/hoi-an","label":"Check Da Nang → Hoi An transfers"},
  {"t":"tip","head":"Best time to visit","html":"February to May is the sweet spot — dry season, before peak heat and humidity set in, reliable for both beach days and Ancient Town walking. June–August is still dry but properly hot and humid; workable if you pack for it."},
  {"t":"warn","head":"Be honest about October–November","html":"September through December is wet and typhoon season, and October–November bring real flood risk in Hoi An specifically — the Ancient Town's riverside streets have gone underwater for a day or two in multiple recent years, affecting ground-floor rooms. Traveling then, book accommodation on higher ground, keep your itinerary loose, and expect the possibility of a rearranged day."},
  {"t":"p","html":"For every dish worth ordering in both cities — including the two Da Nang kitchens above in full — see our <a class='inline' href='/vietnam/where-to-eat-in-da-nang/'>Da Nang &amp; Hoi An food guide</a> below."},
 ],
 "faq": [
  ("How many days do you need for Da Nang and Hoi An?",
   "Four to five days covers both comfortably — two or three based in Da Nang for the beach and food, one or two in Hoi An for the Ancient Town and a day trip to My Son or the Marble Mountains. A week lets you add Ba Na Hills without rushing."),
  ("Should I stay in Da Nang or Hoi An?",
   "Da Nang for beach, a bigger food scene, and a short run to the airport. Hoi An if the lantern-lit Ancient Town is the main event and you don't mind taxiing out for everything else. Plenty of travelers split their nights across both — see our stays picks above."),
  ("How do you get from Da Nang to Hoi An?",
   "About 28–30km, 45 minutes to an hour by road. Grab is the easiest and most transparent option; shared shuttles and metered taxis also run it, and confident riders do it themselves by scooter along the coastal road."),
 ],
}

PAGES = [

# ============================================================ WHERE TO EAT
{
 "city":"vietnam", "slug":"where-to-eat-in-da-nang", "order":1,
 "title":"Where to Eat in Da Nang (and Hoi An)",
 "kicker":"Da Nang & Hoi An · Food",
 "dek":"Two real Da Nang kitchens we've eaten in and photographed, plus every Hoi An dish worth crossing the river for — what to order, and why.",
 "description":"Where to eat in Da Nang and Hoi An: our two featured Da Nang kitchens, plus Hoi An's cao lầu, white rose dumplings and bánh mì Phượng.",
 "read":"9 min", "updated":"July 2026",
 "related":[],
 "blocks":[
  {"t":"lead","html":"Da Nang and Hoi An sit 45 minutes apart and eat almost nothing alike. Da Nang is bold, coastal and built for big bowls; Hoi An has its own tiny, particular repertoire that barely exists anywhere else in Vietnam. Here's what to order in both — starting with the two Da Nang kitchens we've actually eaten in, photographed, and can point you straight to."},
  {"t":"h2","text":"The Da Nang eats we actually feature"},
  {"t":"p","html":"Full disclosure: our own on-the-ground picks are both in Da Nang — that's where our local business network is. Everything we say about Hoi An's food further down is the honest, well-established stuff any good local will tell you; we just don't have a specific stall of our own to send you to there yet."},
  {"t":"eats","ranked":True,"items":[
    {"name":"Bánh Xèo Bà Dưỡng","slug":"banh-xeo-ba-duong","area":"Da Nang · Hai Chau","blurb":"Reviewers who've spent months living in Da Nang call this the benchmark bánh xèo in the city — a crispy turmeric rice-flour pancake, filled with shrimp and pork, that you wrap yourself in fresh herbs and rice paper at the table. It's down a long alley that's 'teeming with activity' at peak hours, and reasonably priced for how good it is. Order the bánh xèo itself, then round it out with nem lụi (grilled lemongrass pork skewers) and bò né (sizzling beef in a hot skillet)."},
    {"name":"Bún Chả Cá 109","slug":"bun-cha-ca-109","area":"Da Nang · Hai Chau","blurb":"Bún chả cá — a noodle soup built on fish and crab cakes — is a genuine Da Nang specialty that's hard to find done well anywhere else in Vietnam. Multiple reviewers describe this spot as a Michelin Guide pick; we haven't independently checked that against Michelin's own listings, but the bowl backs up the reputation either way. The broth arrives fairly plain — regulars add lime, pickled onion, spicy minced garlic and a bit of fermented shrimp paste before the first spoonful, and say it's flat without them."},
  ]},
  {"t":"h2","text":"Da Nang's own dishes"},
  {"t":"ul","items":[
    "<strong>Mì Quảng</strong> — turmeric-yellow broad rice noodles with pork, shrimp or chicken, peanuts, and a crisp rice cracker on top. Central Vietnam's defining noodle bowl, and it's dry, not soupy — you toss everything together at the table rather than sipping broth.",
    "<strong>Bánh xèo</strong> — the crispy turmeric rice-flour pancake, wrapped fresh in herbs and rice paper. Our pick above, Bánh Xèo Bà Dưỡng, is the benchmark.",
    "<strong>Bún chả cá</strong> — fish-and-crab-cake noodle soup, a coastal specialty most of Vietnam doesn't have. Our pick above, Bún Chả Cá 109, does it well.",
    "<strong>Seafood</strong> — Da Nang is a fishing city before it's anything else. Riverside and beachfront grills sell whole grilled fish, prawns and squid by the kilo — point at the tank, agree the weight, and it's on your table in minutes.",
  ]},
  {"t":"h2","text":"Hoi An's own dishes"},
  {"t":"ul","items":[
    "<strong>Cao lầu</strong> — thick, chewy rice noodles under sliced roast pork and crispy croutons; local lore says the noodles only work with water from one specific Hoi An well. Barely exists outside town.",
    "<strong>White rose dumplings</strong> (bánh bao vạc) — translucent steamed shrimp dumplings, hand-folded to resemble a flower. A handful of family kitchens specialize in almost nothing else.",
    "<strong>Bánh mì Phượng</strong> — Madam Khánh's stall, arguably Vietnam's single most famous bánh mì stop. Expect a line, and a sandwich doing more work than you'd think one baguette could hold.",
    "<strong>Cơm gà</strong> — Hoi An-style chicken rice: turmeric-stained rice, shredded poached chicken, herbs and pickle on the side. Simple, and rarely done badly.",
  ]},
  {"t":"h2","text":"Da Nang vs Hoi An, at the table"},
  {"t":"compare","head":["Dish","City","What you're getting"],
   "rows":[
     ["<strong>Mì Quảng</strong>","Da Nang","Dry turmeric rice noodles, pork/shrimp/chicken, peanuts, rice cracker"],
     ["<strong>Bánh xèo</strong>","Da Nang","Crispy rice-flour pancake, wrap-it-yourself in herbs &amp; rice paper"],
     ["<strong>Bún chả cá</strong>","Da Nang","Fish-and-crab-cake noodle soup"],
     ["Seafood","Da Nang","Whole grilled fish, prawns &amp; squid, priced by the kilo"],
     ["<strong>Cao lầu</strong>","Hoi An","Chewy rice noodles, roast pork, crispy croutons"],
     ["<strong>White rose dumplings</strong>","Hoi An","Steamed shrimp dumplings, flower-folded"],
     ["<strong>Bánh mì Phượng</strong>","Hoi An","Vietnam's most famous bánh mì stall"],
     ["<strong>Cơm gà</strong>","Hoi An","Turmeric chicken rice"],
   ],
   "cap":"Da Nang's dishes are bigger and more savory; Hoi An's are smaller, stranger, and barely travel past the town limits. Budget a meal for each."},
  {"t":"book","head":"Cook it yourself in Hoi An","html":"Riverside cooking schools run half-day classes that start with a market walk and end with you making cao lầu and bánh xèo from scratch — one of the best-value things to do in either city.","program":"klook","query":"Hoi An cooking class","label":"Find a Hoi An cooking class"},
  {"t":"tip","head":"Ordering like a local","html":"Cash (VND) still rules most stalls and market kitchens — don't count on cards. Herbs and rice paper on the table are for wrapping your bánh xèo, not garnish. And treat cao lầu and bún chả cá as lunch dishes: the best pots sell out early, well before dinner."},
 ],
 "faq":[
   ("What's the best thing to eat in Da Nang?",
    "Start with mì Quảng, the region's own dry turmeric noodle bowl, then Bánh Xèo Bà Dưỡng for crispy rice pancakes and Bún Chả Cá 109 for the fish-and-crab-cake noodle soup that's hard to find outside the city — both real, photographed picks from our own Da Nang network."),
   ("What food is Hoi An famous for?",
    "Cao lầu (chewy rice noodles with roast pork and croutons), white rose dumplings, cơm gà chicken rice, and bánh mì Phượng — widely considered one of Vietnam's best bánh mì stalls. All are Hoi An originals you won't find quite the same way elsewhere."),
   ("Is the food better in Da Nang or Hoi An?",
    "Different registers, not a contest. Da Nang has the bigger city spread and the seafood; Hoi An has a tight handful of dishes it does better than anywhere on earth. Base in either and day-trip for the other's specialties — 45 minutes buys you both."),
 ],
},

]
