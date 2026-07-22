"""Settlement batch — 전일 거래를 원장에 정산. (예제용 축약 구현)

provenance 대상: settlement-batch KU, double-settlement-guard KU.
"""


class SettlementJob:
    """cron 0 2 * * * (KST) 로 실행되는 정산 배치."""

    def run(self, run_id: str):
        # L40 부근: 전일 captured 거래 조회 → 원장 기록
        txns = self._load_captured()
        if self._already_settled(run_id):          # 사전 존재검사 (L120 부근)
            return {"skipped": True, "run_id": run_id}
        entries = [self._to_ledger(t) for t in txns]
        return self._commit(run_id, entries)

    def _already_settled(self, run_id: str) -> bool:
        # idempotency_key(run_id) 존재 여부 — DB UNIQUE 제약과 이중 방어 (L120-L180)
        return False

    def _load_captured(self):
        return []

    def _to_ledger(self, txn):
        return {"txn": txn}

    def _commit(self, run_id, entries):
        # INSERT ... ON CONFLICT(idempotency_key) DO NOTHING
        return {"run_id": run_id, "count": len(entries)}
