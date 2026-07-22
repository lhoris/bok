---
name: type-labeling
description: KU에 3축 타입(kind/layer/context)을 부여한다. CLI 휴리스틱이 애매한 경우를 사람/LLM이 확정. context 단계.
phase: context
wraps: bok context
---

# type-labeling

## When to use
발굴 KU를 BoK Model 타입 체계로 분류할 때. design/01 A.2.

## Procedure (CLI ↔ LLM)
1. **결정론(CLI)**: `bok context --scope <ctx>` — kind/layer 규칙으로 coverage 영역 자동 매핑.
2. **추론(LLM)**: CLI가 애매하다고 남긴 KU를 확정 —
   - `kind`: reference(사실)/explanation(왜)/how-to/tutorial/glossary (Diátaxis need).
   - `layer`: context/container/component/data/business (C4/EA).
   - `context`: 올바른 bounded context(DDD 의미 경계). 잘못된 경계는 라우팅을 망친다.

## Output
확정된 frontmatter → `bok context` 재실행으로 coverage 재매핑.

## Boundaries
한 KU가 여러 영역에 걸치면 union 허용하되, 인위적 중복은 피한다.
