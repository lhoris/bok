#!/usr/bin/env sh
# Install the BOK Codex adapter.
#   - places AGENTS.md at the target repo root (Codex reads it)
#   - copies slash-command prompts into ~/.codex/prompts/
# Usage (from target repo root):  sh /path/to/bok/adapters/codex/install.sh
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"

# 1) AGENTS.md at repo root (append BOK section if AGENTS.md already exists)
if [ -f AGENTS.md ] && ! grep -q "BOK — AI 에이전트 운영 지침" AGENTS.md; then
  printf '\n\n' >> AGENTS.md; cat "$HERE/../AGENTS.md" >> AGENTS.md
  echo "[bok] appended BOK section to existing AGENTS.md"
elif [ ! -f AGENTS.md ]; then
  cp "$HERE/../AGENTS.md" AGENTS.md
  echo "[bok] wrote AGENTS.md"
else
  echo "[bok] AGENTS.md already has BOK section"
fi

# 2) slash-command prompts
mkdir -p "$HOME/.codex/prompts"
cp "$HERE"/prompts/*.md "$HOME/.codex/prompts/"
echo "[bok] installed 6 prompts into ~/.codex/prompts/ (use /bok-onboard, /bok-discover, ...)"
echo "[bok] ensure a 'bok' shim on PATH -> python <bok-framework>/cli/bok.py \"\$@\""
