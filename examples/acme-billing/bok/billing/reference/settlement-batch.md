---
id:            bok://billing/reference/settlement-batch
title:         정산 배치 (Settlement Batch)
kind:          reference
layer:         component
context:       billing
status:        active
confidence:    corroborated
provenance:
  - kind: code
    locator: src/billing/settle.py#L40-L210
    note: SettlementJob 진입점·스케줄
  - kind: doc
    locator: docs/ops/batch-schedule.md
    note: 매일 02:00 KST 실행 명시
relations:
  - type: depends-on
    target: bok://billing/reference/ledger-store
  - type: defines-term
    target: bok://billing/glossary/idempotency-key
owner:         team-billing
last_verified: 2026-07-20
supersedes:    null
---

## TL;DR
매일 02:00 KST에 전일 거래를 모아 원장(ledger)에 정산 기록을 남기는 배치. 멱등 키로 중복 실행을 방어한다.

## 내용
- **트리거**: cron `0 2 * * *` (KST). `src/billing/settle.py`의 `SettlementJob.run()`.
- **입력**: 전일 `transactions` 중 `status=captured`.
- **출력**: `ledger` 테이블에 정산 엔트리 + `settlement_run` 로그.
- **멱등성**: run 단위 `idempotency_key`로 재실행 시 중복 기록 방지 → `bok://billing/explanation/double-settlement-guard`.

## 근거 상세
- code: `settle.py#L40-L210` — 스케줄·조회·기록 흐름 확인.
- doc: `batch-schedule.md` — 실행 시각·운영 소유 확인(02:00 KST).

## 열린 질문 / 불확실성
- 부분 실패(중간 크래시) 시 재개 지점 처리는 코드에서 명확히 확인되지 않음 → `runtime-behavior` 영역 gap.
