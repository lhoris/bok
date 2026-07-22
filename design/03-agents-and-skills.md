# BOK Design 03 — Agent & Skill 정의

> 설계 입력: `research/_SYNTHESIS.md`, `design/01`, `design/02`.
> 누가(Agent) 무엇을(Skill) 어떻게 수행하는가. 원칙: **소수 역할 + 재사용 절차**. BMAD 12+ 에이전트 과잉을 경계하고(`research/01/bmad-method.md`), 단순성을 우선한다(`research/01/agentic-workflow.md`).
>
> **실체화됨**: 이 설계는 `agents/*.md`(5 에이전트)와 `packs/core/**/SKILL.md`(10 Skill)로 구현되어 있다. 각 파일은 결정론(`bok` CLI)과 LLM 추론이 만나는 지점을 명시한다.

## 0. 핵심 원칙 — Thin Agents, Fat Skills

> 설계 결정 D12 — **에이전트는 얇게(역할·경계·도구만), 재사용 절차는 Skill로 두껍게.**
> 근거: Skills의 progressive disclosure(L1 ~100토큰 메타만 상주, 필요 시 본문 로드, `research/01/claude-code-skills.md`). 절차를 Skill에 넣으면 **에이전트 수를 늘리지 않고** 능력을 확장할 수 있다 → 로스터를 5개로 유지.

- **Agent = 누구** — 페르소나·책임·경계·도구 접근. 소수.
- **Skill = 어떻게** — 이식 가능한 절차 패키지(`SKILL.md` + 리소스). 다수·확장 가능.
- **관계** — 에이전트가 작업 중 관련 Skill을 progressive disclosure로 로드해 수행.

## 0.1 Anthropic 패턴 매핑 (`research/01/agentic-workflow.md`, `/multi-agent.md`)
- discover = **Orchestrator–Worker**
- validate = **Evaluator–Optimizer**
- assemble/context 라우팅 = **Routing**
- 병렬 발굴·교차검증 = **Parallelization(voting)**

---

# 1. Agent 로스터 (5개 핵심 역할)

> `research/_SYNTHESIS §7`의 "소수 핵심 역할: Discover / Structure / Validate / Readiness" + 이를 지휘하는 Orchestrator.

| Agent | SECI/커맨드 | 한 줄 책임 | 인스턴스 |
|-------|------------|-----------|---------|
| `bok-orchestrator` | 나선 전체 | 계획·분해·스폰·게이트·종합 | 1 (Lead) |
| `bok-discoverer` | discover | 자족 발굴 태스크 1건 수행 | N (병렬·일시적) |
| `bok-curator` | context | 후보 KU → 구조화 BoK | 1 |
| `bok-validator` | validate | 상시 비판·검증·confidence | 1 (항상 on) |
| `bok-readiness-assessor` | ready | 커버리지·gap·리스크·판정 | 1 |

## 1.1 `bok-orchestrator` (Lead)
- **책임**: BOK 나선(D8)의 주인. discover 계획 수립(변경 히트맵 우선순위), 워커 스폰·태스크 서술 작성, 단계 게이트(D9) 판정, gap→재발굴 결정, 결과 종합.
- **도구**: 저장소 읽기, 태스크 분해, 워커 스폰, 메모리(`discovery-plan.md`), catalog 질의.
- **경계**: 직접 KU를 쓰지 않는다(종합·조율만). 검증을 대신하지 않는다.
- **근거**: Multi-agent Lead — "전략 수립·메모리 기록·서브에이전트 스폰·종합", "분해 품질이 전부"(`research/01/multi-agent.md`).

## 1.2 `bok-discoverer` (Worker, 병렬·일시적)
- **책임**: Orchestrator가 준 **자족 태스크 1건**(목표+출력형식+경계+관련 Context Pack)을 신선한 컨텍스트에서 수행, 후보 KU 산출(provenance 필수).
- **전문화 = 로드하는 Skill로 결정**: `code-archaeology` | `human-externalization` | `kg-extraction`. (에이전트를 늘리지 않고 Skill로 변신 — D12)
- **경계**: 서로의 존재를 모른다·중간 협응 없다(Multi-agent 원칙). 조율은 Orchestrator 통해서만. 타입 확정·검증은 하지 않는다(context/validate 몫).
- **근거**: "각 서브에이전트는 자족 태스크·출력형식·신선한 컨텍스트, 서로 모름"(`research/01/multi-agent.md`).

## 1.3 `bok-curator`
- **책임**: context 커맨드 수행 — canonicalize, 3축 타입 라벨링, kind별 body 스키마 적용, relations·context-map 구성, catalog 컴파일.
- **도구**: catalog 읽기/쓰기, KU 편집, 스키마 템플릿(Skill).
- **경계**: 새 사실을 **발명하지 않는다**(발굴은 discover). 근거 없는 관계 금지.

## 1.4 `bok-validator` (상시 Adversarial)
- **책임**: grounding 검사, 반례·대안·누락 제기, contradiction 해소, confidence 전이. `verified`는 사람 owner 확인을 **요청**(자동 승격 불가).
- **경계**: **이전 에이전트 결과를 신뢰하지 않는 것이 기본값**(헌장). 통과 못 하면 게이트를 막는다.
- **근거**: Evaluator–Optimizer(`research/01/agentic-workflow.md`) + Adversarial Review(`research/01/bmad-method.md`) + "합의보다 근거"(헌장).

> 설계 결정 D13 — **Validator는 옵션이 아니라 상시 게이트다.** discover/context 산출은 반드시 validate를 거쳐 confidence를 얻는다. "검증 없는 지식 확산 금지"(`research/03`의 자동생성물 맹신 경고).

