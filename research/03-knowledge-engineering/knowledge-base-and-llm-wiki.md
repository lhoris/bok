# Knowledge Base & LLM Wiki (DeepWiki / compile-once-maintain)

> Category: Knowledge Engineering · Phase 3 · (헌장의 "Knowledge Base" + "LLM Wiki" 통합)
> ⭐ Phase 2가 찾던 미싱 링크("발굴→구조화→유지"의 연결)의 가장 근접한 선례.

## 1. 왜 만들어졌는가?

고전 RAG는 질문마다 원문 청크를 다시 검색·처리한다 — 비효율적이고 지식이 축적되지 않는다. **LLM Wiki/DeepWiki** 패턴은 코드·문서를 한 번 분석해 **지속되고 상호연결된 지식 베이스(마크다운 위키)** 로 컴파일하고, 코드 변경에 맞춰 **계속 갱신**한다.

## 2. 어떤 문제를 해결하는가?

- RAG의 "매번 처음부터" 비효율 → **compile once, maintain continuously**
- 코드베이스의 **자동 문서화·온보딩 가속**
- 사람과 AI 모두를 위한 **영속적 접지(grounding) 레이어**

## 3. 핵심 철학

- **컴파일된 지식 > 매번 검색.** 지식을 **원자적 엔티티·토픽**으로 추출해 영속 메모리 레이어를 만든다.
- **저장소에 사는 위키.** docs/ 아래 마크다운, 코드와 함께 버전 관리.
- **사람+AI 공용 접지 레이어.** — BOK 철학("사람과 AI가 같은 BoK 공유")과 **정확히 일치**.
- **소스 접지(grounding).** DeepWiki는 답을 **실제 소스코드에 접지**.

## 4. 구조

- **DeepWiki** — GitHub 저장소의 소스·테스트·문서를 읽어 아키텍처 다이어그램·모듈 관계·데이터 흐름·**설계 근거(design rationale)** 를 구조화한 인터랙티브 위키로 생성. 자연어 질의를 소스에 접지해 응답.
- **LLM Wiki 패턴(llm-wiki-skill)** — 지식을 원자적 엔티티/토픽으로 추출해 상호연결된 마크다운으로 컴파일, ~200 페이지 규모까지 **벡터DB·임베딩 인프라 없이** 동작. 저장소에 버전 관리되며 사람+LLM의 접지 레이어가 됨.
- 갱신: 코드 변경 시 위키를 **최신 상태로 유지**.

## 5. 장점 (BOK 관점)

- **BOK의 물리적 구현 형태의 유력 후보.** "저장소에 사는, 버전 관리되는, 사람+AI 공용 마크다운 지식 베이스"는 BOK가 목표하는 산출물 그 자체.
- **compile-once-maintain = Phase 2의 미싱 링크("유지")** 를 실제로 구현한 사례. 카탈로그 부패 문제의 실용 해법.
- **벡터DB 없이 마크다운 + progressive disclosure** — BOK의 단순성·vendor-neutral·Human Friendly에 완벽 부합. (Claude Skills와 같은 결.)
- **design rationale 추출** — ADR([[../04-documentation-architecture]])과 연결될 "왜" 지식.
- **소스 접지** — BOK의 provenance를 자연스럽게 구현.

## 6. 단점 / 한계 (BOK 관점)

- **코드 중심 · 생성 편향.** DeepWiki류는 대부분 코드에서 문서를 **생성**한다. Phase 3(SECI)이 강조한 **암묵지·업무 규칙·운영 정책**(코드에 없는 90%)은 다루지 못한다.
- **검증·confidence·이해도 게이트 부재.** 생성된 위키가 정확한지, 조직이 이해했는지 평가하지 않는다. "그럴듯한 문서"의 위험(환각).
- **자동 생성물의 신뢰** — 사람 검증 루프 없이 신뢰하면 잘못된 이해를 확산.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **compile-once-maintain 마크다운 위키를 BOK의 물리 산출 포맷으로 채택** — 저장소에 사는, 버전 관리, 사람+AI 공용.
- **벡터DB 없는 마크다운 + progressive disclosure** — 단순성.
- **소스 접지(grounding)** → provenance 구현.
- **design rationale 추출** → "왜" 지식.

**개선할 것 (BOK가 결정적으로 더하는 것)**
- **코드 생성 → 코드+암묵지 발굴**([[knowledge-management-and-engineering]]): 위키에 업무 규칙·운영 정책·이해관계자 지식을 통합.
- **생성 → 검증**: 각 위키 항목에 provenance·confidence·last-verified, 그리고 **사람 검증 루프**(Evaluator–Optimizer).
- **문서 → 이해도 게이트**: 위키 커버리지/검증 수준으로 **Development Readiness** 를 판정.
- 즉 BOK = **"검증되고 이해도가 측정되는 LLM Wiki"**.

---

### Evidence
- RAGFlow, "Explore RAGFlow on DeepWiki" — https://ragflow.io/docs/deepwiki
- nashsu/llm_wiki (GitHub) — https://github.com/nashsu/llm_wiki
- gold24park/open-deepwiki, "Automated Wiki Generation for Codebases Using LLMs" — https://github.com/gold24park/open-deepwiki
- Medium(Dipak Kr das), "Code Wiki: LLM-Maintained Documentation for Your Codebase" — https://medium.com/@dipakkrdas/code-wiki-llm-maintained-documentation-for-your-codebase-fc54f94bef6d
