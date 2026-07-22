# BOK — Body of Knowledge for Brownfield Onboarding

> 낯선 엔터프라이즈 시스템을, 사람과 AI가 함께 **이해 가능한 상태(Understandable) → 개발 가능한 상태(Development-Ready)** 로 끌어올리는 오픈소스 프레임워크.

BOK는 두 개의 상보적 의미를 담는다.

- **Body of Knowledge** — 사람과 AI가 공유하는, 검증되고 구조화된 지식.
- **Brownfield Onboarding Knowledge** — 개발·현대화에 앞서 기존 시스템을 이해하기 위한 지식 획득 과정.

## 한 문장

> BOK = **검증되고 이해도가 측정되는, 저장소에 사는 LLM Wiki.** 곧 SECI(암묵지→형식지 전환)를 AI 시대에 실행 가능하게 만든 Enterprise Onboarding 프레임워크.

## 왜 BOK인가 — 업계 공통의 3대 공백

Spec Kit·BMAD·Backstage·arc42 등 20+ 프레임워크를 근거 기반으로 분석한 결과(→ [`research/`](research/)), 모두 동일한 3대 공백을 공유한다. BOK는 이를 복제하지 않고 **파이프라인을 뒤집어** 메운다.

| 공백 | 기존 도구 | BOK의 답 |
|------|----------|---------|
| ① **생성 편향** — "무엇을 만들지 안다"를 전제 | Spec Kit, BMAD, DDD | 방향 반전: **시스템 → 근거 → 검증된 지식 → 개발** |
| ② **근거·검증 부재** — 산출물이 정확한지 안 봄 | KG추출·LLM Wiki·카탈로그 | `provenance` + `confidence`를 **필수 필드**로 |
| ③ **이해도 미측정** — "썼는가"만, "이해했는가"는 아님 | 전부 | **Development Readiness** = 이해도 정량 게이트 |

> 그리고 업계는 **발굴 진영**(Archaeology/TDD)과 **정리 진영**(Backstage/EA)으로 갈려, 아무도 `발굴→검증→구조화→유지`의 전체 루프를 잇지 않는다. **BOK가 그 루프다.**

## 어떻게 동작하나 — 나선(spiral)

```
bok discover ─▶ bok context ─▶ bok validate ─▶ bok ready ──▶ READY? ─▶ 개발/현대화
 (근거 발굴)     (구조화)       (검증·confidence) (이해도 게이트)   │
     ▲                                                            │ gaps
     └──────────────── 모르는 것(gap) 재발굴 ◀──────────────────────┘
```

| 커맨드 | SECI | 하는 일 |
|-------|------|--------|
| `bok discover` | Externalization | 코드 **+ 사람**에서 근거 발굴(Orchestrator–Worker) → 후보 지식 |
| `bok context` | Combination | 정규화·타입·관계·arc42/C4/ADR 스키마로 구조화 |
| `bok validate` | (BOK 고유) | 근거 대비 검증 + Adversarial 리뷰 → confidence 전이 |
| `bok ready` | Internalization | arc42+TDD 커버리지·confidence → **Readiness 판정** |

## 지식 단위 (Knowledge Unit)

**1 지식 = 1 마크다운 파일 = 1 URL.** 그래프DB·벡터DB 없이 git으로 버전 관리된다.

```yaml
id:            bok://billing/explanation/double-settlement-guard
kind:          explanation        # Diátaxis need-type
layer:         component          # C4 구조 레이어
context:       billing            # DDD bounded context
confidence:    corroborated       # 5단계 (unverified→…→authoritative) — 필수
provenance:                       # 근거 (code/doc/human/data/runtime) — 필수
  - {kind: code,  locator: src/billing/settle.py#L120-L180}
  - {kind: human, locator: interview/2026-07-18-kim-billing}
relations:
  - {type: derived-from, target: bok://billing/reference/settlement-batch}
```

## Development Readiness — 이해도를 숫자로

`bok ready`는 **목적 상대적**으로 판정한다(`ready(scope, purpose)`). 커버리지 신호등 + **Hard gate**(critical 영역이 하나라도 red면 점수 무관 NOT READY) + Tier:

`R1 Mapped → R2 Understood → R3 Development-Ready → R4 Modernization-Ready`

→ 실제 산출물 예: [`examples/acme-billing/bok/_system/readiness-report.md`](examples/acme-billing/bok/_system/readiness-report.md)

## 저장소 구조

```
research/    조사 — 20+ 프레임워크 분석 + _SYNTHESIS.md (설계 근거)
design/      설계 — 01 BoK/Context 모델 … 06 예제·로드맵 (결정 D1–D22)
cli/         구현 — `bok` CLI 8커맨드 (결정론 코어)
agents/      5 코어 에이전트 (CLI↔LLM 경계 정의)
packs/core/  10 코어 Skill (progressive disclosure)
adapters/    런타임 바인딩 — Codex · Claude Code · GitHub Copilot (공용 AGENTS.md)
templates/   KU·coverage·hook 템플릿
examples/    실증 — acme-billing(손+검증), mini-shop(전자동 발굴)
CONTRIBUTING.md · ROADMAP.md
```

## 써보기

실제 사용법은 **[QUICKSTART.md](QUICKSTART.md)** 참고 — `init → discover → context → compile → ready` 5단계.

## 시작하기 (읽는 순서)

1. **왜/무엇** — [`research/_SYNTHESIS.md`](research/_SYNTHESIS.md) (설계의 근거·결론)
2. **어떻게** — [`design/`](design/) 01 → 06
3. **실물** — [`examples/acme-billing/`](examples/acme-billing/)

> ⚙️ **상태**: 조사 ✅ · 설계 ✅ (헌장 산출물 17/17) · 구현 🔜 ([`ROADMAP.md`](ROADMAP.md) M1).

## 설계 원칙

AI-Native · Human-Friendly · Modular · Extensible · **Vendor-Neutral** · Language-Independent · Enterprise-Ready · **단순성 우선**.

## 기여 · 라이선스

[`CONTRIBUTING.md`](CONTRIBUTING.md) 참고. 근거 우선 — 근거 없는 단정은 받지 않는다. License: 저장소 `LICENSE` 참고.
