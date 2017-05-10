from endpoints.Endpoint import Endpoint


class UserEndpoint(Endpoint):

    endpoint_user = "user"
    endpoint_user_person = "user-person"
    endpoint_user_company = "user-company"

    def get_user(self):
        return self.api_client.get(self.endpoint_user).json()["Response"]

    def get_user_person_by_id(self, user_id):
        endpoint = "%s/%d" % (self.endpoint_user_person, user_id)
        return self.api_client.get(endpoint).json()["Response"]

    def get_user_company_by_id(self, user_id):
        endpoint = "%s/%d" % (self.endpoint_user_company, user_id)
        return self.api_client.get(endpoint).json()["Response"]

