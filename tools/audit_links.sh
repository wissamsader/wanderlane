#!/bin/bash
# Wanderlane outbound-link audit — run after ANY change touching links/aff config.
# Tests every unique external href in docs/ with a browser UA, follows redirects,
# flags 404s and homepage-bounces. BOTBLOCK (403/202) entries need a one-time
# real-browser check per URL FORMAT (GYG + Klook affiliate verified 2026-07-20).
cd "$(dirname "$0")/.."
grep -rho 'href="https\?://[^"]*"' docs/ | sed 's/^href="//;s/"$//;s/&amp;/\&/g' | sort -u > /tmp/wl_links.txt
echo "Testing $(wc -l < /tmp/wl_links.txt) unique external links..."
xargs -P 8 -n 1 tools/testlink.sh < /tmp/wl_links.txt > /tmp/wl_audit.tsv 2>/dev/null
cut -f1 /tmp/wl_audit.tsv | sort | uniq -c
echo "--- problems (excluding font preconnects):"
grep -Ev "^OK|fonts\.g" /tmp/wl_audit.tsv | grep -E "^(BROKEN|BOUNCE|CHECK|TIMEOUT)" | cut -f1-3 || echo "none"
