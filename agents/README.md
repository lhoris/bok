# BOK Agents (코어 5)

design/03을 실체화한 **vendor-neutral 역할 정의**. 각 에이전트는 얇다(Thin Agents, D12) — 재사용 절차는 `packs/`의 Skill에 있다.

## CLI ↔ LLM 경계 (핵심)
BOK는 **결정론(`bok` CLI)** 과 **추론(LLM 에이전트)** 을 분리한다.
- **CLI가 하는 것**: 구조 발굴·grounding·confidence 전이·coverage·게이트 계산 (재현 가능·검증 가능).
- **에이전트가 하는 것**: 코드 너머의 "왜"(업무 규칙) 추론, 인적 발굴, adversarial 비판, 애매한 타입 판단.

에이전트는 **가능한 한 CLI를 호출**하고(결정론적 뼈대), 그 위에 추론만 얹는다. 이것이 "근거 우선·단순성"을 지키는 방법이다.

## 로스터
| Agent | 커맨드 | 책임 | 인스턴스 |
|-------|--------|------|---------|
| [bok-orchestrator](bok-orchestrator.md) | 나선 전체 | 계획·스폰·게이트·종합 | 1 |
| [bok-discoverer](bok-discoverer.md) | discover | 자족 발굴 1건 (Skill로 변신) | N |
| [bok-curator](bok-curator.md) | context | 구조화·타입·스키마 | 1 |
| [bok-validator](bok-validator.md) | validate | 상시 비판·검증 | 1 |
| [bok-readiness-assessor](bok-readiness-assessor.md) | ready | 이해도 판정 | 1 |

## 어댑터
이 정의는 프레임워크 중립이다. 특정 런타임(Claude Code subagent, 기타)에는 `adapters/`가 매핑한다(향후). 확장은 에이전트가 아니라 **Skill 팩**으로(D14).
