# BOK 런타임 어댑터 — Codex · Claude Code · GitHub Copilot

BOK의 프레임워크 중립 정의(`agents/*.md`, `packs/core/**/SKILL.md`)를 실제 AI 코딩 CLI에 바인딩한다. 결정론은 `bok` CLI가, 추론은 각 도구의 에이전트가 맡는다.

## 구조 — 하나의 두뇌, 도구별 표면

세 도구 모두 이제 **`AGENTS.md`** 와 **Agent Skills(`SKILL.md`)** 를 읽는다. 그래서:

- **공용 두뇌**: [`AGENTS.md`](AGENTS.md) — 운영 지침(황금률·하드 규칙·나선 절차). 셋 다 이 파일로 BOK를 자연어 구동할 수 있다.
- **공용 Skills**: `packs/core/**/SKILL.md` — 세부 절차. 도구가 skills 지원 시 설치.
- **도구별 슬래시 커맨드**: 편의용 얇은 포인터(각 도구 폴더). AGENTS.md의 단계를 가리킨다.

```
adapters/
  AGENTS.md            ← 공용 운영 지침 (source of truth)
  codex/               ~/.codex/prompts/ 슬래시 커맨드 + install
  claude-code/         .claude/agents 서브에이전트 + .claude/commands + install
  github-copilot/      .github/copilot-instructions.md + prompts + install
```

## 사전조건 (공통)
`bok` 커맨드가 PATH에 있어야 한다 — `python <bok-framework>/cli/bok.py`의 shim. (QUICKSTART.md §0 참고.) Python 3.11+ · pyyaml.

## 설치 (대상 저장소 루트에서)

| 도구 | 명령 | 결과 |
|------|------|------|
| **Codex** | `sh <bok>/adapters/codex/install.sh` | `AGENTS.md`(repo) + `~/.codex/prompts/bok-*.md` |
| **Claude Code** | `sh <bok>/adapters/claude-code/install.sh` | `.claude/agents/*` + `.claude/commands/*` |
| **GitHub Copilot** | `sh <bok>/adapters/github-copilot/install.sh` | `.github/copilot-instructions.md` + `AGENTS.md` |

(Windows는 각 폴더의 `install.ps1`.)

## 슬래시 커맨드 (세 도구 공통 의미)
`/bok-onboard <scope> <purpose>` · `/bok-discover <scope> <src>` · `/bok-context <scope>` · `/bok-validate <scope>` · `/bok-ready <scope> <purpose>` · `/bok-assemble <scope> "<goal>"`

## ⚠️ 검증 상태
`bok` CLI(결정론)는 `cli/test_bok.py` 18개 테스트로 검증됨. **어댑터의 LLM 추론 흐름은 각 도구 실제 세션에서 파일럿 필요**(ROADMAP M6). 파일·형식은 각 도구의 문서화된 규약(AGENTS.md, Codex custom prompts, Copilot custom instructions)에 맞춰 작성됨.
