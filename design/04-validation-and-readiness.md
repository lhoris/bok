# BOK Design 04 — Knowledge Validation & Development Readiness 모델

> 설계 입력: `research/_SYNTHESIS.md`, `design/01–03`.
> BOK의 3번 공백("이해도 미측정")을 **정량화**한다. confidence 전이 규칙, adversarial 종료 조건, coverage 스키마, readiness 점수식, 나선 종료 기준. 조사한 어떤 프레임워크도 하지 않은 부분 — BOK의 결정적 차별점.

## 0. 두 축의 구분
- **Validation** = 개별 지식이 **믿을 만한가** (KU 단위, confidence).
- **Readiness** = 시스템을 **충분히 이해했는가** (BoK 전체, 목적 대비 coverage×confidence).
> Validation은 벽돌의 품질, Readiness는 건물이 입주 가능한지.

---

# PART A — Knowledge Validation

## A.1 confidence 상태 기계 (정밀)

5단계(D01 A.3)의 전이를 규칙으로 확정한다. **주장(claim) 단위로 판정 → KU로 집계.**

```
unverified ──(provenance≥1 연결)──▶ inferred
inferred ──(서로 다른 kind의 독립 근거 2+ 교차지지)──▶ corroborated
corroborated ──(도메인 owner 서명)──▶ verified
(1차 규범 근거: 스펙/계약/법규/DDL) ──▶ authoritative   # 어느 상태에서든 직행
임의 상태 ──(staleness 만료 | 근거 무효화 | contradicts 미해소)──▶ 한 단계 강등 + 재검증 큐
```

- **교차지지(corroborated) 정의**: provenance.kind가 서로 다른(예: code + human) 근거가 **동일 주장**을 지지. 같은 kind 2개는 불충분(단일 관점 편향 방지).
- **authoritative**: 규범적 1차 소스(OpenAPI 스펙, DB DDL, 법규, 서명된 계약). 사람 서명 없이도 최상위 — 소스 자체가 진실.
- **KU 집계 규칙**: KU.confidence = 그 KU의 **핵심 주장들 중 최저값**(약한 고리가 KU 신뢰를 지배). 부차 주장은 본문 `## 열린 질문`에 격리.

> 설계 결정 D15 — confidence는 **주장 단위로 산정하고 KU는 최저값으로 집계**한다. "대체로 맞지만 핵심이 미검증"인 KU가 verified로 위장하는 것을 막는다.

## A.2 staleness (부패) 규칙

| kind | 기본 임계 | 트리거 |
|------|----------|--------|
| reference | 90일 | provenance의 code locator 변경(git) 시 즉시 |
| explanation / glossary | 180일 | 관련 결정 supersede 시 |
| how-to | 코드변경 연동 | 참조 경로 변경 시 즉시 |

임계 초과 → confidence **한 단계 강등** + `last_verified` 플래그 + 재검증 큐(`bok.validate` 부분 실행 대상). 정책은 `bok.yaml`에서 조정(vendor-neutral).

## A.3 Adversarial Review 종료 조건

> 무한 비판 방지(열린 질문 D03-2). Evaluator–Optimizer 루프에 **정지 규칙** 필요.

리뷰는 다음 중 하나에서 종료:
1. **Fixpoint** — 새 라운드에서 **material finding(중대 지적)이 0**. (사소한 문체 지적은 제외)
2. **Budget** — 라운드 상한(기본 3) 도달.
3. **Human escalation** — corroborated↔contradicts 교착 시 owner에게 이관.

종료 후 미해소 **critical 지적은 confidence를 승격시키지 않고 gap으로 기록**(막되, 루프하지 않음). → 진전과 종결을 모두 보장.

> 설계 결정 D16 — Adversarial은 **fixpoint 또는 예산에서 멈추고, 미해소는 gap으로 방출**한다. 비판은 무한하지 않고, 미해소는 숨기지 않는다.

## A.4 Validation 산출 (`validation-report.md`)
강등 목록 · grounding 실패 · 미해소 contradicts · escalation 대기. 각 항목은 해당 KU와 링크(추적성).

---

