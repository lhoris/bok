# BOK Design 05 — Repository / Wiki 구조

> 설계 입력: `research/_SYNTHESIS.md`, `design/01–04`.
> BOK를 **설치·운영하는 물리 형태**를 확정한다: `bok/` 레이아웃, `bok.yaml`, Skill 팩 배포·해석 우선순위, id 무결성.

## 0. 두 저장소를 구분한다

> 설계 결정 D19 — **프레임워크 저장소**(BOK 자체를 개발·배포)와 **대상 저장소**(온보딩되는 엔터프라이즈 시스템)는 다르다. BoK는 대상 저장소 안에 산다(docs-like-code, D05). 프레임워크는 CLI+팩으로 별도 배포되고 버전으로 고정된다.

```
① BOK Framework 저장소 (이 프로젝트)     ② 대상 저장소 (고객 시스템)
   cli/, agents/, packs/core/, templates/    src/... (기존 코드)
        │ 배포(versioned)                     bok/   ← BOK가 여기 설치
        └───────────────────────────────────▶ bok.yaml (프레임워크 버전 고정)
```

---

# 1. 프레임워크 저장소 레이아웃 (BOK 자체)

```
bok/  (이 repo — 배포물)
  cli/                       # `bok` CLI (vendor-neutral 원천, D10)
  agents/                    # 5 코어 에이전트 정의(03)
    bok-orchestrator.md  bok-discoverer.md  bok-curator.md
    bok-validator.md     bok-readiness-assessor.md
  packs/
    core/                    # 코어 Skill 팩(03 §2) — 항상 포함
      discover/  context/  validate/  ready/  shared/
    domain/                  # 공식 도메인 팩(선택 설치)
      pack-billing-domain/   pack-mainframe-cobol/  ...
  templates/
    coverage.template.yaml   # arc42 12 + TDD 영역(04 B.2)
    ku.template.md           # KU frontmatter 스켈레톤(01 A.1.1)
    bok.template.yaml
  adapters/                  # 슬래시/Skill 어댑터(에이전트별, 얇음)
    claude-code/  ...
```

- 배포: `bok` CLI를 패키지로(예: 단일 바이너리/스크립트). 에이전트·팩은 데이터로 동봉. **인터넷 없이도 코어 동작**(오프라인 우선, KG 기밀성 `research/03/knowledge-graph.md`).

---

# 2. 대상 저장소의 `bok/` 레이아웃 (BoK Wiki)

> D01 A.7 확장. **저작물(authored)과 컴파일물(compiled)을 물리적으로 분리.**

```
<target-repo>/
  src/ ...                        # 기존 시스템 코드
  bok.yaml                        # ③ 설정 (§4)
  bok/
    <bounded-context>/            # 예: billing/  identity/  catalog/
      reference/*.md              # 저작 KU (사람+AI, 리뷰 대상)
      explanation/*.md
      how-to/*.md
      tutorial/*.md
      glossary/*.md
    _system/                      # 컴파일물 + 운영 산출 (§3)
      catalog.yaml                #   L1 인덱스 (생성)
      graph.json                  #   컴파일된 관계 그래프 (생성)
      context-map.md              #   bounded context 관계(C4) (curator)
      coverage.yaml               #   커버리지 격자 (context 갱신/ready 평가)
      discovery-plan.md           #   발굴 계획/메모리 (orchestrator)
      validation-report.md        #   검증 결과 (validator)
      readiness-report.md         #   이해도 판정 (ready)
      redirects.yaml              #   id 이동 이력 (§5)
    _packs/                       # 설치된 Skill 팩 스냅샷(선택, 재현성)
```

> 설계 결정 D20 — **두 평면(plane) 분리**: `bok/<context>/**` = 저작물(git 커밋·PR 리뷰·docs-like-code). `bok/_system/**` = **파생물**(CLI가 생성). 파생물은 커밋하되(오프라인·리뷰 가시성) `bok compile`로 재생성 가능한 캐시로 취급 — 손으로 편집 금지(헤더에 `# GENERATED` 명시).

## 3. 저작 vs 생성 규칙
| 경로 | 성격 | 편집 |
|------|------|------|
| `bok/<context>/**.md` | 저작 KU | 사람/AI가 작성, PR 리뷰 |
| `bok/_system/catalog.yaml`,`graph.json` | 생성 | 금지(재컴파일) |
| `bok/_system/*-report.md`, `coverage.yaml`, `context-map.md` | 반생성 | 도구 생성 + 사람 주석 허용(주석 블록) |
| `bok.yaml` | 설정 | 사람 |

---

# 4. `bok.yaml` — 설정 스키마

> 04에서 "조정 가능"이라 한 모든 임계의 단일 소스. vendor-neutral.

