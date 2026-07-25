# 02 — 공통 Knowledge Model & 중간 표현(`bok.json`)

> 세 표현물이 공유하는 단일 컴파일 스냅샷. 오늘 파편화된 `catalog.yaml`+`graph.json`+`coverage.yaml`+리포트를 하나로 미리-조인하고, 표현물이 뷰 시점에 계산해선 안 되는 파생 사실(백링크·상태·초성 버킷)을 컴파일러가 한 번 계산해 담는다.

---

## 1. 필요성 판단 — 새 IR가 정말 필요한가

**반대 근거(단순성 우선)**: 3–6 KU 스케일에서 표현물이 catalog/graph/coverage/KU를 즉석 재조합해도 비용은 무시할 만하다. "표현물이 어긋난다"는 위험은 *파일*이 아니라 *공유 로더 함수* 하나로도 해소된다.

**찬성 근거(헌장이 강제)**: 헌장은 두 가지를 명시했다 — (a) **"자동화 도구가 처리할 수 있는 기계 판독형 메타데이터"**, (b) **self-contained 웹 리포트**. 둘 다 **CLI 밖 소비자**가 전체 스냅샷을 *직렬화된 형태로* 필요로 한다. 오늘은 그런 소비자가 KU를 전부 다시 파싱하고 ready 로직을 재구현해야 한다(중복 금지 위배).

> **결정 D24 — 물질화하되 불변식을 재정의한다.** 단일 원천 보장은 **`build_model()` 빌더 함수**가 준다. `bok.json`은 그 출력의 (i) 외부 기계판독 계약 + (ii) HTML 임베드 소스다. **내부 표현물은 라이브 모델을 소비**(직렬화 왕복 없음)하므로 내부 drift 표면이 없다. → [ADR-02](adr.md).

### 1.1 캐시 정합성 (drift 방지)

`bok.json`은 캐시이고 반드시 언젠가 낡는다(특히 `validate`가 KU confidence를 in-place로 고침). 정합성은 3중:

1. `compile`이 `bok.json`의 **유일한 writer**. 모든 변경 커맨드가 "run `bok compile`"을 안내.
2. `bok.json`에 **`source_digest`**(정렬된 KU 내용 + `coverage.yaml` + 관련 `bok.yaml` 키의 해시). 소비자·`render`는 이걸로 신선도 검사, 불일치 시 **stale 스냅샷 방출 거부**.
3. **커밋 여부는 선택**(D24):
   - *기본(권장)* — `.gitignore`. CI/`compile`에서 생성. **drift 제로**(레드팀 선호). 지식(KU)은 여전히 repo에 거주, 캐시만 일시적.
   - *옵션* — 커밋. `bok compile`을 **pre-commit 훅**에 넣어 "`bok.json` ≠ 새 빌드면 커밋 실패"로 무결성 강제. 오프라인 감사·리뷰 가시성이 필요한 팀용.

> `readiness`의 **purpose-상대 verdict는 `bok.json`에 저장하지 않는다**(낡으면 거짓말이 되는 유일한 필드). purpose-독립 status/score/tier만 저장하고, verdict는 소비자가 `tier`+`hard_gate`+`bok.yaml`의 `purpose_to_tier`로 값싸게 투영.

---

## 2. `bok.json` 스키마 (v1)

```jsonc
{
  "schema_version": "bok.snapshot/1",
  "generated_by": "bok compile",
  "generated_at": "2026-07-25T09:00:00Z",
  "source_digest": "sha256:9f2c…",          // 신선도 검사 (KU+coverage+cfg 해시)
  "project": "acme-billing",
  "bounded_contexts": ["billing"],
  "config": {                                // render가 참조하는 표현 설정 (bok.yaml에서)
    "source_links": { "mode": "relative", "github_base": null }
  },

  "kus": [
    {
      "id": "bok://billing/reference/settlement-batch",
      "title": "정산 배치 (Settlement Batch)",
      "kind": "reference", "layer": "component", "context": "billing",
      "status": "active", "confidence": "corroborated",
      "owner": "team-billing", "last_verified": "2026-07-20", "stale": false,
      "path": "bok/billing/reference/settlement-batch.md",
      "tldr": "매일 02:00 KST 전일 거래를 원장에 정산 기록하는 배치. 멱등 키로 중복 실행 방어.",
      "provenance": [                         // ← catalog.yaml엔 없던 필드
        { "kind": "code", "locator": "src/billing/settle.py#L40-L210", "note": "진입점·스케줄",
          "resolved": { "file": "src/billing/settle.py", "start": 40, "end": 210 } }
      ],
      "relations": {
        "out": [ { "type": "depends-on",  "target": "bok://billing/reference/ledger-store", "resolved": false },
                 { "type": "defines-term", "target": "bok://billing/glossary/idempotency-key", "resolved": true } ],
        "in":  [ { "type": "derived-from", "source": "bok://billing/explanation/double-settlement-guard" } ]  // ← 신규: 백링크
      },
      "coverage_areas": ["context-and-scope"] // coverage.yaml 역인덱스
    }
    // … 나머지 KU
  ],

  "graph": {
    "nodes": ["…"], "edges": [ { "from": "…", "type": "depends-on", "to": "…", "resolved": false } ],
    "views": {                               // 신규 파생 뷰 (§4)
      "by_context": { "billing": ["…"] },
      "clusters":  [ ["…settlement-batch", "…double-settlement-guard", "…idempotency-key"] ]
    }
  },

  "coverage": {                              // coverage.yaml + 계산된 status
    "scope": "billing",
    "areas": [
      { "id": "data-model", "criticality": "critical", "open_gap": false, "kus": [], "status": "red" }
      // … arc42+tdd 전 영역
    ]
  },

  "readiness": {                             // purpose-독립만 (D24)
    "score": 36, "tier": "R0", "hard_gate": { "pass": false, "critical_reds": ["data-model"] },
    "gaps": ["context-and-scope", "data-model"]
    // purpose별 verdict는 저장 안 함 — 소비자가 tier+hard_gate+cfg로 투영
  },

  "glossary": {                              // 신규 초성 투영 (§05)
    "collation": "hangul-choseong",
    "order": ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ","A-Z","numbers-symbols"],
    "buckets": {
      "ㅁ": [ { "id": "bok://billing/glossary/idempotency-key", "term": "멱등 키", "en": "Idempotency Key",
               "context": "billing", "confidence": "authoritative", "sort_key": "ㅁ|멱등 키" } ]
    }
  },

  "diagnostics": {
    "dangling":  [ { "target": "bok://billing/reference/ledger-store",
                     "source": "bok://billing/reference/settlement-batch", "type": "depends-on" } ],
    "duplicate_titles": [], "stale": []
  }
}
```

