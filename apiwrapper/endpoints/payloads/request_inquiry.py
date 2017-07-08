from apiwrapper.endpoints.payloads import Payment


class RequestInquiry(Payment):
    """Payload class for creating a request inquiry
    ref: https://doc.bunq.com/api/1/call/request-inquiry/method/post

    Next to the parameters in the __init__ function, the following
    parameters can be set:
        merchant_reference: str
        status: str, can be 'REVOKED' in PUT requests to cancel the request inquiry
        minimum_age: int
        require_address: str
        redirect_url: str
    """

    def __init__(self, amount, counterparty_alias, description, allow_bunqme):
        super().__init__(amount, counterparty_alias, description)

        self.allow_bunqme = allow_bunqme

