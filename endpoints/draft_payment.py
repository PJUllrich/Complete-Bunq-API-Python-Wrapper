from endpoints.endpoint import Endpoint


class DraftPayment(Endpoint):

    def __get_base_endpoint(self, user_id, account_id):
        return "%s/%d/%s/%d/%s" % (
            self.endpoint_user,
            user_id,
            self.endpoint_monetary_account,
            account_id,
            self.endpoint_draft_payment
        )

    def get_all_draft_payments_for_monetary_account(self, user_id, account_id):
        endpoint = self.__get_base_endpoint(user_id, account_id)

        return self.__make_get_request(endpoint)

    def get_draft_payment_by_id(self, user_id, account_id, draft_id):
        endpoint = self.__get_base_endpoint(user_id, account_id)
        endpoint += "/%d" % draft_id

        return self.__make_get_request(endpoint)
