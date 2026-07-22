---
name: adversarial-review
description: 지식을 그대로 신뢰하지 않고 반례·대안·누락을 체계적으로 제기한다. fixpoint/예산에서 종료, 미해소는 gap. validate 단계.
phase: validate
wraps: null   # 순수 LLM 추론 — CLI로 대체 불가
---

# adversarial-review

## When to use
confidence 승격 전, 지식을 공격해 견디는지 볼 때. research/01/bmad-method(Adversarial Review), 헌장 "합의보다 근거".

## Procedure (LLM 루프, D16)
1. **공격**: 각 주장에 반례·경계조건·누락된 대안·숨은 가정을 제기.
2. **대응**: 지적이 근거로 해소되면 통과, 아니면 confidence 정체 + gap 기록.
3. **종료 규칙**: (a) 새 라운드에 material finding 0(fixpoint), 또는 (b) 라운드 상한(`bok.yaml` adversarial.max_rounds, 기본 3), 또는 (c) 교착 시 owner escalation.
4. 미해소 **critical 지적은 승격 금지 + gap으로 방출**(루프하지 않음).

## Boundaries
무한 비판 금지 — 진전과 종결을 모두 보장. 사소한 문체 지적은 material 아님.
