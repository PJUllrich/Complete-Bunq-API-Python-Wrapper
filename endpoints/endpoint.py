

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

    # TODO Implement the endpoint for these urls
    endpoint_schedule = "schedule"
    endpoint_schedule_payment = "schedule-payment"
    endpoint_schedule_instance = "schedule-instance"

    endpoint_mastercard_action = "mastercard-action"

    endpoint_cash_register = "cash-register"
    endpoint_cash_register_qr = "qr-code"
    endpoint_cash_register_qr_content = "content"

    endpoint_share_inquiry = "share-invite-bank-inquiry"
    endpoint_share_response = "share-invite-bank-response"
    endpoint_share_draft = "draft-share-invite-bank"
    endpoint_share_draft_qr = "qr-code-content"

    endpoint_chat = "chat"
    endpoint_chat_conversation = "chat-conversation"
    endpoint_chat_message = "message"

    endpoint_user_pinned_certificates = "certificate-pinned"

    # Many more. Help!

    def __init__(self, api_client):
        self.api_client = api_client

    def make_get_request(self, endpoint):
        res = self.api_client.get(endpoint)
        return res.json()["Response"]
