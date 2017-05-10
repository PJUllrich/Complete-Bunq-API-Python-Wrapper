from endpoints.endpoint import Endpoint


class Payment(Endpoint):

    def get_base_endpoint(self, user_id, account_id):
        return "%s/%d/%s/%d" % (
            self.endpoint_user,
            user_id,
            self.endpoint_monetary_account,
            account_id
        )

    # Payment Logic
    def get_all_payments_for_monetary_account(self, user_id, account_id):
        endpoint = self.get_base_endpoint(user_id, account_id)
        endpoint += "/%s" % self.endpoint_payment

        return self.make_get_request(endpoint)

    def get_payment_by_id(self, user_id, account_id, payment_id):
        endpoint = self.get_base_endpoint(user_id, account_id)
        endpoint += "/%s/%d" % (self.endpoint_payment, payment_id)

        return self.make_get_request(endpoint)

    # Payment Batch Logic
    def get_all_payments_batches_for_monetary_account(self, user_id,
                                                      account_id):
        endpoint = self.get_base_endpoint(user_id, account_id)
        endpoint += "/%s" % self.endpoint_payment_batch

        return self.make_get_request(endpoint)

    def get_payment_batch_by_id(self, user_id, account_id, batch_id):
        endpoint = self.get_base_endpoint(user_id, account_id)
        endpoint += "/%s/%d" % (self.endpoint_payment_batch, batch_id)

        return self.make_get_request(endpoint)
