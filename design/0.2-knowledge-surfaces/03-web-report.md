# 03 — 대화형 웹 분석 리포트

> 목표(헌장): 화려한 디자인이 아니라 **처음 접하는 엔지니어가 전체 구조와 핵심 위험을 빠르게 이해**하도록 돕는 것. + AI가 아닌 **사람의 열람 표면**. 산출: `bok/_system/report.html`(모델 임베드, 서버 불필요).

---

## 1. 정보 구조 — 적응형, 20섹션 고정 벽 아님

순서 = **orient → structure → behavior → risk → readiness**. **각 섹션은 먹일 데이터가 있을 때만** 렌더. 빈 섹션은 빈 제목이 아니라 **Knowledge Gap 카드**로(지식의 부재도 정보 — 헌장). "프로젝트 유형에 맞게 구성"은 강제 분기가 아니라 **coverage 격자에 무엇이 있느냐에서 창발**한다.

| # | 섹션 | 먹이는 데이터(bok.json) | 렌더 규칙 |
|---|------|------------------------|----------|
| 1 | 프로젝트 요약 + Readiness 배너 | `readiness`, `project`, 카운트 | 항상 |
| 2 | **Knowledge Coverage 격자** | `coverage[]` (arc42+TDD, R/A/G) | 항상 — 아는 것의 지도 |
| 3 | **Knowledge Gaps** | `coverage` red/amber + `dangling` + KU `열린 질문` | gap 있으면 항상 |
| 4 | **Development Readiness** | `readiness`(gaps·목표 tier·verdict) | 항상 |
| 5 | 기술 스택 / 설정 / 실행 | `reference`@`container` + provenance doc/runtime | 있으면 |
| 6 | 저장소 / 모듈 구조·역할 | `reference`@`component` | 있으면 |
| 7 | 아키텍처 & context map | `graph` + `layer:context/container` | context>1 또는 container KU |
| 8 | 의존 / 데이터 흐름 | `graph.edges`(depends-on·part-of) | edge 있으면 |
| 9 | API 목록 & 호출 관계 | `reference`@`component` + `tags:[api]` | 있으면 |
| 10 | DB 구조 | `reference`@`data`(coverage data-model) | 있으면 |
| 11 | 화면 & 기능 | reference + `tags:[screen]` | 있으면 |
| 12 | 비즈니스 도메인 & 핵심 규칙 | `explanation`(business-rules·decisions) | 있으면 |
| 13 | 외부 연계 | 외부로의 depends-on + provenance external | 있으면 |
| 14 | 보안 / 운영 위험 | coverage security-compliance·risks | 있으면 |
| 15 | 용어사전(초성) | `glossary.buckets` (→[`05`](05-glossary.md)) | glossary KU 있으면 |
| 16 | 현대화 기회 | risks-tech-debt + dependencies-eol + `contradicts` | 있으면 |

→ 배치 시스템은 2,3,4,6,8,10,12,14,15가 켜지고, UI 중심 앱은 11이 켜진다. **프로젝트 유형을 하드코딩하지 않고, coverage에 담긴 것을 렌더**한다.

---

## 2. 기술 결정 — 단일 HTML 기본 + split-bundle 폴백 (D28)

> 설계 결정 D28 — **무의존 단일 `report.html`**(임베디드 JSON + 바닐라 JS + 인라인 CSS)을 기본으로, **임계 초과 시 split-bundle**로 폴백. 그래프는 **자체 방출 SVG**(런타임 Mermaid 금지). 검색은 임베디드 역색인. 소스 드릴다운은 설정형 base + 항상 복사 가능한 원시 locator.

### 2.1 대안 비교 (헌장: offline·vendor-neutral·단순성)

