"""Payment gateway adapter."""


class PaymentGateway:
    def charge(self, amount):
        # calls external PSP
        return {"charge_id": "ch_1", "amount": amount}
