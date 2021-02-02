class Module:
    """
    Represents a module from a CFG file. A module may contain
    attributes, or other modules.
    """

    def __init__(self, type: str = 'MODULE'):
        self.type = type


class Attribute:
    """
    Represent an attribute of a module. It is always a pair Key -> Value.
    """

    def __init__(self, key: str, value: str):
        """
        Both, key and value from an attribute, are always strings.
        """
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key

    def __eq__(self, other):
        return (self.key == other.key) and (self.value == other.value)

    def __ne__(self, other):
        return not self.__eq__(other)
