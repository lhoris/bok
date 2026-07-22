---
name: grounding-check
description: KU의 주장이 provenance 근거와 실제로 일치하는지 검증한다. 파일 존재(CLI) + 의미적 뒷받침(LLM). validate 단계.
phase: validate
wraps: bok validate
---

# grounding-check

## When to use
지식을 신뢰하기 전, 근거 접지를 확인할 때. research/03/knowledge-base-and-llm-wiki(소스 접지).

## Procedure (CLI ↔ LLM)
1. **결정론(CLI)**: `bok validate --scope <ctx>` — provenance 파일 존재 검사. 없으면 강등(→unverified).
2. **추론(LLM, 의미적 grounding)**: 파일이 **존재**하는 것과 주장을 **뒷받침**하는 것은 다르다.
   - 인용한 코드/문서를 실제로 읽고, KU 주장이 거기서 도출되는지 확인.
   - 불일치·과장·낡음 발견 시 강등 제안 + `## 열린 질문`에 기록.

## Output
grounding 통과/실패 → confidence 전이 입력. 실패는 validation-report에.

## Boundaries
"파일이 있다" ≠ "검증됐다". 의미 검증 없이 승격 금지.
