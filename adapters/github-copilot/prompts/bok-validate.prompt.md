---
mode: agent
description: 지식을 근거 대비 검증하고 confidence를 전이한다.
---
scope에 대해 `bok validate --scope <ctx>`를 실행한 뒤, 인용 코드가 주장을 실제로 뒷받침하는지 확인하고 반례·대안·누락을 제기하라(미해소 critical은 gap). `verified`가 필요한 KU는 `bok validate --sign <id> --owner <name>`을 사용자에게 안내 — 자동 승격 금지.
