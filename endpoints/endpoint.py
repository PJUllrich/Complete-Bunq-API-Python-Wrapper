

class Endpoint:

    endpoint_card = "card"
    endpoint_monetary_account = "monetary-account"
    endpoint_monetary_account_bank = "monetary-account-bank"
    endpoint_user = "user"
    endpoint_user_person = "user-person"
    endpoint_user_company = "user-company"
    endpoint_payment = "payment"
    endpoint_payment_batch = "payment-batch"
    endpoint_payment_response = "request-response"
    endpoint_request_inquiry = "request-inquiry"
    endpoint_draft_payment = "draft-payment"

    def __init__(self, api_client):
        self.api_client = api_client

    def make_get_request(self, endpoint):
        res = self.api_client.get(endpoint)
        return res.json()["Response"]
