# BOK Design 02 — Workflow & Command 체계

> 설계 입력: `research/_SYNTHESIS.md`, `design/01-bok-model-and-context-model.md`.
> BoK Model(데이터) 위에서 BOK의 **움직임**을 정의한다 — 4개 커맨드의 동작·입출력·게이트·반복 구조.

## 0. 전체 형태 (한눈에)

```
        ┌──────────────────────────────────────────────────────────┐
        │                    BOK Loop (나선, not 직선)               │
        ▼                                                          │
  bok.discover ──▶ bok.context ──▶ bok.validate ──▶ bok.ready ─────┤
  (근거 발굴)      (구조화)        (검증·confidence) (이해도 게이트)  │
      ▲                                                 │          │
      └──────────── gaps / 낮은 confidence 영역 재발굴 ◀─┘          │
                                                                    │
                          READY ▶ (신규 개발 / 현대화) ◀────────────┘
```

> 설계 결정 D8 — **BOK는 직선 파이프라인이 아니라 나선(spiral)이다.** `ready`가 드러낸 gap이 다음 `discover`의 입력이 된다. 근거: SECI 나선(`research/03-knowledge-engineering/knowledge-management-and-engineering.md`), Spec Kit `/converge`의 "잔여 작업 재투입"(`research/01-ai-framework/spec-kit.md`). 한 번에 완벽을 노리지 않고 이해도를 점증시킨다.

> 설계 결정 D9 — **각 커맨드는 게이트를 가진 단계다**(Spec Kit 게이트형, `research/01-ai-framework/spec-kit.md`). 앞 단계의 출력이 품질 기준을 못 넘으면 다음으로 못 간다. 게이트 기준은 각 커맨드 절의 "Exit 조건".

## 0.1 SECI / 자산 매핑 (재확인)

| 커맨드 | SECI | 핵심 흡수 자산 |
|-------|------|--------------|
| discover | Externalization | Archaeology 툴박스 + 인터뷰/Event Storming + KG Extract + Orchestrator–Worker |
| context | Combination | catalog 스키마 + arc42/C4/ADR + KG Canonicalize + Bounded Context + Progressive Disclosure |
| validate | (BOK 고유) | Evaluator–Optimizer + Adversarial Review + 소스 접지 + 대안 필수(MADR) |
| ready | Internalization | TDD 커버리지 + arc42 12섹션 + EA Gap + 리스크/버스팩터 |

## 0.2 커맨드 표면 (surface)

> 설계 결정 D10 — BOK는 **vendor-neutral CLI(`bok`)를 진실의 원천**으로 하고, 에이전트 슬래시 커맨드(`/bok.discover` 등)와 Skill은 그 위의 얇은 어댑터다. 근거: Spec Kit의 30+ 에이전트 중립성 + 템플릿 오버라이드(`research/01-ai-framework/spec-kit.md`), Skills 이식성(`research/01-ai-framework/claude-code-skills.md`). 어떤 에이전트든(또는 사람이 직접) 같은 커맨드를 호출.

```
bok init         # bok/ 스캐폴딩 + bok.yaml(설정: bounded contexts, staleness 정책)
bok discover     # 근거 → 후보 KU
bok context      # 후보 KU → 구조화 BoK
bok validate     # confidence 승격/강등 + 충돌 검출
bok ready        # 이해도 게이트 평가 → 리포트
bok assemble     # (Context Model B.3) 작업용 Context Pack 생성
bok status       # catalog/coverage/confidence 대시보드
```

---

# 1. `bok.discover` — 근거 발굴 (Externalization)

## 1.1 목적
낯선 시스템의 **코드와 사람**에서 지식을 캐내 **후보 KU**(confidence: `unverified`/`inferred`)로 만든다. "무엇이 있는지 모른다"에서 출발하는 BOK의 심장.

## 1.2 입력
`{ scope: bounded context | 서브시스템 | 경로글롭, sources: [code, docs, human, runtime, data], budget }`

## 1.3 동작 — Orchestrator–Worker
> 근거: Multi-agent(`research/01-ai-framework/multi-agent.md`) — "분해 품질이 전부", 자족 태스크 + 신선한 컨텍스트. 비용 15x라 **발굴 단계에 한정**.

