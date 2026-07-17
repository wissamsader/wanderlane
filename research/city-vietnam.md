# Da Nang & Hoi An — City Research Brief
Compiled 2026-07-18. Confidence marked throughout: **[H]** high (multi-source or direct-verified this session), **[M]** medium (single source / established training knowledge, not independently re-verified live), **[L]** low / needs a human check before publishing.

---

## SECTION A — Our Own Business Data (proprietary asset)

### ⚠️ Data integrity finding — read before using this section

The brief for this job assumed `VIETNAM/data/` covers **Da Nang + Hoi An**, with an example mapping `hoi-an-spa` → Hoi An. Having read all 20 JSON files' `addr` (street address) fields — the ground-truth location data — that assumption doesn't hold:

- The dataset's own `city` field only ever contains two values: `"danang"` or `"hcmc"`. **There is no Hoi An tag anywhere, and zero businesses have a street address inside Hoi An town.** It's a **Da Nang + Ho Chi Minh City (Saigon)** dataset — two cities ~760 km apart, not a Da Nang/Hoi An pair.
- **12 businesses** are verified Da Nang (districts: Hải Châu, Sơn Trà, Ngũ Hành Sơn/An Thượng, An Hải).
- **8 businesses** are verified Ho Chi Minh City (districts: Phú Nhuận, Bến Thành, Chợ Quán, Quận 5, etc.) — a different region of Vietnam entirely, out of scope for a Da Nang/Hoi An guide.
- `hoi-an-spa.json` — name is "**Hội An** Spa & Massage" but its address is `142/2 Lê Văn Thứ, **Sơn Trà, Đà Nẵng**` — a district on the Da Nang side of the Han River, ~25 km from actual Hoi An. This reads as a business borrowing Hoi An's tourism cachet for its name, not an actual Hoi An location. Treated below as **Da Nang**, flagged.
- Bonus/current-affairs note **[H]**: as of 1 July 2025 Vietnam's nationwide provincial merger folded Quảng Nam province into an enlarged Đà Nẵng municipality, and Hội An itself was dissolved as an independent city into wards + one island commune inside Đà Nẵng (Wikipedia). So even administratively, "Hoi An" no longer exists as its own city — though nothing changes for visitors; every map, OTA listing, and guidebook still treats it as its own destination, and it's kept as its own place throughout this brief.

**Editorial decision:** feature the 12 verified-Da-Nang businesses fully (genuinely useful, real local intel). Exclude the 8 HCMC businesses from the curated lists — they're listed once at the end of Section A for transparency, not woven into "Da Nang/Hoi An" content since that would misrepresent their location. This also means: **our own data currently has zero Hoi An-town listings** — Section B's Hoi An content leans on general research only.

### A1. Featured Local Eats — Da Nang

Only two `catgroup:"food"` entries verify as Da Nang; both are single-dish local institutions, not general restaurants.

