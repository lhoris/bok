# Multi-Agent Framework

> Category: AI Framework · Phase 1 · Anthropic "How we built our multi-agent research system" 외

## 1. 왜 만들어졌는가?

단일 에이전트는 하나의 컨텍스트 윈도우에 갇혀, 넓고 병렬적인 탐색(리서치)에서 한계가 있다. Anthropic은 **오케스트레이터–워커** 구조의 멀티 에이전트 리서치 시스템으로 단일 에이전트 대비 큰 성능 향상을 얻었다(단일 Opus 4 대비 +90.2%, 단 토큰은 약 15배).

## 2. 어떤 문제를 해결하는가?

- **폭넓은 병렬 탐색** — 한 문제의 여러 측면을 동시에 조사
- 단일 컨텍스트 한계 → **분리된 컨텍스트 윈도우**로 병렬 추론 용량 확대
- 복잡 질의를 서브태스크로 **동적 분해**

## 3. 핵심 철학

- **Orchestrator–Worker.** Lead 에이전트가 전략을 세우고 메모리에 계획을 기록, 서브에이전트를 스폰.
- **서브에이전트는 자족적.** 각자 **자기 완결적 태스크 서술 + 출력 형식 + 신선한 컨텍스트**를 받는다. 서로의 존재를 모르고, 도중에 협응하지 않는다.
- **분해의 품질이 전부.** 명확한 목표·출력형식·도구 사용지침·경계가 없으면 중복 작업/정보 공백 발생.

## 4. 구조

- **Lead(Orchestrator)** — 질의 분석 → 전략 수립 → 계획을 메모리에 저장 → 서브에이전트 스폰 → 결과 종합.
- **Subagents(Workers)** — 각자 독립 컨텍스트에서 병렬 조사, 자족적 지시로 동작.
- **비용 트레이드오프** — 강력하지만 토큰 ~15배. 아무 데나 쓰면 안 되고 **폭넓은 탐색이 정당화될 때** 사용.

## 5. 장점 (BOK 관점)

- **BOK의 발굴(Discover) 단계에 정확히 부합.** 낯선 엔터프라이즈 시스템의 여러 면(코드/DB/운영/이해관계자 문서)을 **병렬로 탐사**하는 것은 전형적 리서치 문제.
- **자족적 태스크 서술**은 BMAD의 Work Sharding, Skills의 자족성과 같은 결 — BOK Context Model을 강하게 지지.
- **분해 품질이 결과를 좌우**한다는 교훈 → BOK는 "무엇을 어떻게 조사할지"의 **표준 태스크 템플릿**을 제공해야 한다.

## 6. 단점 / 한계

- **비싸다(15x).** BOK 원칙(단순성·실용성)상 무분별한 멀티 에이전트는 지양. 발굴처럼 폭이 필요한 단계에 한정.
- 서브에이전트가 **상호 무지** → 지식 간 관계(그래프) 구축·상호 검증은 별도 종합 단계에서 처리해야 함.
- 근거 추적·이해도 평가는 이 아키텍처의 관심사가 아님(오케스트레이션만 제공).

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **Orchestrator–Worker를 `bok.discover`의 실행 구조로 채택**: Lead가 조사 계획 수립·메모리 기록, 워커가 소스별 병렬 채굴.
- **자족적 태스크 서술 + 명시적 출력 형식** → 워커 출력이 곧 구조화된 지식 단위가 되도록.
- **"분해 품질이 전부"** → BOK 발굴 태스크 템플릿(목표·소스·출력형식·근거 필드·경계)을 표준화.

**개선할 것**
- 워커 출력에 **provenance/confidence**를 강제하고, Lead의 **종합 단계에 지식 그래프 구성 + 교차 검증(Evaluator)** 을 추가해 "무지한 병렬 조사"를 "검증된 통합 지식"으로 승격.
- 비용 통제: 멀티 에이전트는 **발굴 단계 한정**, 이후 검증·구조화는 경량 워크플로우로.

---

### Evidence
- Anthropic, "How we built our multi-agent research system" — https://www.anthropic.com/engineering/multi-agent-research-system
- ByteByteGo, "How Anthropic Built a Multi-Agent Research System" — https://blog.bytebytego.com/p/how-anthropic-built-a-multi-agent
- ZenML LLMOps Database (사례 정리) — https://www.zenml.io/llmops-database/building-a-multi-agent-research-system-for-complex-information-tasks
