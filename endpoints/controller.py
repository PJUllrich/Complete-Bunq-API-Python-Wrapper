from api_client import ApiClient
from endpoints.card import Card
from endpoints.draft_payment import DraftPayment
from endpoints.payment import Payment
from endpoints.request_inquiry import RequestInquiry
from endpoints.user import UserEndpoint
from endpoints.monetary_account import MonetaryBankEndpoint


class Controller:

    api_client = ApiClient()
    user_endpoint = UserEndpoint(api_client)
    monetary_account_endpoint = MonetaryBankEndpoint(api_client)
    card_endpoint = Card(api_client)
    payment_endpoint = Payment(api_client)
    request_inquiry_endpoint = RequestInquiry(api_client)
    draft_payment_endpoint = DraftPayment(api_client)
