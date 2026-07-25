# 05 — 도메인 용어사전 (초성 인덱스)

> 엔터프라이즈엔 코드만으로 알기 어려운 업무 용어·약어·화면명·데이터명이 있다. 이를 별도 도메인 용어사전으로 관리하되, **1용어=1KU 원칙(D1)을 유지하고 초성 트리는 생성 인덱스**로 둔다.

---

## 1. 강화된 glossary KU 스키마 (frontmatter 불변, 본문 확장)

frontmatter는 이미 `context`·`provenance`·`confidence`·`relations`·`last_verified`를 담으므로 그대로 두고, 오너의 필드는 **본문**에 넣어 KU를 자족적으로 유지. 신규 템플릿 `templates/ku.glossary.template.md`:

```markdown
---
id:            bok://billing/glossary/idempotency-key
title:         멱등 키 (Idempotency Key)
kind:          glossary
layer:         null
context:       billing              # ← 다의어 분리 (§4)
glossary_term: 멱등 키               # ← 신규 선택 필드: 초성 버킷 키 (§3)
status:        active
confidence:    authoritative
provenance:
  - kind: data
    locator: db/schema/ledger.sql#L22
    note: "settlement_run.idempotency_key VARCHAR(64) NOT NULL UNIQUE"
relations:
  - type: part-of
    target: bok://billing/reference/settlement-batch
  # defines-term 백링크는 자동 (이 용어를 참조하는 KU에서)
owner:         team-billing
last_verified: 2026-07-20
supersedes:    null
---

## TL;DR
같은 작업을 여러 번 실행해도 결과가 한 번 실행과 동일하도록 보장하는 식별자.

## 정의
| 필드 | 값 |
|------|----|
| 용어명(국문) | 멱등 키 |
| 영문명 | Idempotency Key |
| 약어 | — |
| 업무영역 | 정산(billing) |

- **일반적 의미**: 연산을 여러 번 적용해도 결과가 한 번 적용과 동일한 성질.
- **이 프로젝트(billing)에서의 의미**: `settlement_run`의 유일 식별자. 동일 키 재기록을 DB가 거부.
- **차이(일반 vs 프로젝트특화)**: 일반은 성질(연산), 여기서는 그 성질을 강제하는 **컬럼값**을 지칭.

## 관련 지식 (자동 백링크 + 수동)
- 화면/API: —
- 테이블·컬럼: `settlement_run.idempotency_key` (`db/schema/ledger.sql#L22`)
- 코드: `src/billing/settle.py#L120-L180`
- 연관 용어: [[정산 배치]], [[이중 정산 방지]]
- 동의어·유사어: 멱등성 키, dedup key(비권장)

## 근거 상세
- data: DDL의 `UNIQUE NOT NULL` 제약 → 스키마가 규범(authoritative).

## 열린 질문 / 불확실성 (= 확인필요사항)
- 키 생성 규칙 자체의 정확성은 double-settlement-guard KU에서 미검증.
```

**오너 필드 → 기존 메커니즘 매핑** (새 저장소·스키마 포크 없음):

| 오너 요구 | 실현 |
|----------|------|
| 출처·근거 | `provenance` |
| 신뢰도·검증상태 | `confidence` + `stale` |
| 확인필요사항 | `## 열린 질문` |
| 관련 화면/API/테이블/코드 | `relations` + **자동 백링크** |
| 문맥별 의미 분리 | `context` 축 (§4) |
| 동의어·유사어·연관용어 | 본문 + `relations` |

---

## 2. 선택적 `glossary_term` 필드 (D29)

> 오늘 frontmatter엔 `term`/reading 필드가 없다. 유일한 텍스트는 이중언어 `title`("Idempotency Key (멱등 키)")이라, 초성 버킷을 결정론적으로 못 잡는다(영문 우선 title은 A-Z로 오분류).

→ **선택적 `glossary_term`** 추가(비파괴 — `parse_ku`는 `REQUIRED_FIELDS`만 강제). 버킷 키 우선순위:
1. `glossary_term`이 있으면 그것.
2. 없으면 `title`의 첫 비공백 한글 음절.
3. 그것도 없으면 ASCII 첫 글자 대문자(라틴 버킷).

---

## 3. 초성 추출 — 결정론, 컴파일러 내 (D29)

