-- 원장/정산 스키마 (예제)

CREATE TABLE ledger (
    id           BIGINT PRIMARY KEY,
    txn_id       BIGINT NOT NULL,
    amount       INT NOT NULL,
    settled_at   TIMESTAMP NOT NULL
);

CREATE TABLE settlement_run (
    run_id           VARCHAR(64) PRIMARY KEY,
    started_at       TIMESTAMP NOT NULL,
    -- L22 부근: 멱등 키 (이중 정산 방지의 규범적 근거)
    idempotency_key  VARCHAR(64) NOT NULL UNIQUE
);
