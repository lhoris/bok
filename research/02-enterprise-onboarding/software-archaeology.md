# Software Archaeology

> Category: Enterprise Onboarding · Phase 2 · 개념/실무 기법

## 1. 왜 만들어졌는가?

현실의 엔터프라이즈 시스템은 **문서가 없거나 낡았고, 원저자는 떠났다.** 그럼에도 그 안에는 조직의 핵심 업무 규칙이 코드로 굳어 있다. Software Archaeology는 이 **미문서화 레거시에서 설계·의도·업무 규칙을 복원**하기 위한 기법의 집합이다.

## 2. 어떤 문제를 해결하는가?

- **암묵지/유실지의 복원** — 코드에만 존재하고 문서엔 없는 지식
- **아키텍처 복원(architectural recovery)** — 실제 구조를 역설계
- **업무 규칙 복원(business process archaeology)** — 소스에 묻힌 업무 프로세스·규칙 추출·보존

## 3. 핵심 철학

- **증거 기반 발굴.** 시스템의 실제 산출물(코드·커밋 이력·실행 트레이스)에서 지식을 캐낸다. — **이것이 BOK의 "근거 우선" 철학과 가장 직접적으로 일치하는 분야다.**
- **관찰된 행동 → 원설계 재구성.**
- **"왜 이렇게 구조화됐는가"에 대한 추론** 이 이해의 핵심.

## 4. 구조 — 대표 기법

- **저장소 마이닝** — 저자·변경 이력 분석, 변경 빈도로 **히트맵**("hot/cold" 코드) 생성 → 위험·중요 영역 식별.
- **리버스 엔지니어링** — 의존성 그래프·메트릭·다이어그램 생성; 소스가 없으면 디스어셈블/디컴파일.
- **동적 분석** — 실행 트레이스에서 제어 흐름·고수준 구조 재구성.
- **Structure mining / graph-based modeling / template matching** — 데이터 추출·리트로핏 시간 단축.
- **Business Process Archaeology** — 소스에서 업무 프로세스·규칙 복원.

## 5. 장점 (BOK 관점)

- **BOK 발굴(Discover) 단계의 방법론적 심장.** "어떻게 근거에서 지식을 캐낼 것인가"의 검증된 기법 목록을 그대로 제공.
- **변경 히트맵 = 우선순위 지도.** 방대한 시스템에서 "어디를 먼저 이해해야 하는가"를 근거로 정해줌 → BOK의 발굴 우선순위 전략.
- **Business Process Archaeology** — BOK가 반드시 다뤄야 할 "코드로만 아는 업무 규칙" 복원의 직접 선례.
- **증거 기반 프레이밍** — BOK의 provenance 필드에 "어떤 증거에서 왔는가"를 채우는 실질 방법.

## 6. 단점 / 한계

- **기법의 모음이지 프레임워크가 아니다.** 산출물 스키마·검증 게이트·이해도 측정·커맨드 체계가 없다.
- **결과의 구조화·공유** 를 다루지 않는다(캐내고 끝). 사람+AI가 공유하는 BoK로 조직화하는 단계가 비어 있음.
- 대체로 **코드/기술 중심** — 이해관계자 인터뷰 같은 인적 지식 소스와의 통합이 약하다.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **발굴 기법 카탈로그를 `bok.discover`의 실행 도구상자로 채택**: 저장소 마이닝, 변경 히트맵, 의존성 복원, 동적 분석, 업무 규칙 복원.
- **변경 히트맵 기반 우선순위** → 발굴 순서 결정 전략.
- **증거 기반** → provenance 필드의 실제 채움 방법.

**개선/보완할 것**
- 발굴 산출물을 **구조화된 지식 단위 + 검증**으로 연결(archaeology는 여기서 멈추지만 BOK는 이어감).
- **인적 소스 통합** — 코드 발굴 + 이해관계자 지식을 같은 BoK 스키마로 병합.
- 발굴 결과에 **confidence** 부여(추론 vs 확인).

---

### Evidence
- Software archaeology — Wikipedia — https://en.wikipedia.org/wiki/Software_archaeology
- Lattix, "Software Archaeology — Software Architectural Recovery for Legacy Code" — https://www.lattix.com/blog/software-archaeology-software-architectural-recovery-for-legacy-code/
- Thilo Hermann, "Modernize the Legacy — Software Archaeology" — https://thilo-hermann.medium.com/modernize-the-legacy-software-archaeology-a3e7e5942ec3
