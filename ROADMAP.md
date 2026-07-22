# BOK Roadmap

BOK는 "지속적으로 검증하고 개선한다"(헌장)를 지향한다. 아래 단계는 확정이 아니라 **검증 대상 가설**이며, 각 단계는 이전 단계의 실측으로 조정된다.

## 상태 요약
- ✅ **조사(Research)** — 20+ 프레임워크, 4개 카테고리, `research/` + `_SYNTHESIS.md`.
- ✅ **설계(Design)** — `design/01–06`, 예제 `examples/acme-billing/`.
- 🔄 **구현(Implementation)** — **핵심 4-커맨드 파이프라인 실행 가능**:
  `discover → context → validate → ready` (+ init/status/compile). mini-shop에서
  나선 한 바퀴 전체가 도구로 자동 실행됨. LLM 기반 추론(업무규칙·adversarial)은 잔여.

## M1 — Walking Skeleton (최소 동작 CLI) ✅
목표: `examples/acme-billing`을 손이 아니라 도구로 재생성.
- ✅ `bok init` 스캐폴딩(templates/) + `bok status` 대시보드.
- ✅ `bok compile`(catalog·graph·dangling 검사) + KU 스키마 검증.
- ✅ `bok ready`의 coverage→신호등→hard gate→tier 계산(D04) 구현·실증.
- ✅ git pre-commit hook 템플릿(`templates/hooks/pre-commit`, D05 §8).
- **검증 답**: 완결성은 confidence만으로 계산 불가 → `open_gap` 저작 플래그로 해소.
  자동 영역↔KU 매핑 정확도는 M2(discover) 이후 실측. 상세: `cli/README.md` M1 Findings.

## M2 — Discover (근거 발굴) 🔄
- ✅ `bok discover` 결정론적 아키올로지(LLM 없음): import 그래프→패키지 KU+depends-on,
  SQL DDL→데이터모델 KU, git 변경 히트맵→우선순위. provenance 자동, idempotent.
  실증: `examples/mini-shop/`.
- ⬜ LLM 기반 업무 규칙 추론·`kg-extraction` 심화(에이전트 레벨), Orchestrator–Worker 병렬.
- **검증 답**: 자동 발굴 = 전부 `inferred`/`draft`. 발굴≠준비(ready still R0). 도구가
  "코드로 모르는 것(왜)"을 스스로 표식 → M4 인적 발굴 대상 자동 식별. 상세: `cli/README.md` M2 Findings.

## M3 — Validate (검증 루프) 🔄
- ✅ `bok validate`: grounding-check(근거 파일 존재→없으면 강등), cross-support
  자동 승격(inferred→corroborated), staleness 강등, contradiction cap,
  `--sign` owner 서명(corroborated→verified, human-in-the-loop). 실증: acme+mini-shop.
- ⬜ LLM `adversarial-review` 추론 루프(에이전트 레벨), git hook staleness 자동 트리거.
- **검증 답**: 결정론 체크는 단일 패스로 종결. 서명이 readiness gap을 실제로 닫음
  (business-rules→green, score 29→36) 하되 hard gate는 정직하게 유지. 상세: `cli/README.md` M3.

## M4 — Human Externalization
- 인터뷰/Event Storming 가이드 생성·요약 → human provenance KU.
- `verified` owner 서명 워크플로우.
- **검증 질문**: 암묵지(90%) 흡수가 버스팩터 지표를 실제로 낮추는가.

## M5 — Context Assembly & AI 소비 🔄
- ✅ `bok assemble` → Context Pack(units + warnings + **gaps**, D01 B.4). filter→
  seed→expand(relations)→rank(relevance×confidence)→budget trim. acme에서
  design/01 B.4 예제를 실제 데이터로 재현.
- ⬜ 에이전트가 Context Pack으로 실제 개발 태스크 수행하는 레퍼런스 통합.
- **검증 답(D01 D-3)**: 키워드 관련성은 동작하나 한계 노출 — mini-shop에서 goal이
  boilerplate 단어("변경열도")에 매칭됨. **정밀 관련성엔 임베딩 필요**(향후). 현재는
  relations 확장이 이를 보완.

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
