---
description: 이해했는지 목적 상대적으로 판정하고 다음 발굴을 제안한다.
argument-hint: <scope> <purpose=understand|feature|modernization>
---
먼저 실행: `bok ready --scope $1 --purpose ${2:-feature}`.
그다음 AGENTS.md의 READY 단계대로: 리포트를 서사로 해석하고, gap에 위험·버스팩터 가중을 얹어
다음 discover 우선순위를 제안. 수치를 뒤집지 마라(Hard gate FAIL이면 NOT READY). 최종 verdict는 사람 승인.