1. **Plan (Lead)** — scope를 발굴 태스크로 분해. **변경 히트맵**(저장소 마이닝)으로 우선순위: hot/위험 영역 먼저(`research/02-enterprise-onboarding/software-archaeology.md`). 계획을 `bok/_system/discovery-plan.md`에 기록(메모리).
2. **Parallel Workers (자족 태스크)** — 각 워커에 목표+출력형식+경계 부여:
   - **Code Archaeologist** — 의존성/제어흐름 복원, 데이터 모델 추출, 업무 규칙 후보 식별(business process archaeology).
   - **Human Externalizer** — 이해관계자 인터뷰·Event Storming 세션 가이드 생성·요약 → tacit을 KU로(`research/03-knowledge-engineering/domain-modeling.md`). provenance.kind=human.
   - **KG Extractor** — 텍스트/코드에서 엔티티·관계 추출(Extract→Define, `research/03-knowledge-engineering/knowledge-graph.md`).
3. **Emit** — 각 발견을 KU 초안으로 기록: **provenance 필수**, confidence= 단일근거 `inferred` / 미검증 `unverified`. 아직 정규화·타입확정 안 함(그건 context 단계).

## 1.4 출력 / Exit 조건
- 출력: `bok/**/에 후보 KU + discovery-plan.md`.
- **Exit 게이트**: (a) scope 내 모든 워커 태스크 완료·기록, (b) 모든 후보 KU가 provenance ≥1 보유(없으면 폐기 — 근거 없는 지식 금지), (c) 발굴 못 한 영역은 `gaps`로 명시.

## 1.5 안티패턴 방어
- 코드 편향 금지 — Human Externalizer 필수(SECI 90% tacit).
- 멀티에이전트 남용 금지 — discover에만, 이후 단계는 경량.

---

# 2. `bok.context` — 구조화 (Combination)

## 2.1 목적
후보 KU(원석)를 BoK Model에 맞는 **구조화된 지식**으로. explicit→explicit 결합.

## 2.2 동작
1. **Canonicalize** — 중복/동의 KU 병합, 표준 id 부여(`research/03-knowledge-engineering/knowledge-graph.md`의 canonicalize + Pruning으로 노이즈 제거).
2. **Type 부여** — 3축(`kind`/`layer`/`context`) 라벨링(D01 A.2). AI가 초안, 규칙 기반 검증.
3. **Body 스키마 적용** — kind별로 채움: reference→C4/arc42 §3–8, explanation→ADR(Context·Decision·Consequences), glossary→Ubiquitous Language 항목.
4. **Relations 구성** — KG 간선 연결(`depends-on`/`derived-from`/`defines-term`…), `bok/_system/context-map.md`(C4 Context, bounded context 관계) 생성.
5. **Index 컴파일** — `catalog.yaml` 재생성(Progressive Disclosure L1).

## 2.3 출력 / Exit 조건
- 출력: 구조화 KU + `catalog.yaml` + `context-map.md` + glossary.
- **Exit 게이트**: (a) 모든 KU가 유효한 `kind`+`context` 보유, (b) 고아 KU(관계 0) 최소화·정당화, (c) 중복률 임계 이하, (d) catalog 컴파일 성공.

---

# 3. `bok.validate` — 검증 (BOK 고유 게이트)

## 3.1 목적
지식이 **근거와 일치하고 정확한지** 검증하고 **confidence를 승격/강등**한다. BOK가 기존 프레임워크에 더하는 결정적 단계.

## 3.2 동작 — Evaluator–Optimizer + Adversarial
> 근거: Agentic WF Evaluator–Optimizer(`research/01-ai-framework/agentic-workflow.md`) + BMAD Adversarial Review(`research/01-ai-framework/bmad-method.md`) — "이전 산출물을 그대로 신뢰하지 않는다"(헌장).

1. **Grounding 검사** — 각 KU 주장을 provenance locator와 대조(소스 접지, `research/03-knowledge-engineering/knowledge-base-and-llm-wiki.md`). 근거 불일치 → 강등 + 플래그.
2. **Adversarial 리뷰** — 검증 에이전트가 반례·대안·누락을 제기(MADR 대안 필수, `research/04-documentation-architecture/adr.md`). 통과 못 하면 confidence 정체.
3. **Contradiction 해소** — `relations: contradicts` 자동 감지(D01 D4) → 충돌 KU 쌍 검토 강제.
4. **confidence 전이** (D01 A.3):
   - 교차 근거 2+ → `corroborated`
   - owner 서명 → `verified`
   - 1차 규범 → `authoritative`
   - staleness 만료 → 자동 강등 + 재검증 큐
