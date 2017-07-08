class CounterPartyAlias:
    def __init__(self, type, value, name=None):
        if type == 'IBAN' and name is None:
            print('Error: IBAN payment created but no name was given.')

        self.type = type
        self.value = value
        if name is not None:
            self.name = name