```
c = 표시 용어(glossary_term 또는 title)의 첫 비공백 문자
c ← NFC 정규화                              # macOS NFD 분해형 한글 방지 (필수)
if 0xAC00 ≤ ord(c) ≤ 0xD7A3:                 # 한글 음절
    lead = (ord(c) - 0xAC00) // 588           # 0..18 초성 인덱스
    bucket = FOLD[lead]                        # 겹자음 폴딩 ㄲ→ㄱ ㄸ→ㄷ ㅃ→ㅂ ㅆ→ㅅ ㅉ→ㅈ
elif 0x3131 ≤ ord(c) ≤ 0x314E:                # 단독 자모(드묾)
    bucket = FOLD_JAMO[c]
elif c.isascii() and c.isalpha():
    bucket = c.upper()                         # A..Z
else:
    bucket = "numbers-symbols"                 # 숫자·기호·기타 스크립트
```

- `FOLD`는 19 초성(ㄲㄸㅃㅆㅉ 포함)을 오너가 원한 **14 버킷(ㄱ…ㅎ)** 으로 접는다.
- 순서: `["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ", "A-Z", "numbers-symbols"]`.
- 버킷 내 정렬: 전체 용어를 **유니코드 코드포인트 순**(결정론). 한글 음절은 유니코드가 초성/중성/종성 순이라 가·각·간·… = 올바른 한국어 콜레이션.
- `sort_key = bucket + "|" + term`을 방출 → 모든 표현물이 재계산 없이 동일 정렬.
- 검증: 멱(U+BA71) → `(0xBA71-0xAC00)//588 = 6` → 초성 6 = **ㅁ**. "멱등 키"는 ㅁ에 정확히 들어감.

> **주의점은 자모 수학이 아니라 엣지케이스**(레드팀): (1) NFC 정규화, (2) 겹자음 폴딩 정책 문서화, (3) **비한글 용어** 버킷(예시 용어 자체가 영문!), (4) 다단어·혼합어. 위 규칙이 넷을 모두 결정.

---

## 4. 초성 트리 = 생성 투영, 물리 저장 아님 (D27)

KU는 `bok/<context>/glossary/<slug>.md`에 그대로. 초성 트리는 위키에 읽기전용 방출:

```
_system/wiki/glossary/
  index.md          # 전 버킷, 점프 링크: ㄱ ㄴ ㄷ … ㅎ · A-Z · #
  ㅁ/index.md        # 멱등 키 → billing/glossary/idempotency-key.md 링크
  A-Z/index.md
  numbers-symbols/index.md
```

초성 폴더 밑 물리 복제는 (a) 단일 원천 포크, (b) 한 용어가 두 context에 속하는 순간 붕괴, (c) `bok mv` 곡예를 부른다. 투영은 셋 다 없고 값싸게 재생성. **권장: 생성 인덱스/리다이렉트만.** (안정 공유 URL이 필요하면 이미 있는 `redirects.yaml` 활용.)

---

## 5. 다의어 — 기존 `context` 축이 해결 (D27)

덮어쓰지 않는다. 한 용어에 두 의미 = **두 KU**, context별 1개, `context` frontmatter와 별개 `id`/`slug`로 구별:

```
bok://billing/glossary/settlement   title: 정산 (Settlement)  context: billing  "원장 기록 배치"
bok://payout/glossary/settlement    title: 정산 (Settlement)  context: payout   "지급 확정 시점"
```

초성 인덱스는 둘을 ㅈ 아래 충돌 없이, context 태그와 함께 나열:

```markdown
### ㅈ
- **정산 (Settlement)** · `billing` · ● authoritative — 원장에 정산 기록을 남기는 배치
- **정산 (Settlement)** · `payout`  · ◐ corroborated  — 지급이 확정되는 시점
```

버킷 항목이 `context`·`id`를 지녀 동일 `term` 문자열이 병합되지 않는다. 헌장 "문맥별 의미를 분리하여 기록"을 그대로 집행.

---

## 6. 상호 링크

`defines-term` 관계(이미 `graph.json`에: `settlement-batch → idempotency-key`, `double-settlement-guard → idempotency-key`)를 컴파일러가 뒤집어 용어 페이지의 **백링크**로: "이 용어를 쓰는 곳: 정산 배치, 이중 정산 방지." 수작업 없음 — `bok.json`의 `backlinks`에서 그대로 떨어진다. "관련 화면/API/테이블"은 백링크를 소스 KU의 `layer`로 필터(data→테이블, component+`tags:[api]`→API, `tags:[screen]`→화면).

---

## 7. 0.2.0 범위 (이 표현물)

- **0.2.0(값쌈·고가치)**: `templates/ku.glossary.template.md`(템플릿 파일, 거의 0 공수) + 컴파일러의 초성 버킷팅(작은 결정론 함수, §04·§03이 재사용) + `wiki/glossary/` 인덱스. 초성 인덱스는 헤드라인 기능이고, 버킷팅이 컴파일러에 들어가면 값싸다.
- **0.3+**: 용어 페이지의 화면/API/테이블 자동 분류 고도화.
