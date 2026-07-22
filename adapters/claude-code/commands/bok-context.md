---
description: 발굴된 후보 지식을 구조화한다 — 타입 확정, ADR/arc42 본문, 관계, coverage 매핑.
argument-hint: <scope>
allowed-tools: Bash, Read, Edit, Write
---

scope=`$1`을 구조화하라.

1. 실행: `bok context --scope $1` (영역 매핑·중복 표식) 그리고 `bok compile` (catalog/graph·dangling 검출).
2. `bok-curator` subagent로: 애매한 타입 확정, kind별 body 작성(reference→arc42/C4, explanation→ADR+대안필수), `## TL;DR` 필수, 근거 있는 관계 추가.
3. dangling relation이 있으면 미발굴 대상으로 기록 → `/bok-discover` 재실행 후보.

이어서 `/bok-validate $1`.
