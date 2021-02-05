import re
from KSPModule.Module import Module

# This case match closing modules without modules inside.
# Group 1: Attributes of the current Module
# Group 2: Continue of the rawstring outside the current Module
REG_CLOSE = re.compile(
    r'([^\{\}]*)\}\s*(.*)', flags=re.DOTALL)

# This case match opening modules
# Group 1: Attributes of the current Module
# Group 2: Type of a new opening module
# Group 3: Rawstring beyond the new opening module
REG_OPEN = re.compile(
    r'((?:\s*\w*\s*=\s*\w*)*)\s*([A-Z]+)\s*\{\s*(.*)', flags=re.DOTALL)

# This case match attributes
# Group 1: Key
# Group 2: Value
REG_ATTR = re.compile(
    r'(\w+)\s*=\s*(\w+)', flags=re.DOTALL)

# This case match emptiness
REG_EMPTY = re.compile(
    r'^\s*$', flags=re.DOTALL)


class Reader:
    """
    Reader for the CFG files.
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

    def _get_content(self, module: Module, raw: str):

        raw_attributes = ''
        current_raw = raw

        while not re.match(REG_CLOSE, current_raw):
            if re.match(REG_EMPTY, current_raw):
                return ''

            more_attr, module_type, current_raw = re.match(
                REG_OPEN, current_raw).groups()
            raw_attributes += more_attr
            new_module = Module(module_type)
            current_raw = self._get_content(new_module, current_raw)
            module.add_module(new_module)

        last_attr, raw_continue = re.match(REG_CLOSE, current_raw).groups()
        raw_attributes += last_attr

        for k, v in self._attr_from_raw(raw_attributes):
            module.add_attribute(k, v)

        return raw_continue

    def _attr_from_raw(self, rawattr: str):

        return re.findall(REG_ATTR, rawattr)

    def get_modules(self):
        """
        Returns a list containing all the base modules.
        """
        module_container = Module()
        self._get_content(module_container, self.raw)
        return module_container.get_modules()
