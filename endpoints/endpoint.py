from builtins import object


class Endpoint(object):

    endpoint_chat = "chat"


    # TODO Implement the endpoint for these urls
    endpoint_share_inquiry = "share-invite-bank-inquiry"
    endpoint_share_response = "share-invite-bank-response"
    endpoint_share_draft = "draft-share-invite-bank"
    endpoint_share_draft_qr = "qr-code-content"

    endpoint_avatar = "avatar"
    endpoint_attachment_public = "attachment-public"
    endpoint_attachment_public_content = "content"
    endpoint_attachment_tab = "attachment-tab"
    endpoint_attachment_tab_content = "content"

    endpoint_tab = "tab"
    endpoint_tab_attachment = "attachment"
    endpoint_tab_attachment_content = "content"

    def __init__(self, api_client):
        self.api_client = api_client

    def __make_get_request(self, endpoint):
        res = self.api_client.get(endpoint)
        return res.json()["Response"]
