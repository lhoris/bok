# ADR (Architecture Decision Record)

> Category: Documentation & Architecture · Phase 4 · Nygard / MADR

## 1. 왜 만들어졌는가?

코드는 **"무엇을" 하는지는 보여주지만 "왜" 그렇게 했는지는 지운다.** 시간이 지나면 결정의 이유·트레이드오프가 유실되고, 후임자는 같은 실수를 반복하거나 함부로 되돌린다. ADR은 **중요한 결정과 그 맥락·결과를 경량으로 기록**한다.

## 2. 어떤 문제를 해결하는가?

- **의사결정 근거(rationale)의 유실** — "왜 이렇게 했는가"
- 고려된 대안·트레이드오프의 소실
- 결정의 **추적성·역사** 부재

## 3. 핵심 철학

- **경량·마크다운·코드 옆.** 무겁지 않게, 저장소에 함께.
- **결정은 사슬을 이룬다.** 한 ADR의 consequences가 다음 ADR의 context가 된다(패턴 언어처럼).
- **대안을 반드시 기록(MADR).** Considered Options는 선택이 아니라 필수 — 왜 이 선택인지 이해하려면 버려진 대안이 필요.

## 4. 구조

- **핵심 포맷(Nygard)**: Title · Status(Draft/Accepted/Deprecated/Supersedes) · **Context**(문제·드라이버) · **Decision**(선택+근거) · **Consequences**(결과·트레이드오프).
- **MADR(Markdown Any Decision Records)**: full/minimal 템플릿, **Considered Options(장단점)를 필수화**.
- 상태 전이와 supersede 관계로 **결정 이력 그래프** 형성.

## 5. 장점 (BOK 관점)

- **BOK가 반드시 담아야 할 "왜(rationale)" 지식의 표준 형식.** 헌장의 "코드만으로는 알 수 없는 업무 규칙/이유"에 정면 대응. DeepWiki가 말한 design rationale의 구조화 포맷.
- **경량·마크다운·저장소 거주** — BOK 물리 포맷(LLM Wiki)과 완벽 호환.
- **Context→Decision→Consequences 사슬 = 관계 그래프** — KG(Phase 3) relations와 결합해 결정 이력을 추적.
- **대안 필수 기록** — BOK의 "합의보다 근거, 대안 제시" 원칙과 정합. Adversarial Review 산출물의 형식으로도 사용 가능.
- **Status 필드** — confidence/검증 상태 표현의 선례.

## 6. 단점 / 한계 (BOK 관점)

- **미래의 새 결정 기록용** — 기존 시스템의 **과거 결정을 역복원**하는 절차는 없음(brownfield 공백).
- **사람이 쓰는 전제** — 자동 발굴 아님.
- 결정만 다룸 — 시스템 이해의 다른 축(구조·데이터·업무)은 범위 밖(arc42가 보완).

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **ADR 포맷을 BoK의 "왜/의사결정" 지식 단위 스키마로 채택**(Context·Decision·Consequences·Options).
- **Status 필드 → BOK confidence/검증 상태** 표현에 응용.
- **결정 사슬(consequences→context) → KG 관계**로.
- **대안 필수** → Adversarial Review·근거 우선 원칙의 형식.

**개선할 것**
- **역복원(reverse ADR)**: 기존 코드·커밋·이슈에서 **과거 결정을 추론해 ADR 초안 생성** + provenance/confidence(추론 vs 확인) + 사람 검증.
- brownfield용 "관찰된 결정" 상태값 추가.

---

### Evidence
- adr.github.io — Architectural Decision Records — https://adr.github.io/
- Michael Nygard, "Documenting Architecture Decisions" (Cognitect) — https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- About MADR — https://adr.github.io/madr/
