# Agentic Workflow (Patterns)

> Category: AI Framework · Phase 1 · Anthropic "Building Effective Agents" 외

## 1. 왜 만들어졌는가?

"에이전트"라는 말이 과대포장되며, 많은 팀이 불필요하게 복잡한 자율 에이전트를 만든다는 문제의식에서 나왔다. Anthropic은 **워크플로우(정해진 코드 경로로 LLM·도구를 오케스트레이션)** 와 **에이전트(모델이 스스로 경로를 결정)** 를 구분하고, 대부분은 **단순한 조합 가능한 패턴**으로 충분하다고 정리했다.

## 2. 어떤 문제를 해결하는가?

- 과잉 자율성으로 인한 예측 불가·디버깅 곤란
- "언제 워크플로우로 충분하고 언제 에이전트가 필요한가"의 판단 부재
- 재사용 가능한 **표준 조립 블록**의 부재

## 3. 핵심 철학

- **단순성 우선.** 필요 최소한의 복잡도. (BOK의 "복잡성 축소, 단순성 우선"과 동일.)
- **Composable patterns.** 대부분의 프로덕션 시스템은 여러 패턴의 조합.
- **Workflow(예측 가능) vs Agent(동적).** 예측 가능한 부분은 워크플로우로 고정.

## 4. 구조 — 5대 워크플로우 패턴

| 패턴 | 요지 | BOK 적용 후보 |
|-----|------|--------------|
| **Prompt Chaining** | 단계 분해, 앞 출력이 뒤 입력 | discover→context→ready 순차 파이프라인 |
| **Routing** | 분류기가 전문 핸들러로 분기 | 지식 유형(코드/데이터/업무규칙/운영)별 전용 처리 |
| **Parallelization** | 분할(sectioning)/투표(voting) | 여러 소스를 병렬 채굴, 교차 검증(voting) |
| **Orchestrator–Worker** | 중앙이 동적 분해·위임·종합 | 미리 서브태스크를 알 수 없는 미지 시스템 탐사 |
| **Evaluator–Optimizer** | 생성↔평가 루프 | Knowledge Validation(지식 생성↔근거 검증 루프) |

## 5. 장점 (BOK 관점)

- **BOK 워크플로우 설계의 기성 어휘.** 새 오케스트레이션을 발명하지 말고 이 5패턴을 조합.
- **Evaluator–Optimizer**는 BOK의 **검증 루프**에 이상적 — 지식 초안을 근거로 반복 평가.
- **Routing**은 "코드로 알 수 없는 업무 규칙 vs 코드로 아는 구조"를 분기 처리하는 데 적합.
- **단순성 철학**이 BOK 원칙과 정합 — BMAD식 12+ 에이전트 과잉을 경계할 근거.

## 6. 단점 / 한계

- 순수 **메커니즘**이다 — 무엇을 생성/평가할지의 **도메인 내용(엔터프라이즈 이해)** 은 비어 있음.
- 패턴 자체엔 근거·이해도·검증 기준이 없다. BOK가 그 "내용"을 채워야 한다.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **5패턴을 BOK 오케스트레이션의 표준 블록으로 채택**: 파이프라인=Chaining, 소스 분기=Routing, 병렬 채굴·교차검증=Parallelization/voting, 미지 탐사=Orchestrator–Worker, 검증=Evaluator–Optimizer.
- **단순성 우선** 원칙을 에이전트 수 통제의 기준으로.

**개선할 것**
- 각 패턴에 **근거(Evidence) 흐름**을 필수로 얹는다: 어떤 워커든 출력에 출처를 달고, Evaluator는 "근거 대비 지식 정합성 + 이해도"를 평가하도록 특화.

---

### Evidence
- Anthropic, "Building Effective Agents"(5 패턴) — https://www.anthropic.com/research/building-effective-agents
- Spring AI Reference, "Building Effective Agents" — https://docs.spring.io/spring-ai/reference/api/effective-agents.html
