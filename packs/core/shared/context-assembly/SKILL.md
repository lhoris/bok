---
name: context-assembly
description: 특정 작업을 위해 관련 지식만 조립한 Context Pack(gaps 포함)을 만들어 태스크 에이전트에 전달한다. 공용 Skill.
phase: shared
wraps: bok assemble
---

# context-assembly

## When to use
AI(또는 사람)가 특정 개발 작업을 수행하기 전, 필요한 최소 지식을 모을 때. design/01 B.

## Procedure (CLI ↔ LLM)
1. **추론(LLM)**: 작업 목표에서 **핵심 용어·need(kind)·bounded context**를 뽑는다(관련성 정밀화 — 임베딩 없을 때 키워드 한계 보완).
2. **결정론(CLI)**: `bok assemble --scope <ctx> --goal "<goal>" --need <kind> --budget <N>` — filter→seed→relations 확장→예산 트림 → Context Pack.
3. **전달**: Pack의 `units`(L2/L3) + `warnings`(저confidence) + **`gaps`(모르는 것)** 를 태스크 에이전트에 준다.

## Output / handoff
Context Pack → 태스크 에이전트(자족 태스크 서술의 근거). `gaps`가 크면 작업 전 `bok discover` 재실행 권고.

## Boundaries
gaps를 숨기지 않는다 — AI는 **무엇을 모르는지 알고** 작업해야 한다(BOK 시그니처).
