# BOK Core Skill Pack

design/03 §2를 실체화한 코어 Skill들. 각 Skill = `SKILL.md`(progressive-disclosure frontmatter: name+description ~100토큰) + 절차 본문. 에이전트가 작업 중 관련 Skill만 로드한다(research/01/claude-code-skills).

## 구조
```
discover/  code-archaeology · human-externalization · kg-extraction
context/   type-labeling · arc42-authoring · adr-authoring
validate/  grounding-check · adversarial-review
ready/     coverage-assessment
shared/    context-assembly
```

## 해석 우선순위 (D22)
프로젝트 로컬 Skill > 도메인 팩(`packs/domain/*`) > **코어(여기)**. 가장 구체적인 것이 이긴다.

## 원칙
각 Skill은 **결정론적 부분을 `bok` CLI에 위임**하고, LLM 추론만 절차로 기술한다. CLI가 할 수 있는 것을 LLM으로 하지 않는다(단순성·재현성).
