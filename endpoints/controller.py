from api_client import ApiClient
from .certificate_pinned import CertificatePinned
from .chat_conversation import ChatConversation
from .invoice import Invoice
from .card import Card
from .cash_register import CashRegister
from .draft_payment import DraftPayment
from .master_card_action import MasterCardAction
from .monetary_account import MonetaryAccount
from .payment import Payment
from .request_inquiry import RequestInquiry
from .schedule import Schedule
from .scheduled_payment import ScheduledPayment
from .user import User


class Controller:
    api_client = ApiClient()
    user = User(api_client)
    account = MonetaryAccount(api_client)
    card = Card(api_client)
    payment = Payment(api_client)
    request_inquiry = RequestInquiry(api_client)
    draft_payment = DraftPayment(api_client)
    schedule = Schedule(api_client)
    scheduled_payment = ScheduledPayment(api_client)
    cash_register = CashRegister(api_client)
    master_card_action = MasterCardAction(api_client)
    chat_conversation = ChatConversation(api_client)
    certificate_pinned = CertificatePinned(api_client)
    invoice = Invoice(api_client)
