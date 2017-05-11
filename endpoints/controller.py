from api_client import ApiClient
from endpoints.card import Card
from endpoints.draft_payment import DraftPayment
from endpoints.payment import Payment
from endpoints.request_inquiry import RequestInquiry
from endpoints.user import UserEndpoint
from endpoints.monetary_account import MonetaryBankEndpoint


class Controller:

    api_client = ApiClient()
    user = UserEndpoint(api_client)
    monetary_account = MonetaryBankEndpoint(api_client)
    card = Card(api_client)
    payment = Payment(api_client)
    request_inquiry = RequestInquiry(api_client)
    draft_payment = DraftPayment(api_client)
