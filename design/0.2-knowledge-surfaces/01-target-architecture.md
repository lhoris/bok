# 01 — 목표 아키텍처

> 하나의 BoK에서 여러 표현물을 파생시키는 구조. 명령어 책임 경계와, 이 계층이 "문서 생성기"로 미끄러지지 않게 막는 가드레일을 확정한다.

---

## 1. 원칙 — One BoK, Many Surfaces (D23)

> 설계 결정 D23 — 표현물(웹 리포트·Wiki·용어사전)은 **단일 공유 모델 위의 결정론적 투영**이다. 어떤 사실도 표현물별로 재계산하지 않는다.
> 근거: 헌장 "동일 지식을 별개 방식으로 중복 생성하지 말고 공통 지식 모델을 중심으로 여러 표현물을 만들어라" + `design/01` BoK/Context 모델 분리.

### 1.1 계층

```
[1] 원천 (Source of Truth)     bok/<context>/<kind>/*.md         사람+AI 저작·리뷰, git
        │  build_model(root)   ← 결정론·순수함수·LLM 없음·stdlib
        ▼
[2] 모델 (Model)               in-memory 객체  ══▶  bok/_system/bok.json
        │                       (기계판독 계약 + 리포트 임베드 소스)
        │  project()           ← 순수 투영, 재계산 없음
        ▼
[3] 표현물 (Surfaces)          ① report.html   ② wiki/**   ③ glossary index
```

- **[1]만이 진실이다.** [2]·[3]은 전부 `# GENERATED`, 재생성 가능(`design/05` D20 계승 — 이미 `catalog.yaml`·`graph.json`이 이 규칙 하에 커밋되는 파생물이다).
- **단일 원천 보장의 정체**: 파일이 아니라 **함수 `build_model()`** 이다. 세 표현물이 같은 함수의 출력을 소비하므로 서로 다른 사실을 말할 수 없다. `bok.json`은 그 출력의 **직렬화**일 뿐(외부 도구·HTML 임베드용).

### 1.2 왜 "함수가 보장, 파일은 계약"인가

두 검토 의견의 종합:
- **모델 아키텍트**: 표현물이 각자 catalog+graph+coverage+KU를 재조합하면 어긋난다 → 단일 소스 필요.
- **레드팀**: 커밋된 거대 파생 파일은 drift 위험 + 현재 스케일(3–6 KU)에선 과잉.

→ **해소**: 내부 표현물은 `build_model()`의 **라이브 출력**을 소비(직렬화 왕복·drift 없음). `bok.json`은 (a) 외부 자동화 도구, (b) self-contained HTML 임베드 — 즉 **CLI 밖 소비자**를 위해서만 필요하다. 이 둘은 헌장이 명시한 요구("기계 판독형 메타데이터", "self-contained 웹 리포트")이므로 정당하다. → 상세 [`02`](02-knowledge-model-ir.md), [ADR-02](adr.md).

---

## 2. 검증-전면화 원칙 — 문서생성기 비목표 가드레일 (D26)

> 설계 결정 D26 — 표현물은 **confidence·provenance·gap을 콘텐츠만큼 크게** 드러낼 때만 정당하다. `inferred`/`draft`를 `verified`처럼 보이게 하는 표현은 거부한다.
> 근거: ROADMAP 비목표 "문서 생성 도구가 되는 것"; `research/03`의 자동생성물 맹신 경고("잘못된 이해 확산"); 헌장 "생성된 지식은 검증".

이 원칙이 없으면 `bok render`는 기계적으로 그냥 **정적 사이트 생성기**이고, 그건 BOK가 명시적으로 거부한 정체성이다. 경계선:

> 뷰어는 **모든 렌더된 주장이 confidence + provenance + last_verified를 달고, gap/NOT-READY가 콘텐츠만큼 눈에 띌 때만** 정당하다.

**집행 가능한 테스트 (구현·리뷰 체크리스트)**:
- [ ] 지식이 미검증일수록 표현물은 **더 미완성으로 보여야** 한다(빨간 배지, "추정" 태그, muted 배경, 상단 gap 패널).
- [ ] `inferred` KU와 `verified` KU가 **시각적으로 구별 불가능하면 그 표현물은 반려**된다.
- [ ] 웹 리포트는 최상단에 Readiness verdict(예: "NOT READY · 3 areas RED")를 콘텐츠보다 먼저 보여준다.
- [ ] 빈 섹션은 숨기지 않고 **Knowledge Gap 카드**로 렌더한다(지식의 부재도 정보다).

