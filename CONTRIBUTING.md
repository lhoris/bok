# Contributing to BOK

BOK(Body of Knowledge / Brownfield Onboarding Knowledge)는 낯선 엔터프라이즈 시스템을 사람과 AI가 함께 **이해 가능한 상태 → 개발 가능한 상태**로 끌어올리는 오픈소스 프레임워크다. 기여 전 `research/_SYNTHESIS.md`(설계 근거)와 `design/`(설계)를 먼저 읽기를 권한다.

## 핵심 원칙 (기여의 기준)

기여는 다음을 지켜야 한다. 위반하는 PR은 방향과 무관하게 반려될 수 있다.

1. **근거 우선** — 모든 지식/주장에는 provenance가 있다. 근거 없는 단정 금지.
2. **단순성 우선** — 그래프DB·벡터DB·무거운 런타임을 도입하지 않는다. 마크다운 + yaml + git이 기본.
3. **검증 가능성** — 새 기능은 confidence/coverage/readiness 모델과 정합해야 한다.
4. **vendor-neutral** — 특정 에이전트/LLM/스택에 종속되는 코어 금지. 종속은 `adapters/`로.
5. **비판 환영** — 기존 설계도 근거가 있으면 뒤집는다(헌장 "합의보다 근거").

## 무엇을 어떻게 기여하나

### A. Skill / Skill 팩 (권장 확장점, D14)
새 능력은 **에이전트가 아니라 Skill**로 추가한다.
- 위치: 코어는 `packs/core/<phase>/`, 도메인은 `packs/domain/pack-<name>/`.
- 형식: `SKILL.md`(frontmatter `name`+`description` ~100토큰) + 절차 본문 + 리소스.
- 도메인 팩은 `pack.yaml`에 semver·`bok_version` 호환 범위·영역 추가(`coverage.additions.yaml`)를 선언.
- 우선순위(D22): 프로젝트 로컬 > 도메인 팩 > 코어.

### B. 코어 에이전트 (5개, 신중히)
로스터는 의도적으로 5개다(D12, BMAD 12+ 과잉 경계). **새 에이전트 제안은 "Skill로는 불가능한 이유"를 근거로 제시**해야 한다.

### C. 지식 단위(KU) 작성 규칙
- 1 지식 = 1 파일 = 1 URL. frontmatter는 `templates/ku.template.md` 준수.
- `provenance` 최소 1개, `confidence`는 자의로 verified 금지(validate/owner 서명 경유).
- 관계는 **id로 참조**(경로 아님). 파일 이동은 `bok mv`.
- 예제는 `examples/acme-billing/`을 표준 형태로 참고.

### D. 조사(research) 보강
새 프레임워크 분석은 `research/`의 **7질문 템플릿 + Evidence(URL)** 를 따른다. 요약만 있는 PR은 반려.

## PR 체크리스트
- [ ] 관련 설계 문서/조사 근거를 인용했는가.
- [ ] 단순성·vendor-neutral·근거 우선 원칙을 지켰는가.
- [ ] KU/스키마 변경 시 `templates/`와 `examples/`를 함께 갱신했는가.
- [ ] 새 임계값은 `bok.yaml`로 조정 가능한가(하드코딩 금지).
- [ ] `_system/**` 생성물을 손으로 편집하지 않았는가.

## 커밋 규약
`type(scope): summary` (예: `design(06): ...`, `feat(cli): ...`, `docs(research): ...`).

## 행동 강령
근거로 논쟁하고, 사람에게 관대하라. BOK는 "정답 하나"가 아니라 "지속 검증·개선"을 지향한다.
