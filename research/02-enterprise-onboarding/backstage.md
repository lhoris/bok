# Spotify Backstage

> Category: Enterprise Onboarding · Phase 2 · CNCF Incubating · backstage/backstage

## 1. 왜 만들어졌는가?

Spotify가 급성장하며 서비스·팀·도구가 폭증했다. 개발자는 무엇이 존재하는지, 누가 소유하는지, 어떻게 배포하는지 찾아 헤맸다. **온보딩 엔지니어가 10번째 PR을 머지하는 데 평균 60일** 이 걸렸다. Backstage는 "흩어진 것을 한 포털로 모으는" 해법으로 나왔고, 도입 후 그 수치가 **20일** 로 줄었다.

## 2. 어떤 문제를 해결하는가?

- **발견 가능성(discoverability)** — 무엇이 존재하고 누가 소유하는가
- **인지 부하(cognitive load)** — 수십 개 도구·대시보드·설정 파일 사이의 컨텍스트 스위칭
- **온보딩 지연** — 신규 인력이 생산성에 도달하는 시간

## 3. 핵심 철학

- **단일 포털(single pane of glass)** — 필요한 모든 것을 한 곳에서.
- **Docs-like-code** — 문서가 코드 옆에 살고 같은 리뷰·배포 파이프라인을 탄다.
- **Golden Path** — 표준화된 의견 있는(opinionated) 경로로 인지 부하를 낮춘다.

## 4. 구조 — 3대 핵심

1. **Software Catalog** — 서비스뿐 아니라 웹앱·라이브러리·데이터 파이프라인 등 모든 소프트웨어 컴포넌트를 등록. 각 엔티티는 저장소 루트의 **`catalog-info.yaml`** 로 기술(소유팀·설명·문서 참조 등 메타데이터). 이것이 **머신 리더블한 지식 카탈로그**의 표준 사례.
2. **TechDocs** — Markdown(+MkDocs) 문서를 코드와 함께 저장, 포털에서 렌더. Spotify 내부 5000+ 문서 사이트.
3. **Software Templates(Scaffolder)** — Golden Path 기반 셀프서비스 스캐폴딩.

채택: 3,400+ 기업, CNCF incubating.

## 5. 장점 (BOK 관점)

- **BOK가 목표하는 결과(온보딩 60일→20일)의 실증.** "이해 가능한 상태로 만들면 온보딩이 빨라진다"는 BOK 가설의 산업적 증거.
- **`catalog-info.yaml` = 지식의 기계가독 스키마.** BOK의 BoK Model이 지향해야 할 "사람+AI가 같이 읽는 구조화된 엔티티"의 검증된 원형.
- **엔티티 = { 정체성 + 소유권 + 관계 + 문서 링크 }** — BOK 지식 단위 스키마 설계에 직접 이식 가능.
- **Docs-like-code** — 지식이 코드와 함께 살고 같은 검증(리뷰)을 받는다. BOK의 "지식도 검증 대상" 원칙과 정합.

## 6. 단점 / 한계 (BOK 관점)

- **결정적 한계: 카탈로그는 "사람이 채워 넣는" 것.** `catalog-info.yaml`은 누군가 작성해야 존재한다. Backstage는 **지식을 발굴하지 않는다** — 이미 아는 것을 등록하는 그릇일 뿐. BOK의 핵심 난제("무엇이 있는지 모른다")를 풀어주지 않는다.
- **근거·이해도 개념 없음.** 엔티티가 정확한지, 조직이 그것을 이해하는지 평가하지 않는다.
- **코드로 알 수 없는 업무 규칙·운영 정책** 을 담는 1급 구조가 없다(문서 링크로만).
- 플랫폼(설치·운영 부담)이지 경량 프레임워크가 아니다.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **`catalog-info.yaml` 스타일의 기계가독 엔티티 스키마** → BOK 지식 단위의 표준 포맷.
- **엔티티 관계 모델(소유·의존)** → BoK Model의 관계(그래프) 기반.
- **Docs-like-code** → 지식을 저장소에 두고 같은 리뷰로 검증.
- **온보딩 시간 = 성공 지표** → BOK 성공 기준의 정량 지표 후보.

**개선/보완할 것**
- Backstage가 **비워둔 상류(발굴)** 를 BOK가 채운다: `bok.discover`가 소스에서 **카탈로그를 자동/반자동 생성**(사람이 손으로 채우는 대신).
- 각 엔티티에 **provenance·confidence** 를 추가해 "등록됨"을 "검증됨"으로 승격.
- 카탈로그를 **AI가 소비 가능한 Context**로 재구성(단순 UI 포털이 아니라 에이전트가 읽는 BoK).

---

### Evidence
- backstage/backstage (GitHub) — https://github.com/backstage/backstage
- Backstage TechDocs 문서 — https://backstage.io/docs/features/techdocs/
- Port, "Backstage: All You Need to Know" — https://www.port.io/blog/backstage-all-you-need-to-know-about-this-developer-portal
- 온보딩 60→20일: platformengineering.org / Spotify 2021 — https://platformengineering.org/blog/what-is-an-internal-developer-portal
