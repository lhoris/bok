# BOK Design 01 — BoK Model & Context Model

> 설계 입력: `research/_SYNTHESIS.md`. 이 문서는 BOK의 **데이터 토대**를 정의한다 — 지식이 무엇으로 이루어지고(BoK Model), 어떻게 소비되는가(Context Model). 이후 모든 설계(워크플로우·에이전트·검증·Readiness)는 이 위에 선다.

## 0. 두 모델의 구분 (한 줄)

- **BoK Model** = 지식이 **저장·구조화되는 방식** (정적, 저장소에 사는 진실의 원천).
- **Context Model** = 특정 작업을 위해 지식이 **선택·조립·소비되는 방식** (동적, 토큰 예산 안에서).

> 비유: BoK Model은 **도서관**(모든 책과 분류 체계), Context Model은 특정 질문에 답하려 **책상에 펼쳐 놓은 몇 권**.
> 근거: 이 분리는 Context Engineering의 "finite resource + JIT loading"(`research/01/context-engineering.md`)과 LLM Wiki의 "compile once(BoK), consume via synthesized layer(Context)"(`research/03/knowledge-base-and-llm-wiki.md`)에서 도출.

---

# PART A — BoK Model

## A.1 지식 단위 (Knowledge Unit, KU)

BoK의 원자 단위. **하나의 자족적 마크다운 파일** = frontmatter(구조화 메타) + 본문(사람+AI가 읽는 내용).

> 설계 결정 D1 — **"1 지식 = 1 파일 = 1 URL".**
> 근거: Backstage `catalog-info.yaml`의 "컴포넌트당 정규 주소"(`research/02/backstage.md`) + Skills의 "자족적·이식 가능한 폴더 단위"(`research/01/claude-code-skills.md`) + LLM Wiki의 "저장소에 사는 마크다운"(`research/03/knowledge-base-and-llm-wiki.md`). 벡터DB·외부 인프라 불필요(단순성·vendor-neutral).

### A.1.1 스키마 (frontmatter)

```yaml
---
id:            bok://<domain>/<type>/<slug>   # 정규 불변 주소 (D2)
title:         결제 정산 배치의 이중 정산 방지 규칙
kind:          explanation                    # need-type (A.2.1)
layer:         component                       # 구조 레이어 (A.2.2), 없으면 null
context:       billing                         # bounded context (A.2.3)
status:        active                          # active | draft | deprecated | superseded
confidence:    corroborated                    # A.3 — 필수
provenance:                                    # A.4 — 필수, 최소 1개
  - kind: code
    locator: src/billing/settle.py#L120-L180
    note: 멱등 키 검사 로직
  - kind: human
    locator: interview/2026-07-20-kim-billing
    note: "왜 이중 검사인지 배경"
relations:                                     # A.5 — 타입 있는 간선(그래프)
  - type: derived-from
    target: bok://billing/reference/settlement-batch
  - type: defines-term
    target: bok://billing/glossary/idempotency-key
owner:         team-billing                     # 소유(Backstage 계보)
last_verified: 2026-07-21                       # A.6 — 부패 방지
supersedes:    null
---

## TL;DR                # 200자 요약 — Context 요약 계층에서 이것만 로드
## 배경/문제
## 내용 (본문)          # kind별 스키마(A.2.1)에 따름
## 근거 상세            # provenance 각 항목의 인용/발췌
## 열린 질문 / 불확실성  # confidence < verified 인 부분 명시
```

## A.2 타입 시스템 — 3개의 직교 축

지식 단위는 **세 개의 독립 축**으로 분류된다. 하나의 계층 트리로 억지로 합치지 않는다(직교성이 라우팅·검증을 단순하게 만든다).

### A.2.1 축 1 — `kind`: need-type (필수)
> 근거: Diátaxis 4분면(`research/04/diataxis.md`). "지금 이 지식은 어떤 need를 위한 것인가."

| kind | need | BOK에서의 전형 |
|------|------|---------------|
| `reference` | 조회(사실) | 구조·데이터모델·API·설정 — C4/arc42 §3–8 |
| `explanation` | 이해(왜/개념) | 업무 규칙·설계 근거·ADR — arc42 §4/§9 |
| `how-to` | 문제해결 | 운영 절차·배포·장애 대응 |
| `tutorial` | 학습 | 온보딩 여정·첫 기여 가이드 |
| `glossary` | 용어 | Ubiquitous Language 항목(별도 축, `research/03/domain-modeling.md`) |

### A.2.2 축 2 — `layer`: 구조 레이어 (선택)
> 근거: C4 줌 레벨(`research/04/c4-model.md`) + EA 다층(`research/02/enterprise-architecture.md`). Progressive Disclosure를 **구조 지식**에 적용.

`context`(시스템 경계) → `container`(앱/데이터스토어) → `component`(내부 모듈) → `data`(데이터 모델) → `business`(역량/프로세스). 비구조 지식은 `null`.

### A.2.3 축 3 — `context`: bounded context (권장)
> 근거: DDD Bounded Context(`research/03/domain-modeling.md`). 같은 용어가 다른 의미를 갖는 **의미 경계**. 대규모 BoK를 의미 일관 영역으로 분할 → Context 라우팅의 1차 필터.

