# ADR — 0.2 Knowledge Surfaces 주요 의사결정

> MADR 계열(Context·Decision·Alternatives·Consequences). 각 결정은 오너의 판단 원칙("왜 필요한가·어떤 문제·대안·현재보다 나은 이유·복잡도 정당성·장기 유지보수·벤더 종속")에 답한다. 기존 `design/`의 D1–D22를 잇는 D23–D31에 대응.

---

## ADR-01 — 하나의 BoK, 여러 표현물 (D23)

**Context.** 헌장은 웹 리포트·Wiki·용어사전을 요구하되 "중복 생성 금지, 공통 지식 모델에서 파생"을 명시.

**Decision.** 표현물은 **단일 공유 모델(`build_model()`) 위의 결정론적 투영**. 어떤 사실도 표현물별로 재계산하지 않는다.

**Alternatives.** (a) 표현물이 각자 catalog/graph/coverage/KU를 재조합 — 어긋남·중복(헌장 위배). (b) 세 도구를 독립 구현 — 최악의 중복.

**Consequences.** 세 표현물이 구조적으로 무모순. 새 커맨드 `render`가 필요하나 추론 없는 순수 투영이라 CLI↔LLM 경계(D10) 유지. 유지보수: 표현물 로직이 얇아짐(모델이 무거움).

---

## ADR-02 — `bok.json`은 계약, 보장은 함수 (D24)

**Context.** 헌장이 "기계 판독형 메타데이터"와 "self-contained 웹 리포트"를 요구. 오늘 완전 스냅샷을 얻으려면 전 KU 재파싱 + ready 재구현 필요. 한편 커밋된 거대 파생 파일은 drift 위험(레드팀).

**Decision.** 단일 원천 보장은 **`build_model()` 함수**가 준다. `bok.json`은 그 출력의 (i) 외부 기계판독 계약 + (ii) HTML 임베드 소스. 내부 표현물은 라이브 모델 소비(왕복·drift 없음). `source_digest` 스탬프. **purpose-상대 readiness verdict 저장 제외**(낡으면 거짓말이 되는 유일 필드). **커밋 선택**(기본 gitignore=drift 0, 옵션 커밋+필수 pre-commit 무결성 훅).

**Alternatives.** (a) "모든 표현물이 파일만 읽는다"(원안) — 직렬화 왕복 + 내부 drift 재개방. (b) 파일 없이 공유 로더만 — 외부 도구·HTML 임베드 요구 불충족. (c) 항상 커밋 — 스케일 전 과잉·noisy diff.

**Consequences.** "surfaces agree"를 함수로 값싸게 획득, 파일은 CLI 밖 소비자에게만. `graph.json` 흡수·폐기로 순 산출물 순증 없음. 멀티-context는 scope-keyed readiness 필요(스키마 반영).

**벤더 종속.** 없음 — plain JSON, stdlib.

---

## ADR-03 — 웹 리포트는 SSG가 아니라 단일 HTML (D28)

**Context.** offline·vendor-neutral·단순성 헌장. 대안은 성숙한 SSG들.

**Decision.** 무의존 단일 `report.html`(임베디드 JSON + 바닐라 JS + 인라인 CSS) 기본, 임계 초과 시 split-bundle. 그래프는 자체 방출 SVG(런타임 Mermaid 금지). 검색은 임베디드 역색인.

**Alternatives.**
- **mkdocs-material / Docusaurus / Antora / Backstage TechDocs** — Node/Ruby/Java 툴체인 + 빌드 + 온라인 자산 가정. offline·단순성·vendor-neutral 위배. confidence/provenance/readiness 개념 없어 싸워야 함. **비목표(문서생성기)로 끌려감.** → 거부(나중에 `bok export --mkdocs` 어댑터로는 허용).
- **런타임 Mermaid 인라인** — ~1–3MB(예산 붕괴), 비결정론 레이아웃, 컴파일 검증 불가 → 거부, 자체 SVG.
- **Quartz/Obsidian Publish** — Node/TS 또는 유료 호스팅(lock-in) → 거부.

**Consequences.** 에어갭에서 더블클릭. 스케일 천장 존재(Allure 500MB 선례) → split-bundle로 대응. 포터블·오프라인·이동안전 딥링크는 없음 → 설정형 base + 복사 가능 원시 locator.

