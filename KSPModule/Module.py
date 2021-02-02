class Module:
    """
    Represents a module from a CFG file. A module may contain
    attributes, or other modules.
    """

    def __init__(self, type: str = 'MODULE'):
        self.type = type
        self.content = []

    def add_attribute(self, key: str, value: str):
        """
        Add a new attribute to the module. The attribute must be
        a pair key-value of strings.
        One Module can host multiple attributes with the same name.
        """
        self.content.append(Attribute(key, value))

    def get_attribute(self, key: str, n: int = 1):
        """
        Return the value of an Attribute with certain key. If there
        are multiple attributes with the same key, you can specify,
        in order, wich one do you want (n).
        By default, it returns the first one (n=1).
        """
        i = 1
        for obj in self.content:
            if type(obj) is Attribute and obj.key == key:
                if n == i:
                    return obj.value
                i += 1

        if i > 1:
            raise IndexError(
                'The attribute "{0}" does not have that many occurrences.'.format(key))
        raise KeyError(
            'The module does not contain the attribute "{0}".'.format(key))


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
