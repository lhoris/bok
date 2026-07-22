---
description: '"충분히 이해했는가?"를 목적 상대적으로 판정하고 다음 발굴을 제안한다.'
argument-hint: <scope> <purpose=understand|feature|modernization>
allowed-tools: Bash, Read
---

scope=`$1`, purpose=`$2`(기본 feature)의 Readiness를 판정하라.

1. 실행: `bok ready --scope $1 --purpose ${2:-feature}` — 신호등·Hard gate·score·Tier.
2. `bok-readiness-assessor` subagent로: `readiness-report.md`를 서사로 해석, gap에 위험·버스팩터 가중을 얹어 다음 discover 우선순위 제안.
3. 수치를 뒤집지 마라 — Hard gate FAIL이면 NOT READY. 최종 verdict는 사람 승인.

NOT READY면 다음 나선: `/bok-discover $1 <해당 gap 영역>`.