→ [`03` §confidence-전면화](03-web-report.md) 참조.

---

## 3. 표현물은 기존 축의 투영 뷰다 (D27)

> 설계 결정 D27 — 표현물은 **기존 축(`context` × `kind` × `layer` × `coverage-area` × `confidence`)의 투영 뷰**다. 새 물리 축(폴더 facet)을 만들지 않는다.

오너가 예시한 구조들을 새 저장소가 아니라 뷰로 매핑:

| 오너 요구 구조 | 새 저장소인가? | 실제 구현 = 기존 축의 투영 |
|---------------|:-----:|--------------------------|
| Wiki 16개 영역(overview·architecture·modules·API·DB·…) | ❌ | **coverage-area 뷰** + `kind`/`layer` 필터 (§04) |
| "확인되지 않은 지식" 영역 | ❌ | `confidence ∈ {unverified,inferred}` **필터** |
| glossary 초성 트리(ㄱ/ㄴ/…/A-Z) | ❌ | `kind:glossary` KU에 대한 **생성 인덱스**(물리 저장 아님, §05) |
| 다의어(문맥별 의미) | ❌ | 기존 `context` 축 — 1용어·N context = N KU (§05) |

→ **KU는 항상 `bok/<context>/<kind>/*.md`에 그대로 산다.** 표현물은 그 위에 항해 셸을 씌울 뿐, 옮기거나 복제하지 않는다(단일 원천).

---

## 4. 명령어 책임 경계

### 4.1 확장 (비파괴적)

| 커맨드 | 0.1.0 | 0.2 변경 | 성격 |
|-------|-------|---------|------|
| `bok compile` | catalog+graph 방출 | **+ `bok.json` 방출**(백링크·purpose-독립 readiness·초성 버킷 포함) | 결정론 |
| `bok render` | — | **신규**: 모델 → ①HTML ②wiki ③glossary index | 결정론·순수 투영 |
| `bok view` | — | **신규**: 모델 → 터미널/마크다운 요약(readiness·gap·confidence). *일부러 소박* | 결정론 |
| `discover/context/validate/ready/assemble/status/onboard` | — | **계약 불변**. `onboard` 끝에 `render` 단계만 추가 | — |

### 4.2 CLI ↔ LLM 경계 (D10 유지)

- `render`·`view`·`compile`은 **100% 결정론, LLM 없음** — 기존 CLI의 성질과 동일. 순수 문자열 템플릿팅 + JSON 투영.
- 추론(업무규칙·의미 grounding·adversarial)은 여전히 에이전트/skill의 몫. 표현 계층은 **추론을 하지 않는다**(사실을 렌더만 함).

### 4.3 compile ↔ ready 결합 금지 (모델 아키텍트 지적 채택)

`compile`은 **purpose-독립** readiness(area status·score·tier·hard-gate — 코드상 `compute_status`/`compute_tier`가 purpose를 안 받음)만 계산·저장한다. **purpose-상대 verdict는 `ready`가 계속 담당**(`ready(scope, purpose)`, `design/04` D17). `compile`이 scope/purpose를 지어내지 않는다.

→ 상세: [`06`](06-commands-workflow.md).

---

## 5. 헌장 능력과의 매핑 (자기검증)

| 헌장 "핵심 능력" | 본 아키텍처의 답 |
|----------------|----------------|
| 지식 발견 | (기존) discover |
| 근거 추적 | (기존) provenance + (신규) 표현물이 provenance를 드릴다운으로 노출 |
| 구조화·연결 | (기존) relations + (신규) **백링크 해석**(죽은 URI → 항해 가능) |
| 구조·관계 시각화 | (신규) 자체 방출 SVG 그래프(§03) |
| 사람·AI 검색·탐색 | (신규) Wiki 인덱스·백링크·역색인 검색(§03·§04) |
| 정확성·완성도 검증 | (기존) validate + (신규) 표현물이 confidence 전면화(D26) |
| 부족한 지식 식별 | (기존) gap/open_gap + (신규) 표현물 상단 gap 패널 |
| 재사용 | (기존) 팩 + 뷰 투영은 프로젝트 무관 |
| 사람용·AI용 지식 동시 생성 | (신규) 같은 모델 → wiki(사람)·bok.json/assemble(AI) |
| 개발 가능 상태 평가 | (기존) ready + (신규) readiness를 표현물 최상단 배치 |
