#!/usr/bin/env sh
# Install the BOK GitHub Copilot adapter.
#   - .github/copilot-instructions.md  (Copilot custom instructions)
#   - AGENTS.md at repo root           (cross-tool; Copilot also reads it)
#   - .github/prompts/bok-*.prompt.md  (prompt files, IDE)
# Usage (from target repo root):  sh /path/to/bok/adapters/github-copilot/install.sh
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p .github/prompts
cp "$HERE/copilot-instructions.md" .github/copilot-instructions.md
cp "$HERE"/prompts/*.prompt.md .github/prompts/
if [ ! -f AGENTS.md ]; then cp "$HERE/../AGENTS.md" AGENTS.md; echo "[bok] wrote AGENTS.md"; fi
echo "[bok] installed .github/copilot-instructions.md + $(ls "$HERE"/prompts | wc -l) prompt(s)"
echo "[bok] ensure a 'bok' shim on PATH -> python <bok-framework>/cli/bok.py \"\$@\""
echo "[bok] then: ask Copilot '이 저장소 BOK로 이해해줘' or use /bok-onboard"
