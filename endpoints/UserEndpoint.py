from endpoints.Endpoint import Endpoint


class UserEndpoint(Endpoint):

    endpoint = "/user"

    def get_logged_in_user(self):
        return self.api_client.get(self.endpoint)
