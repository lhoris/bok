# Install the BOK Claude Code adapter into the current repo's .claude/ dir.
# Usage (from target repo root):  pwsh <bok>/adapters/claude-code/install.ps1
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$dest = ".claude"
New-Item -ItemType Directory -Force -Path "$dest/agents", "$dest/commands" | Out-Null
Copy-Item "$here/agents/*.md"   "$dest/agents/"   -Force
Copy-Item "$here/commands/*.md" "$dest/commands/" -Force
Write-Host "[bok] installed 5 subagents + 6 commands into $dest/"
Write-Host "[bok] ensure a 'bok' shim on PATH -> python <bok-framework>/cli/bok.py args"
Write-Host "[bok] then run: /bok-onboard <scope> <purpose>"
