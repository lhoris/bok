---
description: BOK 나선 전체를 구동해 낯선 시스템을 이해 가능→개발 가능 상태로. discover→context→validate→ready, gap 재발굴.
argument-hint: <scope> <purpose=understand|feature|modernization>
allowed-tools: Task, Bash, Read, Grep, Glob
---

`bok-orchestrator` subagent를 통해 scope=`$1`, purpose=`$2`(기본 feature)에 대한 BOK onboarding 나선을 구동하라.

1. `bok-orchestrator`에게 위임: 발굴 계획 → `bok-discoverer` 스폰 → `bok-curator`(context) → `bok-validator` → `bok-readiness-assessor`.
2. `bok ready`의 verdict를 보고. NOT READY면 gaps를 다음 나선 입력으로 재순환.
3. 목표 tier 도달 또는 수렴 정체 시 종료하고, 남은 gap을 known-unknowns로 명시.

원칙: 각 단계는 먼저 `bok` CLI(결정론)를 실행하고 추론을 얹는다. verified 승격·최종 verdict는 사람 확인.
