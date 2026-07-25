# 00 — BOK 0.1.0 현황 분석 & 철학-구현 Gap

> 실측 기반(코드 감사). 설계 산문이 아니라 `cli/bok.py`(983줄)와 실제 산출물 트리를 읽어 확인한 것.

---

## A. 0.1.0이 실제로 구현한 것 (Ground Truth)

### A.1 결정론 코어 (전부 동작, LLM 호출 0)

| 커맨드 | 실제 동작 | 읽기/쓰기 |
|-------|----------|----------|
| `init` | `bok/` 스캐폴딩 + `bok.yaml` + `coverage.yaml` 복사 | 템플릿 → `bok/` |
| `discover` | **결정론 아키올로지**(언어 무관 디렉터리 구조, Python `ast` import 그래프, SQL `CREATE TABLE`, git 변경 히트맵). 산출 KU는 전부 `inferred`/`draft` | `--source` 트리 → KU + `discovery-plan.md` |
| `context` | KU→coverage area 매핑(`area_for`), 제목 중복 경고(병합은 LLM 몫) | KU → `coverage.yaml` |
| `validate` | grounding=**파일 존재 검사만**, 교차지지 승격, staleness 강등, `--sign` owner 서명(→`verified`) | KU confidence 라인 in-place 재작성 → `validation-report.md` |
| `ready` | coverage→신호등→hard gate→score→tier(R0–R4). **결과는 마크다운에만** | `coverage.yaml` → `readiness-report.md` |
| `compile` | 스키마 검증 + dangling 검출 | KU → `catalog.yaml`, `graph.json` |
| `assemble` | **키워드 substring** 관련성(임베딩 아님), 관계 확장, 예산 트림 | → `context-pack.yaml` |
| `status`/`onboard` | 대시보드 / 파이프라인 래퍼 | — |

> **결정론이 강점이자 한계.** 모든 CLI 동작이 재현 가능·vendor-neutral(stdlib+PyYAML). 대신 "왜(업무규칙)"·의미적 grounding·adversarial은 전부 **LLM 에이전트로 위임**되어 있고, 그 에이전트 흐름은 **미검증**이다.

### A.2 실제 산출물 트리

```
<target>/bok/
  <context>/<kind>/*.md         # KU (사람+AI, 리뷰 대상) — 유일한 원천
  _system/
    catalog.yaml                # L1 인덱스 (id,title,kind,layer,context,confidence,relations)
    graph.json                  # nodes + typed edges
    coverage.yaml               # area→KU + criticality + open_gap  (status는 미저장)
    discovery-plan / validation-report / readiness-report / context-pack
```

- `acme-billing`(손+검증, 3 KU) · `mini-shop`(전자동 발굴, 6 KU). 실제 glossary KU 1건 존재(`billing/glossary/idempotency-key.md`).
- **HTML/렌더 산출물 0건.** 사이트 생성기·템플릿 엔진 없음.

### A.3 에이전트/스킬 = 명세, 아직 실체 아님

- `agents/*.md` 5개 + `packs/core/**/SKILL.md` 10개 존재. 그러나 **에이전트가 참조하는 skill 4개(`contradiction-detection`·`confidence-transition`·`risk-mapping`·`readiness-scoring`)는 파일로 없다.**
- 어댑터(claude-code/codex/github-copilot)는 파일 복사만 한다(빌드 아님). **LLM 실행 흐름은 파일럿 안 됨**(ROADMAP M6). CLI만 23개 테스트로 검증.

---

## B. 철학-구현 Gap 분석

헌장 철학 각 항목을 현재 구현과 대조.