# PART B — Development Readiness

## B.1 핵심 발상 — Readiness는 목적 상대적(purpose-relative)

> 설계 결정 D17 — **"준비됨"은 절대값이 아니라 "무엇을 위해 준비됐는가"이다.**
> 근거: TDD는 특정 딜(목적)을 위한 평가(`research/02-enterprise-onboarding/technical-due-diligence.md`); Spec Kit 시나리오도 목적별(0→1/현대화, `research/01-ai-framework/spec-kit.md`). 전 시스템을 100% 이해할 필요는 없다 — **하려는 작업의 범위(scope)에 대해** 충분하면 된다.

Readiness는 항상 **scope + 목적**을 받는다:
`ready(scope: billing 서브시스템, purpose: 신규기능 | 현대화 | 단순이해)`.

## B.2 coverage.yaml 스키마

시스템 이해의 **커버리지 격자**. arc42 12섹션 + TDD 체크리스트(`research/04-documentation-architecture/arc42.md`, `research/02-enterprise-onboarding/technical-due-diligence.md`)를 **지식 영역(knowledge area)** 으로 정규화.

```yaml
# bok/_system/coverage.yaml  (context가 갱신, ready가 평가)
scope: billing
areas:
  - id: context-and-scope          # arc42 §3 / C4 Context
    criticality: high
    kus: [bok://billing/reference/system-context]
    status: green                   # 자동 계산(B.3)
  - id: business-rules              # arc42 §4/§9 + business process archaeology
    criticality: critical
    kus: [bok://billing/explanation/double-settlement-guard, ...]
    status: amber                    # 핵심 KU가 corroborated(verified 미달)
  - id: data-model                  # arc42 §5 / data layer
    criticality: critical
    kus: []
    status: red                      # 미발굴 gap
  - id: runtime-behavior            # arc42 §6
  - id: deployment-ops              # arc42 §7 / how-to
  - id: crosscutting-concepts       # arc42 §8
  - id: decisions-rationale         # arc42 §9 / ADR
  - id: quality-requirements        # arc42 §10
  - id: risks-tech-debt             # arc42 §11 / TDD 리스크
  - id: glossary-ubiquitous-lang    # arc42 §12 / DDD
  - id: dependencies-eol            # TDD 의존성
  - id: security-compliance         # TDD
  - id: team-bus-factor             # TDD 팀 의존성
```

> 영역 집합은 **arc42 12 + TDD 보강**이 기본 템플릿이며, Skill 팩으로 도메인 영역 추가 가능(D14).

## B.3 영역 상태(status) 계산 — 신호등

각 영역은 **criticality가 요구하는 최소 confidence**를 만족해야 green.

| criticality | 요구 최소 confidence | 의미 |
|------------|---------------------|------|
| critical | `verified`+ | 틀리면 시스템/사업 치명 — 사람 확인 필수 |
| high | `corroborated`+ | 교차 근거 필요 |
| normal | `inferred`+ | 단일 근거 허용 |
| low | 존재만 | 참고 |

```
영역 status =
  red    : 필수 KU 없음(미발굴 gap)  또는  핵심 KU가 요구 confidence보다 2단계+ 미달
  amber  : KU 존재하나 요구 confidence 1단계 미달  또는  미해소 gap/contradicts 존재
  green  : 필수 KU 존재 + 모두 요구 confidence 충족 + 미해소 critical 없음
```

## B.4 Readiness 판정 — Hard Gate 우선, 그다음 점수

> 설계 결정 D18 — **평균 점수로 통과시키지 않는다. Hard gate가 먼저다.**
> 근거: 단일 미검증 critical 업무 규칙 하나가 전체를 위험에 빠뜨린다(TDD 레드플래그 사고). 평균은 이를 희석하므로 금지.

**1단계 — Hard Gate (통과/실패)**
- scope 내 **criticality=critical 영역 중 red가 하나라도 있으면 → NOT READY** (점수 무관).
- 미해소 contradicts(critical) 존재 → NOT READY.

