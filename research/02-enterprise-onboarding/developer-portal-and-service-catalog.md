# Developer Portal & Service Catalog

> Category: Enterprise Onboarding · Phase 2 · (헌장의 "Developer Portal" + "Service Catalog"를 한 개념 클러스터로 통합 분석. 구현 사례는 [[backstage]] 참조.)

## 1. 왜 만들어졌는가?

개발자는 필요한 정보를 찾느라 시간을 낭비한다 — 어떤 문서가 맞는지, 어떤 도구 버전을 쓰는지, 스테이징에 어떻게 배포하는지. Internal Developer Portal(IDP)은 이 **흩어진 정보를 중앙화**해 인지 부하를 낮추고 셀프서비스 문화를 만들기 위해 등장했다.

## 2. 어떤 문제를 해결하는가?

- **흩어진 지식** — 문서·소유권·운영 정보가 여러 도구에 분산
- **인지 부하 / 컨텍스트 스위칭** — 매 전환마다 새 정보 세트를 뇌에 로드
- **온보딩 지연** — "time to first PR"

## 3. 핵심 철학

- **중앙화된 단일 진입점** — 컴포넌트당 하나의 URL에 모든 메타데이터(소유팀·역할·문서 링크).
- **Golden Path** — 전체 인프라 스택을 몰라도 표준 경로로 일할 수 있게.
- **셀프서비스** — 복잡성을 추상화.

## 4. 구조

- **Service/Component Catalog** — 컴포넌트별 메타데이터 단일 소스(소유·설명·문서·의존).
- **Golden Paths** — 표준화·의견 있는 워크플로우.
- **Scaffolding/Automation** — 셀프서비스 프로비저닝.
- 산업 현황(2025 DORA): **조직의 90%가 최소 하나의 내부 플랫폼 운영**.

## 5. 장점 (BOK 관점)

- **"중앙 카탈로그가 발견 가능성과 온보딩을 개선한다"는 경험적 증거** — BOK 가치의 산업적 뒷받침.
- **컴포넌트당 단일 메타데이터 URL** = BOK가 각 지식 단위에 부여할 **정규 주소(canonical identity)** 개념.
- **인지 부하 프레이밍** — BOK가 사람에게 주는 가치를 설명하는 언어.

## 6. 단점 / 한계 (BOK 관점)

- **카탈로그는 "이해"가 아니라 "정리"다.** 이미 아는 것을 잘 배열할 뿐, 모르는 것을 발굴하거나 이해도를 높이지 않는다.
- **수작업 유지보수 부담** — 카탈로그가 낡으면 신뢰를 잃는다(오히려 잘못된 이해 유발). 근거·검증 메커니즘 부재.
- **AI 소비를 전제로 설계되지 않음** — 사람용 UI 중심.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **카탈로그 = 지식의 단일 소스** 원칙, **컴포넌트당 정규 주소**, **소유권·관계 메타데이터**.
- **인지 부하 감소 / time-to-first-PR** 을 BOK 성공 지표로.

**개선할 것**
- 카탈로그를 **정적 등록부 → 근거 기반 살아있는 지식**으로: 각 항목에 provenance·confidence·last-verified.
- **발굴 자동화** 로 수작업 유지보수 문제 완화(`bok.discover`).
- **AI-native 카탈로그** — 에이전트가 progressive disclosure로 소비하는 구조([[claude-code-skills]] 참조).

---

### Evidence
- platformengineering.org, "What is an Internal Developer Portal" — https://platformengineering.org/blog/what-is-an-internal-developer-portal
- Atlassian, "Internal Developer Platform" — https://www.atlassian.com/developer-experience/internal-developer-platform
- Frontiers, "Platform engineering and internal developer portals: a multivocal literature review" — https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full
