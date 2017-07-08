class RequestInquiryBatch:
    def __init__(self, request_inquiry_obj):
        self.payments = [obj.__dict__ for obj in request_inquiry_obj]
