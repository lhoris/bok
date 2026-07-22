---
id:            bok://<context>/<kind>/<slug>
title:         <제목>
kind:          reference            # reference | explanation | how-to | tutorial | glossary
layer:         null                 # context | container | component | data | business | null
context:       <bounded-context>
status:        active               # active | draft | deprecated | superseded
confidence:    unverified           # unverified→inferred→corroborated→verified→authoritative
provenance:                         # 최소 1개 — 근거 없는 지식 금지
  - kind: code                      # code | doc | human | data | runtime | external
    locator: <path#Lx-Ly | interviewId | url>
    note: <무엇을 뒷받침하는가>
relations: []                       # - {type: derived-from, target: bok://...}
owner:         <team>
last_verified: <YYYY-MM-DD>
supersedes:    null
---

## TL;DR
<200자 요약 — Context 요약 계층(L2)에서 이것만 로드된다>

## 내용
<kind별 스키마: reference→arc42/C4 · explanation→ADR(Context·Decision·Consequences) · glossary→용어 정의>

## 근거 상세
<provenance 각 항목의 인용/발췌>

## 열린 질문 / 불확실성
<confidence가 낮은 부분을 명시 — 여기 적힌 것이 KU의 최저 confidence를 지배한다>
