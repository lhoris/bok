---
id:            bok://billing/explanation/double-settlement-guard
title:         이중 정산 방지 규칙
kind:          explanation
layer:         component
context:       billing
status:        active
confidence:    verified
provenance:
  - kind: code
    locator: src/billing/settle.py#L120-L180
    note: idempotency_key UNIQUE 제약 + 사전 존재검사
  - kind: human
    locator: interview/2026-07-18-kim-billing
    note: "왜 코드+DB 이중 검사인지 — 과거 장애 재발 방지"
relations:
  - type: derived-from
    target: bok://billing/reference/settlement-batch
  - type: defines-term
    target: bok://billing/glossary/idempotency-key
owner:    kim
last_verified:    2026-07-22
supersedes:    null
---

## TL;DR
같은 정산 run이 두 번 원장에 반영되면 이중 청구가 발생한다. 이를 막기 위해 **애플리케이션 사전검사 + DB UNIQUE 제약**의 이중 방어를 둔다.

## 배경 / 문제
2025년 배치 재실행 사고로 일부 고객이 이중 청구됨. 이후 규칙: 정산은 반드시 멱등해야 한다.

## 내용 (Decision)
- **Context**: 배치는 운영자가 수동 재실행할 수 있고, 크래시 후 재시도도 발생.
- **Decision**: `idempotency_key`(run 식별자)에 DB UNIQUE 제약 + 기록 전 존재검사.
- **Considered Options**:
  - (A) DB UNIQUE만 — 채택 안 함: 위반 시 예외 처리가 지저분.
  - (B) 앱 검사만 — 채택 안 함: 경합(race)에서 취약.
  - (C) 앱 검사 + DB UNIQUE — **채택**: 방어 심층화.
- **Consequences**: 재실행 안전. 단, 키 생성 로직이 잘못되면 정산 누락 위험(트레이드오프).

## 근거 상세
- code: UNIQUE 제약·사전검사 위치 확인.
- human(kim): 이중 검사 채택 이유가 과거 사고임을 확인 — 단, 발화자 1인 근거.

## 열린 질문 / 불확실성
- `idempotency_key` 생성 규칙 자체의 정확성은 미검증 → **owner 서명 필요(verified 승격 조건)**.
