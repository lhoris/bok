---
description: 발굴된 지식을 구조화한다 — 타입 확정, ADR/arc42 본문, 관계, coverage 매핑.
argument-hint: <scope>
---
먼저 실행: `bok context --scope $1` 그리고 `bok compile`.
그다음 AGENTS.md의 CONTEXT 단계대로: 애매한 타입 확정, kind별 본문(reference→arc42/C4,
explanation→ADR+대안필수), `## TL;DR` 필수, 근거 있는 관계 추가. dangling은 미발굴 대상으로 기록. 이어서 `/bok-validate $1`.
