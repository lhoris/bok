# BOK 빠른 시작 — 실제로 어떻게 쓰나

> BOK는 **낯선 코드베이스를 이해 가능한 상태로 만드는** 도구다. 마법이 아니다:
> 코드가 알려주는 것(구조)은 자동으로 초안을 잡아주고, 코드가 **알려줄 수 없는 것**(왜·업무규칙)은
> "여기 모른다"고 표식해준다. 그리고 **당신이 얼마나 이해했는지 점수로** 보여준다.

## 0. 준비 (한 번만)

BOK CLI는 파이썬 스크립트 하나다. 짧게 부르려면 `bok` 별칭을 만든다:

```sh
# macOS/Linux — ~/.local/bin/bok 로 저장하고 실행권한
printf '#!/bin/sh\npython /path/to/bok/cli/bok.py "$@"\n' > ~/.local/bin/bok && chmod +x ~/.local/bin/bok

# Windows PowerShell — 프로필에 함수 추가
function bok { python C:\path\to\bok\cli\bok.py @args }
```
(별칭이 귀찮으면 그냥 `python /path/to/bok/cli/bok.py ...` 를 매번 써도 된다. 필요한 건 Python 3.11+ 와 `pyyaml` 뿐.)

## 1. 5단계 흐름 (Python 프로젝트 기준)

**이해하고 싶은 저장소 루트에서** 실행한다:

```sh
bok init     . --project my-system --context core   # ① 지식 저장소 틀 생성
bok discover . --scope core --source src            # ② 코드에서 지식 자동 발굴
bok context  . --scope core                         # ③ 발굴한 지식 정리·분류
bok compile  .                                      # ④ 색인·관계 그래프 생성
bok ready    . --scope core --purpose understand    # ⑤ "충분히 이해했나?" 판정
```

그러면 저장소에 `bok/` 폴더가 생기고, 그 안에:
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

- **Python + SQL만** 구조 발굴된다. 다른 언어는 discover 확장이 필요하다.
- 업무규칙 **자동 추론**은 아직 CLI에 없다 — 사람 또는 Claude Code 어댑터(`adapters/claude-code/`)가 채운다.
- `verified` 승격은 **반드시 사람 서명**(`--sign`). 자동으로 올라가지 않는다 — 그게 핵심이다.

## 5. AI(Claude Code)와 함께 쓰기

대상 저장소에 어댑터를 깔면 슬래시 커맨드로 전 과정을 AI가 구동한다:
```sh
sh /path/to/bok/adapters/claude-code/install.sh   # .claude/ 에 subagent + 커맨드 설치
# 이후 Claude Code에서:  /bok-onboard core understand
```
(어댑터의 LLM 추론 흐름은 아직 파일럿 전 — 형식은 준비됨.)

---
**한 줄 요약:** `init → discover → context → compile → ready` 로 시작하고,
리포트가 알려주는 gap을 **사람+AI가 채우고 검증**하며 이해도를 올린다.
