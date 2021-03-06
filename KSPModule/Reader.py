import re
from io import IOBase
from KSPModule.Module import Module
from KSPModule.Token import Tokenizer, Token


class Reader:
    """
    Reader for the CFG files.
    Receive an String, or an Open file to read.
    """

    def __init__(self, file):
        if isinstance(file, str):
            lines = file.split('\n')
        elif issubclass(type(file), IOBase):
            lines = file.readlines()
        else:
            raise TypeError

        tokenizer = Tokenizer()
        self.modules = []  # List of modules on the base file
        self.loose_attributes = []  # List of all the loose attributes on the base file

        for line in lines:
            line = self._remove_comments(line)
            if line == '':
                continue
            tokenizer.analize(line)

        tokens = tokenizer.getTokens()
        module_stack = []  # Stack of nested modules

        while len(tokens) > 0:
            currentt = tokens.pop(0)
            try:
                nextt = tokens[0]
            except IndexError:
                nextt = None

            if currentt.type is Token.PAIR:
                key, value = currentt.value
                if len(module_stack) == 0:
                    self.loose_attributes.append((key, value))
                else:
                    module_stack[-1].add_attribute(key, value)
            elif currentt.type is Token.NAME:
                if nextt and nextt.type is Token.OPENER:
                    tokens.pop(0)
                    module_stack.append(Module(currentt.value))
                else:
                    print('Ignoring line. Attribute without value or Empty module found: {}'.format(
                        currentt.value))
            elif currentt.type is Token.CLOSER:
                if len(module_stack) == 1:
                    self.modules.append(module_stack.pop())
                elif len(module_stack) > 1:
                    closed_module = module_stack.pop()
                    module_stack[-1].add_module(closed_module)
                else:
                    # Unbalanced brackets error
                    raise UnbalancedBracketsError(
                        'Closing an unexistent module')

        if len(module_stack) > 0:
            # Unbalanced brackets error
            raise UnbalancedBracketsError('Modules left open')
        self.n = 0

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self) -> Module:
        if self.n < len(self.modules):
            result = self.modules[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def _remove_comments(self, text: str):
        return re.sub(re.compile("//.*"), "", text).strip()

    def get_modules(self):
        """
        Returns a list containing all the base modules.
        """
        return self.modules.copy()

    def get_attributes(self):
        """
        Returns a list containing all the loose attributes.
        """
        return self.loose_attributes.copy()


class UnbalancedBracketsError(BaseException):
    """
    Exception that occurs when the parsed code has unbalanced brackets.
    """
    pass
