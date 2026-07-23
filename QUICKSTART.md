# BOK 빠른 시작 — 실제로 어떻게 쓰나

> BOK는 **낯선 코드베이스를 이해 가능한 상태로 만드는** 도구다. 코드가 알려주는 것(구조)은 자동으로
> 초안을 잡고, 코드가 **알려줄 수 없는 것**(왜·업무규칙)은 "여기 모른다"고 표식하며, **당신이 얼마나
> 이해했는지 점수로** 보여준다.

---

## 설치 (한 번만)

```sh
pip install -e /path/to/bok        # bok-framework 저장소 경로. Python 3.11+
```
이러면 어디서든 `bok` 명령이 생긴다.

---

## 사용 방식은 둘 — 먼저 고르세요

| | 방식 A — **AI CLI 안에서** (권장) | 방식 B — 직접 (터미널) |
|--|--------------------------------|----------------------|
| 무엇 | Copilot/Codex/Claude에게 **말로 시킴** | `bok` 명령을 직접 타이핑 |
| 누가 운전 | AI가 `bok`를 대신 돌리고 "왜"까지 추론 | 당신이 직접 (엔진 수동) |
| 언제 | 평소 사용 | 디버깅·검증·자동화 |

---

## 방식 A — AI CLI 안에서 쓰기 (Copilot·Codex·Claude) ★

**핵심: `bok discover` 같은 걸 직접 칠 필요 없다. AI한테 말로 시키면 AI가 `bok`를 대신 실행한다.**

**① 대상 저장소에 어댑터 한 번 설치** (AI에게 "이 저장소는 BOK로 온보딩한다"는 지침을 심음):
```powershell
# GitHub Copilot  (Windows PowerShell)
pwsh C:\path\to\bok\adapters\github-copilot\install.ps1
# Codex          → pwsh ...\adapters\codex\install.ps1
# Claude Code    → pwsh ...\adapters\claude-code\install.ps1
```
```sh
# macOS/Linux 는 install.sh
sh /path/to/bok/adapters/github-copilot/install.sh
```
→ 저장소에 `AGENTS.md`(+ Copilot은 `.github/copilot-instructions.md`)가 생긴다.

**② AI CLI를 켠다:**
```powershell
copilot          # 또는  codex  /  claude
```

**③ 그 안에서 자연어로 시킨다:**
```
이 저장소를 BOK로 온보딩해줘. bok CLI 설치돼 있어.
```
→ AI가 `AGENTS.md`를 읽고 **알아서 `bok onboard .`** 를 실행한 뒤, 코드로 알 수 없는 "왜"를
추론해 채워준다. 슬래시 커맨드를 지원하면 `/bok-onboard core understand` 도 된다.

> ⚠️ `bok` 엔진 자체는 검증됨. 하지만 **AI가 `bok`를 잘 불러주는지는 아직 파일럿 전**이다(형식은 각
> 도구 공식 규약에 맞춤). AI가 엉뚱하게 하거나 `bok`를 못 찾으면 그 화면을 캡처해 제보하면 고친다.

---

## 방식 B — 직접 (터미널에서 `bok`)

한 줄이면 된다 — 대상 저장소 루트에서:
```sh
bok onboard . --scope core --source src
```
이 한 명령이 5단계(init→discover→context→compile→ready)를 다 돈다.
(개별로: `bok init/discover/context/compile/ready`.)

실행하면 `bok/` 폴더가 생긴다:
- `bok/core/reference/*.md` — 자동 생성된 지식 단위(사람도 AI도 읽음)
- `bok/_system/readiness-report.md` — 이해도 리포트(신호등·점수·gap)
- `bok/_system/catalog.yaml`, `graph.json` — 색인·관계 그래프

---

## 그다음 — 여기서부터가 진짜다 (방식 A·B 공통)

`bok ready`는 거의 확실히 **NOT READY**로 나온다. 정상이다 — 자동 발굴은 *구조*만 캐고 전부
`inferred`(추론)이기 때문. 이해도를 올리려면:

1. **생성된 KU를 읽어라.** 각 파일의 `## 열린 질문`이 "코드로는 알 수 없는 것" = 사람에게 물을 목록.
2. **업무 규칙·"왜"를 채워라.** (방식 A면 AI가 도와준다.) 각 지식에 근거(provenance)를 단다.
3. **검증하고 서명하라:** `bok validate . --scope core` → `bok validate . --sign bok://core/... --owner 이름`
4. **다시 판정:** `bok ready`. gap이 줄고 점수가 오른다.
5. **개발할 때:** `bok assemble . --scope core --goal "하려는 작업"` → 필요한 지식 + gaps를 AI에게.

이 **발굴 → 채움 → 검증 → 재판정** 을 반복하며 이해도(R0→R1→R2→R3)를 올린다.

## 무엇을 관찰할까 (이게 진짜 검증)
발굴된 KU가 읽을 만한가? 변경열도 우선순위가 실제 중요한 곳인가? `## 열린 질문`이 정말 물어야 할
것인가? gap이 "진짜 내가 모르네" 싶은가? — 여기서 느끼는 마찰이 다음 버전의 방향이다.

## 한계 (0.1.0)
- **모든 언어**의 디렉터리 구조는 발굴(Java·C# 등 → 패키지 지도). 단 **Python·SQL만 상세**(import·테이블).
  숨김/빌드/vendor 폴더(`.git`·`.agents`·`node_modules`·`target`…)는 자동 제외.
- 업무규칙 **자동 추론**은 CLI엔 없다 — 방식 A(AI)나 사람이 채운다.
- `verified` 승격은 **반드시 사람 서명**. 자동 금지 — 그게 핵심이다.
