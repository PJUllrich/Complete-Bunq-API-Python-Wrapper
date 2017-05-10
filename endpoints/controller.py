from api_client import ApiClient
from endpoints.card import Card
from endpoints.user import UserEndpoint
from endpoints.monetary_account import MonetaryBankEndpoint


class Controller:

    def __init__(self):
        self.api_client = ApiClient()
        self.user_endpoint = UserEndpoint(self.api_client)
        self.monetary_account_endpoint = MonetaryBankEndpoint(self.api_client)
        self.card_endpoint = Card(self.api_client)