5. **Human-in-the-loop** — `verified` 승격은 도메인 owner의 명시적 확인 필요(자동 불가).

## 3.3 출력 / Exit 조건
- 출력: 갱신된 confidence + `bok/_system/validation-report.md`(강등·충돌·미해소 목록).
- **Exit 게이트**: (a) 모든 `contradicts` 검토됨, (b) grounding 실패 KU 0(수정 또는 강등), (c) 미검증 초안(`unverified`) 비율이 임계 이하.

> 설계 결정 D11 — validate는 **부분 실행 가능**(작업 대상 KU만). 전체 재검증은 staleness가 트리거.

---

# 4. `bok.ready` — 개발 준비 게이트 (Internalization)

## 4.1 목적
"충분히 이해했는가?"를 **객관적으로 판정**한다. BOK의 3번 공백("이해도 미측정")의 답. 상세 지표 모델은 산출물 04에서 완성, 여기선 게이트 구조.

## 4.2 동작
1. **Coverage 평가** — `coverage.yaml`을 **arc42 12섹션 + TDD 체크리스트**(`research/04-documentation-architecture/arc42.md`, `research/02-enterprise-onboarding/technical-due-diligence.md`)에 대조. 각 필수 영역에 KU가 있는가.
2. **Confidence 게이트** — 필수 영역 KU가 최소 confidence 이상인가(예: 핵심 업무 규칙은 `verified`+).
3. **Gap 목록** — 비어있거나 저confidence 영역 = EA Gap(`research/02-enterprise-onboarding/enterprise-architecture.md`) → 다음 discover 입력(D8 나선).
4. **Risk & Bus-factor 지도** — 리스크/레드플래그 + 버스팩터(단일 human provenance 집중 영역) 산출(`research/02-enterprise-onboarding/technical-due-diligence.md`).
5. **Readiness Verdict** — 영역별 신호등 + 종합 판정(개발 착수 가능 여부 + 조건).

## 4.3 출력
`bok/_system/readiness-report.md` — 커버리지 그리드, confidence 히트맵, gap 목록, 리스크 지도, verdict.

## 4.4 Exit / 성공 지표 연결
성공 지표(온보딩 시간·time-to-first-PR·버스팩터·커버리지·검증비율, `research/_SYNTHESIS.md §6`)를 리포트에 추적. **verdict가 READY면 신규 개발/현대화로**, 아니면 나선 재순환.

---

# 5. 상태 & 산출물 종합

| 파일 | 생성 커맨드 | 역할 |
|------|-----------|------|
| `bok/**/[ku].md` | discover→context | 지식 단위 |
| `bok/catalog.yaml` | context | L1 인덱스 |
| `bok/_system/context-map.md` | context | bounded context 관계(C4) |
| `bok/_system/discovery-plan.md` | discover | 발굴 계획(메모리) |
| `bok/_system/validation-report.md` | validate | 검증 결과 |
| `bok/_system/coverage.yaml` | ready(평가)/context(갱신) | 커버리지 |
| `bok/_system/readiness-report.md` | ready | 이해도 판정 |

## 6. 헌장 커맨드 예시와의 정합
헌장 예시 `bok.discover / bok.context / bok.ready`를 그대로 채택하고, 그 사이에 **`bok.validate`를 명시적으로 추가**했다 — 이것이 BOK의 차별점("근거·검증")을 커맨드 레벨에서 구현하기 때문(SECI에 없던 단계).

## 7. 열린 질문 (다음 산출물로)
1. discover 워커의 구체 프롬프트/도구 바인딩 → **03 Agent & Skill**.
2. Adversarial 리뷰어의 역할 경계·중단 조건 → 03.
3. coverage.yaml 항목 스키마, confidence 임계의 영역별 값, readiness 점수식 → **04 Validation/Readiness**.
4. 나선 종료 조건(언제 "충분"인가)의 정량 기준 → 04.

## 8. 설계 결정 요약 (이 문서)
- **D8** BOK는 나선(gap→재발굴), 직선 아님.
- **D9** 각 커맨드는 Exit 게이트를 가진 단계.
- **D10** vendor-neutral `bok` CLI가 원천, 슬래시/Skill은 어댑터.
- **D11** validate는 부분 실행 가능, staleness가 전체 재검증 트리거.
