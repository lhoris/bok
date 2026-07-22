# GitHub Copilot — BOK 사용 지침

이 저장소는 **BOK**(Body of Knowledge / Brownfield Onboarding)로 온보딩한다. 낯선 코드를 이해하거나("이 저장소 이해해줘"), 개발 전 컨텍스트가 필요할 때 아래 절차를 따르라.

## 황금률 — 결정론은 CLI, 추론은 너
먼저 `bok` CLI를 실행하고(재현 가능한 뼈대), 그 위에 추론만 얹어라. 검증·점수·게이트는 반드시 CLI가 판정한다. 사전조건: `bok` 커맨드(= `python <bok>/cli/bok.py` shim)가 PATH에 있어야 한다.

## 나선 절차 (각 단계: `bok` 실행 → 추론)
1. **discover**: `bok discover --scope <ctx> --source <dir>` → 이후 각 KU의 `## 열린 질문`을 채운다(hot 코드·커밋에서 "왜" 추론; 코드로 모르면 인터뷰 질문). provenance 필수, confidence는 inferred 유지.
2. **context**: `bok context --scope <ctx>` + `bok compile` → 타입 확정, kind별 본문(reference→arc42/C4, explanation→ADR+대안필수), TL;DR 필수.
3. **validate**: `bok validate --scope <ctx>` → 인용 코드가 주장을 뒷받침하는지 확인, 반례·대안 제기. `verified`는 사람 서명: `bok validate --sign <id> --owner <name>`.
4. **ready**: `bok ready --scope <ctx> --purpose <understand|feature|modernization>` → 리포트 해석 + 다음 발굴 제안. Hard gate FAIL이면 NOT READY(수치 뒤집기 금지).
5. **assemble**(개발 전): `bok assemble --scope <ctx> --goal "<작업>"` → Context Pack의 units + **gaps(모르는 것)** 를 근거로.

## 하드 규칙
- 근거(provenance) 없는 지식 금지 · confidence/score 지어내기 금지 · `verified`는 사람 서명뿐 · **gaps를 숨기지 마라**.

> 전체 지침: 저장소 루트 `AGENTS.md`. 세부 절차: `packs/core/**/SKILL.md`(Agent Skills).
