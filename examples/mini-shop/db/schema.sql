CREATE TABLE products (
    id      BIGINT PRIMARY KEY,
    name    VARCHAR(200) NOT NULL,
    price   INT NOT NULL
);

CREATE TABLE orders (
    id         BIGINT PRIMARY KEY,
    total      INT NOT NULL,
    charge_id  VARCHAR(64) NOT NULL
);

CREATE TABLE payments (
    charge_id  VARCHAR(64) PRIMARY KEY,
    amount     INT NOT NULL
);
