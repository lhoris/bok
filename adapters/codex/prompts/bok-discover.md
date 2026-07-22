---
description: 코드에서 근거를 발굴해 후보 지식 단위를 만든다(결정론 + 업무규칙 추론).
argument-hint: <scope> <source-dir=src>
---
먼저 실행: `bok discover --scope $1 --source ${2:-src}`.
그다음 AGENTS.md의 DISCOVER 단계대로: 각 KU의 `## 열린 질문`을 채우고(hot 코드·커밋에서 "왜" 추론),
코드로 알 수 없는 것은 인터뷰 질문으로. 모든 추론에 provenance, confidence는 inferred 유지. 이어서 `/bok-context $1`.