### 2.1 필드 이주 지도 (오늘 어디 → 새 자리)

| 오늘 | 위치 | 새 자리 |
|------|------|--------|
| id,title,kind,layer,context,confidence | `catalog.yaml` | `kus[].*` |
| relations(`"type:target"` 문자열) | `catalog.yaml` | `kus[].relations.out`(구조화) + `graph.edges` |
| provenance/status/owner/last_verified | **KU 마크다운에만** | `kus[].*` |
| `## TL;DR` | KU 본문 | `kus[].tldr` |
| **백링크** | **없음** | `kus[].relations.in` (신규 계산) |
| nodes/edges | `graph.json` | `graph.*` |
| area status | **없음**(ready가 라이브 계산) | `coverage.areas[].status` |
| score/tier/hard-gate/gaps | **마크다운에만** | `readiness.*` |
| **초성 버킷** | **없음** | `glossary.buckets` (신규 계산) |
| dangling 경고 | `catalog.yaml` | `diagnostics.dangling` |

---

## 3. 백링크 계산 (결정론)

오늘 `KU.relations()`는 **outbound만** 반환한다. 백링크는 전 KU의 edge를 뒤집은 group-by(10줄):

```
inbound = defaultdict(list)
for e in all_edges:               # compile이 이미 만드는 edge 집합
    if e.to in id_set:            # 저작된 대상만 백링크 (dangling 제외)
        inbound[e.to].append({"type": e.type, "source": e.from})
```

`e.to`가 id 집합에 없으면(dangling) 노드·백링크 없이 `diagnostics.dangling`으로만 표면. 각 edge의 `resolved` 불리언이 이를 기록.

---

## 4. 파생 그래프 뷰 (DB 없이, 결정론)

- `views.by_context` — 노드를 KU `context`로 그룹핑. O(n).
- `views.clusters` — resolved edge 위 **약연결 요소**(union-find, 방향 무시). Wiki 이웃 페이지·리포트 의존 클러스터용. 그래프 엔진 불필요. O(n·α).
- (선택) 노드별 in/out degree — 리포트 hotspot 뷰.

모든 출력은 **정렬된 `id` 순서**로 → byte-stable(idempotent render, 깨끗한 diff).

---

## 5. 마이그레이션 / 호환

- `bok.json` = `catalog.yaml` + `graph.json`의 **엄격한 상위집합**.
- **`catalog.yaml` 유지** — 경량 L1 glance 계층(작고 PR-diff 친화). `bok.json`이 크고 비정규화라 L1이 오히려 유용.
- **`graph.json` → `bok.json.graph`로 흡수, standalone 폐기**(1개 전환 릴리스 뒤 `--legacy-artifacts` 뒤로). 그래프 사본 3개 유지는 순수 drift 표면.
- 순 산출물 수: 2(catalog + bok.json), graph.json 은퇴 → **순증가 없음**.

---

## 6. 다중 context readiness (모델 아키텍트 지적)

멀티-context 프로젝트는 `bok.json` 하나에 **scope별 readiness**가 필요하다. 스키마의 `coverage`/`readiness`는 단일 블록이 아니라 scope-keyed로 확장:

```jsonc
"readiness": { "billing": { "score": 36, "tier": "R0", … }, "orders": { … } }
```

acme-billing(단일 context)은 키가 하나. 이 확장은 코딩 전 반영한다(사후 스키마 파괴 방지).
