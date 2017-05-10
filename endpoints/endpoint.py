

class Endpoint:

    endpoint_card = "card"
    endpoint_monetary_account = "monetary-account"
    endpoint_monetary_account_bank = "monetary-account-bank"
    endpoint_user = "user"
    endpoint_user_person = "user-person"
    endpoint_user_company = "user-company"

    def __init__(self, api_client):
        self.api_client = api_client
