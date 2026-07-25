# BOK Design — 설계 단계

> 조사(`research/`) 종료 후, `research/_SYNTHESIS.md`를 유일한 입력으로 삼아 BOK Framework를 설계한다.
> 모든 설계 결정은 조사 근거를 인용한다(→ 파일명/섹션 링크).

## 설계 산출물 순서 (from `_SYNTHESIS.md §9`)

| # | 산출물 | 상태 |
|---|--------|------|
| 01 | **BoK Model & Context Model** — 지식 단위 스키마·관계·저장·소비 | ✅ 완료 |
| 02 | Workflow & Command 체계 (`discover/context/validate/ready`) | ✅ 완료 |
| 03 | Agent & Skill 정의 | ✅ 완료 |
| 04 | Knowledge Validation & Development Readiness 모델 | ✅ 완료 |
| 05 | Repository / Wiki 구조 | ✅ 완료 |
| 06 | 예제 프로젝트 · Contributor Guide · Roadmap | ✅ 완료 |

## 파일 목록
- `01-bok-model-and-context-model.md`
- `02-workflow-and-commands.md`
- `03-agents-and-skills.md`
- `04-validation-and-readiness.md`
- `05-repository-and-wiki-structure.md`
- `06-example-contributor-roadmap.md`

## 0.2 설계 — Knowledge Surfaces (표현 계층 재설계)
> 오너 헌장("BOK 0.1.0 발전 방향 재설계")에 대응. 웹 리포트·LLM Wiki·용어사전을 하나의 BoK에서 파생시키는 통합 설계. 4개 역할 병렬 비판 검토 + 오너 종합.

- [`0.2-knowledge-surfaces/`](0.2-knowledge-surfaces/README.md) — 00 현황·Gap → 01 목표 아키텍처 → 02 공통 Knowledge Model(`bok.json`) → 03 웹 리포트 → 04 LLM Wiki → 05 용어사전 → 06 명령어·Workflow → 07 로드맵·0.2.0 범위 → [ADR](0.2-knowledge-surfaces/adr.md)(D23–D31)

## 산출물 (설계 밖)
- `../examples/acme-billing/` — 실증 예제(1회전 나선)
- `../CONTRIBUTING.md` · `../ROADMAP.md`
