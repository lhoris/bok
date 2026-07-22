---
mode: agent
description: 코드에서 근거를 발굴해 후보 지식 단위를 만든다.
---
scope와 source(기본 src)에 대해: `bok discover --scope <ctx> --source <dir>`를 실행한 뒤, 각 KU의 `## 열린 질문`을 채운다(hot 코드·커밋에서 "왜" 추론; 코드로 모르면 인터뷰 질문). 모든 추론에 provenance, confidence는 inferred 유지.
