# GitHub Spec Kit

> Category: AI Framework · Phase 1 · MIT License · github/spec-kit

## 1. 왜 만들어졌는가?

"Vibe coding"(느낌대로 프롬프트를 던져 코드를 생성하는 방식)의 반대 명제로 등장했다. AI 코딩 에이전트는 강력하지만, **의도(intent)가 구조화되지 않으면** 매번 다른 결과를 내고, 무엇을 만들었는지 추적할 수 없다. Spec Kit은 "명세가 곧 실행물의 소스(specifications become executable)" 라는 발상으로, 개발자가 **무엇(what)** 과 **왜(why)** 를 먼저 확정한 뒤 에이전트가 **어떻게(how)** 를 채우게 한다.

## 2. 어떤 문제를 해결하는가?

- AI 산출물의 **비결정성·비추적성** — 같은 요청에 다른 결과
- 명세를 "1회용 발판"으로 버리는 관행 → 명세를 **지속되는 소스**로 승격
- 여러 코딩 에이전트(Copilot, Claude Code, Codex 등 30+) 간 **워크플로우 파편화**

## 3. 핵심 철학

- **Intent-driven / Spec-Driven Development(SDD).** "What before How."
- **Executable specification.** 명세는 문서가 아니라 구현을 생성하는 실행 가능한 산출물.
- **Technology independence.** 특정 에이전트·스택에 묶이지 않는 실험적 목표.

## 4. 구조

CLI `specify` (uv 설치, Python 3.11+, Git 필요)가 에이전트별 슬래시 커맨드와 스캐폴딩을 설치한다. 워크플로우는 순차적 7단계 + 선택 정제 커맨드:

| 단계 | 커맨드 | 산출물 |
|-----|--------|--------|
| 1 | `/speckit.constitution` | 프로젝트 지배 원칙·개발 가이드라인 |
| 2 | `/speckit.specify` | 요구사항·유저 스토리 (what) |
| 3 | `/speckit.plan` | 기술 아키텍처·스택 결정 (how) |
| 4 | `/speckit.tasks` | 실행 가능한 태스크 목록 |
| 5 | `/speckit.taskstoissues` | 태스크 → GitHub 이슈 |
| 6 | `/speckit.implement` | 태스크 실행(구현) |
| 7 | `/speckit.converge` | 코드베이스 ↔ spec/plan/tasks 정합성 평가 후 잔여 작업 추가 |

정제 커맨드: `/speckit.clarify`(미결 영역 해소), `/speckit.analyze`(교차 정합성), `/speckit.checklist`(품질 검증).

스캐폴딩: `.specify/`(templates/memory/extensions/presets), `.claude/commands/`(에이전트별), `specs/`(명세 산출물). 커스터마이징은 **Extensions/Presets/Bundles** 3계층. 템플릿 해석 우선순위: project overrides > presets > extensions > core.

3대 사용 시나리오: 0→1(greenfield), Creative Exploration(병렬 구현), **Iterative Enhancement(brownfield 현대화)**.

## 5. 장점

- **게이트 기반 순차 진행** — 각 단계가 검증되기 전엔 다음으로 넘어가지 않음(품질 체크포인트). BOK의 "이해 검증(Knowledge Validation)" 게이트에 직접 대응 가능.
- **Constitution** — 프로젝트 원칙을 최상위 컨텍스트로 고정. 재사용 가능한 거버넌스 레이어.
- **커맨드 체계가 명료** — `bok.discover / bok.context / bok.ready` 같은 BOK 커맨드 설계의 좋은 참조.
- **에이전트 중립성 + 템플릿 오버라이드 계층** — vendor-neutral 요구에 부합.
- **`/converge`, `/analyze`** — 산출물 간 정합성을 기계적으로 검증하는 발상.

## 6. 단점 / 한계 (BOK 관점)

- **Greenfield 생성 편향.** 핵심은 "명세 → 코드 생성". 그러나 BOK의 문제는 **이미 존재하는 시스템을 이해**하는 것. Spec Kit은 "무엇을 만들지"를 인간이 이미 안다고 가정한다. BOK는 "무엇이 이미 있는지 모른다"에서 출발한다.
- **Evidence(근거) 개념 없음.** 명세는 인간의 의도에서 나오지, 기존 코드·문서·사람으로부터 **채굴·검증**되지 않는다. BOK는 지식을 근거에서 도출·검증해야 한다.
- **업무 지식/도메인 용어/운영 정책** 을 다루는 계층이 없다. 코드 생성 파이프라인이지 지식 베이스가 아니다.
- **이해도(Understanding)를 측정하지 않는다.** 정합성은 검사하지만 "우리가 이 시스템을 충분히 이해했는가?"는 질문하지 않는다.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **게이트형 단계 워크플로우** + 단계별 명시적 산출물.
- **Constitution** 개념 → BOK의 프로젝트 상수/제약 레이어.
- **명료한 슬래시 커맨드 네이밍**과 정제 커맨드(`clarify/analyze/checklist`) 패턴.
- **템플릿 오버라이드 3계층** → BOK의 확장성/vendor-neutral 확보.

**개선/재설계할 것**
- 방향을 뒤집는다: Spec Kit은 *의도 → 코드*. BOK는 *기존 시스템 → 근거 → 검증된 지식 → (그 다음에야) 의도/개발*.
- `/specify` 대신 **`bok.discover`(채굴)** 를 상류에 둔다. 명세 이전에 **Body of Knowledge 구축**이 온다.
- `/analyze`(코드-명세 정합성)를 **Knowledge Validation**(지식-근거 정합성, 이해도 평가)으로 확장한다.

---

### Evidence
- github/spec-kit 저장소 (README/docs 발췌, MIT, 커맨드·스캐폴딩 구조) — https://github.com/github/spec-kit
- Spec Kit 공식 문서 — https://github.github.com/spec-kit/
- GitHub Blog, "Spec-driven development with AI" — https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- Microsoft for Developers, "Diving Into Spec-Driven Development" — https://developer.microsoft.com/blog/spec-driven-development-spec-kit/
