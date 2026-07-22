---
name: coverage-assessment
description: coverage 격자와 Readiness 판정을 해석하고 다음 발굴 우선순위를 제안한다. ready 단계.
phase: ready
wraps: bok ready
---

# coverage-assessment

## When to use
"충분히 이해했는가"를 판정하고 다음 나선을 계획할 때. design/04.

## Procedure (CLI ↔ LLM)
1. **결정론(CLI)**: `bok ready --scope <ctx> --purpose <p>` — 신호등·Hard gate·score·Tier(전부 수치).
2. **추론(LLM)**:
   - readiness-report를 **서사로 해석**(리더 대상, 인지 부하↓).
   - gap 목록에 **위험·버스팩터 가중**을 얹어 다음 `bok discover` 우선순위 제안.
   - purpose→tier 매핑의 잔여 리스크를 명시.

## Output / handoff
next-discover 우선순위 → `bok-orchestrator`(나선 D8). verdict → 사람 리더 승인.

## Boundaries
수치를 뒤집지 않는다 — Hard gate FAIL이면 READY라 말할 수 없다. 주관 금지.
