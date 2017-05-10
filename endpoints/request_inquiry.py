from endpoints.endpoint import Endpoint


class RequestInquiry(Endpoint):

    def get_base_endpoint(self, user_id, account_id):
        return "%s/%d/%s/%d" % (
            self.endpoint_user,
            user_id,
            self.endpoint_monetary_account,
            account_id
        )

    # Request Inquiry Logic
    def get_all_inquiries_for_monetary_account(self, user_id, account_id):
        endpoint = self.get_base_endpoint(user_id, account_id)
        endpoint += "/%s" % self.endpoint_request_inquiry

        return self.make_get_request(endpoint)

    def get_request_inquiry_by_id(self, user_id, account_id, request_id):
        endpoint = self.get_base_endpoint(user_id, account_id)
        endpoint += "/%s/%d" % (self.endpoint_request_inquiry, request_id)

        return self.make_get_request(endpoint)

    # Request Inquiry Batch Logic
    def get_all_batch_inquiries_for_monetary_account(self, user_id,
                                                     account_id):
        endpoint = self.get_base_endpoint(user_id, account_id)
        endpoint += "/%s" % self.endpoint_payment_batch

        return self.make_get_request(endpoint)

    def get_batch_inquiry_by_id(self, user_id, account_id, inquiry_id):
        endpoint = self.get_base_endpoint(user_id, account_id)
        endpoint += "/%s/%d" % (self.endpoint_payment_batch, inquiry_id)

        return self.make_get_request(endpoint)

    # Request Response Logic
    def get_all_request_responses_for_monetary_account(self, user_id,
                                                       account_id):
        endpoint = self.get_base_endpoint(user_id, account_id)
        endpoint += "/%s" % self.endpoint_payment_response

        return self.make_get_request(endpoint)

    def get_request_response_by_id(self, user_id, account_id, response_id):
        endpoint = self.get_base_endpoint(user_id, account_id)
        endpoint += "/%s/%d" % (self.endpoint_payment_response, response_id)

        return self.make_get_request(endpoint)
