from endpoints.Endpoint import Endpoint


class UserEndpoint(Endpoint):

    endpoint = "user"

    @property
    def user(self):
        return self.api_client.get(self.endpoint).json()
