# BMAD Method (Breakthrough Method for Agile AI-Driven Development)

> Category: AI Framework · Phase 1 · bmad-code-org/BMAD-METHOD

## 1. 왜 만들어졌는가?

두 가지 반복되는 실패에서 출발했다. (1) **계획의 비일관성** — AI에게 곧바로 "만들어줘"라고 하면 평균적이고 얕은 결과가 나온다. (2) **컨텍스트 손실** — 큰 작업을 진행하면 컨텍스트 윈도우 한계로 앞의 결정·의도가 유실된다. BMAD는 이 둘을 **역할 분업 + 구조화된 산출물 핸드오프**로 해결하려 한다.

## 2. 어떤 문제를 해결하는가?

- "생각 없는 AI 위임"으로 인한 저품질 → **에이전트가 결정권자가 아니라 안내자**가 되도록 워크플로우로 통제
- **컨텍스트 윈도우 한계** → 압축이 아니라 **설계로** 해결(Work Sharding)
- 계획–구현 간 단절 → 각 단계 산출물이 다음 단계의 입력이 되는 **조립 라인**

## 3. 핵심 철학

- **Agentic Agile.** 애자일 역할(분석가·PM·아키텍트·스크럼 마스터·개발자·QA)을 전문 AI 에이전트로 구현.
- **Structured artifacts as context.** 각 단계는 문서 산출물을 만들고, 그 문서가 다음 에이전트의 정확한 컨텍스트가 된다.
- **Context engineering over compression.** 컨텍스트를 요약해 우겨넣지 않고, 필요한 것만 담은 **자족적(self-contained) 스토리 파일**로 전달.

## 4. 구조

**2단계(Two-Phase) 모델**
1. **Agentic Planning (웹 UI / web bundle)** — 브레인스토밍, 프로젝트 브리프, PRD, PRFAQ, UX 스펙, 시장·산업 리서치 등 상류 기획을 웹 LLM 구독에서 수행 → 정제된 산출물을 IDE로 반입.
2. **Context-Engineered Development (IDE)** — 반입한 산출물을 바탕으로 구현 루프(Checkpoint Preview, Adversarial Review, 자율 개발 루프).

**에이전트(12+ 도메인 전문가)** — Analyst, PM, Architect, UX, Scrum Master, Developer, QA/Test Architect 등. "Party Mode"로 다수 페르소나를 한 세션에 모아 토론.

**핵심 메커니즘 — Work Sharding**
- Analyst → 프로젝트 브리프. PM → 브리프 기반 **PRD**. Architect → PRD 기반 **아키텍처 문서**.
- **Scrum Master 에이전트가 PRD/아키텍처를 "자족적 스토리 파일"로 분해(shard)** 한다. 각 스토리 파일은 Developer 에이전트가 필요로 하는 컨텍스트를 **정확히** 담아, 컨텍스트 손실을 설계로 차단.

**모듈/확장 팩** — BMad Builder, Test Architect, Game Dev Studio, Creative Intelligence Suite 등. 소프트웨어를 넘어 창작·비즈니스 시뮬레이션까지 확장 가능. (V6에서 Skills 아키텍처 준비 중.)

## 5. 장점

- **역할 기반 멀티 에이전트 + 산출물 핸드오프**가 명확하고 재현적. BOK의 Agent Team 설계에 직접 참조.
- **Work Sharding = 컨텍스트 엔지니어링의 구체적 구현.** "필요한 것만 담은 자족적 단위"는 BOK의 **Context Model** 핵심 아이디어와 일치.
- **2단계 분리**(무거운 기획은 웹, 정밀 구현은 IDE)로 비용·컨텍스트를 최적화.
- **확장 팩**으로 도메인 특화 → BOK의 modular/extensible 요구에 부합.
- **Adversarial Review** — 이전 산출물을 그대로 신뢰하지 않고 비판하는 절차. BOK의 "Agent Team 운영 원칙(비판·검증·대안)"과 정확히 공명.

## 6. 단점 / 한계 (BOK 관점)

- **역시 Greenfield/생성 편향.** Analyst→PM→Architect→Dev 파이프라인은 "새로 만든다"를 전제. 기존 brownfield 시스템의 **암묵지 채굴**은 다루지 않는다.
- **근거(Evidence) 기반이 아니다.** 산출물은 인간 아이디어에서 상류로 생성되며, 기존 코드·DB·운영 로그·이해관계자로부터 **역방향으로 검증**되지 않는다.
- **무겁다.** 12+ 에이전트, 2단계, 다수 문서 → 학습·운영 비용이 큼. BOK의 "복잡성을 줄이고 단순성 우선" 원칙과 충돌 위험.
- **이해도 측정 부재.** "충분히 이해했는가"를 판단하는 게이트가 없다. 스토리는 만들되 시스템 이해를 평가하지 않는다.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **자족적 컨텍스트 단위(Work Sharding)** → BOK **Context Model**의 기본 단위로 채택(단, "스토리" 대신 "지식 단위/근거 단위").
- **역할 기반 에이전트 + 산출물 핸드오프** → BOK Agent Team의 뼈대.
- **Adversarial Review** → BOK 품질 원칙(합의보다 근거)을 실행하는 검증 에이전트로 상시화.
- **2단계 분리** 발상 → BOK의 "이해(Understand) 단계"와 "개발 준비(Ready) 단계" 분리에 응용.

**개선/재설계할 것**
- 파이프라인 방향을 뒤집는다: 생성(Analyst→Dev)이 아니라 **채굴·검증(Source→Evidence→Validated Knowledge)**.
- 에이전트 수를 **대폭 축소**한다. 12+가 아니라, BOK 문제에 꼭 필요한 소수 역할(Discover / Validate / Structure / Readiness)로 단순화.
- 스토리 파일의 자족성 아이디어는 유지하되, 그 안에 **근거 링크(evidence provenance)** 를 필수 필드로 넣어 추적 가능성을 확보.

---

### Evidence
- bmad-code-org/BMAD-METHOD 저장소(2단계·web bundle·모듈·Party Mode 발췌) — https://github.com/bmad-code-org/BMAD-METHOD
- BMAD 공식 문서(Analysis/Planning/Development 단계, Skills V6) — https://docs.bmad-method.org/
- Medium, "BMAD Method Explained"(Work Sharding·스크럼 마스터 스토리 파일) — https://medium.com/@anubhavbhatt/the-bmad-method-a-smarter-way-to-build-with-ai-11c6ec07567e
- Diego Rodrigo, "BMAD in Practice" — https://diegorodrigo.dev/en/2026/04/06/bmad-in-practice-the-complete-ai-agent-development-workflow/
