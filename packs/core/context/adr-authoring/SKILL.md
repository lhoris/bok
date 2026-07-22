---
name: adr-authoring
description: explanation/의사결정 지식을 ADR(Context·Decision·Consequences + 대안 필수)로 작성한다. 코드가 지우는 "왜"를 보존. context 단계.
phase: context
wraps: null
---

# adr-authoring

## When to use
설계 근거·업무 규칙의 "왜"를 기록할 때. research/04-documentation-architecture/adr (Nygard/MADR).

## Procedure (LLM)
1. **Context**: 문제·드라이버(기능·비기능).
2. **Decision**: 선택 + 근거.
3. **Considered Options**: 버려진 대안과 장단점 — **필수**(MADR). 왜 이 선택인지 이해하려면 대안이 필요.
4. **Consequences**: 결과·트레이드오프. 이것이 다음 결정의 Context가 된다(결정 사슬 → `derived-from`/`supersedes` 관계).
5. brownfield: 과거 결정을 코드/커밋에서 **역복원**할 때 provenance에 confidence(추론 vs 확인) 명시.

## Boundaries
대안 없는 ADR은 불완전(adversarial-review가 반려). 역복원 결정은 owner 서명 전 verified 금지.
