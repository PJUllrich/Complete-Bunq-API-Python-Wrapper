from endpoints.endpoint import Endpoint


class MonetaryBankEndpoint(Endpoint):

    def get_monetary_account_for_user_all(self, user_id):
        endpoint = "%s/%d/%s" % (
            self.endpoint_user,
            user_id,
            self.endpoint_monetary_account
        )
        res = self.api_client.get(endpoint)
        return res.json()["Response"]

    def get_monetary_account_for_user_by_id(self, user_id, account_id):
        endpoint = "%s/%d/%s/%d" % (
            self.endpoint_user,
            user_id,
            self.endpoint_monetary_account,
            account_id
        )
        res = self.api_client.get(endpoint)
        return res.json()["Response"]

    def get_monetary_account_bank_for_user_all(self, user_id):
        endpoint = "%s/%d/%s" % (
            self.endpoint_user,
            user_id,
            self.endpoint_monetary_account_bank
        )
        res = self.api_client.get(endpoint)
        return res.json()["Response"]

    def get_monetary_account_bank_for_user_by_id(self, user_id, account_id):
        endpoint = "%s/%d/%s/%d" % (
            self.endpoint_user,
            user_id,
            self.endpoint_monetary_account_bank,
            account_id
        )
        res = self.api_client.get(endpoint)
        return res.json()["Response"]