| 방식 | 판정 | 이유 |
|------|------|------|
| **SSG** (mkdocs-material / Docusaurus / Antora / Backstage TechDocs) | **거부** | Node/Ruby/Java 툴체인 + 빌드 스텝 + 기본 온라인 자산 가정. offline·vendor-neutral·단순성 위배. 또 SSG는 *범용 문서 사이트* — confidence 배지·provenance 드릴다운·readiness 게이트 개념이 없어 싸워야 함. **비목표("문서생성기")로 끌려감.** 나중에 `bok export --mkdocs` *어댑터*로는 가능, 코어로는 불가. |
| **단일 HTML** | **기본 채택** | 1 파일, 더블클릭으로 열림(에어갭 노트북 OK), 이메일 가능. 서버·빌드 없음. 선행 예: pytest-html·Allure·Evidently·nbconvert `--embed`. |
| **split-bundle** (`report.html` + `bok.report.js`) | **폴백 채택** | 임계 초과 시. `fetch` 대신 `bok.report.js`가 `window.BOK={…}` 할당(`<script src>`) → `file://` CORS 회피. 브라우저가 JS 캐시, 본문 온디맨드. |

> **Allure 교훈**: 단일 파일 모드가 모든 걸 base64 인라인 → ~50% 팽창 → 500MB+ 리포트가 안 열림. **단일 파일에 천장이 있음을 인정**하고 폴백을 지금 설계한다(나중에 볼트온 아님).

### 2.2 스케일 임계 규칙 (컴파일러 내, 결정론)

```
embedded = size(minified bok.json for report)      # 초기 페이로드 = frontmatter + TL;DR + relations (L1/L2)
if embedded <= 4 MB   → 단일 report.html (JSON을 <script type="application/json">에 인라인)
else                  → split-bundle: report.html + bok.report.js + bodies/ 사이드카(드릴다운 시 주입)
```

초기 페이로드에 **본문(L3)을 넣지 않는다** → 리포트가 곧 progressive disclosure(`design/01` L1/L2/L3)를 구현. 전 KU의 L3를 선적하지 않고, 드릴다운 시 해당 본문만 로드.

### 2.3 다이어그램 — 컴파일 타임 SVG (런타임 Mermaid 반대)

표현 설계자·레드팀 공통 반대를 채택: **KU 의존 그래프는 컴파일러가 직접 plain SVG로 방출**한다.
- 런타임 Mermaid는 (1) ~1–3MB(단일 파일 예산 붕괴), (2) **런타임 레이아웃이 비결정론적**(버전마다 좌표 이동 → "100% 결정론 CLI"·깨끗한 diff 위배), (3) 컴파일 타임 검증 불가.
- KU 그래프는 nodes+edges뿐 — Mermaid 없이 **레이어드 레이아웃 SVG**를 직접 그리면 충분. 상호작용(hover 이웃 하이라이트, click 선택)은 SVG의 `data-id`에 바닐라 JS 몇 줄.
- 작성자가 손으로 쓴 Mermaid 소스는 `<details>`에 원문 보존(다른 데 붙여넣기용), JS 없으면 코드블록으로 graceful degrade.

### 2.4 검색 — 서버 없이

컴파일 타임에 역색인 구축·임베드. `title+tldr+term+en+owner+context` 토큰화 → `{token → [unit 인덱스]}`. 바닐라 JS가 prefix + AND 조회, `confidence`→relevance 순 랭크. 수천 KU에도 수십–수백 KB. Lunr 등 의존 불필요.

### 2.5 소스 드릴다운 — self-contained의 최난제

단일 파일은 repo 절대위치를 모른다. **세 형태를 모두 data-attr로 방출하고 설정으로 하나를 활성**, 기본은 오프라인에서 늘 안전한 것:

| mode | 링크 | 오프라인 | 공유 | 설정 |
|------|------|:---:|:---:|:---:|
| `relative` (**기본**) | `src/…#L40-L210` 표시, 클릭=클립보드 복사 | ✅ | ✅ | 없음 |
| `vscode` | `vscode://file/<root>/src/…:40` | ✅(VSCode 설치 시) | ⚠ 절대경로 | `repo_root` |
| `github` | `{github_base}/blob/{sha}/src/…#L40-L210` | ❌ 네트워크 | ✅ | `github_base` |