| Name | Slug | City | Rating | What to order / why | Demo |
|---|---|---|---|---|---|
| **Bánh Xèo Bà Dưỡng** | `banh-xeo-ba-duong` | Da Nang (Hải Châu) | 4.3★ | Order the **bánh xèo** (crispy turmeric-rice pancake) — comes with fresh herbs and rice paper to wrap it yourself, plus their **nem lụi** (grilled lemongrass pork skewers) and **bò né** (sizzling beef). Reviewers (multi-month Da Nang residents) call it the benchmark bánh xèo in the city — tucked down a long alley, "teeming with activity," reasonably priced. | https://wissamsader.github.io/vietnam/banh-xeo-ba-duong/ |
| **Bún Chả Cá 109** | `bun-cha-ca-109` | Da Nang (Hải Châu) | 4.2★ | Order **bún chả cá** (fish/crab-cake noodle soup) — a genuine Da Nang specialty, hard to find elsewhere in Vietnam. Two independent reviewers flag it as a **Michelin Guide–recommended** pick **[M — from our scraped review text, not independently confirmed against Michelin's own site]**. Regulars' tip: add lime, pickled onion, spicy minced garlic, and a bit of fermented shrimp paste to the broth — reviewers say the broth is flat without it. | https://wissamsader.github.io/vietnam/bun-cha-ca-109/ |

*Excluded (verified Ho Chi Minh City, not Da Nang/Hoi An):* `com-sai-gon` (Com Sai Gon, Vietnamese rice dishes), `com-tam-sa-bi-chuong` (Cơm Tấm Sà Bì Chưởng, broken-rice specialist), `quan-339` (Bún Thịt Nướng Quán 339, grilled-pork vermicelli). All three are strong operators — just ~760 km/a domestic flight from this itinerary.

### A2. Our Stays

Brief asked for `kon-tiki-hostel`, `my-friend-hotel`, `nha-bo-homestay`, `maison-royale` as one group — but only 2 of those 4 verify as Da Nang. Splitting honestly:

**Da Nang (in scope):**

| Name | Slug | Rating | Type | Area | Demo |
|---|---|---|---|---|---|
| **Kon-Tiki Hostel** | `kon-tiki-hostel` | 4.4★ | Hostel (budget) | An Hải, between the Hàn River and Mỹ Khê beach | https://wissamsader.github.io/vietnam/kon-tiki-hostel/ |
| **Nhà Bơ Homestay** | `nha-bo-homestay` | 4.9★ | Homestay | An Hải | https://wissamsader.github.io/vietnam/nha-bo-homestay/ |

**Ho Chi Minh City (out of scope for this guide, flagged only):** My Friend Hotel (`my-friend-hotel`, 4.3★, Chợ Quán), Maison Royale (`maison-royale`, 4.9★, Xuân Hòa), and T Zone House (`t-zone-house`, 4.9★, hostel, Quận 5 — not in the original 4-slug list but same situation).

### A3. Other Featured — Spas & Barbers (Da Nang)

**Spas / massage:**
| Name | Slug | Rating | Area | Photos |
|---|---|---|---|---|
| Deep Spa & Massage | `deep-spa` | 4.6★ | An Thượng 4, Ngũ Hành Sơn (beach area) | 9 |
| Harmony Haven Spa & Massage | `harmony-haven-spa` | 4.8★ | An Thượng 29, Ngũ Hành Sơn (beach area) | 4 |
| Hội An Spa & Massage *(name only — see flag above)* | `hoi-an-spa` | 5.0★ | Sơn Trà, Da Nang | 4 |
| MÂY Spa & Massage | `may-spa` | 4.9★ | An Thượng Night Market, Ngũ Hành Sơn (beach area) | 3 |
| Thu Nguyên Spa & Massage | `thu-nguyen-spa` | 4.9★ | Sơn Trà | 4 |

**Barbers / hair:**
| Name | Slug | Rating | Area | Photos |
|---|---|---|---|---|
| Athena Barber Shop | `athena-barber` | 4.9★ | Hải Châu (city center) | 11 |
| John Hồ Barber Shop | `john-ho-barber` | 5.0★ | Sơn Trà | 6 |
| Salon Quốc Phong | `salon-quoc-phong` | 4.9★ | Hải Châu (city center) | 12 |

Demo URL pattern for all: `https://wissamsader.github.io/vietnam/<slug>/` — spot-checked live on `banh-xeo-ba-duong` and `kon-tiki-hostel`, both resolve correctly with full content **[H]**.

Note on "reviews": the JSON schema stores a Google **rating** (all entries above) plus a small sample of 0 or 3 scraped review snippets/author names — **not** a true total review count, so review counts aren't reported here to avoid fabricating a number.

### A4. Out of scope — same dataset, Ho Chi Minh City (Saigon)

Listed for transparency only, not curated for this Da Nang/Hoi An brief: Bình Nguyễn Hair Salon (`binh-nguyen-salon`, hair, 5.0★), Com Sai Gon (`com-sai-gon`, food, 4.9★), Cơm Tấm Sà Bì Chưởng (`com-tam-sa-bi-chuong`, food, 4.7★), KING PREMIUM Barbershop (`king-premium-barber`, hair, 5.0★), Maison Royale (`maison-royale`, hotel, 4.9★), My Friend Hotel (`my-friend-hotel`, hotel, 4.3★), Bún Thịt Nướng Quán 339 (`quan-339`, food, 4.4★), T Zone House (`t-zone-house`, hotel, 4.9★). Could seed a future Saigon-specific guide.

---

## SECTION B — Essentials for Travelers (Da Nang & Hoi An)

### B1. Orientation

Da Nang and Hoi An work as **one linked trip**, not two separate stops — ~28–30 km apart, 45 min–1 hr by road along a coastal route **[H]**. Most travelers base in one and day-trip to the other, or split their nights across both.

- **Da Nang** = the modern half: a genuine beach city with My Khe (regularly ranked among Asia's best urban beaches), a growing digital-nomad/expat scene centered on An Thượng, big engineered spectacles (Golden Bridge, the fire-breathing Dragon Bridge), strong seafood, and the region's international airport **[H]**.
- **Hoi An** = the heritage half: a UNESCO World Heritage-listed Ancient Town (inscribed 1999) of preserved 15th–19th-century trading-port shophouses, lantern-lit at night, home to 400+ tailor shops, with a slower, more romantic pace and its own beach (An Bang) and coconut village (Cẩm Thanh) nearby **[H]**.
- **Airport**: Da Nang International Airport (**DAD**) — Vietnam's third-largest — sits inside Da Nang city and is the gateway for all of central Vietnam, including Hoi An (there is no airport in Hoi An itself). Direct international routes include Bangkok, Singapore, Seoul, Taipei, Hong Kong, and Kuala Lumpur, plus domestic links to Hanoi and Ho Chi Minh City **[H]**.
- Current-affairs footnote **[H]**: since 1 July 2025, Hoi An is technically no longer an independent city — Vietnam's provincial merger folded it into an enlarged Đà Nẵng municipality as wards. Purely a governance change; every map, OTA, and local still calls it "Hoi An" and it reads as a completely distinct destination on the ground.

### B2. Best Areas to Stay

**Da Nang:**
- **My Khe Beach** — the main beachfront strip; wide sandy beach, resort towers, water sports. Best if you want a beach-first stay with easy city access **[H]**.
- **An Thượng** — the walkable "nomad village" just inland of the My Khe/Ngũ Hành Sơn beach stretch; cafés, bars, coworking spots, younger crowd (also where several of our own spa listings — Deep Spa, Harmony Haven, MÂY — actually sit) **[H]**.
- **City center / Han River** — near Dragon Bridge, the markets, and the Cham Sculpture Museum; more local and urban, less beachy, good for food-focused stays **[H]**.

**Hoi An:**
- **Ancient Town** — inside the UNESCO core; lantern-lit, walkable to everything, motorbike-free at night, but touristy and the first area to flood in Oct–Nov **[H]**.
- **An Bang Beach** — ~4–5 km from the Ancient Town; quieter, a relaxed beachfront café strip, popular with longer-stay travelers **[H]**.
- **Cẩm Thanh (coconut village)** — rural, basket-boat and bicycle territory, rice paddies and coconut-palm waterways; a slow base best suited to travelers with their own scooter or bike **[H]**.

### B3. Where to Stay — 6 real, bookable options across both cities

All listed as normally findable on Agoda/Booking.com; confidence marked per property since only one was independently re-verified this session (WebSearch was unavailable — session budget exhausted before this task started).

| Property | City / area | Band | Why |
|---|---|---|---|
| **InterContinental Danang Sun Peninsula Resort** | Sơn Trà Peninsula, Da Nang | Luxury | Bill Bensley–designed flagship resort on its own private beach; hosted the APEC 2017 leaders' summit. **[H — Wikipedia-verified this session: confirmed open, 197 rooms, opened 2012]** |
| **Furama Resort Danang** | My Khe Beach, Da Nang | Upper-mid / luxury | One of Vietnam's original beachfront 5-star resorts (opened late 1990s); long operating history on the main beach strip. **[M — training knowledge, not re-verified live this session]** |
| **Danang Backpackers Hostel**-type social hostel | Da Nang (An Thượng/city area) | Budget | Representative of the sociable dorm-hostel category clustered around An Thượng — several operate here and show up on Booking.com/Hostelworld; treat the specific name as indicative, confirm current top-rated pick on the app before booking. **[L — name not independently re-verified this session; verify live]** |
| **Anantara Hoi An Resort** | Riverside, walking distance to Hoi An Ancient Town | Upper-mid / boutique | Long-running riverside resort in French-colonial style, inside walking distance of the Ancient Town — rare for a resort of its size. **[M — training knowledge, not re-verified live this session]** |
| **Little Hoi An Central Boutique Hotel & Spa** (or similar central boutique) | Hoi An, near Ancient Town | Boutique / mid | Representative of the small boutique-hotel band inside/adjacent to the Ancient Town — courtyard-style, walkable to everything. **[L — verify current name/rating live before publishing]** |
| **Hoi An hostel/budget guesthouse cluster** (e.g. Hoi An Space-type hostels) | Hoi An | Budget | Representative of the dorm/guesthouse band a few minutes' walk from the Ancient Town. **[L — verify current top-rated pick live]** |

**Recommendation for the final published guide:** re-run a live search (Agoda/Booking.com or WebSearch once budget resets) to confirm the three **[L]**-marked picks by current name and rating before publishing — the **[H]** and **[M]** picks are large, long-established properties low-risk enough to publish as-is, but a quick live price/availability check is good practice for any travel guide regardless.

### B4. Top Things to Do (11)

1. **Hoi An Ancient Town by day + lantern night** — UNESCO core, river-front shophouses; after dark the streets go motorbike-free and lantern-lit, especially vivid on the monthly Lantern/Full-Moon Festival (14th day of the lunar month) **[H]**.
2. **Japanese Covered Bridge** — Hoi An's icon, a covered wooden bridge built in the early 1600s; small entry fee **[H]**.
3. **An Bang Beach** — Hoi An's quieter beach escape, café strip right on the sand **[H]**.
4. **My Khe Beach** — Da Nang's main urban beach, resorts and water sports **[H]**.
5. **Marble Mountains (Ngũ Hành Sơn)** — five marble/limestone hills named for the five elements, riddled with caves holding Buddhist/Hindu shrines (Huyền Không Cave, Tam Thai Temple); 156 steps or elevator to the top for panoramic views **[H]**.
6. **Ba Na Hills & the Golden Bridge** — French-era hill station at 1,500 m reached by a record-length (~5.8 km) cable car; the Golden Bridge's giant stone "hands" went viral globally. Heavily oversubscribed — **book via Klook/GetYourGuide** for skip-some-queue combo tickets **[H]**.
7. **Son Trà Peninsula (Monkey Mountain)** — a scooter loop around a forested peninsula with coastal viewpoints and resident wild macaques **[H]**.
8. **Lady Buddha at Linh Ứng Pagoda** — a 67 m Buddha statue on Son Trà, one of Vietnam's tallest, with sweeping bay views **[H]**.
9. **My Son Sanctuary** — ruined 4th–13th century Hindu temple complex of the Champa kingdom, UNESCO-listed 1999; ~36 km south of Hoi An / ~68 km from Da Nang, comparable in significance (smaller in scale) to Angkor. Almost always visited as a **guided half-day tour — sells heavily on Klook/GetYourGuide**, including sunrise options **[H]**.
10. **Cẩm Thanh basket-boat tour** — spin around the coconut-palm water village in a round bamboo basket boat, often with a "basket-boat dance" from the rower; a big Klook/GetYourGuide seller, usually bundled with a bike tour **[H]**.
11. **Hoi An cooking class + market tour** — multiple riverside schools teach cao lầu, bánh xèo, and other central-Vietnamese dishes starting with a market walk; sells well on Klook/GetYourGuide **[H]**.
12. *(bonus)* **Tailoring in Hoi An** — 400+ tailor shops turn around custom suits/dresses in 1–3 days (roughly $49–150+ depending on garment/fabric); a signature Hoi An activity in its own right, book fittings early in your stay to allow for a second fitting **[H]**.

*(Lantern-making workshops are widely offered alongside cooking classes in Hoi An town — folded into #1/#11 above rather than a separate line, since most operators bundle it.)*

### B5. Signature Food

**Da Nang** — the coastal-central-Vietnam table: **mì Quảng** (turmeric-yellow broad rice noodles with pork/shrimp/chicken, peanuts, and rice crackers), **bánh xèo** (crispy turmeric rice-flour pancake wrapped in herbs and rice paper), **bún chả cá** (fish/crab-cake noodle soup — see our own Bún Chả Cá 109 pick above), and abundant fresh **seafood** at riverside/beachfront grills **[H]**.

**Hoi An** — its own distinct micro-cuisine, some dishes barely exist outside town: **cao lầu** (thick, chewy rice noodles — the water is traditionally said to come from a specific local well — topped with slices of roast pork and crispy croutons), **white rose dumplings** (bánh bao vạc, translucent steamed shrimp dumplings folded to resemble a flower), **bánh mì Phượng** (Madam Khánh's stall, arguably Vietnam's most internationally famous bánh mì stop), and **cơm gà** (Hoi An-style chicken rice, turmeric rice with shredded poached chicken) **[H]**.

### B6. Getting There & Around

- **Fly into Da Nang International Airport (DAD)** — the only airport for this whole region; both Da Nang and Hoi An are reached from here **[H]**.
- **Airport/city → Hoi An**: ~28–30 km, 45 min–1 hr. Grab (ride-hailing app) is the easiest and most transparent option at roughly 300,000–400,000 VND; a metered/negotiated taxi runs 200,000–500,000 VND depending on haggling; shared shuttle buses run around 130,000 VND/person for the same 45-minute run. The coastal road route between the two is scenic in its own right **[M — specific VND figures pulled from a single travel-guide source dated 2023–2024, worth a live spot-check for current pricing]**.
- **Grab** is the default ride-hailing app across both cities/for the inter-city hop — far more transparent than street taxis **[H]**.
- **Scooter/motorbike rental** is the classic way to get around and do the Da Nang–Hoi An coastal drive independently — roughly 80,000–150,000 VND/day for a 100–110cc bike; an international driving permit is technically required by Vietnamese law **[M]**.
- **Metered taxis** (Mai Linh, Vinasun) are reliable fallbacks in Da Nang when Grab is scarce **[M]**.
- **Inter-city/onward travel bookable on 12Go**: 12Go.asia is the standard aggregator for Vietnam bus/train/private-transfer bookings and covers the Da Nang–Hoi An corridor plus onward routes (e.g., to Hue, or overnight trains/buses further afield) **[M — 12Go's general Vietnam coverage is well-established; I could not load a live fare page this session to confirm current DaNang–Hoi An pricing, so treat specific numbers as needing a live check]**.
- Within the Hoi An Ancient Town core, walking or bicycle (~20,000 VND/day rental) is the norm — it's motorbike-restricted at various hours **[H]**.

### B7. Best Time to Visit

- **Best window: February–May [H]** — the region's dry season, before peak heat/humidity sets in; broadly the most reliable stretch for both beach days and Ancient Town walking.
- **June–August**: still technically dry season, but hot and humid — workable, just pack for heat **[M]**.
- **September–December: wet/typhoon season [H]** — rain and storm risk rises through the back half of the year.
- **October–November: flood risk, be honest about it [H]** — Hoi An in particular "regularly floods" in November per multiple travel sources; river water has been reported reaching several blocks up from the riverside into the Ancient Town and affecting ground-floor hotel rooms. This isn't a rare-disaster caveat — it's a recurring seasonal pattern locals and hoteliers plan around. Anyone traveling Oct–Nov should book accommodation on higher ground, keep the itinerary flexible, and expect the possibility of the Ancient Town's riverside streets being underwater for a day or two.

---

## Confidence key
- **[H]** High — cross-checked across 2+ sources this session (Wikipedia + Wikivoyage + our own data, or 2+ independent fetches), or directly verified (e.g., demo URLs live-checked).
- **[M]** Medium — from a single live source this session, or from well-established training knowledge not re-verified live; reasonable to publish but worth a spot-check.
- **[L]** Low — training-knowledge placeholder where live verification failed or wasn't attempted (mainly the smaller boutique/budget hotel picks in B3); flag for a follow-up pass before this goes in front of a traveler.

**Research note:** WebSearch was unavailable for this entire task — the session had already used its full 200/200 search budget before this job started. All of Section B was built via targeted WebFetch calls to Wikipedia/Wikivoyage (which mostly worked) plus training knowledge for gaps (several hotel-booking-site and Wikipedia-hotel-page fetches 403'd/404'd — likely bot protection). If a fresh WebSearch budget becomes available, prioritize re-verifying the three **[L]** hotel picks in B3 and the specific VND transfer prices in B6.
