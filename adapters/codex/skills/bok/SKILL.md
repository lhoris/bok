---
name: "bok"
description: "Onboard and understand an unfamiliar/legacy/brownfield codebase by building a validated Body of Knowledge with the `bok` CLI. Use when the user asks to understand, onboard, map, or explain an existing repository or subsystem before developing or modernizing it — e.g. '이 저장소 이해해줘/온보딩해줘', 'what does this system do', 'map this legacy code', or before starting a feature/modernization on code you don't yet understand. Runs the deterministic `bok` engine (discover→context→validate→ready) and layers reasoning (business rules, the 'why') on top. Do NOT use for greenfield code generation or when the codebase is already well understood."
---

# BOK — Brownfield Onboarding Skill

낯선 코드베이스를 **이해 가능 → 개발 가능** 상태로 끌어올린다. 결정론은 `bok` CLI가, 추론은 네가 맡는다.

## 사전조건
`bok` 커맨드가 있어야 한다(= `pip install -e <bok-framework>`). 없으면 사용자에게 설치를 먼저 안내하라.

## 황금률
**항상 `bok` CLI를 먼저 실행하고, 그 위에 추론만 얹어라.** 검증·점수·게이트는 CLI가 판정한다 — 지어내지 마라.

## 빠른 시작 (원커맨드)
사용자가 "이 저장소 이해/온보딩해줘"라고 하면:
```
bok onboard . --scope <ctx> --source <소스디렉터리>
```
→ init→discover→context→compile→ready 1회전을 한 번에 돈다. `<ctx>`는 core 등 짧은 이름, `<소스디렉터리>`는 실제 코드 경로(예: `src`, `posco_std_source`). 결과는 `bok/` 폴더 + `bok/_system/readiness-report.md`.

## 그다음 (추론으로 채우기)
1. 생성된 `bok/<ctx>/**/*.md`의 `## 열린 질문`("코드로 알 수 없는 왜")을 읽는다.
2. hot 코드·커밋·이슈에서 업무 규칙·의도를 **추론**해 채운다(각 지식에 provenance 필수, confidence는 inferred 유지).
3. 코드로 알 수 없으면 사용자에게 물을 **인터뷰 질문**을 제시한다.

## 검증·판정
- `bok validate . --scope <ctx>` — 근거 grounding·cross-support 승격.
- `verified` 승격은 사람 서명뿐: `bok validate . --sign <id> --owner <이름>`. **자동 금지.**
- `bok ready . --scope <ctx> --purpose <understand|feature|modernization>` — Hard gate·score·Tier. FAIL이면 NOT READY(수치 뒤집기 금지). gap을 다음 discover 우선순위로.

## 작업용 컨텍스트
개발 전: `bok assemble . --scope <ctx> --goal "<작업>"` → units + **gaps(모르는 것)** 를 근거로.

## 하드 규칙
근거 없는 지식 금지 · confidence/score 지어내기 금지 · verified는 사람 서명 · **gaps를 숨기지 마라**.

## 개별 커맨드
init · discover · context · compile · validate · ready · assemble · status. 슬래시 커맨드로도 노출됨(`/bok-onboard` 등, `~/.codex/prompts/`).
