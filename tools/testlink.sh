#!/bin/bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
u="$1"
out=$(curl -s -o /dev/null -w "%{http_code}\t%{url_effective}" -L --max-redirs 8 --connect-timeout 15 -m 45 -A "$UA" -H "Accept-Language: en" "$u" 2>/dev/null)
code="${out%%	*}"; final="${out#*	}"
# homepage-bounce: original had a path/query but final is bare root
opath=$(python3 - "$u" <<'PY'
import sys,urllib.parse
p=urllib.parse.urlparse(sys.argv[1]); print((p.path or "/")+("?" if p.query else ""))
PY
)
fpath=$(python3 - "$final" <<'PY'
import sys,urllib.parse
p=urllib.parse.urlparse(sys.argv[1]); print((p.path or "/")+("?" if p.query else ""))
PY
)
tag="OK"
case "$code" in
  2*) if [ "$opath" != "/" ] && [ "$fpath" = "/" ]; then tag="BOUNCE"; fi ;;
  404|410) tag="BROKEN" ;;
  403|202|429|503) tag="BOTBLOCK" ;;
  000) tag="TIMEOUT" ;;
  *) tag="CHECK" ;;
esac
printf "%s\t%s\t%s\t%s\n" "$tag" "$code" "$u" "$final"