```yaml
bok_version: "0.1.0"              # 프레임워크 버전 고정(재현성)
project: acme-billing
bounded_contexts:                # DDD 경계(01 A.2.3) — 라우팅 1차 필터
  - id: billing
  - id: identity

staleness:                       # 04 A.2
  reference_days: 90
  explanation_days: 180
  glossary_days: 180

confidence:                      # 04 A.1 — corroborated 정의 등 정책
  cross_support_requires_distinct_kinds: true

readiness:                       # 04 B.3/B.4
  criticality_weights: {critical: 4, high: 3, normal: 2, low: 1}
  required_confidence: {critical: verified, high: corroborated, normal: inferred}
  tier_thresholds: {R3_score: 80}
  purpose_to_tier: {understand: R2, feature: R3, modernization: R4}

adversarial:                     # 04 A.3
  max_rounds: 3

packs:                           # §6 Skill 팩 소스 + 우선순위
  - source: core                 # 항상
  - source: domain/pack-billing-domain@1.2.0
  - source: ./bok-local-skills   # 프로젝트 로컬(최우선)

coverage_template: arc42+tdd     # templates/coverage.template.yaml
```

---

# 5. id 무결성 (리팩터링 안전)

> 열린 질문 D01-4의 답. id는 불변(D02)인데 파일은 이동한다.

> 설계 결정 D21 — **id는 경로와 분리된 불변 식별자.** 파일 이동/이름변경은 `bok mv`로만:
> 1. frontmatter `id`는 유지(불변).
> 2. 물리 경로 변경을 `redirects.yaml`에 기록(옛 경로→새 경로).
> 3. 모든 `relations.target`은 경로가 아니라 **id로 참조** → 이동해도 간선 무결.
> 4. `bok compile`이 **dangling relation(존재하지 않는 id)** 을 오류로 검출 → 참조 무결성 강제(KG 품질, `research/03/knowledge-graph.md`).

- KU 삭제 시: 삭제 대신 `status: deprecated` + `supersedes` 권장. 실삭제는 참조 검사 후.
- id 재명명은 예외적 — alias를 `redirects.yaml`에 남겨 외부 링크 보존.

---

# 6. Skill 팩 — 배포·버전·해석 우선순위

> 열린 질문 D03-3의 답. 근거: Spec Kit Extensions/Presets/Bundles 오버라이드 계층(`research/01/spec-kit.md`) + BMAD 모듈(`research/01/bmad-method.md`).

## 6.1 팩 구조
```
pack-billing-domain/
  pack.yaml            # name, version(semver), bok_version 호환범위, 제공 Skill 목록
  discover/  context/  validate/  ready/   # SKILL.md들
  coverage.additions.yaml                   # 도메인 영역 추가(04 B.2)
```

## 6.2 해석 우선순위 (동일 Skill명 충돌 시)
> 설계 결정 D22 — **프로젝트 로컬 > 도메인 팩 > 코어** (Spec Kit 오버라이드 계승). 가장 구체적인 것이 이긴다. `bok.yaml` `packs` 순서가 tie-break.

## 6.3 버전·재현성
- 팩은 semver, `bok.yaml`에 `@version` 고정. `bok_version` 호환 범위를 `pack.yaml`이 선언(비호환 시 설치 거부).
- 선택: `bok/_packs/`에 설치 스냅샷을 커밋해 완전 재현(오프라인·감사).

---

# 7. 시스템이 여러 저장소에 걸칠 때
- **모노레포**: `bok/`는 루트 1개, `bounded_contexts`로 분할.
- **멀티레포**: 각 저장소에 `bok/` + 상위 **aggregator**가 각 `catalog.yaml`을 취합(향후; graph.json은 id 전역 유일하므로 병합 가능). context-map이 저장소 경계를 넘는 의존을 표현.

## 8. Git 통합
- **pre-commit hook**: 변경된 KU의 frontmatter 스키마 검증(`bok-schema`) + `bok compile`(catalog/graph 갱신) + dangling relation 검사.
- **staleness**: code locator가 가리키는 파일이 변경된 커밋에서 관련 KU를 재검증 큐에 추가(04 A.2).
- BoK는 코드와 **같은 PR·리뷰·CI**를 탄다(docs-like-code, `research/02/backstage.md`).

## 9. 헌장 정합
| 헌장/원칙 | 이 설계 |
|----------|---------|
| vendor-neutral·language-independent | CLI+마크다운+yaml, 특정 스택 무관 |
| 단순성 | 그래프/벡터 DB 없음, git+파일 |
| 확장성 | Skill 팩 계층 |
| 재현성·감사 | 버전 고정 + 스냅샷 + 생성물 분리 |
| 살아있음 | hook 기반 재컴파일·재검증 |

## 10. 설계 결정 요약
- **D19** 프레임워크 저장소 ↔ 대상 저장소 분리, BoK는 대상에 거주.
- **D20** 저작 평면(`<context>/`) ↔ 파생 평면(`_system/`) 물리 분리.
- **D21** id는 경로 분리·불변, `bok mv`+redirects+id참조로 무결성.
- **D22** 팩 우선순위 프로젝트 로컬 > 도메인 팩 > 코어.

## 11. 열린 질문 (다음 산출물)
1. 실제 KU 작성 시 frontmatter/본문의 손맛, 영역 자동 매핑 정확도 → **06 예제 프로젝트**에서 실증.
2. aggregator(멀티레포) 상세 → Roadmap.
