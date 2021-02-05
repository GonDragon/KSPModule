import unittest

from KSPModule.Module import Module


class ModuleTestCase(unittest.TestCase):

    def setUp(self):
        self.empty_module = Module()

    def test_save_attribute(self):
        self.empty_module.add_attribute('foo', 'bar')

        self.assertEqual(self.empty_module.get_attribute('foo'), 'bar')

    def test_save_multiple_attribute(self):
        self.empty_module.add_attribute('foo', 'bar')
        self.empty_module.add_attribute('foo', 'bar')
        self.empty_module.add_attribute('foo', 'bar')
        self.empty_module.add_attribute('foo', 'bar')
        self.empty_module.add_attribute('bar', 'bar')

        self.assertEqual(self.empty_module.get_attribute('bar'), 'bar')

    def test_save_multiple_attribute_index(self):
        self.empty_module.add_attribute('foo', '1')
        self.empty_module.add_attribute('foo', '2')
        self.empty_module.add_attribute('bar', 'bar')
        self.empty_module.add_attribute('foo', '3')
        self.empty_module.add_attribute('foo', '4')
        self.empty_module.add_attribute('bar', 'bar')

        self.assertEqual(self.empty_module.get_attribute('foo', 3), '3')

    def test_module_saved(self):
        new_module = Module()
        new_module.add_module(self.empty_module)

        self.assertIn(self.empty_module, new_module.get_modules())

    def test_has_attribute(self):
        self.empty_module.add_attribute('foo', 'bar')

        self.assertTrue(self.empty_module.has_attribute('foo'))
        self.assertFalse(self.empty_module.has_attribute('bar'))
