# 예제: mini-shop — `bok discover` 실증 (M2)

`acme-billing`이 **손으로 작성한** BoK라면, `mini-shop`은 BOK가 **원시 코드에서 스스로 캐낸** BoK다. 실제 소스(`src/`, `db/schema.sql`)에 `bok discover`를 돌려 후보 지식을 자동 생성한다.

## 재현
```bash
python cli/bok.py init     examples/mini-shop --project mini-shop --context shop --force
python cli/bok.py discover examples/mini-shop --scope shop --source src
python cli/bok.py compile  examples/mini-shop
python cli/bok.py ready    examples/mini-shop --scope shop --purpose feature
```

## `bok discover`가 한 일 (결정론적 아키올로지, LLM 없음)
> 근거: Software Archaeology(`research/02/software-archaeology.md`) — 저장소 마이닝·변경 히트맵·의존성 복원.

- **import 그래프**(Python `ast`) → 패키지 KU 3개(`pkg-orders/payments/catalog`)와 `depends-on` 관계. `orders`가 `payments`·`catalog`에 의존함을 코드에서 복원.
- **데이터모델 추출**(SQL DDL `CREATE TABLE`) → 테이블 KU 3개(`table-products/orders/payments`).
- **변경 히트맵** → 우선순위(`orders > payments > catalog`). git 이력이 있으면 커밋 수, 없으면 LOC 대체(정직하게 출력).
- 산출: `bok/shop/reference/*.md` 6개 + `_system/discovery-plan.md`.

## 핵심 — 발굴 ≠ 이해 ≠ 준비

생성된 모든 KU는:
- `confidence: inferred` · `status: draft` — **단일 자동 근거**. 사람 검증 전.
- `## 열린 질문`에 스스로 한계를 명시: *"업무 규칙·의도(왜)는 코드 구조만으로 알 수 없음 → human-externalization 필요."*

그래서 `bok ready` = **NOT READY (R0, score 0)**. 코드 구조를 캤어도 이해도는 0에 가깝다.
→ 다음: `bok validate`(M3, owner 검증→confidence 승격) + 인적 발굴(업무 규칙) + coverage 매핑.

> 이것이 BOK가 "생성 도구"와 다른 지점이다. DeepWiki류는 여기서 "문서 완성"이라 말하지만, BOK는 **"inferred 초안일 뿐, 아직 모른다"** 고 말한다.

## idempotent
`discover`를 다시 돌려도 기존 id는 건드리지 않는다(0 신규). 저작물 보호(D05 D21).
