# Phase 2 통합 노트 — Enterprise Onboarding

> 대상: Backstage, Developer Portal & Service Catalog, Software Archaeology, Enterprise Architecture, Technical Due Diligence
> 목적: Phase 1의 "방향 반전" 가설을 산업 사례로 **검증**하고, 발굴·구조화·완결성에 대한 구체 자산을 확보한다.

---

## A. Phase 1 가설의 검증 결과

Phase 1은 "생성이 아니라 이해에서 출발한다"는 가설을 세웠다. Phase 2는 이를 **실증**한다.

- **가설 확증 ✅** — 이 분야 전체가 "생성이 아닌 이해"를 다룬다. Backstage(온보딩 60일→20일)는 **"이해 가능 상태로 만들면 온보딩이 빨라진다"** 를 수치로 증명. TDD는 "낯선 시스템 + 시간제약 + 외부자"라는 **BOK와 동형의 상황**을 이미 실무로 다룬다.
- **그러나 결정적 공백 발견** — 이 분야는 두 진영으로 갈린다:
  - **정리(organize) 진영** — Backstage/IDP/EA: 지식을 잘 **배열**하지만, 그 지식을 **발굴하지 않는다**(사람이 `catalog-info.yaml`을 채워야 함). 낡으면 신뢰를 잃는다.
  - **발굴(excavate) 진영** — Software Archaeology/TDD: 근거에서 지식을 **캐내지만**, 재사용 가능한 살아있는 BoK로 **구조화·유지하지 않는다**(캐고 끝, 일회성 스냅샷).

## B. BOK의 위치 = 두 진영의 미싱 링크

> **아무도 "발굴 → 검증 → 구조화 → 유지"의 전체 루프를 잇지 않는다.**
> BOK = **Archaeology/TDD(발굴)** 를 **Backstage/EA(구조화)** 로 연결하고, 그 위에 **근거·검증·이해도 게이트**를 얹는 프레임워크.

```
[소스] --발굴(archaeology,TDD)--> [근거] --검증--> [구조화된 BoK(catalog/다층모델)] --이해도 게이트--> [Development Ready]
        └ Phase2 발굴 진영이 잘함        └ 아무도 안 함      └ Phase2 정리 진영이 잘함           └ 아무도 안 함
```

## C. 가져올 자산 (매핑)

| 출처 | 자산 | BOK 편입 위치 |
|-----|------|--------------|
| Backstage | `catalog-info.yaml` 기계가독 엔티티 스키마 | **지식 단위 표준 포맷** |
| Backstage | 엔티티 관계 모델(소유·의존), Docs-like-code | BoK Model 관계 그래프 / 지식도 리뷰 검증 |
| Backstage/IDP | 온보딩 시간·인지 부하·time-to-first-PR | **BOK 성공 지표(정량)** |
| Dev Portal | 컴포넌트당 정규 주소(canonical identity) | 지식 단위 주소 체계 |
| Software Archaeology | 발굴 기법 툴박스(저장소 마이닝·변경 히트맵·의존성/동적 분석·업무규칙 복원) | **`bok.discover` 실행 도구** |
| Software Archaeology | 변경 히트맵 기반 우선순위 | 발굴 순서 전략 |
| Enterprise Architecture | 다층 모델(비즈니스/앱/데이터/기술), Capability Map | **BoK Model 레이어/지식 유형** |
| Enterprise Architecture | Gap 식별 | Readiness의 "무엇을 아직 모르는가" |
| Technical Due Diligence | 영역 체크리스트 | **발굴 스코프 + Readiness 커버리지 게이트** |
| Technical Due Diligence | 리스크/레드플래그 산출물, 버스팩터 정량화 | BoK 산출물 + 성공 지표 |

## D. 경계할 것 (안티패턴)

- **수작업 카탈로그의 부패(Backstage/EA)** — 발굴 자동화 + last-verified/confidence로 방지.
- **하향식 대규모 선행 모델링(TOGAF)** — BOK는 상향식·증거 기반·점진적. 필요한 만큼만.
- **일회성 스냅샷(TDD)** — BOK는 재실행 가능·버전 관리되는 살아있는 BoK.
- **사람 전용 산출물** — 모든 것은 사람+AI가 함께 소비(AI-native).

## E. Phase 1+2 종합으로 굳어지는 BOK 골격 (가설, Phase 3~4로 검증)

- **파이프라인**: `bok.discover`(archaeology 툴박스 + Multi-agent 병렬) → `bok.context`(catalog 스키마 + EA 다층 모델로 구조화, progressive disclosure) → `bok.validate`(근거 대비 검증, Evaluator–Optimizer) → `bok.ready`(TDD 커버리지 + Gap = 이해도 게이트).
- **지식 단위**: `catalog-info.yaml`형 자족 엔티티 = { identity/주소 + 유형(EA 레이어) + 내용 + **provenance**(어떤 소스·발굴기법에서) + **confidence** + relations + last-verified }.
- **산출물**: 구조화 BoK + 리스크/레드플래그 지도 + Gap 목록.
- **성공 지표**: 온보딩 시간↓, time-to-first-PR↓, 버스팩터↓, 커버리지↑.

## F. Phase 3~4로 넘길 검증 질문

- **Knowledge Engineering(Phase 3)**: provenance·confidence·relations를 **어떻게 정식으로 모델링**하나(Knowledge Graph)? 이해도/신뢰도를 정량화하는 검증된 방법은? 지식 유지·부패 방지의 선례는?
- **Documentation/Architecture(Phase 4)**: catalog 엔티티의 **내용 스키마**를 무엇으로 채우나? arc42(아키텍처 문서 구조), C4(다층 뷰 — EA보다 경량), ADR(의사결정·"왜"), Diátaxis(지식 유형 4분면)이 BoK Model의 산출 스키마를 제공하는가?
