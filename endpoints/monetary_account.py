from endpoints.endpoint import Endpoint


class MonetaryBankEndpoint(Endpoint):

    def __get_base_endpoint(self, user_id):
        return "%s/%d" % (
            self.endpoint_user,
            user_id
        )

    # Monetary Account Logic
    def get_all_monetary_accounts_for_user(self, user_id):
        endpoint = self.__get_base_endpoint(user_id)
        endpoint += "/%s" % self.endpoint_monetary_account

        return self.__make_get_request(endpoint)

    def get_monetary_account_by_id(self, user_id, account_id):
        endpoint = self.__get_base_endpoint(user_id)
        endpoint += "/%s/%d" % (self.endpoint_monetary_account, account_id)

        return self.__make_get_request(endpoint)

    # Monetary Account Bank Logic
    def get_all_monetary_account_banks_for_user(self, user_id):
        endpoint = self.__get_base_endpoint(user_id)
        endpoint += "/%s" % self.endpoint_monetary_account_bank

        return self.__make_get_request(endpoint)

    def get_monetary_account_bank_by_id(self, user_id, account_id):
        endpoint = self.__get_base_endpoint(user_id)
        endpoint += "/%s/%d" % (self.endpoint_monetary_account_bank, account_id)

        return self.__make_get_request(endpoint)
