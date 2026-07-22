---
description: 특정 작업을 위한 Context Pack(관련 지식 + gaps)을 만들어 준다.
argument-hint: <scope> "<goal>"
allowed-tools: Bash, Read
---

scope=`$1`, goal=`$2`에 대한 Context Pack을 조립하라.

1. goal에서 핵심 용어·need(kind)·bounded context를 뽑아라(관련성 정밀화).
2. 실행: `bok assemble --scope $1 --goal "$2"` (필요 시 `--need`, `--budget`).
3. Pack의 `units`(L2/L3) + `warnings`(저confidence) + **`gaps`(모르는 것)** 를 제시하라. gaps가 크면 작업 전 `/bok-discover $1 <gap>` 권고.

원칙: gaps를 숨기지 마라 — AI는 무엇을 모르는지 알고 작업해야 한다.