**2단계 — Readiness Score (hard gate 통과 후, 0–100)**
```
score = Σ_area ( weight(criticality) × status_value )  /  Σ_area weight(criticality) × 100
  status_value: green=1.0, amber=0.5, red=0.0
  weight: critical=4, high=3, normal=2, low=1   # bok.yaml 조정 가능
```

**3단계 — Readiness Tier (목적별 문턱)**

| Tier | 이름 | 조건 | 이 상태에서 가능한 것 |
|------|------|------|---------------------|
| R0 | Opaque | 착수 전 | — |
| R1 | Mapped | 구조 영역(context/container/data) green | 시스템 지도 파악, 온보딩 시작 |
| R2 | Understood | + business-rules·decisions green(critical verified) | 안전한 논의·소규모 변경 |
| R3 | Development-Ready | scope hard gate 통과 + score ≥ 80 | **신규 기능 개발 착수** |
| R4 | Modernization-Ready | R3 + risks·dependencies·bus-factor green | **현대화/대규모 개편 착수** |

`ready`는 목적을 tier로 변환: 신규기능→R3, 현대화→R4, 단순이해→R2.

## B.5 나선 종료 조건 ("언제 충분한가")

> 열린 질문 D02-4의 답.

`bok.ready`는 매 나선마다 판정. 종료(=개발 착수)는:
1. **목표 tier 도달** — purpose가 요구하는 tier의 hard gate+score 충족. → 정상 종료.
2. **수렴 정체(diminishing returns)** — 최근 N 나선의 gap 종결률이 임계 미만인데 목표 미달 → **사람에게 escalation**(자동 지속 금지). 남은 gap은 "known unknowns"로 명시하고 리스크로 이관.
3. 즉 BOK는 "완벽한 이해"가 아니라 **"목적에 충분한, 그리고 모르는 것을 아는 이해"** 에서 멈춘다.

## B.6 성공 지표 추적 (`research/_SYNTHESIS §6`)
readiness-report에 시계열로 기록:
- **버스 팩터** = 영역별 단일-human-provenance 집중도(낮을수록 위험). team-bus-factor 영역과 연동.
- **커버리지** = green 영역 비율. **검증 비율** = verified+ KU 비율.
- 온보딩 시간·time-to-first-PR = 도입 조직이 외부 계측(BOK는 훅 제공).

## B.7 readiness-report.md 구성
커버리지 신호등 격자 · confidence 히트맵 · **gap 목록(→ 다음 discover)** · 리스크/버스팩터 지도 · Hard gate 결과 · score · **Tier verdict + 조건**.

---

## C. 예시 (billing, purpose=신규기능→R3)
```
Hard Gate: FAIL — [data-model] critical 영역이 red(미발굴)
Score:     62/100
Tier:      R1 (Mapped) — 목표 R3 미달
Gaps:      data-model(미발굴), business-rules(verified 미달 1건)
Verdict:   NOT READY. 다음 discover 대상: billing 데이터 모델.
           business-rules의 double-settlement-guard → owner 검증 필요.
```
→ Orchestrator가 gap을 다음 나선 입력으로(D8).

## D. 헌장 목표 충족 (자기검증)
| 헌장 질문 | 답 |
|----------|-----|
| 이해도를 객관적으로 평가? | coverage 신호등 + score + Tier(수치) |
| 현대화 전 정보 검증? | R4 게이트(risks/deps/bus-factor green) |
| 특정 사람 의존? | 버스 팩터 지표 + critical은 교차근거 강제 |
| 개발 착수 충분? | Hard gate + R3, gap 명시 |

## E. 설계 결정 요약
- **D15** confidence는 주장 단위 산정·KU 최저값 집계.
- **D16** Adversarial은 fixpoint/예산에서 종료, 미해소는 gap 방출.
- **D17** Readiness는 목적 상대적(scope+purpose→tier).
- **D18** Hard gate 우선(critical red면 실패), 그다음 가중 점수.

## F. 열린 질문 (다음 산출물)
1. coverage 영역↔KU 자동 매핑 정확도(어떤 KU가 어느 영역인지) → **06 예제**에서 실측.
2. Skill 팩·bok.yaml·id 무결성의 물리 배치 → **05 Repository 구조**.
