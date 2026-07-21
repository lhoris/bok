---
id:            bok://billing/glossary/idempotency-key
title:         Idempotency Key (멱등 키)
kind:          glossary
layer:         null
context:       billing
status:        active
confidence:    authoritative
provenance:
  - kind: data
    locator: db/schema/ledger.sql#L22
    note: "settlement_run.idempotency_key VARCHAR(64) NOT NULL UNIQUE"
relations:
  - type: part-of
    target: bok://billing/reference/settlement-batch
owner:         team-billing
last_verified: 2026-07-20
supersedes:    null
---

## TL;DR
같은 작업을 여러 번 실행해도 결과가 한 번 실행한 것과 동일하도록 보장하는 식별자. billing에서는 정산 run 단위로 부여된다.

## 정의
- **용어**: Idempotency Key
- **billing에서의 의미**: `settlement_run`의 유일 식별자. 동일 키의 재기록을 DB가 거부.
- **규범 근거**: `ledger.sql`의 `UNIQUE NOT NULL` 제약 → 스키마가 진실(authoritative).

## 근거 상세
- data: DDL이 제약을 규범적으로 정의 → 사람 서명 없이도 최상위 신뢰.
