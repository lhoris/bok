# Context Engineering

> Category: AI Framework · Phase 1 · Anthropic 외 · 개념/원리

## 1. 왜 만들어졌는가?

프롬프트 엔지니어링만으로는 에이전트 실패를 못 막는다는 관찰에서 나왔다. **"오늘날 대부분의 에이전트 실패는 모델 실패가 아니라 컨텍스트 실패"** — 모델은 멀쩡한데 잘못된/부족한/과다한 정보를 넣어 틀린다.

## 2. 어떤 문제를 해결하는가?

- 유한한 컨텍스트 윈도우에, 끊임없이 팽창하는 정보 우주에서 **무엇을 넣을지 큐레이션**하는 문제
- 관련 없는 응답, 이전 맥락 망각 → 대부분 **정보 공급의 문제**
- 컨텍스트를 유한 자원으로 보고 **토큰 효용을 최적화**

## 3. 핵심 철학

- **컨텍스트 엔지니어링 = 프롬프트 엔지니어링의 자연스러운 진화.** 프롬프트뿐 아니라 시스템 지시·도구·외부 데이터·메시지 이력 전체를 설계.
- **Right info + right tools, in the right format, at the right time.**
- **Just-in-time 전략.** 모든 걸 미리 넣지 않고, **경량 식별자(파일 경로·저장된 쿼리·링크)** 만 유지하다가 실행 시점에 도구로 필요한 데이터를 동적 로드.

## 4. 구조 (원리 세트)

- **Context as finite resource** — 토큰은 예산이다.
- **Just-in-time loading** — 참조(포인터)만 들고 있다가 필요할 때 적재. (Claude Skills의 progressive disclosure와 같은 뿌리.)
- **Curation over accumulation** — 쌓기보다 고르기.
- **Format matters** — 같은 정보라도 구조·형식이 성능을 좌우.

## 5. 장점 (BOK 관점)

- BOK의 **Context Model**은 사실상 "Enterprise Onboarding에 특화된 Context Engineering"이다 — 이 분야가 BOK의 이론적 토대.
- **경량 식별자 + JIT 로딩** = 거대한 엔터프라이즈 지식을 다루는 유일하게 확장 가능한 방식. BoK는 방대하므로 "전부 로드"는 불가능; **포인터 + 온디맨드 근거 로딩**이 필수.
- **"실패는 컨텍스트 실패"** 라는 명제가 BOK의 존재 이유를 정당화 — AI가 틀리는 건 이해(컨텍스트)가 부족해서다.

## 6. 단점 / 한계

- 원리이지 **방법론·산출물·게이트가 아니다.** "무엇을 큐레이션할지"는 알려주지만, 엔터프라이즈 시스템에서 **그 지식을 어떻게 발굴·검증·구조화할지**는 공백.
- 도메인 지식/업무 규칙 같은 **비코드 지식**의 획득 절차가 없다.

## 7. BOK에서 가져올 것 / 개선할 것

**가져올 것**
- **BOK Context Model의 설계 원리로 통째 채택**: finite resource, JIT loading, 경량 식별자(포인터), format-matters.
- **"컨텍스트 실패" 프레이밍**을 BOK 가치 제안의 근거로 사용.

**개선/확장할 것**
- 원리에 **절차와 산출물**을 붙인다: `bok.discover`(발굴) → `bok.context`(큐레이션·구조화) → `bok.ready`(검증). 즉 Context Engineering을 **Enterprise Onboarding용 실행 프레임워크로 구체화**하는 것이 BOK의 몫.

---

### Evidence
- Anthropic, "Effective context engineering for AI agents" — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- The Decoder, "context engineering beats prompt engineering" — https://the-decoder.com/anthropic-claims-context-engineering-beats-prompt-engineering-when-managing-ai-agents/
- LangChain, "Context Engineering for Agents" — https://www.langchain.com/blog/context-engineering-for-agents