## 1.5 `bok-readiness-assessor`
- **책임**: coverage.yaml ↔ arc42/TDD 대조, confidence 게이트, gap·리스크·버스팩터 지도, Readiness verdict.
- **경계**: 지식을 만들지 않는다(측정·판정만). verdict는 근거(커버리지·confidence 수치)에 기반, 주관 금지.

## 1.6 로스터를 5개로 유지하는 이유
발굴의 다양성(코드/사람/KG)은 **에이전트가 아니라 Skill**로 흡수한다(D12). 도메인 특화(게임·결제·금융)도 에이전트 추가가 아니라 **Skill 확장 팩**으로(§3). → 헌장 "복잡성 축소, 단순성 우선".

---

# 2. Skill 카탈로그

> 각 Skill = `SKILL.md`(frontmatter: name·description ~100토큰) + 절차 본문 + 리소스(템플릿·스크립트). progressive disclosure로 로드. 이식 가능·vendor-neutral(`research/01/claude-code-skills.md`).

## 2.1 Discover Skills
| Skill | 절차 요지 | 근거 |
|-------|----------|------|
| `code-archaeology` | 의존성/제어흐름 복원, 변경 히트맵, 데이터모델·업무규칙 후보 추출 | `research/02/software-archaeology.md` |
| `human-externalization` | 인터뷰·Event Storming 가이드 생성·요약 → tacit KU (provenance.kind=human) | `research/03/domain-modeling.md`, `/knowledge-management-and-engineering.md` |
| `kg-extraction` | 텍스트/코드에서 엔티티·관계 추출(Extract→Define) | `research/03/knowledge-graph.md` |

## 2.2 Context (Structuring) Skills
| Skill | 절차 요지 |
|-------|----------|
| `canonicalization` | 중복/동의 KU 병합, id 부여, pruning |
| `type-labeling` | 3축(kind/layer/context) 라벨링 규칙 |
| `arc42-authoring` | reference 본문을 arc42 §3–8 구조로 |
| `adr-authoring` | explanation/결정을 Context·Decision·Consequences(+대안 필수)로 |
| `c4-authoring` | 구조 지식을 C4 텍스트 다이어그램(Mermaid)으로 |
| `glossary-building` | Ubiquitous Language 항목화 |

## 2.3 Validate Skills
| Skill | 절차 요지 |
|-------|----------|
| `grounding-check` | KU 주장 ↔ provenance locator 대조 |
| `adversarial-review` | 반례·대안·누락 체계적 제기 |
| `contradiction-detection` | `relations: contradicts` 스캔·충돌쌍 리포트 |
| `confidence-transition` | A.3 전이 규칙 적용(승격/강등) |

## 2.4 Ready Skills
| Skill | 절차 요지 |
|-------|----------|
| `coverage-assessment` | arc42 12섹션 + TDD 체크리스트 대조 |
| `risk-mapping` | 리스크/레드플래그 + 버스팩터 산출 |
| `readiness-scoring` | 영역 신호등 + 종합 verdict(수식은 04) |

## 2.5 공용 Skill
`context-assembly`(B.3 Context Pack 생성), `bok-schema`(KU frontmatter 검증).

---

# 3. 확장성 — Skill 확장 팩 (Extension Packs)

> 설계 결정 D14 — **BOK의 확장점은 에이전트가 아니라 Skill 팩이다.**
> 근거: BMAD 모듈 + Spec Kit Extensions/Presets/Bundles(`research/01/bmad-method.md`, `/spec-kit.md`). 도메인/기술 특화는 Skill 팩으로 배포(예: `pack-mainframe-cobol`, `pack-billing-domain`, `pack-spring-boot`). 코어 5 에이전트는 불변, 능력만 확장. vendor-neutral.

레이어 우선순위(Spec Kit 오버라이드 계승): 프로젝트 로컬 Skill > 도메인 팩 > 코어 기본.

---

# 4. Human-in-the-loop 접점

> SECI 90% tacit(`research/03`) + `verified` 사람 서명(D01 A.3, D02 §3). BOK는 완전 자동이 아니라 **사람+AI 협업**.

| 접점 | 누가 | 무엇 |
|------|------|------|
| 인적 발굴 | `bok-discoverer`(human-externalization) + 도메인 전문가 | 인터뷰·Event Storming 입력 |
| `verified` 승격 | `bok-validator` → owner | 도메인 소유자 확인 서명 |
| Readiness 판정 검토 | `bok-readiness-assessor` → 리더 | verdict 최종 승인 |

## 5. 상호작용 예시 (discover 나선 1회)
```
orchestrator: 계획(히트맵) → discovery-plan.md
  ├─ spawn discoverer#1 [skill: code-archaeology]  → 후보 KU(inferred)
  ├─ spawn discoverer#2 [skill: human-externalization] → 후보 KU(human)
  └─ spawn discoverer#3 [skill: kg-extraction] → 엔티티·관계
orchestrator: 종합 → curator(context) → 구조화 BoK + catalog
validator(상시): grounding+adversarial+contradiction → confidence 전이
readiness-assessor: coverage+gap+risk → verdict
  └─ gap 발견 → orchestrator 재계획 (나선 D8)
```

## 6. 열린 질문 (다음 산출물로)
1. confidence 전이·readiness 점수의 **정확한 수식/임계** → **04**.
2. adversarial-review 중단 조건(무한 비판 방지) → 04 검증 프로세스.
3. Skill 팩 배포·버전·해석 우선순위의 물리 구현 → **05 Repository 구조**.

## 7. 설계 결정 요약 (이 문서)
- **D12** Thin Agents, Fat Skills — 절차는 Skill로, 로스터 5개 유지.
- **D13** Validator는 상시 게이트(옵션 아님).
- **D14** 확장점은 에이전트가 아니라 Skill 확장 팩.
