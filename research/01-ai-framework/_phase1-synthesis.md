# Phase 1 통합 노트 — AI Framework

> 대상: Spec Kit, BMAD Method, Claude Code Skills, Context Engineering, Agentic Workflow, Multi-Agent
> 목적: 6개 조사를 가로질러 **BOK가 가져올 자산**과 **반드시 뒤집거나 채워야 할 공백**을 확정한다.

---

## A. 관통하는 3대 공백 (= BOK의 차별점)

여섯 프레임워크를 같은 렌즈("이해를 얼마나 돕는가")로 보면 동일한 빈자리가 반복된다.

1. **생성(Generation) 편향 → BOK는 방향을 뒤집는다.**
   Spec Kit(의도→코드), BMAD(Analyst→Dev) 모두 *"무엇을 만들지 인간이 이미 안다"* 를 전제한다. 나머지(Skills/Context/Workflow/Multi-agent)는 방향이 없는 순수 메커니즘이다.
   BOK는 정반대 지점 — *"무엇이 이미 있는지 모른다"* — 에서 출발한다.
   → **파이프라인: 기존 시스템 → 근거(Evidence) → 검증된 지식 → (그다음) 개발.**

2. **Evidence(근거) 부재 → BOK는 provenance를 1급 시민으로.**
   어떤 프레임워크도 산출물을 기존 코드·DB·운영·이해관계자로부터 **역방향 검증**하지 않는다. 모든 지식 단위는 **출처(provenance)** 와 **검증 수준(confidence)** 을 필수 필드로 갖는다.

3. **이해도(Understanding) 미측정 → BOK는 Readiness 게이트로.**
   정합성(consistency)은 검사해도 *"충분히 이해했는가?"* 는 아무도 묻지 않는다.
   → **Development Readiness = 이해도를 객관적으로 평가하는 게이트.**

## B. 가져올 자산 (매핑)

| 출처 | 자산 | BOK 편입 위치 |
|-----|------|--------------|
| Spec Kit | 게이트형 단계 워크플로우 | `bok.discover → context → ready` 게이트 |
| Spec Kit | Constitution(프로젝트 원칙 레이어) | BOK 프로젝트 상수/제약 |
| Spec Kit | 명료한 커맨드 + 정제 커맨드(clarify/analyze) | BOK 커맨드 체계 |
| Spec Kit | 템플릿 오버라이드 3계층 | 확장성·vendor-neutral |
| BMAD | Work Sharding = 자족적 컨텍스트 단위 | **Context Model 기본 단위** |
| BMAD | 역할 기반 에이전트 + 산출물 핸드오프 | Agent Team 뼈대 |
| BMAD | Adversarial Review | 상시 검증 에이전트("합의보다 근거") |
| Skills | Progressive Disclosure(인덱스→요약→상세) | **BoK Model 층화 구조** |
| Skills | 자족적·이식 가능한 폴더 단위 | 지식 단위 물리 포맷 |
| Context Eng. | finite resource · JIT · 경량 식별자(포인터) | **Context Model 설계 원리** |
| Agentic WF | 5패턴(chaining/routing/parallel/orch/eval) | 오케스트레이션 표준 블록 |
| Agentic WF | 단순성 우선 | 에이전트 수 통제 기준 |
| Multi-Agent | Orchestrator–Worker + 자족 태스크 | **`bok.discover` 실행 구조** |
| Multi-Agent | "분해 품질이 전부" | 발굴 태스크 표준 템플릿 |

## C. 경계할 것 (안티패턴)

- **에이전트 과잉(BMAD 12+)** — BOK는 소수 핵심 역할로 단순화: *Discover / Validate / Structure / Readiness*.
- **멀티 에이전트 남용(비용 15x)** — 폭이 필요한 **발굴 단계 한정**. 검증·구조화는 경량 워크플로우.
- **생성 파이프라인 그대로 이식** — 방향 반전 없이 가져오면 BOK가 아니라 "또 하나의 Spec Kit"이 된다.

## D. Phase 1이 시사하는 BOK 초기 골격 (가설 — Phase 2~4로 검증 필요)

- **커맨드**: `bok.discover`(병렬 채굴·Orchestrator–Worker) → `bok.context`(구조화·큐레이션·Progressive Disclosure) → `bok.validate`(Evaluator–Optimizer 검증) → `bok.ready`(이해도 게이트).
- **지식 단위**: 자족적 폴더 = { 내용 + provenance + confidence + relations }. (Skills+BMAD+Multi-agent의 공통 결)
- **에이전트**: 소수 역할 + 상시 Adversarial 검증.
- **원리**: finite context / JIT 로딩 / 근거 기반 / 단순성 우선.

## E. 다음 단계로 넘길 검증 질문

- **Enterprise Onboarding(Phase 2)**: Backstage/Service Catalog는 "생성이 아닌 이해"의 실제 사례 — BOK의 방향 반전 가설을 뒷받침하는가? 카탈로그 모델을 BoK Model에 어떻게 흡수하나?
- **Knowledge Engineering(Phase 3)**: provenance·confidence·relations를 실제로 구조화하는 검증된 방법(Knowledge Graph)은? 이해도를 정량화하는 선례가 있나?
- **Documentation/Architecture(Phase 4)**: arc42/C4/ADR/Diátaxis가 BoK Model의 **산출 스키마**를 제공하는가? (특히 Diátaxis의 4분면 ↔ BOK 지식 유형)
