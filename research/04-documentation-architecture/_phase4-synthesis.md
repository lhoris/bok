# Phase 4 통합 노트 — Documentation & Architecture

> 대상: arc42, ADR, C4 Model, Diátaxis
> 목적: Phase 3이 남긴 마지막 질문 — "지식 단위의 **내용**을 무엇으로 채우나(산출 스키마)" — 에 답한다.

---

## A. 답: 4개 표준이 BoK Model의 스키마를 층위별로 완성한다

Phase 4의 넷은 경쟁이 아니라 **상보적**이며, 합치면 BoK 지식 단위의 완전한 스키마가 된다.

| 표준 | 제공하는 것 | BoK Model에서의 역할 |
|-----|-----------|--------------------|
| **arc42** | 12섹션 = 시스템 이해의 **커버리지 체크리스트** | BoK **목차/완결성 게이트** (무엇을 알아야 하나) |
| **C4** | 구조의 **줌 레벨**(Context→Container→Component) | 구조 지식의 **progressive disclosure 층위** |
| **ADR** | 결정의 **Context·Decision·Consequences** | **"왜(rationale)" 지식 단위 스키마** |
| **Diátaxis** | need 기반 **4분면 타입**(Ref/Explanation/How-to/Tutorial) | 지식 단위의 **need-type 라벨 + 라우팅** |

교차 매핑이 자연스럽게 성립한다:
- arc42 §12 Glossary = DDD Ubiquitous Language = Diátaxis의 용어 축.
- arc42 §9 Decisions = ADR = Diátaxis **Explanation**.
- arc42 §3–8 (구조/런타임/배포) = C4 뷰 = Diátaxis **Reference**.
- arc42 §11 Risks = TDD 리스크 지도(Phase 2).

## B. 관통하는 공통 한계 = BOK의 존재 이유(4번째 확인)

넷 모두 **동일한 한계**를 가진다 — 그리고 이건 Phase 1·2·3에서 반복 확인된 바로 그 3대 공백이다:

1. **정적·수작업 저작** — 자동 발굴 없음.
2. **근거·confidence·검증 없음** — "썼는가"만 보장, "정확·검증됐는가"는 아님. → 부패 위험.
3. **"작성" ≠ "이해"** — 이해도를 측정하지 않음.

> 즉 Phase 4의 표준들은 **훌륭한 그릇(스키마)** 이지만, **채우고·검증하고·이해도를 재는 엔진이 없다.** BOK가 그 엔진이다.

## C. 가져올 자산

- **arc42 12섹션** → BoK 목차 + Readiness 커버리지 게이트(경량·선택적).
- **C4 4레벨(텍스트 DSL/Mermaid)** → 구조 지식 progressive disclosure + 저장소 거주.
- **ADR(+MADR 대안 필수)** → "왜" 지식 스키마 + confidence(Status) + 결정 사슬(KG 관계) + Adversarial Review 형식.
- **Diátaxis 4분면** → 지식 단위 need-type 라벨 + need 기반 라우팅(특히 Reference↔Explanation 분리).
