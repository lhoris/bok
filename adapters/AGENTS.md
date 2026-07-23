# BOK — AI 에이전트 운영 지침 (공용)

> 이 파일은 **도구 중립**이다. Codex(`AGENTS.md`), GitHub Copilot(`AGENTS.md` / `.github/copilot-instructions.md`), Claude Code(`CLAUDE.md`/`AGENTS.md`)가 모두 이 형식을 읽는다. 대상 저장소에 이 파일이 있으면, 에이전트는 자연어로도 아래 절차를 수행할 수 있다("이 저장소 이해해줘" → BOK 나선).

## 황금률 — 결정론은 CLI, 추론은 너

BOK는 두 층이다. **먼저 `bok` CLI를 실행하고(재현 가능한 뼈대), 그 위에 추론만 얹어라.** CLI가 할 수 있는 것을 추론으로 대체하지 마라 — 검증·점수·게이트는 반드시 CLI가 판정한다(그래야 신뢰할 수 있다).

- 사전조건: `bok` 커맨드가 PATH에 있어야 한다(= `python <bok>/cli/bok.py`의 shim). 없으면 사용자에게 설치를 안내하라.
- 산출물은 대상 저장소의 `bok/` 폴더에 마크다운으로 쌓인다(사람도 너도 읽는다).

## 하드 규칙 (위반 금지)
1. **근거 없는 지식 금지.** 모든 KU는 provenance(코드/문서/사람/데이터)를 가진다.
2. **confidence·score를 지어내지 마라.** 오직 `bok validate`/`bok ready`가 판정한다.
3. **`verified` 승격은 사람 서명뿐.** `bok validate --sign <id> --owner <name>`. 자동 금지.
4. **gaps를 숨기지 마라.** "모르는 것"을 항상 드러내라 — 그게 BOK의 핵심이다.

## 빠른 시작 (원커맨드)
사용자가 "이 저장소 이해해줘/온보딩해줘"라고 하면, 먼저 **`bok onboard . --scope <ctx> --source <dir>`**
를 실행하라 — 아래 discover→context→compile→ready 1회전을 한 번에 돈다. 그 뒤 자동 발굴이
채우지 못한 `## 열린 질문`(코드로 알 수 없는 "왜")을 추론으로 채우고, 필요하면 단계를 개별 반복하라.

## 나선 절차 (각 단계: CLI 먼저 → 추론)

### DISCOVER — 근거 발굴
`bok discover --scope <ctx> --source <dir>` 실행(import 그래프·변경 히트맵·데이터모델 → 후보 KU, inferred/draft).
→ 이후 각 KU의 `## 열린 질문`("업무 규칙·의도는 코드로 알 수 없음")을 채운다: hot 코드·커밋·이슈에서 "왜"를 추론하고, 코드로 알 수 없으면 사람에게 물을 인터뷰 질문을 만든다. 모든 추론에 provenance. confidence는 inferred 유지.

### CONTEXT — 구조화
`bok context --scope <ctx>` (영역 매핑) + `bok compile` (색인·그래프·dangling 검출) 실행.
→ 애매한 타입(kind/layer/context) 확정, kind별 본문 작성(reference→arc42/C4, explanation→ADR: Context·Decision·Consequences+대안 필수), `## TL;DR` 필수, 근거 있는 관계 추가.

### VALIDATE — 검증 게이트
`bok validate --scope <ctx>` 실행(파일 grounding·cross-support 승격·staleness·contradiction).
→ adversarial 추론: 인용 코드가 주장을 실제로 뒷받침하는지 확인, 반례·대안·누락 제기(fixpoint 또는 라운드 상한에서 종료, 미해소 critical은 gap으로). `verified`가 필요하면 사용자에게 `--sign`을 안내.

### READY — 이해도 판정
`bok ready --scope <ctx> --purpose <understand|feature|modernization>` 실행(신호등·Hard gate·score·Tier R0–R4).
→ 리포트를 서사로 해석하고, gap에 위험·버스팩터 가중을 얹어 다음 discover 우선순위를 제안. 수치를 뒤집지 마라(Hard gate FAIL이면 NOT READY). 최종 verdict는 사람 승인.

### ASSEMBLE — 작업용 컨텍스트
개발 작업 전: goal에서 용어·need를 뽑아 `bok assemble --scope <ctx> --goal "<goal>"` 실행 → Context Pack(units + warnings + **gaps**)을 근거로 작업. gaps가 크면 먼저 discover.

## 나선
`ready`가 NOT READY면 gaps를 다음 discover 입력으로. 목표 tier 도달 또는 수렴 정체(사람 escalation)에서 멈춘다.

## Skills
세부 절차는 `packs/core/**/SKILL.md`(Agent Skills 형식)에 있다 — 도구가 skills를 지원하면 설치해 progressive disclosure로 로드하라.
