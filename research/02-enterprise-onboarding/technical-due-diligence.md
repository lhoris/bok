# Technical Due Diligence

> Category: Enterprise Onboarding · Phase 2 · M&A/투자 실무

## 1. 왜 만들어졌는가?

인수·투자 전, 낯선 회사의 기술 자산을 **짧은 시간에 외부자 관점에서 평가**해야 한다. 잘못 판단하면 인수 후 수백만 달러의 기술부채·리스크를 떠안는다. Technical Due Diligence(TDD)는 이 **고위험·시간제약 하의 시스템 이해·리스크 평가** 를 위한 체계다.

## 2. 어떤 문제를 해결하는가?

- **미지 시스템의 빠른 평가** — 아키텍처·코드품질·인프라·보안·컴플라이언스·DevOps·데이터 거버넌스
- **숨은 리스크 발굴** — 기술부채, 보안 취약점, 아키텍처 한계, **사람 의존성(team dependency)**
- **가치 평가에의 반영** — TDD는 밸류에이션 리스크의 20~30%를 완화

## 3. 핵심 철학

- **체크리스트 기반 체계성.** 표준 영역을 빠짐없이 훑는다.
- **리스크·레드플래그 중심.** "무엇이 위험한가"를 먼저 본다.
- **외부자 관점의 시간제약 평가.** — BOK가 상정하는 "낯선 시스템에 투입된 신규 인력/AI"와 상황이 동일하다.

## 4. 구조 — 평가 영역(체크리스트)

- **아키텍처** — 유형(모놀리식/모듈/마이크로서비스/서버리스), 확장성, 부하·스트레스 대응, 베스트프랙티스 정렬.
- **코드베이스 품질** — 유지보수성, 문서·테스트 커버리지.
- **의존성** — 외부 서비스·라이브러리의 deprecated/미유지/EOL 여부.
- **리스크** — 기술부채, 보안, 아키텍처 한계, **팀 의존성(버스 팩터)**.
- 그 외 인프라·보안·컴플라이언스·DevOps·데이터 거버넌스.

## 5. 장점 (BOK 관점)

- **상황이 BOK와 동형(isomorphic).** "낯선 시스템 + 시간제약 + 외부자"는 BOK의 온보딩 시나리오 그 자체 → TDD 체크리스트는 **BOK 발굴 범위(scope)의 검증된 목록**.
- **레드플래그/리스크 관점** — BOK가 이해와 함께 **리스크 지도** 를 산출해야 함을 시사(현대화 전 필수).
- **팀 의존성(버스 팩터)** — BOK의 명시 목표("특정 사람에게만 의존하지 않는가")와 정확히 일치. 정량 평가 선례.
- **체크리스트 = 완결성 게이트.** BOK의 Development Readiness를 "필수 영역 커버리지"로 조작화하는 모델.

## 6. 단점 / 한계 (BOK 관점)

- **일회성 스냅샷.** 딜 시점에 평가하고 끝 — **지속 유지·공유되는 지식 베이스가 아니다.** BOK는 살아있는 BoK를 목표.
- **평가(judgment) 중심, 지식 축적 중심이 아님.** "좋다/나쁘다"를 말하지, 사람+AI가 재사용할 구조화 지식을 남기지 않는다.
- **업무 도메인 지식·용어**보다 기술 리스크에 치우침.
- 대체로 **사람(전문가) 수행** 전제 — AI/자동화·재현성 약함.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **TDD 체크리스트를 BOK 발굴/Readiness의 "커버리지 체크리스트"로 채택** — 어떤 영역을 이해해야 완결인지의 기준.
- **리스크·레드플래그 산출물** → BoK의 표준 산출물 중 하나(현대화 준비의 입력).
- **팀 의존성/버스 팩터 정량화** → BOK 성공 지표.
- **완결성 게이트 발상** → Development Readiness 모델의 뼈대.

**개선할 것**
- **일회성 → 지속형**: 스냅샷 평가를 살아있는 BoK로 전환(재실행 가능·버전 관리).
- **평가 → 지식 축적**: 리스크 판단과 함께 **재사용 가능한 구조화 지식**을 남긴다.
- **사람 전용 → 사람+AI 반복 가능**: 체크리스트를 에이전트가 실행 가능한 발굴 태스크로 조작화([[multi-agent]]의 자족 태스크).

---

### Evidence
- M&A Science, "Tech Due Diligence — Complete Checklist" — https://www.mascience.com/plays/tech-due-diligence-checklist
- DevCom, "IT Due Diligence for M&A: Technology Audit Guide & Checklist" — https://devcom.com/tech-blog/it-due-diligence-for-ma-technology-audit-guide-checklist/
- MEV, "Technical Due Diligence Guide: Process, Checklist & Red Flags" — https://mev.com/blog/technology-due-diligence-how-to-do-it
