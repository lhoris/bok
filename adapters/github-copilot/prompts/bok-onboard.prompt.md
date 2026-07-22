---
mode: agent
description: BOK 나선 전체로 낯선 시스템을 이해 가능→개발 가능 상태로.
---
`.github/copilot-instructions.md`(또는 `AGENTS.md`)의 나선 절차를 인자로 준 scope와 purpose(기본 feature)에 대해 수행하라: discover→context→validate→ready. 각 단계는 먼저 `bok` CLI를 실행하고 추론을 얹는다. NOT READY면 gaps를 다음 discover로 재순환. verified·최종 verdict는 사람 확인.
