# BOK Research — 조사 단계

> BOK Framework는 처음부터 설계하지 않는다. 먼저 기존의 검증된 프레임워크를 **근거(Evidence) 기반**으로 분석하고, 각 접근의 장점과 한계를 도출한 뒤, "Enterprise Onboarding"이라는 문제를 중심으로 통합·개선한다.

이 폴더는 그 조사의 산출물을 누적한다. 모든 분석은 요약으로 끝내지 않고 아래 **분석 템플릿**의 7개 질문에 답한다.

---

## 조사 단계 (Phasing)

조사는 4개 카테고리로 진행하고, 각 카테고리 완료 후 **중간 통합 노트**를 남긴다. 마지막에 전체를 관통하는 **Synthesis(종합)** 를 작성해 설계 단계의 입력으로 삼는다.

| Phase | 카테고리 | 대상 | 상태 |
|------|---------|------|------|
| 1 | AI Framework | Spec Kit, BMAD Method, Claude Code Skills, Context Engineering, Agentic Workflow, Multi-Agent | ✅ 완료 |
| 2 | Enterprise Onboarding | Backstage, Developer Portal, Service Catalog, Software Archaeology, EA, Technical Due Diligence | ✅ 완료 |
| 3 | Knowledge Engineering | KM, Knowledge Engineering, Knowledge Graph, Knowledge Base, LLM Wiki, Domain Modeling | ⬜ 대기 |
| 4 | Documentation & Architecture | arc42, ADR, C4 Model, Diátaxis | ⬜ 대기 |
| — | **Synthesis** | 4개 카테고리 교차 통합 → 설계 입력 | ⬜ 대기 |

## 분석 템플릿 (모든 조사가 답해야 하는 질문)

각 대상 파일은 다음 구조를 따른다.

1. **왜 만들어졌는가?** — 등장 배경, 해결하려던 고통
2. **어떤 문제를 해결하는가?** — 문제 정의
3. **핵심 철학** — 근간이 되는 관점
4. **구조** — 아키텍처, 워크플로우, 커맨드, 산출물
5. **장점** — 뛰어난 지점
6. **단점 / 한계** — 약점, BOK의 문제(Enterprise Onboarding)에 부적합한 지점
7. **BOK에서 가져올 것 / 개선할 것** — 흡수할 요소와 재설계할 요소

각 파일 하단에 **Evidence(출처)** 를 남겨 근거를 추적 가능하게 한다.

## 조사 원칙

- 근거 없는 주장 금지. 공식 문서/저장소를 1차 출처로 삼는다.
- "Spec Kit / BMAD를 복제하지 않는다." 학습 대상이지 모방 대상이 아니다.
- BOK는 **개발 준비(Development Ready)** 가 아니라 **이해 가능(Understandable)** 을 1차 목표로 한다. 모든 분석은 "이 프레임워크는 *이해*를 얼마나 돕는가?" 라는 렌즈로 본다.

## 파일 목록

**Phase 1 — AI Framework (✅)**
- `01-ai-framework/spec-kit.md`
- `01-ai-framework/bmad-method.md`
- `01-ai-framework/claude-code-skills.md`
- `01-ai-framework/context-engineering.md`
- `01-ai-framework/agentic-workflow.md`
- `01-ai-framework/multi-agent.md`
- `01-ai-framework/_phase1-synthesis.md` ← 통합 노트

**Phase 2 — Enterprise Onboarding (✅)**
- `02-enterprise-onboarding/backstage.md`
- `02-enterprise-onboarding/developer-portal-and-service-catalog.md`
- `02-enterprise-onboarding/software-archaeology.md`
- `02-enterprise-onboarding/enterprise-architecture.md`
- `02-enterprise-onboarding/technical-due-diligence.md`
- `02-enterprise-onboarding/_phase2-synthesis.md` ← 통합 노트

**Phase 3~4** — (이후 추가)
