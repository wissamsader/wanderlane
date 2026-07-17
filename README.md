# Wanderlane

Honest, on-the-ground city guides — where to eat, where to stay, and what's actually worth your time.
Chiang Mai · Beirut · Barcelona · Palermo · Berlin · Da Nang & Hoi An · Damascus.

**Live:** https://wissamsader.github.io/wanderlane/

## How it's built
A small static-site generator. Content lives in `content/*.py`; `build.py` renders it into `docs/`
(served by GitHub Pages). The design system is in `static/`. Research notes are in `research/`.

```bash
python3 build.py     # rebuild docs/
./deploy.sh          # build + push live
```

Add a city or guide by dropping a file in `content/` (copy `content/chiangmai.py` as the template),
then rebuild. Guides feature real, independently-run local businesses; some outbound booking links are
affiliate links (see the site's disclosure page).
