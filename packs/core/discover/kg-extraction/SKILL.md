---
name: kg-extraction
description: 텍스트·코드·문서에서 엔티티와 관계를 추출해 지식 그래프 간선을 만든다. Extract→Define→Canonicalize. discover/context 단계.
phase: discover
wraps: null
---

# kg-extraction

## When to use
KU 간 관계(의존·정의·결정 사슬)를 구조화해야 할 때. research/03-knowledge-engineering/knowledge-graph.

## Procedure (LLM)
1. **Extract**: 대상 텍스트에서 엔티티(컴포넌트·용어·결정)와 관계 후보 추출.
2. **Define**: BOK 관계 타입으로 매핑(`depends-on`/`derived-from`/`defines-term`/`decides`/`contradicts`…). 최소 집합만(오버엔지니어링 경계).
3. **Canonicalize**: 동의 엔티티 병합, 기존 KU id로 정렬. 새 관계는 `relations`에 **id 참조**로 기록.

## Output / handoff
KU frontmatter의 `relations` 갱신 → `bok compile`이 graph로 컴파일하고 dangling 검출.

## Boundaries
추론한 관계에도 근거를 남긴다. `contradicts`는 임의로 만들지 말고 실제 충돌만(validate가 검토).
