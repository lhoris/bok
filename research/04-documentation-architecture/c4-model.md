# C4 Model

> Category: Documentation & Architecture · Phase 4 · Simon Brown (2006–2011)

## 1. 왜 만들어졌는가?

UML 같은 무거운 표기는 배우기 어렵고 이해관계자와 소통하기 힘들다. C4는 **소수의 추상화 + 다이어그램 유형** 으로 아키텍처를 **줌인/줌아웃** 하며 기술·비기술 청중 모두에게 설명하기 위해 만들어졌다.

## 2. 어떤 문제를 해결하는가?

- 아키텍처 시각화의 **복잡성·진입장벽**(UML 대비)
- **추상화 수준 혼재** — 한 그림에 모든 것을 욱여넣는 문제
- 청중별 **적정 상세도** 제공

## 3. 핵심 철학

- **단순성·유연성.** 배우기·그리기·설명하기 쉬운 최소 추상화.
- **줌 레벨(계층적 상세화).** 지도처럼 축척을 바꿔 본다.
- **하나의 모델, 여러 뷰.**

## 4. 구조 — 4 레벨

1. **Context** — 시스템과 사용자·외부 시스템의 관계(최상위 조망).
2. **Container** — 시스템을 앱/데이터스토어 단위로 분해.
3. **Component** — 컨테이너 내부를 컴포넌트로 분해.
4. **Code**(선택, 거의 안 씀) — 클래스/ER 등 UML 수준.

## 5. 장점 (BOK 관점)

- **Progressive Disclosure의 아키텍처 버전.** Phase 1(Skills)의 "인덱스→요약→상세"를 **구조 지식에 그대로 적용** — BoK Model의 구조 뷰를 레벨로 층화.
- **arc42보다 경량한 다층 뷰** — EA(TOGAF)의 무거움 없이 비즈니스↔컨테이너↔컴포넌트를 표현. BOK 단순성 원칙과 정합.
- **Context 레벨 = 이해의 출발점** — 낯선 시스템 온보딩에서 가장 먼저 필요한 "이 시스템은 무엇과 연결되는가".
- **텍스트로 표현 가능(Structurizr/DSL, Mermaid)** — 저장소 거주·버전 관리·AI 생성에 적합.

## 6. 단점 / 한계 (BOK 관점)

- **구조(정적) 중심** — 업무 규칙·데이터 의미·운영 정책·"왜"는 다루지 않음(arc42/ADR/DDD가 보완).
- **수작업 작도 전제** — 자동 발굴·최신화·검증 없음(부패 위험).
- **다이어그램은 표현이지 검증된 지식이 아님** — 그럴듯한 그림의 함정.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **4레벨(특히 Context/Container/Component)을 BoK 구조 지식의 progressive disclosure 층위로 채택.**
- **텍스트 기반 다이어그램(DSL/Mermaid)** → 저장소 거주·AI 생성·버전 관리.
- **Context-first** → 발굴/온보딩의 시작점.

**개선할 것**
- **코드/의존성에서 C4 뷰를 자동 생성**([[../02-enterprise-onboarding/software-archaeology]]의 의존성 복원 + [[../03-knowledge-engineering/knowledge-graph]] 관계) + provenance/confidence + 사람 검증.
- 다이어그램 노드를 **BoK 지식 단위와 링크**(그림↔검증된 지식 상호참조).

---

### Evidence
- C4 model 공식 사이트 — https://c4model.com/
- Wikipedia, "C4 model" — https://en.wikipedia.org/wiki/C4_model
- IcePanel, "What is the C4 model?" — https://icepanel.io/blog/2024-07-18-what-is-the-c4-model
