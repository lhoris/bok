# arc42

> Category: Documentation & Architecture · Phase 4 · 아키텍처 문서 템플릿

## 1. 왜 만들어졌는가?

아키텍처를 "어디에 무엇을 쓸지" 매번 새로 고민하는 낭비를 없애기 위해, **아키텍처 소통·문서화의 표준 골격**으로 만들어졌다. 백지의 공포 대신 검증된 12개 섹션을 채우면 된다.

## 2. 어떤 문제를 해결하는가?

- 아키텍처 문서의 **구조 부재**(무엇을 어디에 쓸지)
- 이해관계자 간 **소통 표준**의 부재
- 지식의 **누락 방지**(체크리스트로서의 목차)

## 3. 핵심 철학

- **표준 골격 + 전 섹션 선택적(optional).** 필요한 것만 채운다(경량·실용).
- **소통 우선.** 문서는 이해관계자 소통 수단.
- **품질을 시나리오로.** 품질 목표를 시나리오·품질 트리로 구체화.

## 4. 구조 — 12 섹션

1 Introduction & Goals(품질 목표·이해관계자) · 2 Constraints · 3 Context & Scope · 4 Solution Strategy · 5 **Building Block View**(정적 분해, 필수·계층적) · 6 Runtime View(시나리오) · 7 Deployment View · 8 Cross-cutting Concepts · 9 **Architecture Decisions**(→ ADR) · 10 Quality Requirements(시나리오·품질 트리) · 11 **Risks & Technical Debt** · 12 **Glossary**(도메인·기술 용어).

## 5. 장점 (BOK 관점)

- **BoK Model의 "내용 스키마" 후보.** Phase 3이 남긴 질문("지식 단위의 내용을 무엇으로 채우나")에 대한 **검증된 목차** — 시스템을 이해했다는 것이 무엇을 아는 것인지의 체크리스트.
- **12섹션 = 이해 커버리지 게이트.** TDD 체크리스트(Phase 2)와 결합해 **Development Readiness의 "무엇을 알아야 완결인가"** 를 정의.
- **명시적 섹션들이 BOK 요구와 정확히 대응**: §12 Glossary=Ubiquitous Language, §9 Decisions=ADR/"왜", §11 Risks=TDD 리스크 지도, §3 Context=C4 Context.
- **전 섹션 optional = 단순성.** 필요한 만큼만.

## 6. 단점 / 한계 (BOK 관점)

- **정적 문서 · 수작업.** 사람이 작성하는 전제. 자동 발굴·검증·AI 소비를 상정하지 않음.
- **생성물의 근거·confidence 없음** — 섹션을 채웠다고 정확·검증된 것은 아님.
- **부패 위험** — 코드와 동기화 메커니즘 부재(Phase 2 카탈로그 부패와 동일 문제).
- **"이해했는가"가 아니라 "썼는가"** 만 보장.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **12섹션을 BoK Model의 표준 내용 스키마/커버리지 체크리스트로 채택**(단, 경량·선택적 유지).
- §12 Glossary·§9 Decisions·§11 Risks를 BOK 필수 산출물과 직접 매핑.
- **품질을 시나리오로** 표현하는 방식.

**개선할 것**
- **정적 문서 → 발굴로 자동 초안 생성 + 검증**: 각 섹션을 `bok.discover`가 근거에서 채우고 `bok.validate`가 검증.
- 각 섹션 항목에 **provenance·confidence·last-verified**.
- "작성 완료"가 아니라 **"검증된 이해 커버리지"** 로 Readiness 판정.

---

### Evidence
- arc42 Template Overview — https://arc42.org/overview
- arc42 Documentation, "Introduction and Goals" — https://docs.arc42.org/section-1/
- arc42/arc42-template (GitHub) — https://github.com/arc42/arc42-template
