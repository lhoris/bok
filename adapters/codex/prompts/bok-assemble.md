---
description: 특정 작업을 위한 Context Pack(관련 지식 + gaps)을 만든다.
argument-hint: <scope> "<goal>"
---
goal에서 핵심 용어·need를 뽑은 뒤 실행: `bok assemble --scope $1 --goal "$2"`.
결과의 units(L2/L3) + warnings(저confidence) + **gaps(모르는 것)** 를 제시하라.
gaps가 크면 작업 전 `/bok-discover $1 <gap>` 권고. gaps를 숨기지 마라.
