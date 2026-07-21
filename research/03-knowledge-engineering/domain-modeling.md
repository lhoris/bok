# Domain Modeling (Domain-Driven Design)

> Category: Knowledge Engineering · Phase 3 · DDD (Evans)

## 1. 왜 만들어졌는가?

소프트웨어의 진짜 복잡성은 기술이 아니라 **도메인(업무)** 에 있다. 개발자와 업무 전문가가 서로 다른 언어를 쓰면 지식이 번역 과정에서 소실된다. DDD는 **업무 지식을 코드·설계와 정렬**하기 위한 방법론이다.

## 2. 어떤 문제를 해결하는가?

- 개발자 ↔ 업무 전문가의 **언어 단절**(용어 모호성)
- 대규모 시스템에서 **용어 의미의 불일치**
- 업무 지식이 설계·코드로 **충실히 전달되지 않는 문제**

## 3. 핵심 철학

- **Ubiquitous Language(유비쿼터스 언어)** — 개발자·업무 전문가·이해관계자가 공유하는 **단일 어휘**. 코드·테스트·대화가 모두 같은 용어.
- **Knowledge Crunching** — 업무 전문가와 **직접 소통**하며 지식을 정제. 번역은 지식 정제를 빈혈 상태로 만든다.
- **Bounded Context** — 특정 모델의 용어가 **일관된 의미**를 갖는 경계.

## 4. 구조

- **Ubiquitous Language** — 도메인 어휘 사전(용어·의미).
- **Bounded Context** — 모델 경계 분리로 용어 일관성 보존.
- **Context Mapping** — 경계 간 관계 매핑.
- **Event Storming** — 협업 워크숍으로 도메인 이벤트를 발견·모델링 → 클러스터가 bounded context로 형식화. **암묵지를 끌어내는 실전 발굴 기법**.

## 5. 장점 (BOK 관점)

- **BOK가 반드시 산출해야 할 "업무 용어 사전"의 방법론.** 헌장이 지목한 "업무 용어를 모른다" 문제의 정면 해법 = **Ubiquitous Language**.
- **Bounded Context = BoK Model의 지식 경계/모듈화 단위.** 방대한 엔터프라이즈 지식을 의미 일관 영역으로 분할하는 검증된 방법(→ progressive disclosure 라우팅과 결합).
- **Event Storming = 암묵지 발굴 워크숍** — SECI Externalization의 구체적 실행 기법. `bok.discover`의 인적 발굴 도구.
- **Knowledge Crunching(번역 없는 직접 정제)** — BOK의 "근거 우선, 추측 배제"와 정합.

## 6. 단점 / 한계 (BOK 관점)

- **사람 집약적·수작업.** Event Storming·knowledge crunching은 워크숍 기반 → 확장·자동화가 어려움(최근 LLM 프롬프트 프레임워크로 자동화 시도 중).
- **신규 설계(greenfield) 지향이 강함** — 기존 시스템에서 **역방향으로** Ubiquitous Language를 복원하는 절차는 약함(코드→용어 추출).
- **검증·confidence·이해도 측정 부재.**
- 실무 적용 난이도·오버헤드가 크다는 실증 연구 존재.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **Ubiquitous Language를 BoK Model의 필수 산출물("도메인 용어집")로 채택.**
- **Bounded Context를 BoK의 지식 경계/모듈 단위**로 — KG 온톨로지·progressive disclosure 라우팅과 결합.
- **Event Storming을 `bok.discover`의 인적 발굴 기법**으로(SECI Externalization 실행).
- **Knowledge Crunching** 정신 — 직접 근거에서 정제.

**개선할 것**
- **역방향 복원 추가**: 기존 코드·DB·로그에서 **Ubiquitous Language 후보를 자동 추출**(archaeology + KG extract) 후 사람이 검증 → greenfield 편향 극복.
- 용어·컨텍스트에 **provenance·confidence** 부착.
- 워크숍 산출물을 **구조화 지식 단위**로 자동 변환(사람 집약 완화).

---

### Evidence
- O'Reilly, "Context Mapping — What Is Domain-Driven Design?" — https://www.oreilly.com/library/view/what-is-domain-driven/9781492057802/ch04.html
- IBM Cloud Architecture Center, "Domain Driven Design"(Event Storming→bounded context) — https://ibm-cloud-architecture.github.io/refarch-eda/methodology/domain-driven-design/
- Domain-Driven Design Reference (Evans) — https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
