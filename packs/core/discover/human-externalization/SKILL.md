---
name: human-externalization
description: 이해관계자의 암묵지를 인터뷰·Event Storming으로 끌어내 형식지 KU로 만든다. 조직 지식의 90%(tacit)를 다루는 discover 단계.
phase: discover
wraps: null   # 순수 LLM/사람 — CLI 결정론 부분 없음
---

# human-externalization

## When to use
코드로 알 수 없는 업무 규칙·운영 정책·"왜"가 필요할 때. SECI Externalization(research/03).

## Procedure (LLM + 사람)
1. **대상 식별**: `bok ready`의 gap + `code-archaeology`의 `## 열린 질문` + 버스팩터 높은 영역(단일 human 의존).
2. **가이드 생성**: 해당 영역의 **인터뷰 질문지** 또는 **Event Storming** 세션 가이드 작성(도메인 이벤트→bounded context, research/03/domain-modeling).
3. **표출**: 사람의 답변/워크숍 결과를 KU로 구조화 — provenance `kind: human, locator: interview/<id>`, confidence `inferred`(단일 발화) 또는 교차 시 `corroborated`.
4. **용어 수집**: 등장한 도메인 용어를 `glossary` KU(Ubiquitous Language)로.

## Output / handoff
human-provenance KU → curator/validator. code 근거와 **교차**되면 validate가 corroborated로 승격(cross-support).

## Boundaries
발화를 사실로 단정하지 않는다 — 1인 발화는 inferred. verified는 owner 서명 필요.
