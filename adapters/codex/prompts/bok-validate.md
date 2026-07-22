---
description: 지식을 근거 대비 검증하고 confidence를 전이한다(grounding + adversarial + 서명 안내).
argument-hint: <scope>
---
먼저 실행: `bok validate --scope $1`.
그다음 AGENTS.md의 VALIDATE 단계대로: 인용 코드가 주장을 실제로 뒷받침하는지 확인, 반례·대안·누락 제기
(fixpoint/라운드 상한에서 종료, 미해소 critical은 gap). `verified`가 필요한 KU는 사용자에게
`bok validate --sign <id> --owner <name>`을 안내. 자동 승격 금지. 이어서 `/bok-ready $1`.
