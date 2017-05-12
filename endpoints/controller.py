from api_client import ApiClient
from endpoints.annual_overview import AnnualOverview
from endpoints.attachment_public import AttachmentPublic
from endpoints.attachment_tab import AttachmentTab
from endpoints.avatar import Avatar
from endpoints.customer_statement import CustomerStatement
from endpoints.draft_share_invite_bank import DraftShareInviteBank
from endpoints.share_invite_bank_inquiry import ShareInviteBankInquiry
from endpoints.share_invite_bank_response import ShareInviteBankResponse
from endpoints.card import Card
from endpoints.cash_register import CashRegister
from endpoints.certificate_pinned import CertificatePinned
from endpoints.chat_conversation import ChatConversation
from endpoints.draft_payment import DraftPayment
from endpoints.invoice import Invoice
from endpoints.master_card_action import MasterCardAction
from endpoints.monetary_account import MonetaryAccount
from endpoints.payment import Payment
from endpoints.request_inquiry import RequestInquiry
from endpoints.schedule import Schedule
from endpoints.scheduled_payment import ScheduledPayment
from endpoints.tab import Tab
from endpoints.user import User


class Controller:
    api_client = ApiClient()
    user = User(api_client)
    monetary_account = MonetaryAccount(api_client)
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
    annual_overview = AnnualOverview(api_client)
    attachment_public = AttachmentPublic(api_client)
    attachment_tab = AttachmentTab(api_client)
    avatar = Avatar(api_client)
    customer_statement = CustomerStatement(api_client)
    draft_invite = DraftShareInviteBank(api_client)
    share_inquiry = ShareInviteBankInquiry(api_client)
    share_response = ShareInviteBankResponse(api_client)
    tab = Tab(api_client)
