---
description: 지식을 근거 대비 검증하고 confidence를 전이한다(grounding + adversarial + 서명 안내).
argument-hint: <scope>
allowed-tools: Bash, Read, Grep, Edit
---

scope=`$1`을 검증하라.

1. 실행: `bok validate --scope $1` — 파일 grounding, cross-support 승격, staleness 강등, contradiction cap.
2. `bok-validator` subagent로 adversarial 추론: 인용 코드가 주장을 실제로 뒷받침하는지 확인, 반례·대안·누락 제기(fixpoint/라운드 상한에서 종료), 미해소 critical은 gap으로.
3. `verified` 승격이 필요한 KU는 사람에게 안내: `bok validate --sign <id> --owner <name>`. **자동 승격 금지.**

`validation-report.md`를 요약 보고. 이어서 `/bok-ready $1 <purpose>`.
