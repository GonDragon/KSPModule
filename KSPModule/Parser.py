import re


class Parser:
    """
    Parser for the CFG files.
    """

    def __init__(self, raw):
        self.raw = raw
        self._remove_comments()

    def _remove_comments(self):
        lines = self.raw.split('\n')
        lines = list(map(lambda string: re.sub(
            re.compile("//.*"), "", string).rstrip(), lines))
        while '' in lines:
            lines.remove('')
        self.raw = '\n'.join(lines)
