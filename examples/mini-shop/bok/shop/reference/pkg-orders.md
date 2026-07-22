---
id: bok://shop/reference/pkg-orders
title: orders 패키지
kind: reference
layer: component
context: shop
status: draft
confidence: inferred
provenance:
- kind: code
  locator: src/orders/repository.py
  note: auto-discovered module
- kind: code
  locator: src/orders/service.py
  note: auto-discovered module
relations:
- type: depends-on
  target: bok://shop/reference/pkg-catalog
- type: depends-on
  target: bok://shop/reference/pkg-payments
owner: unassigned
last_verified: '1970-01-01'
supersedes: null
---

## TL;DR
`orders` 패키지 (2 모듈). 변경열도(loc (uncommitted)): 23. 내부 의존: catalog, payments

## 내용
(자동 발굴 초안 — import 그래프에서 구조를 복원했다.)

## 열린 질문 / 불확실성
- ⚠️ AUTO-DISCOVERED, confidence=inferred. 사람/owner 검증 전까지 신뢰 금지.
- 이 패키지의 **업무 규칙·의도(왜)**는 코드 구조만으로 알 수 없음 → human-externalization 필요.
