# Knowledge Graph (+ LLM 기반 구축)

> Category: Knowledge Engineering · Phase 3 · KG construction / ontology / provenance

## 1. 왜 만들어졌는가?

흩어진 정보를 **엔티티와 관계의 그래프**로 표현하면, 사실 간 연결을 추론하고 질의할 수 있다. 최근에는 LLM이 텍스트에서 엔티티·관계를 추출해 **KG 구축을 자동화**하면서, "비정형 소스 → 구조화된 지식"의 실용 경로가 열렸다.

## 2. 어떤 문제를 해결하는가?

- 비정형 정보의 **구조화·연결** (사실 간 관계 표현)
- LLM 환각 완화 — KG로 **사실성(factuality) 접지(grounding)**
- 도메인 지식의 **질의 가능·추론 가능** 한 표현

## 3. 핵심 철학

- **엔티티 + 관계 + 속성**이 지식의 기본 단위.
- **온톨로지/스키마가 의미를 제약** — 클래스·카테고리·관계·속성을 형식적으로 정의해 일관성 확보.
- **Extract → Define → Canonicalize** — 추출한 엔티티/관계에 타입을 부여하고 정규화해 일관된 그래프로.

## 4. 구조 — LLM 기반 KG 파이프라인

- 텍스트를 청크로 분할 → LLM이 사용자 정의 프롬프트/스키마로 **엔티티·관계 추출**.
- **온톨로지 정렬(ontology alignment)** 로 품질 향상, chain-of-thought로 관계 추출 일관성 개선.
- **Canonicalization** — 동의어/중복 엔티티 병합.
- **Pruning** — 정보 이득(information gain) 기반 그래프 가지치기(노이즈 제거).
- 엔터프라이즈 특유 이슈: **기밀성** — 내부 정보를 외부에 공유 못 함(온프레미스/셀프호스팅 필요).

## 5. 장점 (BOK 관점)

- **BOK의 "relations" 필드를 정식으로 모델링하는 방법.** Phase 1/2에서 "지식 단위 = {내용+provenance+confidence+relations}"로 세웠는데, **relations를 어떻게 구조화하나**의 답이 여기 있다.
- **온톨로지/스키마 = BoK Model의 타입 시스템.** EA의 다층 뷰(비즈니스/앱/데이터/기술)를 KG 스키마로 형식화 가능.
- **LLM 자동 추출 파이프라인** — `bok.discover`가 소스에서 엔티티·관계를 뽑는 실행 방법(Extract→Define→Canonicalize).
- **Canonicalization/Pruning** — 발굴 노이즈를 정리해 신뢰 가능한 BoK로.
- **기밀성 요구** — BOK가 **vendor-neutral·셀프호스팅·로컬 우선** 이어야 하는 근거.

## 6. 단점 / 한계 (BOK 관점)

- **자동 추출의 정확도 문제** — LLM 추출은 오류·환각을 낳는다. **검증(validation) 없이는 위험** → BOK의 confidence·근거 검증이 필수임을 재확인.
- **그래프는 표현이지 이해가 아니다** — 방대한 트리플이 곧 "사람이 이해 가능"을 뜻하진 않는다(사람 친화적 서사·요약 필요).
- **온톨로지 설계 비용** — 과도하게 형식적이면 BOK의 단순성 원칙과 충돌.
- **이해도 측정은 여전히 부재.**

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **엔티티+관계+속성 + 온톨로지** 를 BoK Model의 **관계/타입 구조**로 채택(단, 경량).
- **Extract→Define→Canonicalize + Pruning** 을 `bok.discover`/`bok.context` 파이프라인으로.
- **셀프호스팅/기밀성** 원칙.

**개선할 것**
- 모든 추출 트리플에 **provenance(어느 소스·청크에서) + confidence(추출 신뢰)** 를 필수 부착 → "자동 추출의 부정확"을 검증 가능한 형태로.
- 그래프 위에 **Progressive Disclosure 서사 레이어**([[claude-code-skills]]) — 사람은 요약을, AI는 그래프를 소비.
- 온톨로지를 **최소한으로**(BOK 필수 타입만) — over-engineering 회피.

---

### Evidence
- NVIDIA Technical Blog, "Insights, Techniques, and Evaluation for LLM-Driven Knowledge Graphs" — https://developer.nvidia.com/blog/insights-techniques-and-evaluation-for-llm-driven-knowledge-graphs/
- "Ontology-grounded Automatic KG Construction by LLM under Wikidata schema" (arXiv) — https://arxiv.org/pdf/2412.20942
- Medium(Branzan), "From LLMs to Knowledge Graphs: Building Production-Ready Graph Systems" — https://medium.com/@claudiubranzan/from-llms-to-knowledge-graphs-building-production-ready-graph-systems-in-2025-2b4aff1ec99a