> **포터블·오프라인·이동안전을 동시 만족하는 딥링크는 없다**(레드팀 확인). 기본 `relative`+복사(가정 0, offline 준수), 팀이 `vscode`/`github`을 opt-in. `provenance[].resolved`를 저장해 뷰 시점 `#Lx-Ly` 파싱 제거.

---

## 3. 검증-전면화 (D26 집행) — 이 리포트의 헌법

confidence 범례를 상시 표시, 모든 카드에 배지:

```
authoritative ● 규범   verified ● 사람확인   corroborated ◐ 교차   inferred ○ 추론   unverified ◌ 미검증
```

- `inferred`/`unverified` 카드 = muted 배경 + "추정" 태그. `stale:true` = ⏳.
- `design/01` 원칙("낮은 confidence는 숨기지 않고 경고와 함께 포함") 시각 집행.
- **리포트가 미검증일수록 더 미완성으로 보인다.** 이것이 doc-gen 비목표를 지키는 선(D26·[ADR-05](adr.md)).

---

## 4. 와이어프레임

```
┌───────────────────────────────────────────────────────────────────────────┐
│ acme-billing · BoK Report     [🔎 검색………]   Readiness: R0 ▉▁▁▁ 36/100      │
│                                                   Hard Gate: ✗ FAIL (feature)│
├──────────────┬────────────────────────────────────────────────────────────┤
│ NAV          │  § Knowledge Coverage                                        │
│ ▸ 요약        │  ┌ context-scope amber ┐┌ business-rules green ┐            │
│ ▸ Coverage ● │  ┌ data-model  RED    ┐┌ runtime-behavior RED ┐  ← 클릭 →   │
│ ▸ Gaps    ▲3 │  ┌ risks       RED    ┐┌ glossary        green┐            │
│ ▸ Readiness  │                                                             │
│ ▸ 구조        │  § 정산 배치                   ● corroborated   ⏳ 5d stale │
│ ▸ 의존        │  TL;DR 매일 02:00 KST 전일 거래를 원장에 정산…                │
│ ▸ DB         │  ▸ provenance: src/billing/settle.py#L40-L210 [복사][vscode]│
│ ▸ 규칙        │  ▸ depends-on → ledger-store  ⚠ dangling (미발굴)           │
│ ▸ 용어사전     │  ▸ defines-term → 멱등 키                                   │
│ ▸ 위험        │  [ 의존 SVG: settlement→ledger, →멱등 키 ]                   │
│ ── 범례 ──    │  ┌─ GAP PANEL ───────────────────────────────────────────┐ │
│ ● 규범        │  │ 🔴 data-model (critical) — 미발굴 → run `bok discover`  │ │
│ ● 검증        │  │ 🔴 runtime-behavior — 부분 실패 재개 미확인             │ │
│ ◐ 교차        │  │ ⚠ dangling: ledger-store                               │ │
│ ○ 추론        │  │ ❓ idempotency_key 생성 규칙 정확성 미검증 (열린 질문)    │ │
│ ◌ 미검증      │  └────────────────────────────────────────────────────────┘ │
└──────────────┴────────────────────────────────────────────────────────────┘
```

---

## 5. 0.2.0 범위 (이 표현물)

- **0.2.0**: 섹션 1–4 + 15만(요약·Coverage·Gaps·Readiness·용어사전). 단일 파일. 자체 SVG 그래프, 역색인 검색, confidence 배지, `relative` 드릴다운.
- **0.3+ 연기**: split-bundle 폴백, `vscode`/`github` 링크, 섹션 5–14/16. 대화형 HTML 자체가 **가장 비싼 산출물**이므로 데이터 계층이 신뢰될 때까지 최소로.
- 근거: coverage+gaps+readiness+용어사전 코어만으로도 오너 목표("구조와 핵심 위험 빠른 파악")를 현재 스케일 repo에서 달성. → [`07`](07-roadmap-and-scope.md).
