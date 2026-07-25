# Install the BOK Codex adapter.  Usage (from target repo root): pwsh <bok>/adapters/codex/install.ps1
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$agents = Join-Path $here "..\AGENTS.md"

if ((Test-Path "AGENTS.md") -and -not (Select-String -Path "AGENTS.md" -Pattern "BOK — AI 에이전트 운영 지침" -Quiet)) {
  "`n`n" | Add-Content "AGENTS.md"; Get-Content $agents | Add-Content "AGENTS.md"
  Write-Host "[bok] appended BOK section to existing AGENTS.md"
} elseif (-not (Test-Path "AGENTS.md")) {
  Copy-Item $agents "AGENTS.md"; Write-Host "[bok] wrote AGENTS.md"
} else { Write-Host "[bok] AGENTS.md already has BOK section" }

$dst = Join-Path $HOME ".codex\prompts"
New-Item -ItemType Directory -Force -Path $dst | Out-Null
Copy-Item "$here\prompts\*.md" $dst -Force
Write-Host "[bok] installed 6 prompts into ~/.codex/prompts/ (type / -> /bok-onboard, ...)"

# the 'bok' skill (shows up as a Codex skill)
$skill = Join-Path $HOME ".codex\skills\bok"
New-Item -ItemType Directory -Force -Path $skill | Out-Null
Copy-Item "$here\skills\bok\*" $skill -Recurse -Force
Write-Host "[bok] installed skill into ~/.codex/skills/bok/ (restart Codex to pick it up)"
Write-Host "[bok] ensure 'bok' is installed -> pip install -e <bok-framework>"
