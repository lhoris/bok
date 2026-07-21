# Enterprise Architecture (TOGAF / ArchiMate)

> Category: Enterprise Onboarding · Phase 2 · TOGAF(방법론) + ArchiMate(모델링 언어)

## 1. 왜 만들어졌는가?

대규모 조직은 비즈니스·데이터·애플리케이션·기술이 얽힌 거대한 랜드스케이프를 가진다. Enterprise Architecture(EA)는 이 전체를 **일관된 방법으로 기술·정렬**해, 전략과 시스템을 연결하고 의사결정을 지원하기 위해 발전했다.

## 2. 어떤 문제를 해결하는가?

- 조직 전체 시스템·역량의 **전체 조망(landscape) 부재**
- 비즈니스 목표와 IT의 **정렬(alignment)** 문제
- 이해관계자 간 **소통 언어**의 부재

## 3. 핵심 철학

- **다층 모델링** — 비즈니스 / 데이터·정보 / 애플리케이션 / 기술 레이어를 분리·연결.
- **역량 중심(Capability-centric)** — 조직이 "무엇을 할 수 있는가"를 먼저 그린다.
- **표준 방법론(TOGAF ADM)** + **표준 표기(ArchiMate)** 의 결합.

## 4. 구조

- **TOGAF** — Architecture Development Method(ADM), 반복적 아키텍처 개발·거버넌스 방법론.
- **ArchiMate** — 컴포넌트와 관계의 그래픽 표기 언어(TOGAF와 상보적).
- **Business Capability Map** — 조직 역량을 시각화, 전략 정렬·격차(gap) 식별·이해관계자 소통의 기반. ADM의 핵심 산출물.
- **Information Mapping** — 정보/데이터를 역량·기능에 매핑.

## 5. 장점 (BOK 관점)

- **다층 모델(비즈니스↔앱↔데이터↔기술)** — BOK의 BoK Model이 "코드 + 데이터 모델 + 업무 + 운영 정책"을 층으로 담아야 한다는 요구에 대응하는 검증된 구조.
- **Capability Map** — 코드보다 상위의 **업무/역량 관점** 을 제공. BOK가 "업무 용어·업무 규칙"을 다루는 데 필요한 상위 뷰.
- **Gap 식별** — "무엇을 아직 모르는가/부족한가"를 드러내는 발상 → BOK 이해도 평가의 힌트.
- **이해관계자 소통 언어** — 사람+AI 공유 지식의 목표와 정합.

## 6. 단점 / 한계 (BOK 관점)

- **무겁고 하향식(top-down)·문서 중심.** 대규모 선행 모델링을 요구 → BOK의 "단순성 우선"과 충돌. 실무에서 낡고 실제와 괴리되기 쉽다(ivory tower 비판).
- **정적·수작업.** 자동 발굴·근거 검증·AI 소비를 전제로 하지 않는다.
- **온보딩 속도**가 목표가 아니라 **전략적 거버넌스**가 목표 — BOK의 실용적 온보딩 초점과 다르다.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **다층 뷰(비즈니스/애플리케이션/데이터/기술)** → BoK Model의 지식 유형/레이어 골격.
- **Capability Map 개념** → 코드 위의 "업무 역량" 지식 유형.
- **Gap 식별** → Development Readiness의 "무엇을 아직 모르는가" 평가.

**개선할 것**
- **하향식·대규모 선행 모델링을 버린다.** BOK는 **상향식·증거 기반·점진적**으로 같은 다층 뷰를 구성(archaeology로 캐내고 필요한 만큼만).
- **정적 문서 → 살아있는 검증된 지식**(provenance·confidence).
- 무게를 덜어 **경량·실용** 유지.

---

### Evidence
- Visual Paradigm, "ArchiMate Capability Map in TOGAF" — https://guides.visual-paradigm.com/understanding-and-creating-an-archimate-capability-map-in-togaf/
- TOGAF Series Guide: Information Mapping (Open Group) — https://pubs.opengroup.org/togaf-standard/business-architecture/information-mapping.html
- KnowledgeHut, "TOGAF Business Capability Model" — https://www.knowledgehut.com/blog/it-service-management/business-capability-modelling