## A.3 confidence — 검증 수준 (필수)

> 근거: BOK의 2번 공백("근거·검증 부재")의 정면 대응. 모든 지식은 **얼마나 믿을 수 있는지**를 명시한다. ADR Status 계열(`research/04/adr.md`) + KG 추출 신뢰(`research/03/knowledge-graph.md`).

| confidence | 의미 | 승격 조건 |
|-----------|------|----------|
| `unverified` | 발굴 직후, 미검증 초안 | discover 산출 기본값 |
| `inferred` | 근거에서 **추론**(단일 소스·AI 해석) | 1개 provenance |
| `corroborated` | 2+ 독립 근거가 교차 지지 | 서로 다른 kind의 provenance 2+ |
| `verified` | 사람(도메인 소유자)이 확인 | owner 검토 서명 |
| `authoritative` | 권위 소스로 확정(스펙·계약·법규) | 1차 규범 문서 |

> 설계 결정 D3 — **confidence는 `bok.validate`가 올리고, `last_verified` 만료 시 자동 강등**(부패 방지). Development Readiness는 "특정 커버리지 영역이 최소 confidence 이상"을 게이트로 삼는다(산출물 04에서 상세).

## A.4 provenance — 출처 (필수, 최소 1개)

> 근거: Software Archaeology의 "증거 기반 발굴"(`research/02/software-archaeology.md`) + DeepWiki 소스 접지(`research/03/knowledge-base-and-llm-wiki.md`). **근거 없는 지식은 BoK에 존재할 수 없다.**

