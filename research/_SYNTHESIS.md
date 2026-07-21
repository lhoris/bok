# BOK Research — Master Synthesis (조사 종합)

> 4개 Phase(AI Framework · Enterprise Onboarding · Knowledge Engineering · Documentation/Architecture), 총 20+ 프레임워크/개념의 근거 기반 조사를 관통하는 최종 종합.
> **이 문서가 설계 단계(Design)의 유일한 입력이다.** 이후 모든 설계 결정은 여기서 근거를 인용한다.

---

## 1. 한 문장 정의

> **BOK = 저장소에 사는, 근거로 검증되고 이해도가 측정되는 LLM Wiki(Body of Knowledge)를 구축함으로써, 낯선 엔터프라이즈 시스템을 사람과 AI가 함께 "이해 가능한 상태 → 개발 가능한 상태"로 끌어올리는 Enterprise Onboarding 프레임워크. 본질적으로 SECI(암묵지→형식지 전환)를 AI 시대에 실행 가능하게 만든 것.**

## 2. 핵심 통찰 — 왜 BOK인가 (4 Phase가 4번 확인한 것)

조사한 모든 프레임워크는 **동일한 3대 공백**을 공유한다. 이건 우연이 아니라 **구조적 빈자리**다.

| 공백 | 누가 이걸 안 하나 | BOK의 답 |
|-----|-----------------|---------|
| **① 생성 편향** — "무엇을 만들지 안다"를 전제 | Spec Kit, BMAD, DDD, arc42/ADR/C4 | **방향 반전**: 시스템→근거→검증된 지식→개발 |
| **② 근거·검증 부재** — 산출물이 정확한지 안 봄 | KG추출·LLM Wiki·카탈로그·문서 전부 | **provenance·confidence·검증 게이트**를 1급 시민으로 |
| **③ 이해도 미측정** — "썼는가"만, "이해했는가"는 아님 | 전부 | **Development Readiness** = 이해도 정량 게이트 |

그리고 Phase 2가 발견한 **미싱 링크**: 업계는 **발굴 진영**(Archaeology/TDD — 캐내지만 유지 안 함)과 **정리 진영**(Backstage/EA — 배열하지만 발굴 안 함)으로 갈려 있고, **아무도 `발굴→검증→구조화→유지`의 전체 루프를 잇지 않는다.** BOK가 그 루프다.

## 3. 이론적 뼈대 — SECI를 실행하는 4-커맨드 파이프라인

```
SECI Externalization  →  bok.discover   (tacit·code → evidence)
SECI Combination      →  bok.context    (evidence → structured BoK)
      (SECI엔 없음)    →  bok.validate   (BOK가 더하는 검증 게이트)
SECI Internalization  →  bok.ready      (BoK → 사람·AI의 이해 → 측정)
```

| 커맨드 | 하는 일 | 흡수한 자산(출처) |
|-------|--------|------------------|
| **`bok.discover`** | 코드 발굴 + 인적 발굴 병렬 | Software Archaeology(저장소 마이닝·변경 히트맵·의존성/동적 분석·업무규칙 복원) + Event Storming/인터뷰(SECI·DDD) + KG Extract + Multi-agent Orchestrator–Worker + "분해 품질이 전부" |
| **`bok.context`** | 근거를 구조화·큐레이션 | catalog-info 스키마(Backstage) + EA 다층/Capability + KG 온톨로지·Canonicalize + Bounded Context(DDD) + Progressive Disclosure(Skills/C4) + arc42 목차 |
| **`bok.validate`** | 근거 대비 검증 + 이해도 평가 | Evaluator–Optimizer(Agentic WF) + Adversarial Review(BMAD) + 소스 접지(DeepWiki) + 대안 필수(ADR/MADR) |
| **`bok.ready`** | 개발 준비 게이트 | TDD 커버리지 체크리스트 + arc42 12섹션 커버리지 + EA Gap 식별 + 리스크/버스팩터 지표 |

## 4. BoK Model — 지식 단위 스키마

