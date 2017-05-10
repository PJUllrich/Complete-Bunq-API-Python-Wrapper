from ApiClient import ApiClient
from endpoints.UserEndpoint import UserEndpoint


class EndpointController:

    def __init__(self):
        self.api_client = ApiClient()
        self.user_endpoint = UserEndpoint(self.api_client)
