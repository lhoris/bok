# BOK 빠른 시작 — 실제로 어떻게 쓰나

> BOK는 **낯선 코드베이스를 이해 가능한 상태로 만드는** 도구다. 마법이 아니다:
> 코드가 알려주는 것(구조)은 자동으로 초안을 잡아주고, 코드가 **알려줄 수 없는 것**(왜·업무규칙)은
> "여기 모른다"고 표식해준다. 그리고 **당신이 얼마나 이해했는지 점수로** 보여준다.

## 0. 설치 (한 번만)

```sh
pip install -e /path/to/bok        # bok-framework 저장소 경로. Python 3.11+
```
이러면 어디서든 `bok` 명령을 쓸 수 있다 (긴 `python .../cli/bok.py` 필요 없음).

## 1. 한 줄로 시작 — `bok onboard`

**이해하고 싶은 저장소 루트에서** 딱 이거 하나:

```sh
bok onboard . --scope core --source src
```

이 한 명령이 안에서 5단계(init→discover→context→compile→ready)를 다 돌린다.
(단계를 따로 돌리고 싶으면 `bok init/discover/context/compile/ready`를 개별 실행해도 된다.)

실행하면 저장소에 `bok/` 폴더가 생기고, 그 안에:
- `bok/core/reference/*.md` — **자동 생성된 지식 단위**(사람도 AI도 읽는다)
- `bok/_system/readiness-report.md` — **이해도 리포트**(신호등·점수·gap 목록)
- `bok/_system/catalog.yaml`, `graph.json` — 색인·관계 그래프

## 2. 그다음 — 여기서부터가 진짜다

`bok ready`는 거의 확실히 **NOT READY**로 나온다. 정상이다. 자동 발굴은 *구조*만 캐고,
전부 `inferred`(추론) 상태이기 때문이다. 이해도를 올리려면:

1. **생성된 KU를 읽어라.** 각 파일의 `## 열린 질문`이 "코드로는 알 수 없는 것" —
   즉 **당신이 사람에게 물어야 할 것들**이다.
2. **업무 규칙·"왜"를 채워라.** 직접 알거나, 아는 사람에게 묻거나(인터뷰), AI에게
   코드를 읽혀 초안을 잡게 한다. 각 지식에 **근거(provenance)** 를 단다.
3. **검증하고 서명하라:**
   ```sh
   bok validate . --scope core                        # 근거 검사 + 자동 승격
   bok validate . --sign bok://core/... --owner 이름   # 확인된 지식에 서명 → verified
   ```
4. **다시 판정:** `bok ready`. gap이 줄고 점수가 오른다. 남은 gap이 다음에 볼 곳이다.
5. **개발할 때:** `bok assemble . --scope core --goal "하려는 작업"` →
   그 작업에 필요한 지식 + **모르는 것(gaps)** 을 묶은 Context Pack을 AI에게 준다.

이 **발굴 → 채움 → 검증 → 재판정** 을 반복하면서 이해도(R0→R1→R2→R3)를 올린다.

## 3. 무엇을 관찰할까 (이게 진짜 검증)

- 발굴된 KU가 **읽을 만한가**, 아니면 노이즈인가?
- 변경열도 우선순위가 **실제로 중요한 곳**을 가리키나?
- `## 열린 질문`이 **정말 물어야 할 것**인가?
- readiness의 gap이 **"아, 이건 진짜 내가 모르네"** 싶은가?

여기서 느끼는 마찰이 다음 버전의 방향이다. `bok status .` 로 언제든 현황(지식 수·confidence 분포)을 본다.

## 4. 한계 (지금 버전 0.1.0)

- **모든 언어**의 디렉터리 구조는 발굴된다(Java·C#·JS 등 → 패키지 지도). 단 **Python·SQL만 상세**(import 그래프·테이블). 숨김/빌드/vendor 폴더(`.git`·`.agents`·`node_modules`·`target`…)는 자동 제외.
- 업무규칙 **자동 추론**은 아직 CLI에 없다 — 사람 또는 Claude Code 어댑터(`adapters/claude-code/`)가 채운다.
- `verified` 승격은 **반드시 사람 서명**(`--sign`). 자동으로 올라가지 않는다 — 그게 핵심이다.

## 5. AI CLI 안에서 쓰기 (Codex · Claude Code · GitHub Copilot)

핵심: AI CLI는 **터미널에서 대화하는 에이전트**다. 어댑터를 깔면 에이전트가 저장소의
지침(`AGENTS.md` / `.github/copilot-instructions.md`)을 읽고, **네가 자연어로 시키면 `bok`를 대신 돌린다.**

**① 어댑터 설치 (대상 저장소 루트에서, 한 번):**
```sh
sh /path/to/bok/adapters/github-copilot/install.sh   # GitHub Copilot
sh /path/to/bok/adapters/codex/install.sh            # Codex
sh /path/to/bok/adapters/claude-code/install.sh      # Claude Code
```
(Windows는 `install.ps1`. `bok`가 설치돼 있어야 함 — §0.)

**② AI CLI를 켜고, 자연어로 시킨다:**
```
# 터미널에서 copilot 실행 → 그 안에서:
이 저장소를 BOK로 온보딩해줘
```
그러면 Copilot이 `AGENTS.md`를 읽고 `bok onboard .`를 실행한 뒤, 코드로 알 수 없는 "왜"를
추론해 채워준다. 슬래시 커맨드가 지원되면 `/bok-onboard core understand`도 된다.

> **PowerShell에서 직접 `bok onboard`** 를 치는 것 = 결정론 엔진만 실행(사람이 운전).
> **AI CLI 안에서 자연어로 시키는 것** = 에이전트가 `bok`를 운전 + "왜"까지 추론(권장).
> 어댑터의 LLM 추론 흐름은 아직 파일럿 전 — 형식은 각 도구 규약에 맞춰 준비됨.

---
**한 줄 요약:** `init → discover → context → compile → ready` 로 시작하고,
리포트가 알려주는 gap을 **사람+AI가 채우고 검증**하며 이해도를 올린다.
