from endpoints.endpoint import Endpoint


class MonetaryBankEndpoint(Endpoint):

    endpoint_monetary_account = "monetary-account"
    endpoint_monetary_account_bank = "monetary-account-bank"

    def get_monetary_account_for_user_all(self, user_id):
        endpoint = "user/%d/%s" % (user_id, self.endpoint_monetary_account)
        res = self.api_client.get(endpoint)
        return res.json()["Response"]

    def get_monetary_account_for_user_by_id(self, user_id, account_id):
        endpoint = "user/%d/%s/%d" % \
                   (user_id, self.endpoint_monetary_account, account_id)
        res = self.api_client.get(endpoint)
        return res.json()["Response"]

    def get_monetary_account_bank_for_user_all(self, user_id):
        endpoint = "user/%d/%s" % \
                   (user_id, self.endpoint_monetary_account_bank)
        res = self.api_client.get(endpoint)
        return res.json()["Response"]

    def get_monetary_account_bank_for_user_by_id(self, user_id, account_id):
        endpoint = "user/%d/%s/%d" % \
                   (user_id, self.endpoint_monetary_account_bank, account_id)
        res = self.api_client.get(endpoint)
        return res.json()["Response"]
