class Payment:
    def __init__(self, amount, counterparty_alias, description):
        """A model object for the payment endpoint

        :param amount: Double, the amount of the payment (per default in EUR)
        :param counterparty_alias: CounterpartyAlias object
        :param description: String, not more than 140 characters
        :param attachment: Optional, Array of Attachment IDs
        """
        self.amount = {
            'value': str(amount),
            'currency': 'EUR'
        }
        self.counterparty_alias = counterparty_alias.__dict__
        self.description = description

    def set_attachment(self, attachment_ids):
        """Adds attachment ids to the payment object

        :param attachment_ids: Array of Integers, the IDs of the attachments
        """
        self.attachment = []
        for id in attachment_ids:
            self.attachment.append({'id': id})

    # TODO: Check that description is not more than 140 characters