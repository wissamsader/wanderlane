# Travel Affiliate Programs — Monetization Reference

Research date: 2026-07-18. Sourced from each program's official partner/affiliate pages, official help-center articles, and cross-checked against 2–4 independent third-party affiliate-program review sites per program. **Web search budget was exhausted mid-task** (200/200 used) — a handful of secondary details below rely on WebFetch-only verification or a single corroborating source; these are flagged explicitly. Do not wire real money-tracking code against any field marked Low confidence without re-verifying inside the actual partner dashboard after signup.

**Confidence key** (matches this project's other research docs)
- **High** — verified directly on the program's own official page/docs, or corroborated by 3+ independent sources with no conflicts.
- **Medium** — verified on official or near-official sources but with some conflicting numbers across sources, or only one official source reached.
- **Low** — could not reach an official source; third-party aggregator claims only, or sources actively conflict. Treat as "needs manual verification at signup."

Feeds: the link-generation/monetization layer for the whole site (stays.md, food.md, transport-tours-nomad.md content).

---

## Executive summary (read this first)

**Travelpayouts verdict:** Sign up on Travelpayouts first. One application gets you into Agoda, Booking.com, Hostelworld, Klook, GetYourGuide, 12Go, Airalo, Tripadvisor, and Kiwi.com — 9 of the 11 programs in scope — under one login, one link format, and one consolidated payout. In the cases I could directly compare, Travelpayouts' rate was **at parity with or better than** signing up direct (e.g. Agoda 6–7.2% via Travelpayouts vs ~4% direct starter tier; Airalo and GetYourGuide pay identically either way). The two programs that matter for this site and are **not** on Travelpayouts — SafetyWing and TheFork — must be joined directly regardless.

**Recommended shortlist (in order):** (1) Travelpayouts, (2) SafetyWing Ambassador (direct, recurring commission, not on Travelpayouts), (3) Amazon Associates (bolt-on for packing-list content). Full reasoning in [§14](#14-recommended-signup-order).

**Could not fully verify the tracking-parameter format for:** 12Go's *native* parameter (only Travelpayouts' wrapper format is confirmed), Airalo's Impact.com link format, and TheFork's parameter/network entirely. See each section's confidence line.

---

## Quick-reference: tracking parameters at a glance

| Program | Attribution parameter | Confidence on param |
|---|---|---|
| Travelpayouts (any brand) | `shmarker=ID.subid` + `promo_id=` + `custom_url=` (deep link), or simple `marker=ID` | High |
| Agoda (direct) | `cid=` (+ `hid=` for a specific hotel) | Medium–High |
| Booking.com (direct via CJ) | `aid=` | High |
| Hostelworld (Partnerize) | `clickref=` | Medium–High (confirmed via Partnerize's own docs, not a Hostelworld-specific example) |
| Klook (direct) | `aid=` | Medium–High |
| GetYourGuide (direct) | `partner_id=` (+ optional campaign tag) | High |
| 12Go (direct/native) | Unconfirmed — dashboard mentions "deep-links" and "sub-ID tracking" but no public param name found | **Low** |
| Airalo (Impact.com) | Unconfirmed — Impact.com typically issues per-advertiser short redirect links | **Low** |
| SafetyWing Ambassador | `referenceID=` (+ `utm_source=`, `campaign=invitationapp`, `utm_medium=Ambassador`) | Medium–High |
| TheFork | Unconfirmed | **Low** |
| Amazon Associates | `tag=` | High (general knowledge, extremely stable/well-documented program) |

---

## 1. Travelpayouts (aggregator/network) — PRIORITY FINDING

**What it is:** An affiliate *network/aggregator*, not a brand itself. You create one Travelpayouts account, get one Partner ID ("marker"), and then join individual brand "programs" inside the dashboard — each join is closer to a checkbox than a fresh application, since Travelpayouts is the applicant-of-record with the brand.

**Brands confirmed live on Travelpayouts in 2026** (verified via each brand's own `travelpayouts.com/en/offers/…` page or official Travelpayouts blog post, not just marketing copy):
- **Booking.com** — confirmed, own offer page fetched directly.
- **Agoda** — confirmed.
- **Hostelworld** — confirmed.
- **Klook** — confirmed, own offer page fetched directly.
- **GetYourGuide** — confirmed.
- **12Go / 12Go Asia** — confirmed, own offer page fetched directly.
- **Airalo** — confirmed, own offer page + blog post fetched, 10% commission / 30-day cookie stated explicitly.
- **Tripadvisor** — confirmed (8% on Experiences bookings; up to 50% of Tripadvisor's own commission on hotel-search clicks; 14-day cookie).
- **Kiwi.com** — confirmed (flights; example deep link found in official SubID docs).
- Also present: trivago, Viator, Omio, Rail Europe, Rentalcars, Busbud, CheapOair, Tiqets, Ticketmaster, BlaBlaCar, plus travel insurance and lounge-pass offers.
- **NOT found on Travelpayouts:** SafetyWing (runs its own direct "Ambassador" program only) and TheFork (no evidence of a Travelpayouts listing; its affiliate access is regional/fragmented — see §9).

**(1) Signup/partner page:** https://www.travelpayouts.com/en/ (free, single registration).

**(2) Approval requirements:** Free to join with no site required to *register*, but individual brand programs inside the dashboard have their own gates — e.g. Booking.com via Travelpayouts explicitly requires "content websites, specifically travel blogs," bars social-media-only traffic (unless pre-approved), and reviews applications within ~3 business days. Other brands (12Go, Airalo) are more permissive of social-only traffic. Content/guide sites are explicitly the target audience across the board.

**(3) Tracking parameter + deep link system:**
Every affiliate gets one Partner ID ("marker") baked into every tool automatically. Two link mechanisms exist:
- **Simple redirect:** `https://tp.media/r?marker=YOUR_ID&p=OFFER_ID&u=DESTINATION_URL`
- **Deep link / custom link** (what you'd use to link to a *specific* hotel/route/activity page), built per-brand on a numbered subdomain:
  `https://c[N].travelpayouts.com/click?shmarker=[MARKER_ID].[SUBID]&promo_id=[BRAND_ID]&source_type=customlink&type=click&custom_url=[URL-ENCODED DESTINATION]`

  Verified real examples pulled directly from official brand offer pages:
  - Booking.com: `https://c84.travelpayouts.com/click?shmarker=iddqd&promo_id=3650&source_type=customlink&type=click&custom_url=https%3A%2F%2Fbooking.com`
  - 12Go: `https://c44.travelpayouts.com/click?shmarker=[your_id]&promo_id=1764&source_type=customlink&type=click&custom_url=[destination_url]`
  - Kiwi.com: `https://c111.travelpayouts.com/click?shmarker=78606.kiwicom&promo_id=3791&source_type=customlink&type=click&custom_url=https://www.kiwi.com/deep`

  **SubID:** appended after a dot inside `shmarker` (e.g. `shmarker=78606.kiwicom`). Alphanumeric + underscore only, max 4096 characters. Used for per-page/per-campaign attribution in Travelpayouts' own reporting (filter/group stats by SubID).
  - Short-link variant: take any pre-made short affiliate link, append `?sub_id=VALUE`.

**(4) Commission rate/structure (per brand, via Travelpayouts):**
- Booking.com: 5% on completed hotel stay, €1.50/flight booking, 5% prepaid car rental (3% pay-at-location)
- Agoda: 6% of total booking value ex-tax (one third-party source cites a blended 7.2%)
- Hostelworld: 40% of the deposit revenue Hostelworld collects
- 12Go: 50% revenue share, ~$2.90–3 average per booking
- Klook: 5% most categories, 2% "Special Activities," 5% travel insurance
- GetYourGuide: 8%
- Airalo: 10% of final sale value
- Tripadvisor: 8% (Experiences) / up to 50% of TA's own commission (hotel-search clicks)
- Reported tiering: Travelpayouts' own blog claims a 10% rate increase for affiliates earning >$3,000/month — unverified beyond that one self-reported claim.

**(5) Cookie windows (per brand, via Travelpayouts):**
Booking.com = **one session only** (notably short); Agoda = 1 day; 12Go = 30 days; Klook = 30 days; GetYourGuide = 31 days; Airalo = 30 days; Tripadvisor = 14 days.

**(6) Payout method + threshold:** PayPal (min **$50**), WebMoney, or bank transfer/Wise. Earnings "fix" on the 10th of each month, verified, then paid out roughly the 11th–20th. This threshold is shared across *all* brands in one account — meaning small earnings from several different brands pool together and clear the $50 floor faster than any single direct program's own threshold would. This is a genuine practical advantage for a brand-new, low-traffic site.

**(7) Content/guide sites allowed:** Yes — explicitly the core target audience.

**Travelpayouts vs. direct — the actual tradeoffs:**
- *For:* one approval instead of nine; commission at parity-or-better in the cases directly comparable (Agoda, Airalo, GetYourGuide all matched or beat the direct starter rate); one pooled payout threshold instead of nine scattered ones (useful given e.g. 12Go's direct bank-transfer minimum is a punishing 33,000 THB / ~$956 — pooled through Travelpayouts you'd never need to hit that via bank transfer).
- *Against:* your payout depends on two parties settling correctly (brand → Travelpayouts → you) instead of one; Travelpayouts' own dashboard/reporting is a re-packaging of the brand's data, less granular than some native dashboards; at meaningful traffic volume, going direct with a brand can unlock negotiated tier upgrades a shared network rate won't match (this last point is general affiliate-industry inference, not something verified per-brand today — flagged as such).
- *Must go direct regardless:* SafetyWing, TheFork (neither is on Travelpayouts).

**Confidence: High** on the mechanism, parameter format, and brand-availability list (each cross-checked against the brand's own official Travelpayouts offer page). **Medium** on some individual commission figures where sources gave slightly different numbers (Agoda 6% vs 7.2%; Hostelworld "40% of deposit" vs the direct program's "18–22% of booking value" — plausibly the same underlying number described two different ways, not necessarily a contradiction). **Medium** on total brand count (Travelpayouts markets "100+"; one detailed review counted 59 *currently active*; I did not independently count).

---

## 2. Agoda Partners (direct)

- **(1) Signup:** https://partners.agoda.com/en-us/signup (main hub: partners.agoda.com)
- **(2) Approval requirements:** An existing website is required to register as a standard Market Affiliate Partner. Exceptions exist for travel agents, but require additional documentation. Applications go through a review process before Affiliate Center access is granted.
- **(3) Tracking parameter:** `cid=` is the affiliate/partner ID; `hid=` specifies a particular hotel for a deep link. Verified example (parameter names are long-established/stable across Agoda's own WordPress plugin and partner tools, though the specific example below is from an older cached source — dates are illustrative only, replace with real future dates):
  `https://www.agoda.com/partners/partnersearch.aspx?cid=YOUR_CID&hid=463019&currency=USD&checkin=2026-11-02&checkout=2026-11-05&NumberofAdults=2&Rooms=1`
- **(4) Commission:** Progressive/tiered model — commonly cited starting around 4% for a new affiliate, scaling toward 7%+ with volume. (Via Travelpayouts this is effectively pre-negotiated at 6–7.2% from day one — see §1.)
- **(5) Cookie window:** Not independently confirmed today for the *direct* program (Agoda's own FAQ page returned no fetchable content — blocked/JS-rendered). Third-party sources and the Travelpayouts-mediated figure both point to a short window (commonly cited as 1 day, last-click). **Verify directly in Partner Center after signup.**
- **(6) Payout method + minimum:** Not independently confirmed today (official FAQ page unreachable). Flag for manual verification at signup.
- **(7) Content/guide sites allowed:** Yes — required, in fact (must have a site to register as this partner type).

**Confidence: Medium.** Signup URL, approval gate, and the `cid=`/`hid=` parameter names are well-established and stable (also confirmed indirectly via multiple third-party plugin/tool docs), but I could not reach Agoda's own FAQ page directly today (blocked), so cookie window and payout threshold are **Low confidence** — verify in-dashboard before building against them.

---

## 3. Booking.com Affiliate Partner Programme (direct)

- **(1) Signup:** https://www.booking.com/affiliate-program/v2/index.html — the actual registration flow explicitly routes to **CJ Affiliate**: "Select your region and complete your registration with CJ," linking to `cj.com/en-gb/publisher/partners/booking.com`. Confirmed on two separate fetches of Booking's own page (English and en-GB versions).
- **(2) Approval requirements:** Marketed as "free and easy." Content sites/travel blogs are explicitly welcomed. Restrictions noted: no social-media-only traffic (unless separately approved), no domains confusable with "Booking," no toolbars/browser extensions, no pop-ups, no adult/gambling content. ~3 business day review cited (though this detail came from the Travelpayouts-mediated version of the program, not confirmed identical for the direct/CJ path).
- **(3) Tracking parameter:** `aid=` — confirmed on Booking's own official page (`aid=1328032` shown in a property-referral link) and independently in multiple third-party sources. Well-established, stable. Example deep link pattern: `https://www.booking.com/hotel/th/[property-slug].html?aid=YOUR_AID&checkin=2026-11-02&checkout=2026-11-05`
- **(4) Commission:** Revenue-share of *Booking's own* commission from the hotel (not a flat % of booking price). Base tier ≈ 25% of Booking's cut, scaling with monthly confirmed-booking volume toward ~40%. Since Booking typically earns ~15% from a hotel, this nets out to roughly the commonly-cited "4–5% of total booking price" for a new affiliate.
- **(5) Cookie window:** **Materially conflicting across sources — flag this as the single most important thing to verify before building anything around it.** Some sources describe the direct/Partner Hub tracking as **session-based** (booking must complete in the same browsing session as the click — no persistent multi-day cookie at all). Other sources cite a 30-day cookie. The Travelpayouts-mediated version of this same program is explicitly listed as "one session." Given two independent signals both point to session-based/very-short attribution, treat that as the more likely reality and **confirm directly in your approved CJ/Partner dashboard** — this materially changes how you'd design "read now, book later" content around Booking.com versus, say, GetYourGuide's 31-day window.
- **(6) Payout method + minimum:** €100 minimum for bank transfer (accounts in EUR/USD/GBP); PayPal also available (EUR only). Commission confirms 60–90 days after guest checkout (hotel stays), paid monthly thereafter.
- **(7) Content/guide sites allowed:** Yes — explicitly designed for this.

**Confidence: Medium overall; High on signup path and `aid=` parameter; Low specifically on cookie window** due to direct source conflict (session vs. 30 days) — this is a "verify before you build" item, not a "trust this number" item.

---

## 4. Hostelworld affiliate

- **Network: Partnerize** (formerly Performance Horizon Group — explains the "PHG" payment-platform references in Hostelworld's own FAQ). Confirmed via Partnerize's own signup URL pattern.
- **(1) Signup:** https://partners.hostelworld.com/ → "Sign Up Today" → https://signup.partnerize.com/signup/en/hostelworld
- **(2) Approval requirements:** Manual review, takes a few days depending on site/social quality. Eligibility is broad: "If you have a travel related website or like to share your adventures with fellow travellers then we want to work with you" — social media traffic (YouTube, Facebook groups, email newsletters) explicitly accepted, not just blogs.
- **(3) Tracking parameter:** `clickref=` — this is Partnerize's standard parameter used across all campaigns on its platform, confirmed directly from Partnerize's own official documentation (not a Hostelworld-specific example, since Hostelworld's own partner dashboard generates your actual per-affiliate links). General pattern: `https://www.hostelworld.com/...?clickref=YOUR_ID`. Note: the clickref value must match exactly between click-time and conversion-time (case-sensitive).
- **(4) Commission:** Two figures found that likely describe the same underlying number differently — Hostelworld's own FAQ states "40% of the deposit" revenue Hostelworld collects; independent affiliate-review sites describe it as "18–22% of the total booking value." (Hostelworld bookings are typically a small deposit + pay-at-property balance, so 40% of a small deposit could plausibly equal ~18–22% of the total stay value — plausible reconciliation, not independently confirmed.) CPA basis, paid once the booking is completed.
- **(5) Cookie window:** 30 days.
- **(6) Payout method + minimum:** Monthly, via the Partnerize/PHG platform, **$30 minimum**, bank transfer (manual release or scheduled automatic transfer in your chosen currency).
- **(7) Content/guide sites allowed:** Yes.

**Confidence: Medium-High.** Network, signup path, cookie window, and payout threshold are solidly confirmed from official sources. The exact commission percentage has two plausible-but-not-reconciled framings (flagged above), and the tracking parameter is confirmed at the Partnerize-platform level but not with a live Hostelworld-specific example URL.

---

## 5. Klook Affiliate Program

- **(1) Signup:** https://affiliate.klook.com/home (Klook's own in-house affiliate portal — also reachable via Travelpayouts, Involve Asia, and Ecomobi as alternate networks, possibly at different rates).
- **(2) Approval requirements:** Content and travel-related sites accepted. Explicitly prohibited: PPC traffic, clickbot traffic, "branded" Facebook pages, bidding on "Klook" as a brand keyword, and using discount codes not sourced through the program.
- **(3) Tracking parameter:** `aid=` — confirmed via a real example URL found from an active affiliate's account: `https://www.klook.com/activity/1292-half-day-city-tour-kuala-lumpur/?aid=1234` (the blogger's real partner ID, 2319, was cited alongside it).
- **(4) Commission:** Tiered by category (consistent across 2–3 independent aggregator sources, but I could not load Klook's own official rate-card page to confirm firsthand — the page returned only its tagline, no body content):
  - eSIM: 20%
  - India-origin bookings: 10%
  - Tours/activities/hotels/select premium products: 6.5%
  - Most other categories: 5%
  - Special activities & gift cards: 2%
- **(5) Cookie window:** 30 days (7 days for hotels and car rentals specifically).
- **(6) Payout method + minimum:** No stated minimum threshold found. Paid monthly, ~90 days after validation; bank transfer and PayPal supported.
- **(7) Content/guide sites allowed:** Yes.

**Confidence: Medium-High** on signup/approval/parameter (real example URL found); **Medium** on the exact commission table (corroborated across multiple secondary sources but not confirmed on Klook's own rendered page today).

---

## 6. GetYourGuide Partner Program

- **(1) Signup:** https://partner.getyourguide.com/
- **(2) Approval requirements:** Open — described as suitable for "anyone with an audience," applications "promptly considered." No explicit minimum-traffic requirement found.
- **(3) Tracking parameter:** `partner_id=` — confirmed via a real example: `https://www.getyourguide.com/s/?partner_id=XIBGHEV&q=London`. The dashboard's Affiliate Link Builder also produces shortened `gyg.me/...` links with the partner ID and an optional campaign-name tag embedded.
- **(4) Commission:** 8% base rate per booking for new partners.
- **(5) Cookie window:** 31 days.
- **(6) Payout method + minimum:** PayPal has **no minimum**, paid monthly. Bank transfer requires a **€50/$50 minimum**; below that, earnings roll to the next month. Payment runs on the 5th business day of the month if the threshold is met.
- **(7) Content/guide sites allowed:** Yes.

**Confidence: High.** This is the best-verified direct program in this reference — official partner ID example, commission, cookie window, and payout terms were all corroborated from the official Partner Resource Center content and independently from a detailed blogger review citing the same figures.

---

## 7. 12Go / 12Go Asia

- **(1) Signup:** https://agent.12go.asia/ — **note:** this is the correct *content/publisher* affiliate program. Do not confuse it with `reseller.12go.asia`, which is a separate B2B program for travel agencies that book and resell tickets directly to customers (different business model, different signup).
- **(2) Approval requirements:** No website required — you can register and share links purely via social media accounts. Explicitly open to "travel bloggers, social media communities, SEO-specialists, online travel agencies, travel agents."
- **(3) Tracking parameter:** **Could not confirm the native parameter name.** 12Go's own site mentions "deep-links" and optional "sub-ID tracking" capability inside the dashboard but does not publicly document the literal query-string parameter. (The Travelpayouts-mediated version uses Travelpayouts' own wrapper — `shmarker=`/`promo_id=`/`custom_url=` — which is Travelpayouts' format, not 12Go's native one; do not assume they're the same if you sign up direct.) **Action item: log in after signup, generate a test link, and inspect the resulting URL.**
- **(4) Commission:** 50% revenue share, averaging ~$2.90–3 per booking, confirmed directly on the official page.
- **(5) Cookie window:** 30 days, last-click basis (a later partner's link overrides an earlier one if the user clicks both within the window).
- **(6) Payout method + minimum:** PayPal or Wise, minimum **300 THB** (~$8–9) — easily reachable. Bank transfer minimum **33,000 THB** (~$950+) — unrealistic for a new/small site; use PayPal/Wise instead.
- **(7) Content/guide sites allowed:** Yes.

**Confidence: High** on everything except the tracking parameter, which is **Low/unconfirmed** — this is one of the two programs (with Airalo) where the exact link format needs hands-on verification after signup.

---

## 8. Airalo Partners (eSIM)

- **(1) Signup:** Runs on **Impact.com** — direct signup link: `app.impact.com/campaign-promo-signup/Airalo-The-Worlds-First-eSIM-store.brand` (also reachable via `partners.airalo.com/solutions/affiliates`).
- **(2) Approval requirements:** Application form + review; approved partners typically go live "within a few days."
- **(3) Tracking parameter:** **Could not confirm a concrete example URL.** Impact.com typically issues per-advertiser branded short redirect links (its platform-wide sub-tracking parameter is commonly `irclickid=`, but I did not find an Airalo-specific example to confirm this is exposed the same way here). Partners receive "custom codes and custom links" through a Regional Affiliate Manager per Airalo's own program description — **action item: confirm the actual link format inside the Impact.com dashboard after approval.**
- **(4) Commission:** 10% standard rate on final sale value (after any discounts). Confirmed identically both directly (Impact.com) and via Travelpayouts — i.e., no discount for going direct or premium for using the aggregator here.
- **(5) Cookie window:** 30 days.
- **(6) Payout method + minimum:** **$15 minimum**, paid via bank account or PayPal (PayPal payouts carry an extra 2% fee). Paid on the 28th of the month following the sale; sales validate on the 7th of the subsequent month.
- **(7) Content/guide sites allowed:** Yes — explicitly courts content creators.

**Confidence: Medium-High** on program terms (commission/cookie/payout all corroborated across multiple sources and match the Travelpayouts-mediated figures exactly); **Low** on the tracking parameter specifically — flagged as needing manual verification.

---

## 9. SafetyWing Ambassador (nomad insurance)

- **Not available via Travelpayouts** — direct/in-house program only.
- **(1) Signup:** https://safetywing.com/ambassador (also `hello.safetywing.com/ambassador-page`)
- **(2) Approval requirements:** Light-touch — registration takes "under 5 minutes," asks about your business/content, no stated minimum audience size.
- **(3) Tracking parameter:** `referenceID=` — confirmed via a real referral-tool-generated example: `safetywing.com/nomad-insurance/?referenceID=[ambassadorID]&campaign=invitationapp&utm_source=[ambassadorID]&utm_medium=Ambassador`. **Caveat:** SafetyWing has reorganized/renamed product lines before (e.g. "Nomad Insurance" vs. "Remote Health"); confirm the current product URL slug at signup rather than assuming `/nomad-insurance/` is still current for every plan.
- **(4) Commission — RECURRING, this is the standout feature of this program:** ~10% of the premium, and because most SafetyWing plans are subscription/recurring, the ambassador keeps earning on that same referred customer's **renewal payments**, not just the first purchase. This recurring credit applies for **364 days after the customer's initial sign-up** — i.e., it's recurring-within-a-window, not indefinitely-forever. No other program in this reference pays on renewals at all, which makes this disproportionately valuable for "digital nomad guide"-style content even though the per-transaction commission looks modest next to e.g. 12Go's 50%.
- **(5) Cookie/attribution window:** 364 days.
- **(6) Payout method + minimum threshold:** PayPal and/or Wise. **Exact minimum threshold unconfirmed — sources conflict** ($10 vs. $50 vs. "no minimum" all appear across different reviews, and I could not find SafetyWing's own canonical statement of this number today). Paid monthly.
- **(7) Content/guide sites allowed:** Yes — nomad/travel bloggers are the program's core target audience.

**Confidence: Medium-High** on the recurring-commission mechanic and 364-day window (well corroborated across sources); **Medium** on the `referenceID=` parameter (real example found, but from a third-party tool, and the product-slug caveat above); **Low** on the exact payout minimum threshold.

---

## 10. TheFork affiliate

- **Not available via Travelpayouts** (no listing found).
- **Important distinction:** `thefork.com/sponsorship` — the page you'd naturally land on searching for this — is actually a **consumer refer-a-friend loyalty program** ("Yums" points for referring friends to book their first reservation), **not** a publisher/content-site affiliate program. Don't confuse the two.
- **(1) Signup:** **Unclear/fragmented.** The actual CPA-style publisher affiliate access appears to run through **different regional third-party CPA networks per country** rather than one unified global program — e.g. "TheFork FR" is listed on the French network Kwanko; the Spanish brand ("ElTenedor ES") is listed separately via FlexOffers. I could not find one canonical global signup page, and Kwanko's program page requires a logged-in publisher account to reveal actual terms (commission/cookie/payout were hidden behind login).
- **(2)–(6):** Some third-party aggregator sources cite **40% commission on bookings from new users / 15% from returning users**, with a **20-day cookie window**, for at least one regional (French) program — but I could not verify this against an official TheFork source; treat as unconfirmed.
- **(3) Tracking parameter:** Not verified at all.
- **(7) Content/guide sites allowed:** Presumably yes for a restaurant-focused content site, but unconfirmed.
- **Relevance flag, independent of the above:** TheFork's restaurant-reservation footprint is overwhelmingly Europe-focused (France, Spain, Italy, Portugal, Benelux, Switzerland) with minimal-to-no presence in Thailand. **Low priority for a Chiang Mai/SE Asia guide regardless of how solvable the signup fragmentation turns out to be.**

**Confidence: Low across the board.** This is the weakest-verified entry in this reference, both because official sources were unreachable and because the program itself appears genuinely fragmented by region rather than me simply missing a page.

---

## 11. Amazon Associates (secondary — "what to pack" angle)

Makes sense as a **bolt-on, not a priority signup**, specifically for gear/packing-list content ("what to pack for Chiang Mai," mosquito repellent, packing cubes, universal adapters, etc.) where purchase intent is high and Amazon's checkout trust is universal.

- **(1) Signup:** https://affiliate-program.amazon.com/
- **(2) Approval:** Requires a live site with actual content before applying (Amazon reviews the site); also requires 3 qualifying sales within 180 days of joining to stay approved, or the account is closed (well-known program mechanic).
- **(3) Tracking parameter:** `tag=` — e.g. `https://www.amazon.com/dp/PRODUCTID?tag=YOUR-TAG-20`. (High confidence — this is extremely stable, long-documented Amazon Associates mechanics, not something that changes.)
- **(4) Commission:** Category-based, generally **1–10%** for most goods (the oft-cited "20%" figure applies only to the irrelevant Amazon Games category). **Luggage specifically sits at 4%** per current rate-card research; most general gear/outdoors items land in a similar 3–4% band. This is meaningfully lower than any travel-specific program in this reference.
- **(5) Cookie window:** **24 hours** from click. Important nuance: if the shopper adds an item to their cart within that 24-hour window, the sale still counts even if they don't check out until later — cart contents are tracked for up to ~90 days. But anything not added to cart within the first 24 hours earns nothing.
- **(6) Payout:** Direct deposit, check, or Amazon gift card; standard threshold ~$10 (gift card) to $100 (check), varies by method and region.
- **(7) Content/guide sites allowed:** Yes — this is the program's core use case.

**Practical caveat worth flagging:** Amazon Associates is country-specific (amazon.com vs. .co.uk vs. .de, separate accounts/tags per marketplace). An international audience needs a link-localizer (e.g. a service like Genius Link, or a custom redirect) to route each visitor to their local Amazon store and preserve attribution — real added engineering cost, not a copy-paste `tag=` situation once traffic is international.

**Confidence: High** on program mechanics (cookie, tag parameter, approval gate — all stable, well-documented); **Medium** on the specific 4%-for-luggage figure (single rate-card snapshot, Amazon revises this periodically).

---

## 12. Legal & disclosure requirements

Two genuinely separate things get conflated in a lot of affiliate-marketing advice — worth keeping distinct in implementation:

**FTC disclosure (US legal requirement, addressed to the reader, about money):**
The FTC's standard is "clear and conspicuous," evaluated on a 4-factor test: **Proximity** (close to the affiliate link/claim itself, not buried elsewhere), **Prominence** (large/visible enough to actually notice), **Presentation** (plain language, no jargon), **Placement** (visible *before* the reader reaches the link — not only reachable via a separate "disclosure" page, and not only at the bottom of a long article). For blog/guide content specifically: put a disclosure near the top of the page (above the fold if possible) in addition to (not instead of) it being near each cluster of affiliate links. This is a US legal requirement, not a suggestion; it applies regardless of where the *site owner* is based if US readers are a meaningful audience.

**`rel="sponsored"` (Google/SEO guideline, addressed to search engines, about link equity — NOT an FTC or legal requirement):**
Google's Search Central guidance explicitly asks sites to mark affiliate links with `rel="sponsored"` (or `rel="nofollow"`) so they aren't treated as an organic editorial "vote" for search-ranking purposes. This is a **webmaster guideline**, not law — Google has stated there's no direct ranking penalty for omitting it, but it's still best practice and low-cost to implement site-wide (`rel="nofollow sponsored"` is commonly used to satisfy both signals at once). **Separately, check each individual program's own affiliate terms of service** — some programs' own contracts (this varies by program and I did not verify each one's TOS text today) may independently require nofollow/sponsored-style tagging as a condition of staying in the program, which is a different obligation from Google's general ask. Build the link-generation helper to add `rel="sponsored nofollow noopener" target="_blank"` by default on every outbound affiliate link — cheap to do up front, and satisfies Google's guidance regardless of any individual program's specific contract language.

**Confidence: High** on the FTC 4-factor framework and the Google-vs-FTC distinction (both directly sourced from FTC guidance summaries and Google's own Search Central documentation). **Medium** on whether any specific program here contractually mandates nofollow tagging beyond Google's general guidance — not individually verified per-program today.

---

## 13. Travelpayouts vs. direct — final verdict

**Use Travelpayouts as the default on-ramp for everything except SafetyWing and TheFork.** The evidence gathered today shows no clear commission penalty for using the aggregator (Agoda and GetYourGuide match or beat direct-starter rates; Airalo pays identically either way), while the approval friction, payout-pooling, and single-dashboard advantages are real and material for a brand-new site. The honest tradeoff isn't "worse rates" — it's counterparty concentration (one more link in the payment chain) and the loss of upside from later negotiating a direct, higher, volume-based tier once the site has real traffic history. That's a "revisit in 6–12 months" concern, not a launch-day one.

**Go direct on day one only for:** SafetyWing (not on Travelpayouts at all, and its recurring-commission structure is uniquely valuable for nomad-guide content) — and optionally Amazon Associates once there's enough packing-list content to justify the integration engineering (link localization).

**Skip for now:** TheFork (weak Thailand relevance + fragmented, unverifiable signup path — revisit only if the site adds a serious European-market angle, which a Chiang Mai guide has no reason to).

---

## 14. Recommended signup order

Ranked for money-per-effort on a Chiang Mai/SE Asia guide launching now, given the site already has stays/food/transport content in progress:

1. **Travelpayouts** — one signup, covers Agoda + Booking.com + Hostelworld + Klook + GetYourGuide + 12Go + Airalo + Tripadvisor + Kiwi.com. Highest leverage single action available; do this first. Inside it, prioritize activating **12Go** (matches the existing transport-tours-nomad.md content directly, 50% commission), **Agoda/Booking.com/Hostelworld** (matches stays.md directly), then **GetYourGuide/Klook** (matches the "things to do"/cooking-class/temple-tour content).
2. **SafetyWing Ambassador** — direct signup, 5 minutes, no traffic minimum, the only recurring-commission program in this set, and a natural fit anywhere the site talks to digital nomads / long-stay travelers (which transport-tours-nomad.md already does).
3. **Airalo** (via Travelpayouts, already covered by #1 — call out separately only because eSIM is close to a universal purchase for every reader and deserves its own dedicated placement, e.g. in a "getting a Thai SIM/eSIM" or digital-nomad-guide section, not because it needs a separate signup).
4. **Amazon Associates** — low-effort bolt-on once a "what to pack for Chiang Mai" page exists; do not prioritize the international link-localization engineering until traffic is large enough to matter.
5. *(Later, not now)* **Revisit going direct with Agoda/Booking.com/Klook individually** once monthly booking volume through Travelpayouts is large enough that a brand's own account manager would offer a materially better negotiated tier than the shared network rate.
6. *(Skip / revisit only on a pivot)* **TheFork** — not worth the fragmented signup effort for a Thailand-focused guide today.

---

## Sources

- [Travelpayouts](https://www.travelpayouts.com/en/) · [Booking.com offer page](https://www.travelpayouts.com/en/offers/bookingcom-affiliate-program/) · [12Go offer page](https://www.travelpayouts.com/en/offers/12go-affiliate-program) · [Klook offer page](https://www.travelpayouts.com/en/offers/klook-affiliate-program/) · [ID/SubID help article](https://support.travelpayouts.com/hc/en-us/articles/203955653-ID-and-SubID-Affiliate-marker-and-additional-marker)
- [Agoda Partners signup](https://partners.agoda.com/en-us/signup)
- [Booking.com Affiliate Program](https://www.booking.com/affiliate-program/v2/index.html) · [en-GB version](https://www.booking.com/affiliate-program/v2/index.en-gb.html)
- [Hostelworld Partnerize signup](https://partners.hostelworld.com/) · [Partnerize clickref docs](https://help.phgsupport.com/hc/en-us/articles/4845024714269-Tracking-FAQ-s-Clickref-Pixel)
- [Klook Affiliate Program](https://affiliate.klook.com/home)
- [GetYourGuide Partner Program](https://partner.getyourguide.com/) · [Partner Resource Center](https://partner.getyourguide.support/hc/en-us)
- [12Go affiliate program](https://agent.12go.asia/) (vs. [12Go reseller/agent B2B program](https://reseller.12go.asia/), a different product)
- [Airalo Partners](https://partners.airalo.com/solutions/affiliates) · [Impact.com signup](https://app.impact.com/campaign-promo-signup/Airalo-The-Worlds-First-eSIM-store.brand)
- [SafetyWing Ambassador](https://safetywing.com/ambassador) · [Ambassador page](https://hello.safetywing.com/ambassador-page)
- [TheFork Sponsorship (consumer referral, not publisher affiliate)](https://www.thefork.com/sponsorship) · [Kwanko TheFork FR listing](https://www.kwanko.com/program-directory/program/affiliate/affiliation/The%20fork%20FR%20/77979/)
- [Amazon Associates](https://affiliate-program.amazon.com/)
- [FTC disclosure guidance summary](https://www.referralcandy.com/blog/ftc-affiliate-disclosure) · [Google Search Central — qualifying outbound links](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links)
