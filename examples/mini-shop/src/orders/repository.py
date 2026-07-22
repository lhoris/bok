"""Order persistence."""


class OrderRepository:
    def save(self, cart, charge):
        # INSERT INTO orders ...
        return {"id": 1, "items": cart, "charge_id": charge}