`kind ∈ {code, doc, human, runtime, data, external}` + `locator`(파일#라인 / 인터뷰ID / 로그쿼리 / URL) + `note`. 이것이 SECI Externalization의 "무엇에서 표출됐는가"를 기록한다(`research/03/knowledge-management-and-engineering.md`).

## A.5 relations — 지식 그래프 (타입 있는 간선)

> 근거: Knowledge Graph 엔티티+관계(`research/03/knowledge-graph.md`) + ADR 결정 사슬(`research/04/adr.md`) + Backstage 소유/의존.

핵심 관계 타입(최소 집합, 오버엔지니어링 경계):

`part-of` · `depends-on` · `derived-from`(근거 지식) · `defines-term` · `decides`(→결정) · `supersedes` · `owned-by` · `contradicts`(⚠ 검증 트리거).

> 설계 결정 D4 — **관계는 파일 frontmatter에 분산 저장**(단일 그래프 DB 없음). 그래프는 파일들에서 **컴파일**된다. → vendor-neutral·git 친화·단순성. `contradicts`는 `bok.validate`가 자동 감지해 충돌 검토를 강제.

## A.6 last_verified & 수명주기

> 근거: SECI 콘텐츠 수명주기 + Phase 2 "카탈로그 부패" 교훈(`research/02/_phase2-synthesis.md`).

각 KU는 `last_verified` 날짜를 갖고, `kind`별 staleness 임계(예: reference 90일, explanation/glossary 180일, how-to 코드변경 연동)를 넘기면 **confidence 자동 강등 + 재검증 큐**. → "살아있는 BoK".

## A.7 물리 레이아웃 (BoK Wiki)

```
bok/                          # 대상 저장소에 사는 Body of Knowledge
  catalog.yaml                # A.8 컴파일된 인덱스(자동 생성)
  billing/                    # bounded context별
    reference/settlement-batch.md
    explanation/double-settlement-guard.md
    glossary/idempotency-key.md
  _system/
    context-map.md            # bounded context 관계도(C4 Context)
    coverage.yaml             # arc42 12섹션 커버리지(→ Readiness)
```

> 설계 결정 D5 — BoK는 **대상 저장소 안 `bok/`** 에 산다(코드와 함께 버전 관리, docs-like-code). LLM Wiki 패턴(`research/03/knowledge-base-and-llm-wiki.md`).

## A.8 catalog.yaml — 컴파일된 인덱스

모든 KU의 frontmatter만 모은 자동 생성 인덱스(id·title·kind·layer·context·confidence·relations). **Progressive Disclosure 1계층**이며 그래프 질의·라우팅의 진입점. git hook/`bok` CLI가 재생성.

---

# PART B — Context Model

## B.1 목적

BoK 전체를 컨텍스트에 넣는 것은 불가능하다(엔터프라이즈 규모). Context Model은 **주어진 작업(task/need)에 필요한 최소 지식만 조립**한다.
> 근거: "context는 유한 자원, JIT 로딩, 경량 식별자"(`research/01/context-engineering.md`) + Multi-agent의 "자족적 태스크 서술"(`research/01/multi-agent.md`).

## B.2 3계층 Progressive Disclosure

> 근거: Claude Skills 3단 로딩(`research/01/claude-code-skills.md`) + C4 줌.

| 계층 | 로드 대상 | 토큰 | 언제 |
|-----|----------|------|------|
| **L1 Catalog** | `catalog.yaml`(id·title·kind·context·confidence) | 작음 | 항상 — 무엇이 있는지 |
| **L2 Summary** | 관련 KU들의 frontmatter + `## TL;DR` | 중간 | 관련성 판단 후 |
| **L3 Detail** | 해당 KU 본문 + provenance 인용 + 링크된 근거 | 큼 | 실제 작업 수행 시 |

에이전트는 L1으로 후보를 좁히고 → L2로 확정 → 필요한 것만 L3로 확장. **포인터(id) 먼저, 내용은 나중에.**

## B.3 Context Assembly (조립 알고리즘)

입력: `{ 작업 목표, need(kind), bounded context, 토큰 예산 }`

1. **Filter** — `context`(bounded context) + `kind`(need)로 catalog 1차 필터. (Diátaxis need 라우팅 + DDD 경계)
2. **Seed** — 목표와 의미적으로 관련된 KU 선정(제목/TL;DR 기반).
3. **Expand** — seed에서 `relations`를 따라 확장(`depends-on`, `derived-from`, `defines-term`). 깊이·예산으로 제한.
4. **Rank & Trim** — 관련성 × confidence로 정렬, 토큰 예산까지. **낮은 confidence는 경고 라벨과 함께 포함**(숨기지 않음).
5. **Emit Context Pack** — 조립 결과를 B.4 형식으로 반환.

> 설계 결정 D6 — Assembly는 **Orchestrator–Worker의 서브에이전트 태스크 서술**로도 사용된다(`research/01/multi-agent.md`): 각 워커에게 "자족적 목표 + 관련 Context Pack + 출력 형식"을 준다.

## B.4 Context Pack (조립 산출물)

```yaml
context_pack:
  goal: "정산 배치에 재시도 안전성 추가"
  need: how-to
  bounded_context: billing
  units:                         # 포함된 KU와 로드 계층
    - {id: bok://billing/explanation/double-settlement-guard, tier: L3, confidence: corroborated}
    - {id: bok://billing/reference/settlement-batch,          tier: L3, confidence: verified}
    - {id: bok://billing/glossary/idempotency-key,            tier: L2, confidence: authoritative}
  warnings:
    - "double-settlement-guard 는 corroborated(사람 미검증) — 결정 전 owner 확인 권장"
  gaps:
    - "재시도 실패 시 알림 경로에 대한 지식 없음 → discover 필요"
  token_estimate: 4200
```

> 설계 결정 D7 — Context Pack은 **`gaps`(모르는 것)를 명시**한다. 이것이 BOK의 3번 공백("이해도")을 작업 수준에서 노출하고, `bok.discover` 재실행/`bok.ready` 게이트로 연결된다.

## B.5 사람 vs AI 소비

같은 BoK, 다른 표면:
- **사람** — 렌더된 위키를 L1→L3로 탐색(TL;DR·다이어그램 중심). 인지 부하↓(`research/02/developer-portal-and-service-catalog.md`).
- **AI** — Context Pack을 주입받아 작업. 동일 마크다운·동일 근거.
> "사람과 AI가 같은 Body of Knowledge를 공유"(헌장) = **하나의 BoK Model, 두 소비 경로.**

---

## C. 이 모델이 헌장 목표를 충족하는가 (자기검증)

| 헌장 질문 | 이 모델의 답 |
|----------|------------|
| 이해 가능? | L1→L3 progressive disclosure + arc42 커버리지 |
| AI가 작업 가능? | Context Pack(자족 태스크 + 근거) |
| 특정 사람 의존↓? | provenance에 human 소스를 명시적 KU로 흡수(암묵지→형식지) |
| 근거 기반? | provenance·confidence 필수, 없으면 KU 불성립 |
| 이해도 평가? | confidence + coverage.yaml + Context Pack의 gaps |
| 단순? | 마크다운+git, 그래프DB/벡터DB 없음, 최소 관계 타입 |

## D. 열린 설계 질문 (다음 산출물로 이월)

1. **confidence 승격/강등의 정확한 규칙** → 산출물 04(Validation/Readiness).
2. **coverage.yaml ↔ arc42/TDD 체크리스트 매핑의 구체 항목** → 04.
3. **Assembly의 "의미적 관련성" 구현**(임베딩 없이 어디까지? 제목·TL;DR·relations만으로 충분한가) → 02(Workflow) 프로토타입에서 검증.
4. **id 재명명/이동 시 관계 무결성**(리팩터링) → 05(Repository 구조)에서 `bok` CLI 정책으로.

## E. 설계 결정 요약

- **D1** 1 지식 = 1 파일 = 1 URL(자족 마크다운).
- **D2** 불변 정규 id `bok://context/kind/slug`.
- **D3** confidence는 validate가 올리고 staleness가 내린다.
- **D4** 관계는 파일에 분산, 그래프는 컴파일(그래프DB 없음).
- **D5** BoK는 대상 저장소 `bok/`에 거주(docs-like-code).
- **D6** Context Assembly = 서브에이전트 태스크 서술의 기반.
- **D7** Context Pack은 `gaps`(모르는 것)를 명시한다.
