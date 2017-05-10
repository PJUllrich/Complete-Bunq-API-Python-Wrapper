from endpoints.endpoint import Endpoint


class Card(Endpoint):

    def get_card_for_user_all(self, user_id):
        endpoint = "%s/%d/%s" % (
            self.endpoint_user,
            user_id,
            self.endpoint_card
        )
        res = self.api_client.get(endpoint)
        return res.json()["Response"]

    def get_card_for_user_by_id(self, user_id, card_id):
        endpoint = "%s/%d/%s/%d" % (
            self.endpoint_user,
            user_id,
            self.endpoint_card,
            card_id
        )
        res = self.api_client.get(endpoint)
        return res.json()["Response"]
