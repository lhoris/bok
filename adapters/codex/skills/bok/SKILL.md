---
name: "bok"
description: "Onboard and understand an unfamiliar/legacy/brownfield codebase by building a validated Body of Knowledge with the `bok` CLI. Use when the user asks to understand, onboard, map, or explain an existing repository or subsystem before developing or modernizing it (e.g. 'onboard this repo', 'what does this system do', 'map this legacy code'), or before starting a feature/modernization on code you do not yet understand. Runs the deterministic `bok` engine (discover, context, validate, ready) and layers reasoning (business rules, the 'why') on top. Do NOT use for greenfield code generation or when the codebase is already well understood."
---

# BOK - Brownfield Onboarding Skill

Bring an unfamiliar codebase to an understood -> development-ready state. The deterministic
work is done by the `bok` CLI; you add the reasoning on top. (Instructions in English on
purpose - Windows agents can mangle non-ASCII skill text.)

## Prerequisite
The `bok` command must be available (`pip install -e <bok-framework>`). If it is missing,
tell the user to install it first.

## Golden rule
ALWAYS run the `bok` CLI first, then add reasoning. Validation, scores and gates are decided
by the CLI - never invent them.

## Quick start (one command)
When the user asks to understand/onboard a repo, run from the repo root:
```
bok onboard . --scope <ctx> --source <source-dir>
```
This runs init -> discover -> context -> compile -> ready in one pass. Use a short `<ctx>`
like `core`; `<source-dir>` is the real code path (`.`, `src`, etc.). Output lands in `bok/`
plus `bok/_system/readiness-report.md`.

## Then (fill the gaps with reasoning)
1. Read the `## Open questions` section in each generated `bok/<ctx>/**/*.md` - these are the
   things code alone cannot reveal.
2. Infer business rules and intent from hot code, commits and issues, and write them as
   knowledge units (each needs `provenance`; keep `confidence: inferred`).
3. If code cannot tell you, propose interview questions for the user.

## Validate & assess
- `bok validate . --scope <ctx>` - grounding + cross-support promotion.
- `verified` promotion requires a human signature: `bok validate . --sign <id> --owner <name>`.
  Never auto-promote to verified.
- `bok ready . --scope <ctx> --purpose <understand|feature|modernization>` - hard gate, score,
  tier. If it says NOT READY, do not override the numbers; feed the gaps into the next discover.

## Assemble context for a task
Before coding: `bok assemble . --scope <ctx> --goal "<task>"` and use the returned units plus
the explicit `gaps` (what is not known).

## Hard rules
No knowledge without provenance. Never invent confidence/scores. `verified` needs a human
signature. Never hide gaps.

## Commands
init, discover, context, compile, validate, ready, assemble, status.
