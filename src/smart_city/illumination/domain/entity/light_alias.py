class LightAlias:
    def __init__(self, alias: str):
        self.alias = alias

    def __eq__(self, other):
        return isinstance(other, LightAlias) and other.alias == self.alias

    def __str__(self):
        return self.alias
