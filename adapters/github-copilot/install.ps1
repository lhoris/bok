# Install the BOK GitHub Copilot adapter. Usage (from target repo root): pwsh <bok>/adapters/github-copilot/install.ps1
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
New-Item -ItemType Directory -Force -Path ".github\prompts" | Out-Null
Copy-Item "$here\copilot-instructions.md" ".github\copilot-instructions.md" -Force
Copy-Item "$here\prompts\*.prompt.md" ".github\prompts\" -Force
if (-not (Test-Path "AGENTS.md")) { Copy-Item (Join-Path $here "..\AGENTS.md") "AGENTS.md"; Write-Host "[bok] wrote AGENTS.md" }
Write-Host "[bok] installed .github/copilot-instructions.md + prompts"
Write-Host "[bok] ensure a 'bok' shim on PATH -> python <bok-framework>/cli/bok.py args"
Write-Host "[bok] then: ask Copilot to onboard the repo with BOK, or use /bok-onboard"