| 헌장 철학 | 현재 상태 | Gap |
|----------|----------|-----|
| 코드보다 지식이 먼저 | KU 모델·나선 구현됨 | ✅ 토대 충족 |
| 추측보다 근거 우선 | provenance·confidence 필수 필드 | ✅ 강점. 단 grounding이 "파일 존재"까지만 |
| 사람+AI가 함께 사용 | 마크다운 = 공용 원천 | ⚠️ AI가 **항해**할 방법 없음(링크 죽어있음), 사람이 **열람**할 표면 없음 |
| 지식은 탐색·발견이 쉬워야 | catalog=L1만 | ❌ 인덱스·백링크·검색·용어사전 인덱스 없음 |
| 동일 지식을 여러 표현 형태로 | 단일 마크다운 | ❌ **표현 계층 전무** — 이번 재설계의 핵심 대상 |
| 정보 부족 시 Knowledge Gap 명시 | `open_gap`, dangling, RED area, NOT READY | ✅ 정직성 메커니즘 존재. ⚠️ 표현물이 이를 노출해야 유효 |
| 문서의 양보다 이해 가능성 | — | ⚠️ 이해도(readiness) 계산은 있으나 **저장·표현 안 됨** |
| 일관된 BoK를 기능 수보다 우선 | — | ⚠️ 세 표현물을 **중복 구현하면 이 철학 위배** → 단일 모델 파생이 필수 |

### B.1 결정적 3대 공백 (이번 설계가 메울 것)

1. **통합 IR 부재** — 완전한 스냅샷을 얻으려면 모든 KU를 다시 읽고 ready 로직을 재실행해야 함. 표현물이 여기서 각자 재계산하면 **서로 어긋난다**(중복 금지 위배). → [`02`](02-knowledge-model-ir.md)
2. **표현/항해 계층 전무** — 관계는 죽은 `bok://` URI. 백링크·인덱스·검색·다이어그램 없음. 사람도 AI도 "탐색"할 수 없음. → [`03`](03-web-report.md)·[`04`](04-llm-wiki.md)
3. **용어사전 인덱스 없음** — glossary는 kind로 존재하나 초성/알파벳 인덱스·풍부한 스키마 없음. → [`05`](05-glossary.md)

### B.2 그러나 — 가장 중요한 Gap은 "표현"이 아니다

레드팀이 정확히 지적: **현재 실제 KU는 100% `inferred`/`draft`**다. `verified`·human-provenance 코퍼스가 아직 없다. BOK가 "repo에 AI 붙이기" 베이스라인(aider repomap·DeepWiki)을 **이기는 유일한 지점은 코드에 없는 암묵지 + 사람이 서명한 검증 지식**인데, 그게 아직 안 만들어졌다.

> **함의**: 검증되지 않은 지식 위에 화려한 표현을 먼저 지으면, 독자가 `inferred`를 완성된 것으로 신뢰하게 되어 **BOK가 막으려던 바로 그 해악(잘못된 이해 확산)** 을 일으킨다. → 그래서 [`07`](07-roadmap-and-scope.md)의 **검증 우선 시퀀싱(D30)** 과 [`01`](01-target-architecture.md)의 **검증-전면화 원칙(D26)** 이 이 설계의 두 기둥이다.

---

## C. 유지할 것 vs 재설계할 것

| 구분 | 항목 |
|------|------|
| **유지 (건드리지 않음)** | KU 스키마(D1·D2), provenance·confidence(D3), 3축 타입(A.2), 나선 파이프라인(D8), readiness 모델(D15–D18), 저장소 이중 평면(D20), id 무결성(D21), 결정론 CLI가 원천(D10) |
| **확장 (비파괴적 추가)** | `bok.json` 모델 방출(compile), `bok render`/`bok view` 신규 커맨드, 선택적 `glossary_term` 필드, glossary 본문 스키마 강화, 백링크 계산 |
| **재설계/정리** | 유령 skill 4개(파일 추가 or 에이전트 참조 삭제), `graph.json`을 `bok.json`에 흡수(전환기 후 폐기), "표현=문서생성기" 오해를 막는 비목표 가드레일 명문화 |
| **명시적 비구현 (0.2.0 안 함)** | 대화형 HTML 풀 기능, 커밋되는 IR 캐시, 임베딩 검색, 멀티레포 aggregator |
