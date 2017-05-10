from endpoints.endpoint import Endpoint


class UserEndpoint(Endpoint):

    def get_logged_in_user(self):
        return self.make_get_request(self.endpoint_user)

    def get_user_person_by_id(self, user_id):
        endpoint = "%s/%d" % (self.endpoint_user_person, user_id)

        return self.make_get_request(endpoint)

    def get_user_company_by_id(self, user_id):
        endpoint = "%s/%d" % (self.endpoint_user_company, user_id)

        return self.make_get_request(endpoint)

