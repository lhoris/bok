# 예제: acme-billing

가상의 결제 시스템 `billing` 서브시스템에 BOK를 적용한 **최소 실증 예제**. 설계(`design/01–05`)의 추상 개념이 실제 파일로 어떻게 나타나는지 보여준다.

> 이 예제는 **1회전 나선의 스냅샷**이다. 의도적으로 **NOT READY**에서 멈춰, BOK가 "무엇을 모르는지"를 산출하는 방식을 보여준다.

## 무엇을 보여주나

| 개념(설계) | 이 예제에서 |
|-----------|------------|
| KU = 1파일 1URL (D01 D1) | `bok/billing/**/*.md` 3개 |
| 3축 타입 (D01 A.2) | reference / explanation / glossary × context=billing |
| provenance 필수 (D01 A.4) | code·doc·human·data 4종 kind 모두 등장 |
| confidence 5단계 (D04 A.1) | authoritative(글로서리, DDL) · corroborated(교차근거) |
| KU 최저값 집계 (D04 D15) | double-settlement-guard: 핵심 주장 미검증 → corroborated 고정 |
| 관계 그래프 (D01 A.5) | derived-from / defines-term / part-of / depends-on |
| dangling relation 검출 (D05 D21) | `ledger-store` 참조하나 미저작 → catalog warning |
| 저작 vs 생성 분리 (D05 D20) | `billing/**`(저작) vs `_system/**`(# GENERATED) |
| coverage 격자 (D04 B.2) | `_system/coverage.yaml` |
| Hard gate 우선 (D04 D18) | data-model 1개 red → 점수 무관 NOT READY |
| Readiness Tier (D04 B.4) | R1(Mapped), 목표 R3 미달 |
| 나선 gap→재발굴 (D02 D8) | readiness-report §5 → 다음 discover 입력 |

## 파일
```
bok.yaml                                  # 설정(D05 §4)
bok/billing/reference/settlement-batch.md
bok/billing/explanation/double-settlement-guard.md
bok/billing/glossary/idempotency-key.md
bok/_system/catalog.yaml        (GENERATED)
bok/_system/coverage.yaml
bok/_system/readiness-report.md (GENERATED)
```

## 나선 1회전 읽는 순서
1. `bok.yaml` — 이 프로젝트가 어떻게 설정됐나(임계·팩).
2. `billing/**` 3개 KU — 실제 지식 단위의 손맛(frontmatter + 본문 스키마).
3. `_system/catalog.yaml` — L1 인덱스로 컴파일된 모습 + dangling 경고.
4. `_system/coverage.yaml` — arc42+TDD 영역 격자.
5. `_system/readiness-report.md` — **Hard gate FAIL → gap 4개 → 다음 나선.**

## 다음 나선이 하는 일 (문서상 시나리오)
`discover(data-model)` → `ledger-store` KU 생성 → `validate`로 double-settlement-guard owner 서명(→verified) → data-model green + business-rules green → `ready` 재판정 시 R3 근접.
