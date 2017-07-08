class PaymentBatch:
    def __init__(self, payment_objs):
        self.payments = [obj.__dict__ for obj in payment_objs]
