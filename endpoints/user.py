from endpoints.endpoint import Endpoint


class UserEndpoint(Endpoint):

    endpoint_user = "user"
    endpoint_user_person = "user-person"
    endpoint_user_company = "user-company"

    def get_user(self):
        res = self.api_client.get(self.endpoint_user)
        return res.json()["Response"]

    def get_user_person_by_id(self, user_id):
        endpoint = "%s/%d" % (self.endpoint_user_person, user_id)
        res = self.api_client.get(endpoint)
        return res.json()["Response"]

    def get_user_company_by_id(self, user_id):
        endpoint = "%s/%d" % (self.endpoint_user_company, user_id)
        res = self.api_client.get(endpoint)
        return res.json()["Response"]

