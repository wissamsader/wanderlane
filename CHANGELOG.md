# Changelog

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
