# 06 — 명령어 · Workflow · 증분 갱신

> 표현 계층을 나선(`design/02` D8)에 붙인다. 신규 커맨드 2개, `compile` 확장 1개. 나머지 계약 불변.

---

## 1. 커맨드 표면 (변경분)

```
bok compile     # (확장) catalog + graph + bok.json  ← 모델 방출자, 유일한 writer
bok render      # (신규) 모델 → ① report.html  ② wiki/**  ③ glossary index
bok view        # (신규) 모델 → 터미널/마크다운 요약 (readiness·gap·confidence). 일부러 소박
```

기존 `init/discover/context/validate/ready/assemble/status`는 **계약 불변**. `onboard`는 마지막에 `render` 단계만 추가.

### 1.1 `bok compile` (확장)

- 오늘: `catalog.yaml` + `graph.json` 방출, dangling 검출.
- 추가: `build_model()` → `bok/_system/bok.json`. 백링크 계산, 그래프 뷰, **purpose-독립 readiness**(area status·score·tier·hard-gate — `coverage.yaml` 있을 때), 초성 버킷, `source_digest`.
- **`ready`를 호출하지 않는다**(§2). `coverage.yaml`이 없으면 readiness 블록을 생략(graceful).

### 1.2 `bok render` (신규, 순수 투영)

- 입력: 라이브 모델(= `bok.json`; `source_digest` 신선도 검사, 불일치 시 거부).
- 출력: `--report` / `--wiki` / `--glossary`(기본 전부). `_system/report.html`, `_system/wiki/**`, `_system/wiki/glossary/**`.
- **순수·결정론·LLM 없음·네트워크 없음.** `render(model) → files`는 모델의 전(total) 함수 → idempotent(동일 `source_digest`면 byte-identical, 본문에 타임스탬프 없음).

### 1.3 `bok view` (신규, 게이트 우선 표면)

일부러 소박한 터미널/마크다운 표면. **검증 상태를 숨길 수 없게** 만든다(D26). 예:

```
$ bok view --scope billing
BILLING · Readiness R0 (36/100) · Hard Gate ✗ FAIL
RED   data-model (critical, 미발굴)      → bok discover
RED   runtime-behavior                   → bok discover
AMBER context-and-scope (open_gap)
KU 6개: authoritative 1 · verified 0 · corroborated 1 · inferred 4 · unverified 0
⚠ dangling: ledger-store
```

`bok render`(예쁜 HTML)의 **검증 안전판**: 코퍼스가 미성숙할 때 0.2.0의 정직한 1차 표면(→[`07`](07-roadmap-and-scope.md) D30).

---

## 2. compile ↔ ready 분리 (결합 금지)

`compile`과 `ready`는 시그니처가 다르다: `compile`은 경로만, `ready(scope, purpose)`는 목적 상대(`design/04` D17). 결합하면 compile이 scope/purpose를 지어내야 한다.

- **purpose-독립**(area status·score·tier·hard-gate)은 `compute_status`/`compute_tier`가 purpose를 안 받으므로 **compile이 계산·저장**.
- **purpose-상대 verdict**는 `ready`가 계속 담당. verdict = `tier` + `hard_gate` + `bok.yaml`의 `purpose_to_tier`의 값싼 투영이라 `bok.json`에 저장 불필요.
- `ready`는 사람용 마크다운 + exit code로 그대로. 선택적으로 자기 scope의 readiness 블록을 `bok.json`에 refresh.

---

## 3. 나선에서의 위치

```
discover → context → compile → validate → ready ──▶ (gap) ──┐
                        │  bok.json                          │
                        ▼                                    │ 재발굴
                   render / view  ← 표현물은 매 나선 갱신      │
                        └──────────── 사람·AI가 현재 이해도를 본다 ┘
```

표현물은 나선의 **관찰 창**이다: 매 회전마다 render가 최신 confidence·gap·readiness를 반영. 표현물이 나선을 바꾸지 않는다(읽기 전용 투영).

---

## 4. 증분 갱신 (D31)

> 헌장 기준 ⑦("전체 재생성 없이 갱신"). 레드팀이 현행 full-regen을 FAIL로 지적 → 정면 대응.

- render/compile은 **모델의 순수 함수**. 증분 = KU 변경 감지(`render.lock`의 mtime/hash) → 바뀐 KU만 재렌더.
- **인덱스·백링크·area·glossary 페이지는 전량 재계산**(bok.json에서 값싼 투영이라 diff 추적 불필요, 낡을 수 없음).
- pre-commit 훅: 변경 KU 스키마 검증 + `bok compile` + `bok render --changed`.
- 스케일 임계 전까진 전량 재생성도 무해(수 ms). 증분은 수천 KU에서 발효 — 설계는 지금, 최적화는 스케일 도달 시.

---

## 5. 에이전트/스킬 경계 (D10·D12 유지)

- `render`/`view`/`compile`은 **결정론 CLI** — 에이전트가 호출하지만 추론 없음. 새 에이전트 불필요(로스터 5개 불변, D12).
- 표현은 **skill이 아니다**(절차적 추론이 아니라 순수 투영). `packs/core`에 render skill을 만들지 않는다 — 과잉.
- 정리 과제: 에이전트가 참조하나 파일 없는 skill 4개(`contradiction-detection`·`confidence-transition`·`risk-mapping`·`readiness-scoring`)는 **파일 추가 또는 참조 삭제**로 명세-실체 격차 해소(→[`07`](07-roadmap-and-scope.md)).
