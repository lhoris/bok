# BOK Design 06 — 예제 프로젝트 · Contributor Guide · Roadmap · 설계 종결

> 설계 입력: `design/01–05`. 추상 설계를 **실제 파일로 실증**하고, 헌장의 산출물 목록을 종결한다.

## 1. 예제 프로젝트 — `examples/acme-billing/`

설계 01–05를 실제 파일로 구현한 **1회전 나선 스냅샷**. 상세는 `examples/acme-billing/README.md`.

의도적으로 **NOT READY**에서 멈춰 BOK의 핵심 가치("모른다는 것을 안다")를 보여준다:
- 저작 KU 3개(reference/explanation/glossary)에 4종 provenance(code·doc·human·data)와 confidence(authoritative/corroborated).
- `catalog.yaml`이 dangling relation(`ledger-store`)을 검출 → coverage의 `data-model` red와 일치.
- `bok ready --purpose feature`가 **Hard gate FAIL**(critical `data-model` red) → Tier R1 → **gap 4개를 다음 discover 입력으로**.

> 실증으로 확인된 것: 설계의 모델들(KU 스키마·confidence 집계·dangling 검출·hard gate·나선)이 **서로 모순 없이 하나의 흐름으로 연결**된다. 남은 검증(자동 매핑 정확도 등)은 구현(ROADMAP M1)으로 이월.

## 2. Contributor Guide — `CONTRIBUTING.md`
기여 5원칙(근거/단순성/검증가능성/vendor-neutral/비판환영), 확장점(Skill 팩 우선), KU 작성 규칙, PR 체크리스트, 커밋 규약. 헌장의 Agent Team 운영 원칙을 사람 기여자에게 확장.

## 3. Roadmap — `ROADMAP.md`
조사·설계 완료 → M1(Walking Skeleton) … M6(파일럿). 각 단계에 **검증 질문**을 붙여 "확정 계획"이 아니라 "검증 대상 가설"로 둔다. 명시적 비목표(코드 생성/문서 생성/EA 스위트가 되지 않음)로 정체성을 고정.

---

## 4. 헌장 산출물 목록 — 종결 확인 (자기검증)

| 헌장 산출물 | 위치 | 상태 |
|-----------|------|:-:|
| 프로젝트 비전 | `README.md` + `_SYNTHESIS §1` | ✅ |
| 핵심 철학 | `_SYNTHESIS §2,§7` | ✅ |
| 전체 아키텍처 | `design/01`, `design/02 §0` | ✅ |
| Workflow | `design/02` | ✅ |
| Agent 정의 | `design/03 §1` | ✅ |
| Skill 정의 | `design/03 §2` | ✅ |
| Command 체계 (`bok.discover/context/ready`) | `design/02` (+validate 추가) | ✅ |
| Repository 구조 | `design/05` | ✅ |
| Wiki 구조 | `design/05 §2`, 예제 | ✅ |
| Body of Knowledge 모델 | `design/01 PART A` | ✅ |
| Context 모델 | `design/01 PART B` | ✅ |
| Knowledge Validation 모델 | `design/04 PART A` | ✅ |
| Development Readiness 모델 | `design/04 PART B` | ✅ |
| 검증 프로세스 | `design/04`, `design/02 §3` | ✅ |
| 예제 프로젝트 | `examples/acme-billing/` | ✅ |
| Contributor Guide | `CONTRIBUTING.md` | ✅ |
| Roadmap | `ROADMAP.md` | ✅ |

**헌장 산출물 17/17 충족.**

## 5. 헌장 성공 기준 — 최종 대조

| 헌장 질문 | 충족 근거 |
|----------|----------|
| 새 개발자가 빠르게 이해? | progressive disclosure 위키(D01 B.2) + 온보딩 여정(Diátaxis) |
| AI가 충분히 이해하고 작업? | Context Pack(자족 태스크 + 근거 + gaps, D01 B.4) |
| 특정 사람 의존 안 함? | 암묵지 externalization(D03 §1.2) + 버스팩터 지표(D04 B.6) |
| 지식이 체계적으로 정리? | BoK Model 3축 + KG 관계(D01) |
| 신규 개발 착수 충분? | Readiness R3 hard gate(D04 B.4) |
| 현대화 전 검증? | R4 + 리스크/의존성 green(D04 B.4) |
| 이해도를 객관적으로 평가? | coverage 신호등 + score + Tier(D04) |

## 6. BOK가 기존 오픈소스와 다른 이유 (한 문단, 최종)
Spec Kit·BMAD·Backstage·arc42는 모두 훌륭하지만 **생성 편향·근거 부재·이해도 미측정**이라는 동일한 3대 공백을 공유한다(`_SYNTHESIS §2`, 4개 Phase가 4번 확인). BOK는 이들을 복제하지 않고, 그들의 자산(게이트·Work Sharding·progressive disclosure·catalog 스키마·arc42/ADR/C4/Diátaxis)을 흡수하되 **파이프라인을 뒤집어**(시스템→근거→검증된 지식→개발) 그 공백을 메운다. 결과물은 "**검증되고 이해도가 측정되는, 저장소에 사는 LLM Wiki**" — 즉 SECI를 AI 시대에 실행 가능하게 만든 Enterprise Onboarding 프레임워크다.

## 7. 설계 단계 종료
조사(20+ 프레임워크) → 설계(01–06) → 예제 실증 완료. 헌장 산출물 17/17. 다음은 구현(ROADMAP M1: Walking Skeleton).
