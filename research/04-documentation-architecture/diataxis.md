# Diátaxis

> Category: Documentation & Architecture · Phase 4 · Daniele Procida

## 1. 왜 만들어졌는가?

문서가 뒤죽박죽인 근본 원인은 **서로 다른 사용자 need를 한데 섞기 때문**이다. Diátaxis는 "무엇을 쓸지/어떻게 쓸지/어떻게 조직할지"를 **사용자 need의 구조**로 풀어낸다.

## 2. 어떤 문제를 해결하는가?

- 문서의 **내용(what) · 문체(how) · 구조(organise)** 문제를 동시에
- 학습·문제해결·조회·이해라는 **이질적 need의 혼재**

## 3. 핵심 철학

- **4가지 need = 4가지 문서 유형.** 각 유형은 목적이 다르므로 섞지 말고 분리.
- **2축 그리드**: Acquisition↔Application(수평), Action↔Cognition(수직).

## 4. 구조 — 4분면

| 유형 | need | 성격 | 축 |
|-----|------|------|----|
| **Tutorials** | 학습 | 손잡고 하는 실습 | Action + Acquisition |
| **How-to Guides** | 문제해결 | 특정 과업 단계별 | Action + Application |
| **Reference** | 조회 | 정확한 사실·명세 | Cognition + Application |
| **Explanation** | 이해 | 개념·배경·"왜" | Cognition + Acquisition |

## 5. 장점 (BOK 관점)

- **BoK 지식 단위의 "타입 시스템"을 제공.** Phase 3의 "지식 단위 유형"을 무엇으로 분류할지에 대한 검증된 답 — 각 지식이 **어떤 need를 위한 것인지** 라벨링.
- **need 기반 분리 = progressive disclosure/라우팅과 결합.** 사용자(또는 AI)가 지금 필요한 need(이해? 조회? 실습?)에 맞는 지식만 소비.
- **Reference vs Explanation 구분이 특히 중요** — BOK는 "사실(Reference)"과 "왜/개념(Explanation, ADR·rationale)"을 명확히 분리해야 함. 헌장의 "코드로 아는 것 vs 코드로 모르는 업무 규칙" 구분과 공명.
- **온보딩 정렬** — 신규자는 Tutorial/Explanation, 개발 중엔 How-to/Reference. BOK의 이해→개발 여정과 매핑.

## 6. 단점 / 한계 (BOK 관점)

- **저작(authoring) 프레임워크** — 사람이 쓰는 전제. 발굴·검증·근거를 다루지 않음.
- **분류 체계일 뿐** — 내용을 발굴하거나 정확성을 보장하지 않음.
- 4분면이 **모든 엔터프라이즈 지식(데이터 모델·운영 정책·리스크)** 을 커버하는지는 보강 필요(arc42가 보완).

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **4분면을 BoK 지식 단위의 need-type 라벨로 채택** — 특히 Reference(사실) ↔ Explanation(왜/개념) 분리.
- **need 기반 라우팅** → progressive disclosure로 상황에 맞는 지식 제공(사람+AI).
- **온보딩 여정 매핑**(Tutorial/Explanation → How-to/Reference).

**개선할 것**
- 저작 분류 → **발굴 산출물의 자동 태깅**(발굴된 지식이 어느 분면인지 AI가 라벨 + provenance/confidence).
- 4분면을 arc42/C4/ADR 스키마와 **교차**: Reference=구조/데이터 사실(C4·arc42 §3–8), Explanation=결정/근거(ADR·arc42 §4,§9), Glossary=별도 용어 축(Ubiquitous Language).

---

### Evidence
- Diátaxis 공식 — https://diataxis.fr/
- "Start here — Diátaxis in five minutes" — https://diataxis.fr/start-here/
- I'd Rather Be Writing, "What is Diátaxis?" — https://idratherbewriting.com/blog/what-is-diataxis-documentation-framework
