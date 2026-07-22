"""Order service — orchestrates checkout."""
from orders.repository import OrderRepository
from payments.gateway import PaymentGateway
from catalog.products import ProductCatalog


class OrderService:
    def __init__(self):
        self.repo = OrderRepository()
        self.payments = PaymentGateway()
        self.catalog = ProductCatalog()

    def checkout(self, cart):
        total = sum(self.catalog.price(i) for i in cart)
        charge = self.payments.charge(total)
        return self.repo.save(cart, charge)
