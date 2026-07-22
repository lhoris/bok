---
name: arc42-authoring
description: reference 지식의 본문을 arc42/C4 구조로 작성한다 — 컨텍스트·빌딩블록·런타임·배포. context 단계.
phase: context
wraps: null
---

# arc42-authoring

## When to use
구조 지식(reference)을 사람+AI가 읽을 표준 형식으로 정리할 때. research/04-documentation-architecture/arc42, /c4-model.

## Procedure (LLM)
1. KU의 `layer`에 맞는 arc42 섹션을 채운다: context-and-scope(§3), building-blocks(§5, C4 Container/Component), runtime-behavior(§6), deployment(§7).
2. 구조는 **텍스트 다이어그램(Mermaid/C4 DSL)** 으로 — 저장소 거주·버전 관리·progressive disclosure.
3. `## TL;DR`(200자)을 반드시 작성 — Context L2에서 이것만 로드된다.

## Boundaries
근거(provenance) 있는 사실만. 추정은 `## 열린 질문`으로. 다이어그램은 검증된 지식이 아니라 표현이므로 confidence는 별도.
