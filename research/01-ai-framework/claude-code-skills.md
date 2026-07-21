# Claude Code / Agent Skills

> Category: AI Framework · Phase 1 · Anthropic · SKILL.md + Progressive Disclosure

## 1. 왜 만들어졌는가?

에이전트에게 능력을 부여하는 두 방식 — 시스템 프롬프트에 전부 넣기, 또는 MCP로 모든 도구를 초기 로드하기 — 은 **컨텍스트 윈도우를 낭비**한다. Skills는 "필요할 때 필요한 만큼만" 지식을 로드하는 **파일 시스템 기반 능력 패키지**로 이 낭비를 해결한다.

## 2. 어떤 문제를 해결하는가?

- 능력(지식·절차·스크립트)이 많아질수록 컨텍스트가 초기부터 오염되는 문제
- MCP가 "시작 시 전부 로드"하는 것과 대비되는 **지연 로딩(lazy loading)** 필요
- 재사용 가능한 전문 지식을 **이식 가능한 단위(SKILL.md + 리소스)** 로 패키징

## 3. 핵심 철학

- **Progressive Disclosure(점진적 공개).** 정보를 단계적으로 노출해 토큰 효율 유지.
- **파일 시스템이 곧 지식 저장소.** 에이전트는 경로/메타데이터만 알고, 실행 시점에 본문·리소스를 읽는다.
- **자족성 + 이식성.** 스킬은 자기 완결적이고 다른 에이전트/프로젝트로 옮길 수 있다.

## 4. 구조

3계층 로딩:
1. **Discovery** — 세션 시작 시 모든 스킬의 `name`+`description`(YAML frontmatter, 스킬당 ~100 토큰)만 시스템 프롬프트에 적재.
2. **Inspection** — 작업과 관련돼 보이면 그때 `SKILL.md` 본문(전체 지시)을 읽음.
3. **Full Context** — 더 깊이가 필요하면 보조 파일(references/scripts/assets)을 마저 읽음.

즉 **"인덱스 → 요약 → 상세"** 의 3단 점진 공개. 이 구조 자체가 지식 조직화의 강력한 패턴이다.

## 5. 장점

- **점진적 공개는 BOK의 지식 조직화 원리로 직결.** BOK의 Body of Knowledge도 "한 번에 다 읽히는 문서 더미"가 아니라 **인덱스 → 요약 → 근거 상세**로 층화되어야 한다.
- **메타데이터 우선 탐색** — `description`으로 관련성을 판단하는 방식은 BOK Wiki/Context Model의 라우팅에 그대로 적용 가능.
- **이식성** — 스킬 = 자족 폴더. BOK의 지식 단위도 이식 가능한 폴더로 설계할 근거.
- **사람도 같은 파일을 읽는다** — AI Native이면서 Human Friendly. BOK 철학("사람과 AI가 같은 BoK 공유")과 정확히 일치.

## 6. 단점 / 한계 (BOK 관점)

- Skills는 **"어떻게 행동할지"(능력)** 를 담지, **"이 시스템이 무엇인지"(이해)** 를 담는 구조가 아니다. 지식 검증·근거 추적·이해도 측정은 범위 밖.
- 스킬 간 관계(지식 그래프)를 표현하지 않는다 — 평면적 폴더 집합.
- 콘텐츠의 **신뢰도/출처**를 다루는 필드가 없다.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **Progressive Disclosure를 BOK의 1급 원리로 채택.** BoK 모델 = 인덱스(카탈로그) → 요약(개요) → 근거(상세)의 층화.
- **메타데이터 우선(description 기반) 라우팅** → Context Model에서 "지금 이 작업에 필요한 지식만 로드".
- **자족적·이식 가능한 폴더 단위** → BOK 지식 단위의 물리 포맷.

**개선할 것**
- 각 지식 단위에 **provenance(출처/근거)**, **confidence(검증 수준)**, **relations(연결)** 필드를 추가해 "능력 패키지"를 "**검증된 지식 패키지**"로 승격.

---

### Evidence
- Agent Skills — Claude Platform Docs — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- "Claude Agent Skills: A First Principles Deep Dive" — https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/
- MCPJam, "Progressive Disclosure Might Replace MCP" — https://www.mcpjam.com/blog/claude-agent-skills
