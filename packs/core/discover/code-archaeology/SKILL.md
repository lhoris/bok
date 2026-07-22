---
name: code-archaeology
description: 레거시/낯선 코드에서 구조·의존·데이터모델·업무규칙 후보를 발굴한다. 저장소 마이닝·변경 히트맵·의존성 복원. discover 단계.
phase: discover
wraps: bok discover
---

# code-archaeology

## When to use
낯선 코드베이스의 구조와 그 안에 굳은 지식을 캐야 할 때. `bok-discoverer`가 로드.

## Procedure
1. **결정론(CLI)**: `bok discover --scope <ctx> --source <dir>` 실행 → 패키지 KU(+depends-on), 데이터모델 KU, 변경열도 우선순위, provenance 자동. (research/02/software-archaeology)
2. **추론(LLM)** — CLI가 남긴 `## 열린 질문`을 채운다:
   - **hot 코드**(변경열도 상위)부터 읽어 **업무 규칙 후보**를 추출(business process archaeology). 근거: 조건 분기·검증 로직·예외 처리.
   - 커밋 메시지·이슈·주석에서 **"왜"(의도)** 를 추론 → `explanation` KU 초안.
   - 각 추론에 provenance(파일#라인/커밋) 부착, confidence는 **inferred 유지**(검증 전).

## Output / handoff
후보 KU(draft/inferred) → `bok-curator`(context). 확실치 않은 것은 `## 열린 질문`에 남겨 human-externalization·validate로.

## Boundaries
코드에 **없는** 것(암묵지·미문서 정책)은 추론하지 말고 gap으로. provenance 없는 지식 금지.
