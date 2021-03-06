from apiwrapper.endpoints.endpoint import Endpoint
from apiwrapper.endpoints.monetary_account import MonetaryAccount


class ScheduledPayment(Endpoint):

    __endpoint_schedule_payment = "schedule-payment"

    @classmethod
    def _get_base_endpoint(cls, user_id, account_id, payment_id=None):
        endpoint = MonetaryAccount._get_base_endpoint(user_id, account_id)
        endpoint += "/%s" % cls.__endpoint_schedule_payment
        if payment_id is not None:
            endpoint += "/%d" % payment_id
        return endpoint

    def get_all_scheduled_payments_for_account(self, user_id, account_id):
        endpoint = self._get_base_endpoint(user_id, account_id)

        return self._make_get_request(endpoint)

    def get_scheduled_payment_by_id(self, user_id, account_id, payment_id):
        endpoint = self._get_base_endpoint(user_id, account_id, payment_id)

        return self._make_get_request(endpoint)