**복잡도 정당성.** HTML/CSS/JS를 직접 소유하는 비용 vs SSG 툴체인·온라인 종속·개념 불일치. 후자가 헌장을 더 크게 위반 → 자체 최소 구현이 정당.

---

## ADR-04 — 용어사전 1용어=1KU + 생성 초성 인덱스 (D27·D29)

**Context.** 오너가 초성 폴더 트리(ㄱ/ㄴ/…/A-Z)와 풍부한 용어 스키마, 다의어 분리를 요구.

**Decision.** KU는 `bok/<context>/glossary/*.md`에 그대로(1용어=1KU, D1). 초성 트리는 **생성 인덱스**(물리 저장 아님). 선택적 `glossary_term` 필드 + 결정론 초성(NFC·겹자음 폴딩·비한글 버킷). 다의어는 기존 `context` 축(N context = N KU).

**Alternatives.** (a) 초성 폴더에 KU 물리 저장 — 단일 원천 포크, 다중 context 붕괴, `bok mv` 곡예 → 거부. (b) 별도 용어사전 저장소 — 헌장 "중복 금지" 위배 → 거부. (c) frontmatter에 term 없이 title로 버킷 — 영문우선 이중언어 title 오분류 → `glossary_term`로 해소.

**Consequences.** 오너 필드 전부가 기존 메커니즘(provenance·confidence·relations·context·열린질문)으로 매핑 — 스키마 포크 없음. 초성은 유니코드 수학(의존성 0).

**벤더 종속.** 없음 — 한글 자모 분해는 stdlib.

---

## ADR-05 — 검증-전면화 원칙 (D26) — 비목표 가드레일

**Context.** `bok render`는 기계적으로 정적 사이트 생성기다. 그건 BOK가 명시적으로 거부한 정체성(ROADMAP 비목표). 미검증 지식을 예쁘게 렌더하면 `research/03`의 "잘못된 이해 확산" 해악.

**Decision.** 표현물은 **confidence·provenance·gap을 콘텐츠만큼 크게** 드러낼 때만 정당. `inferred`/`draft`를 `verified`처럼 보이게 하는 표현은 **반려**. 집행 체크리스트: 미검증일수록 더 미완성으로 보이기 / `inferred`와 `verified` 시각 구별 가능 / readiness를 콘텐츠보다 먼저 / 빈 섹션은 gap 카드.

**Alternatives.** 원칙 없이 예쁜 문서 렌더 — DeepWiki-with-worse-coverage로 전락, 비목표 침범 → 거부.

**Consequences.** 이 원칙이 "지식 뷰어"와 "또 하나의 SSG"를 가르는 선. 리뷰·테스트에서 집행 가능(전면화 테스트).

---

## ADR-06 — 검증 우선 시퀀싱 (D30)

**Context.** 실제 KU 100% `inferred`/`draft`. LLM 파이프라인 미검증(M6). 유령 skill 4개. BOK 차별점(verified·암묵지)이 아직 미실현.

**Decision.** 0.2.0은 **검증-중립 데이터 토대(P0)** + **검증-중립 표현(P1: wiki 내비·용어사전)** + **게이트 우선 표면(P1.5: `bok view`)** 까지. **비싼 대화형 HTML(P2)은 파일럿으로 `verified` 코퍼스 확보를 게이트**. 병렬로 LLM 파이프라인 성숙 + 유령 skill 정리.

**Alternatives.** (a) 세 표현물 풀 구현 우선(원 요청의 문자적 해석) — 미검증 위 진열장, `inferred` 신뢰 조장, 지식 모델이 파일럿 피드백으로 바뀌면 렌더 계약 재작업 → 거부. (b) 표현 전면 보류 — wiki 내비·용어사전은 검증 품질과 무관하게 BoK를 개선하므로 과보류 → 거부.

**Consequences.** 오너의 세 표현물을 **포기하지 않되 순서를 바꾼다**. 헌장 "기능 수보다 일관된 BoK 우선"과 정합. 가장 값싸고 검증-무관한 것(wiki 내비·용어사전·`bok view`)부터, 가장 비싸고 검증-의존적인 것(대화형 HTML)을 마지막.

**이것이 오너 관점의 핵심 판단이다** — 구현자라면 요청된 세 기능을 바로 만들었겠지만, 프로젝트 오너로서 BOK의 정체성(검증되는 지식)을 지키려면 검증을 표현보다 앞세워야 한다.