저장소에 사는 마크다운 엔티티(사람+AI 공용, 버전 관리, 벡터DB 불필요):

```yaml
# 지식 단위 = 자족적 마크다운 파일 (frontmatter + 본문)
identity:        # 정규 주소 (Backstage catalog-info)
type:            # need-type (Diátaxis: reference|explanation|how-to|tutorial)
                 #  + 구조 레이어 (C4: context|container|component)
                 #  + bounded context (DDD)
provenance:      # 어느 소스/발굴기법에서 (KG·archaeology·grounding)  ← 필수
confidence:      # 검증 수준 (추론 vs 확인, ADR Status 계열)          ← 필수
relations:       # 엔티티 간 관계 그래프 (KG triples)
last_verified:   # 부패 방지 (SECI 수명주기 / 카탈로그 유지)
# 본문: arc42 섹션/ADR(Context·Decision·Consequences)/C4(Mermaid) 스키마로 채움
```

## 5. 필수 산출물 (BoK Deliverables)

1. **구조화 BoK 위키** (arc42 골격 + C4 뷰) — 저장소 거주.
2. **도메인 용어집** (Ubiquitous Language / arc42 §12).
3. **관계 그래프** (KG — 컴포넌트·데이터·결정의 연결).
4. **의사결정/왜 기록** (ADR — 역복원 포함).
5. **리스크 & Gap 지도** (TDD + EA Gap) — 현대화 준비 입력.

## 6. 성공 지표 (측정 가능)

- 온보딩 시간 ↓ (Backstage 실증: 60일→20일)
- time-to-first-PR ↓
- 버스 팩터 ↓ (특정 사람 의존 제거 — 헌장 목표)
- 이해 커버리지 ↑ (arc42/TDD 체크리스트 대비)
- 검증된 지식 비율(confidence) ↑

## 7. 설계 원칙 (조사에서 도출)

- **AI-native + Human-friendly** — 같은 마크다운을 사람·AI가 공유(LLM Wiki·Skills).
- **단순성 우선** — 소수 커맨드/에이전트(Agentic WF의 5패턴, BMAD 12+ 과잉 경계, TOGAF 무게 경계).
- **근거 우선** — provenance/confidence 없는 지식은 없다.
- **Vendor-neutral·로컬 우선** — 기밀성(KG), 벡터DB 불필요(LLM Wiki).
- **점진적·상향식** — 하향식 대규모 선행 모델링(EA) 거부. 필요한 만큼만.
- **살아있음** — compile-once-maintain, last_verified로 부패 방지.

## 8. 경계할 안티패턴 (조사에서 도출)

- 생성 파이프라인 무비판 이식(→ 또 하나의 Spec Kit).
- 에이전트/온톨로지/문서 오버엔지니어링(단순성 위배).
- 자동 생성물 맹신(검증 없는 KG/Wiki = 잘못된 이해 확산).
- 코드 편향(SECI 90% 암묵지 경고).
- 일회성 스냅샷·수작업 부패(TDD/카탈로그 교훈).

## 9. 설계 단계로의 인계 (다음 산출물)

조사 종료. 헌장의 산출물 목록을 이 종합에 근거해 설계한다. 권장 순서:
1. **BoK Model & Context Model** (§4 스키마 구체화) — 지식 단위·관계·저장 구조.
2. **Workflow & Command 체계** (§3) — `bok.discover/context/validate/ready` 상세.
3. **Agent & Skill 정의** — 소수 역할 + Adversarial 검증.
4. **Knowledge Validation & Development Readiness 모델** (§3 validate/ready, §6 지표).
5. **Repository/Wiki 구조** — 물리 레이아웃.
6. **예제 프로젝트 · Contributor Guide · Roadmap.**

---

### 근거
각 주장의 1차 근거는 `research/0X-*/`의 개별 분석 파일과 그 하단 Evidence(공식 문서/저장소 URL)에 있다. Phase별 통합은 각 `_phaseN-synthesis.md` 참조.
