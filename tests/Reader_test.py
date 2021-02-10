import unittest

from KSPModule import Reader, UnbalancedBracketsError
from KSPModule import Module


class ReaderTestCase(unittest.TestCase):

    def loadCFG(self, file: str):
        with open('tests/input/{0}.cfg'.format(file), 'r', errors='ignore', encoding='utf-8') as cfgFile:
            return Reader(cfgFile)

    def test_deleteComments(self):
        commented = self.loadCFG('simple')
        uncommented = self.loadCFG('simple_commented')
        self.assertEqual(next(commented), next(uncommented))

    def test_create_one_module(self):
        simple = self.loadCFG('simple')
        modules = simple.get_modules()
        self.assertEqual(len(modules), 1)
        self.assertIsInstance(modules[0], Module)

    def test_create_multiple_modules(self):
        multiple = self.loadCFG('multiple')
        modules = multiple.get_modules()
        self.assertEqual(len(modules), 3)
        for module in modules:
            self.assertIsInstance(module, Module)

    def test_create_one_module_nested(self):
        nested = self.loadCFG('nested')
        modules = nested.get_modules()
        self.assertEqual(len(modules), 1)
        self.assertIsInstance(modules[0], Module)

    def test_create_multiple_modules_nested(self):
        multiple = self.loadCFG('multiple_nested')
        modules = multiple.get_modules()
        self.assertEqual(len(modules), 3)
        for module in modules:
            self.assertIsInstance(module, Module)

    def test_create_one_module_nested_without_spacing(self):
        nested = self.loadCFG('nested_without_spacing')
        modules = nested.get_modules()
        self.assertEqual(len(modules), 1)
        self.assertIsInstance(modules[0], Module)

    def test_create_one_module_nested_double(self):
        nested = self.loadCFG('nested_double')
        modules = nested.get_modules()
        self.assertEqual(len(modules), 1)
        self.assertIsInstance(modules[0], Module)

    def test_works_with_strings(self):
        simple = self.loadCFG('simple')
        modules = simple.get_modules()

        string = str(modules[0])
        new_reader = Reader(string)
        modules = new_reader.get_modules()

        self.assertEqual(len(modules), 1)
        self.assertIsInstance(modules[0], Module)

    def test_unbalanced_brackets(self):
        self.assertRaises(UnbalancedBracketsError,
                          self.loadCFG, 'unbalanced_1')
        self.assertRaises(UnbalancedBracketsError,
                          self.loadCFG, 'unbalanced_2')
