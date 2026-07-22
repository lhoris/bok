#!/usr/bin/env sh
# Install the BOK Claude Code adapter into the current repo's .claude/ dir.
# Usage (from target repo root):  sh /path/to/bok/adapters/claude-code/install.sh
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
DEST=".claude"
mkdir -p "$DEST/agents" "$DEST/commands"
cp "$HERE"/agents/*.md   "$DEST/agents/"
cp "$HERE"/commands/*.md "$DEST/commands/"
echo "[bok] installed 5 subagents + 6 commands into $DEST/"
echo "[bok] ensure a 'bok' shim on PATH -> python <bok-framework>/cli/bok.py \"\$@\""
echo "[bok] then run: /bok-onboard <scope> <purpose>"
