# Phase 3 통합 노트 — Knowledge Engineering

> 대상: Knowledge Graph, Knowledge Management & Engineering(SECI), Knowledge Base & LLM Wiki, Domain Modeling(DDD)
> 목적: Phase 2가 "아무도 안 한다"고 남겨둔 부분 — provenance·confidence·relations의 정식 모델링, 이해도 정량화, 유지 — 의 **방법론**을 확보한다.

---

## A. Phase 2의 3대 공백에 대한 Phase 3의 답

| Phase 2가 비워둔 것 | Phase 3의 답 | 출처 |
|---|---|---|
| relations를 어떻게 구조화? | 엔티티+관계+온톨로지, Extract→Define→Canonicalize | Knowledge Graph |
| "유지(maintain)"는 누가? | **compile-once, maintain-continuously** 마크다운 위키 | LLM Wiki/DeepWiki |
| 코드 밖 지식(업무·암묵지)은? | tacit 90%, **SECI Externalization**, Event Storming, Ubiquitous Language | KM/SECI, DDD |
| 검증은 여전히 공백 | (부분) 소스 접지(grounding)는 있으나 **검증 게이트는 아직 아무도 안 함** | — |

## B. 이번 Phase의 결정적 발견 2가지

**1. BOK의 물리적 형태가 정해졌다 — "검증되는 LLM Wiki".**
LLM Wiki 패턴(저장소에 사는·버전 관리되는·벡터DB 없는 마크다운·사람+AI 공용 접지 레이어)은 BOK가 목표하는 산출물과 거의 동일하다. 그리고 **compile-once-maintain** 은 Phase 2의 미싱 링크("유지")를 실제로 구현했다.
→ **BOK = LLM Wiki + (근거·confidence·검증·이해도 게이트).** 즉 BOK는 "검증되고 이해도가 측정되는 LLM Wiki"로 포지셔닝된다.

**2. 발굴 대상이 코드에서 사람으로 확장됐다 — "90%는 암묵지".**
SECI가 못박는다: 조직 지식의 최대 90%가 tacit(사람 머릿속). Phase 2의 archaeology(코드 발굴)만으로는 절반도 못 캔다.
→ `bok.discover`는 **코드 발굴 + 인적 발굴(Externalization: 인터뷰·Event Storming)** 을 동등하게 포함해야 한다. 헌장이 지목한 "업무 용어/업무 규칙을 모른다"는 정확히 이 암묵지 영역.

## C. 이론적 뼈대 확정 — BOK = "AI 시대에 실행 가능해진 SECI"

SECI 나선이 BOK 워크플로우의 이론 프레임과 일대일 대응한다:

```
Externalization(tacit→explicit)  =  bok.discover  (archaeology + interview + event storming + KG extract)
Combination(explicit→explicit)   =  bok.context   (구조화: catalog 스키마 + EA 다층 + KG 온톨로지 + bounded context)
                                     bok.validate  (← SECI엔 없음. BOK가 더하는 검증 게이트)
Internalization(explicit→tacit)  =  bok.ready      (사람/AI가 BoK로 시스템을 이해 → 이해도 측정)
```

## D. 가져올 자산 (매핑)

| 출처 | 자산 | BOK 편입 위치 |
|-----|------|--------------|
| Knowledge Graph | 엔티티+관계+온톨로지, Extract→Define→Canonicalize, Pruning | BoK relations/타입 구조, discover/context 파이프라인 |
| Knowledge Graph | 트리플 provenance/confidence, 셀프호스팅(기밀성) | 검증 가능성, vendor-neutral |
| KM / SECI | tacit/explicit, SECI 4모드, 콘텐츠 수명주기 | **BOK 워크플로우 이론 프레임**, 인적 발굴, 부패 방지 |
| LLM Wiki / DeepWiki | compile-once-maintain 마크다운 위키, 소스 접지, design rationale | **BOK 물리 산출 포맷**, provenance 구현 |
| Domain Modeling | Ubiquitous Language, Bounded Context, Event Storming | **도메인 용어집 산출물**, 지식 경계/모듈, 인적 발굴 기법 |

## E. 경계할 것 (안티패턴)

- **자동 생성물의 맹신** — KG 추출·LLM Wiki 모두 환각 위험. **검증 없이는 잘못된 이해를 확산**(BOK의 검증 게이트가 존재 이유).
- **온톨로지/DDD 오버엔지니어링** — 형식성 과잉은 단순성 원칙 위배. 최소 타입만.
- **코드 편향** — SECI 90% 경고. 인적/업무 지식을 코드와 동등하게.
- **사람 집약 워크숍의 확장성** — Event Storming 산출물을 AI로 구조화해 완화.

## F. Phase 1~3 종합 — BOK 골격 (Phase 4에서 산출 스키마만 확정하면 설계 착수 가능)

- **정체성**: BOK = "검증되고 이해도가 측정되는, 저장소에 사는 LLM Wiki(Body of Knowledge)". SECI를 AI로 실행.
- **파이프라인**: `bok.discover`(archaeology + 인적 발굴 + KG extract, Multi-agent 병렬) → `bok.context`(catalog+EA다층+온톨로지+bounded context로 구조화, progressive disclosure) → `bok.validate`(근거 대비 검증 + 사람 루프, Evaluator–Optimizer) → `bok.ready`(TDD 커버리지 + Gap + 이해도 = Readiness 게이트).
- **지식 단위**: 마크다운 엔티티 = { identity/주소 + 유형(EA레이어/bounded context) + 내용 + **provenance**(소스·발굴기법) + **confidence** + relations(KG) + last-verified }.
- **필수 산출물**: 구조화 BoK 위키 + 도메인 용어집(Ubiquitous Language) + 관계 그래프 + 리스크/Gap 지도.
- **성공 지표**: 온보딩 시간↓, time-to-first-PR↓, 버스팩터↓, 커버리지↑, 검증된 지식 비율↑.

## G. Phase 4로 넘길 마지막 질문 (산출 스키마)

지식 단위의 **"내용"을 무엇으로 채우나?** — arc42(아키텍처 문서 표준 구조), C4(EA보다 경량한 다층 뷰), ADR(의사결정·"왜" = design rationale의 형식), Diátaxis(지식 유형 4분면 = 지식 단위 타입 분류)가 BoK Model의 **산출 스키마/템플릿**을 제공하는지 확인하면, 조사 종료 후 설계에 착수한다.
