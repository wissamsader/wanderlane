# Changelog

## 2026-08-17
Weekly guide: Barcelona, Beirut, Berlin, Palermo and Vietnam were tied for
fewest published articles (4 each, excluding Damascus by design). Per the
type ladder (where-to-stay → best-things-to-do → itinerary → best-time-to-
visit → getting-around → on-a-budget → day-trips-from), all five tied cities
already have a-c; none had a best-time-to-visit-* guide, so that's the type
this run adds. Picked Barcelona (first alphabetically among the tied
cities). Added `content/barcelona-auto.py` — **Best Time to Visit
Barcelona** (`/barcelona/best-time-to-visit-barcelona/`) — built only from
facts in `research/city-barcelona.md` §B6 (seasons, temperatures, the
August small-business-closure trade-off, Gràcia's Festa Major, and the
overtourism note already used elsewhere on the Barcelona hub).

Note on this run: this environment doesn't have the `BIZ_REPOS` local photo
source directory that `build.py`'s `eat_photo()`/`thumb_pool()` read from —
same issue as the 2026-08-09 run. A full `python3 build.py` here silently
replaces real business photos with placeholders/hero fallbacks across every
existing city page, not just Barcelona's. To avoid shipping that
regression, `docs/` was **not** bulk-rebuilt this run. Only the new
article's own output directory (`docs/barcelona/best-time-to-visit-
barcelona/`) was kept from the build; `docs/barcelona/index.html` (guide
count 5→6, new "Go deeper" card) and `docs/sitemap.xml` (new URL) were
hand-patched to match what a correct build would produce, using the same
photo (`barcelona-bodega-marin.jpg`, already committed in
`docs/assets/eats/`) that a real build's `thumb_pool()` rotation would have
picked. Every other existing page in `docs/` is untouched. Whoever runs
`build.py` next from a machine with `BIZ_REPOS` present should do a full
rebuild to reconcile any drift.

PIN NEEDED: pin-barcelona-best-time.png -> /barcelona/best-time-to-visit-barcelona/ (Barcelona)

## 2026-08-09
Weekly guide: Beirut had the fewest published articles (3) of any non-Damascus
city, and was missing an itinerary guide (where-to-stay and best-things-to-do
already existed). Added `content/beirut-auto.py` — **3 Days in Beirut: The
Perfect Itinerary** (`/beirut/3-days-in-beirut/`) — built only from facts in
`research/city-beirut.md`.

Note on this run: this environment doesn't have the `BIZ_REPOS` local photo
source directory that `build.py`'s `eat_photo()`/`thumb_pool()` read from, so
a full `python3 build.py` here silently drops real business photos (falls
back to placeholder cards) across *every* existing city page, not just
Beirut's. To avoid shipping that regression, `docs/` was **not** bulk-rebuilt
this run. Instead, only the new article's own output directory was kept from
the build, and `docs/beirut/index.html` (guide count + a new "Go deeper"
card) and `docs/sitemap.xml` (new URL) were hand-patched to match what a
correct build would produce. Every other existing page in `docs/` is
untouched. Whoever runs `build.py` next from a machine with `BIZ_REPOS`
present should do a full rebuild to reconcile any drift.

## 2026-08-10
no-op: all cities covered. Excluding Damascus, every non-Chiang-Mai city
(Barcelona, Beirut, Berlin, Palermo, Vietnam) is tied for fewest published
articles at 4 each, and every one of those tied cities already has a
where-to-stay-*, a best-things-to-do-*, and a 3-days/itinerary guide (plus a
where-to-eat guide). Per the priority rule, no new article was warranted
this run — no content files were added or modified.
