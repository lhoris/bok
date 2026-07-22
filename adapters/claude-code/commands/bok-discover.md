---
description: 코드에서 근거를 발굴해 후보 지식 단위를 만든다(결정론 + 업무규칙 추론).
argument-hint: <scope> <source-dir=src>
allowed-tools: Bash, Read, Grep, Glob
---

scope=`$1`, source=`$2`(기본 src)에 대해 발굴하라.

1. 실행: `bok discover --scope $1 --source ${2:-src}` — 구조·의존·데이터모델·히트맵에서 후보 KU(inferred/draft).
2. `bok-discoverer` subagent로 CLI가 남긴 `## 열린 질문`을 채워라 — hot 코드에서 업무 규칙 추론, 커밋/이슈에서 "왜" 추론. 코드로 알 수 없는 것은 인터뷰 가이드로 사람에게.
3. 모든 추론에 provenance. confidence는 inferred 유지(승격은 `/bok-validate`).

이어서 `/bok-context $1`.
