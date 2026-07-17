#!/bin/bash
# Wanderlane — rebuild and publish to GitHub Pages (wissamsader/wanderlane, served from /docs).
set -e
ROOT="$HOME/CLAUDE-DEEPSEEK/wanderlane"
cd "$ROOT"

echo "→ building…"
/opt/homebrew/bin/python3 build.py

if [ ! -d .git ]; then
  git init -q
  git branch -M main
  git remote add origin https://github.com/wissamsader/wanderlane.git
fi
git add -A
git commit -q -m "Deploy Wanderlane $(date '+%Y-%m-%d %H:%M')" || { echo "nothing new to deploy"; exit 0; }
git push -q -u origin main
echo "✓ pushed — live in ~1 min at https://wissamsader.github.io/wanderlane/"
