import re


# This case match attributes
# Group 1: Key
# Group 2: Value
REG_PAIR = re.compile(r'^(.+)\s*=\s*(.*)$')

REG_NAME = re.compile(r'^\w+$')

REG_NAMEOPENER = re.compile(r'^(\w+)\s*\{$')

REG_OPENER = re.compile(r'^\{$')

REG_CLOSER = re.compile(r'\}')


class Token:
    """
    Saves information about the type and value of a portion of code.
    """

    PAIR = 1
    NAME = 2
    NAMEOPENER = 3
    OPENER = 4
    CLOSER = 5

    UNKNOWN = 6

    def __init__(self, type: int = UNKNOWN, value: object = None):
        self.type = type
        self.value = value


class Tokenizer:
    """
    An object that analizes strings, and store those strings as
    tokens, in the order they are analyzed.
    """

    def __init__(self):
        self.tokens = []
        self.identifiers = [
            (REG_PAIR, Token.PAIR),
            (REG_NAME, Token.NAME),
            (REG_NAMEOPENER, Token.NAMEOPENER),
            (REG_OPENER, Token.OPENER),
            (REG_CLOSER, Token.CLOSER)
        ]

    def getTokens(self) -> list:
        return self.tokens.copy()

    def analize(self, string: str):
        """
        Analize the string, and convert it into a token.
        """
        self.tokens += self._analize(string)

    def _analize(self, string: str) -> Token:
        for identifier in self.identifiers:
            match = re.match(identifier[0], string)
            if match:
                match_type = identifier[1]
                if match_type == Token.PAIR:
                    k, v = match.groups()
                    return [Token(type=Token.PAIR, value=(k.strip(), v.strip()))]
                if match_type == Token.NAME:
                    return [Token(type=Token.NAME, value=string)]
                if match_type == Token.OPENER:
                    return [Token(type=Token.OPENER)]
                if match_type == Token.NAMEOPENER:
                    return [Token(type=Token.NAME, value=string), Token(type=Token.OPENER)]
                if match_type == Token.CLOSER:
                    tokens = []
                    for _ in re.findall(identifier[0], string):
                        tokens.append(Token(type=Token.CLOSER))
                    return tokens
        print('Unknown line found. Ignoring. Value: {}'.format(string))
        return []
