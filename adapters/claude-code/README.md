# BOK ⇄ Claude Code 어댑터

BOK의 프레임워크 중립 정의(`agents/*.md`, `packs/core/**/SKILL.md`)를 **Claude Code 런타임**에 바인딩한다. 결정론은 `bok` CLI가, 추론은 이 subagent들이 맡는다(agents/README의 CLI↔LLM 경계).

> ⚠️ **검증 상태**: 이 어댑터 파일들은 Claude Code의 subagent/슬래시 커맨드 **형식에 맞게** 작성됐으나, 라이브 LLM 실행은 이 저장소의 테스트 범위 밖이다. `bok` CLI 부분(결정론)은 `cli/test_bok.py`로 검증됨. 어댑터의 추론 흐름은 실제 Claude Code 세션에서 파일럿 검증이 필요하다(ROADMAP M6).

## 설치
대상 저장소(온보딩할 시스템)에서:

```sh
# 1) BOK CLI를 `bok`로 접근 가능하게 (shim)
#    예: ~/.local/bin/bok  ->  python /path/to/bok-framework/cli/bok.py "$@"
# 2) 어댑터를 .claude/로 복사
bash  /path/to/bok-framework/adapters/claude-code/install.sh    # macOS/Linux
pwsh  /path/to/bok-framework/adapters/claude-code/install.ps1   # Windows
```

설치 후 대상 저장소의 `.claude/`에 subagent(`agents/`)와 슬래시 커맨드(`commands/`)가 생긴다.

## 슬래시 커맨드
| 커맨드 | 하는 일 |
|--------|--------|
| `/bok-onboard <scope> <purpose>` | orchestrator가 나선 전체를 구동(discover→…→ready), gap 재발굴 |
| `/bok-discover <scope> <source>` | CLI 발굴 + 업무규칙 추론(code-archaeology) |
| `/bok-context <scope>` | CLI 구조화 + 타입/ADR/arc42 본문 작성 |
| `/bok-validate <scope>` | CLI grounding/전이 + adversarial 추론 + owner 서명 안내 |
| `/bok-ready <scope> <purpose>` | CLI 판정 + 서사 해석 + 다음 발굴 제안 |
| `/bok-assemble <scope> "<goal>"` | 목표에서 용어 추출 + CLI Context Pack(gaps) |

## Subagents
`bok-orchestrator · bok-discoverer · bok-curator · bok-validator · bok-readiness-assessor`
— 각 subagent는 프레임워크 정의(`agents/bok-*.md`)를 런타임 프롬프트로 옮긴 것. 확장은 subagent가 아니라 **Skill 팩**으로(D14).

## 원칙 (재확인)
CLI가 할 수 있는 것을 LLM으로 하지 않는다. subagent는 항상 먼저 `bok` 커맨드를 실행하고(결정론적 뼈대), 그 위에 추론만 얹는다. 모든 지식에 provenance, 승격은 validate 게이트 경유, `verified`는 사람 서명.
