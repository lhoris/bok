---
description: BOK 나선 전체로 낯선 시스템을 이해 가능→개발 가능 상태로 (discover→context→validate→ready).
argument-hint: <scope> <purpose=understand|feature|modernization>
---
AGENTS.md의 "나선 절차" 전체를 scope=`$1`, purpose=`${2:-feature}`로 수행하라.
DISCOVER→CONTEXT→VALIDATE→READY 순으로, 각 단계는 먼저 `bok` CLI를 실행하고 추론을 얹는다.
`bok ready`가 NOT READY면 gaps를 다음 discover 입력으로 재순환. verified·최종 verdict는 사람 확인.
