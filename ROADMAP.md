# BOK Roadmap

BOK는 "지속적으로 검증하고 개선한다"(헌장)를 지향한다. 아래 단계는 확정이 아니라 **검증 대상 가설**이며, 각 단계는 이전 단계의 실측으로 조정된다.

## 상태 요약
- ✅ **조사(Research)** — 20+ 프레임워크, 4개 카테고리, `research/` + `_SYNTHESIS.md`.
- ✅ **설계(Design)** — `design/01–06`, 예제 `examples/acme-billing/`.
- ⬜ **구현(Implementation)** — 아래 M1~.

## M1 — Walking Skeleton (최소 동작 CLI) ✅
목표: `examples/acme-billing`을 손이 아니라 도구로 재생성.
- ✅ `bok init` 스캐폴딩(templates/) + `bok status` 대시보드.
- ✅ `bok compile`(catalog·graph·dangling 검사) + KU 스키마 검증.
- ✅ `bok ready`의 coverage→신호등→hard gate→tier 계산(D04) 구현·실증.
- ✅ git pre-commit hook 템플릿(`templates/hooks/pre-commit`, D05 §8).
- **검증 답**: 완결성은 confidence만으로 계산 불가 → `open_gap` 저작 플래그로 해소.
  자동 영역↔KU 매핑 정확도는 M2(discover) 이후 실측. 상세: `cli/README.md` M1 Findings.

## M2 — Discover (근거 발굴)
- `code-archaeology` Skill: 의존성·변경 히트맵·데이터모델 추출 → 후보 KU(provenance 자동).
- `kg-extraction` Skill: 엔티티·관계 추출.
- Orchestrator–Worker 병렬(발굴 한정, 비용 통제).
- **검증 질문**: 자동 발굴 KU의 초기 confidence 분포와 사람 수정 비용.

## M3 — Validate (검증 루프)
- `grounding-check`·`adversarial-review`·`contradiction-detection`.
- confidence 전이 + staleness 강등(git hook 연동).
- **검증 질문**: adversarial fixpoint 종료(D16)가 실제로 수렴하는가.

## M4 — Human Externalization
- 인터뷰/Event Storming 가이드 생성·요약 → human provenance KU.
- `verified` owner 서명 워크플로우.
- **검증 질문**: 암묵지(90%) 흡수가 버스팩터 지표를 실제로 낮추는가.

## M5 — Context Assembly & AI 소비
- `bok assemble` → Context Pack(gaps 포함, D01 B.4).
- 에이전트가 Context Pack으로 실제 개발 태스크 수행하는 레퍼런스 통합.
- **검증 질문**: 임베딩 없이(제목·TL;DR·relations) 조립 관련성이 충분한가(D01 D-3).

## M6 — 확장 생태계 & 파일럿
- 도메인/기술 Skill 팩(예: mainframe, spring). 팩 레지스트리.
- 실제 브라운필드 시스템 파일럿 → 성공 지표 측정(온보딩 시간·time-to-first-PR·버스팩터, `_SYNTHESIS §6`).
- 멀티레포 aggregator(D05 §7).

## 장기 가설
- **BOK가 온보딩 시간을 유의미하게 줄이는가** — Backstage 60→20일(`research/02/backstage.md`)에 준하는 효과를 근거로 검증.
- **"검증되는 LLM Wiki"가 생성-only 도구보다 신뢰를 주는가** — 파일럿에서 잘못된 이해로 인한 사고율 비교.

## 명시적 비목표 (Non-goals)
- 코드 생성 파이프라인이 되는 것(그건 Spec Kit/BMAD의 하류 — BOK는 그 **상류**).
- 문서 생성 도구가 되는 것(BOK 산출물은 검증·이해도 게이트가 붙은 지식).
- 무거운 EA 스위트가 되는 것(하향식 대규모 모델링 거부).
