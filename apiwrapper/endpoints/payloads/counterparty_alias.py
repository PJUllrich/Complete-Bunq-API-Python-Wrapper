class CounterPartyAlias:
    def __init__(self, type, value, name=None):
        self.type = type
        self.value = value
        if name is not None:
            self.name = name
