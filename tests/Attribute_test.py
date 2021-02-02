import unittest

from KSPModule.Module import Attribute


class AttributeTestCase(unittest.TestCase):

    def setUp(self):
        self.attribute = Attribute('Key', 'Value')

    def test_equals(self):
        equal = Attribute('Key', 'Value')
        not_equal_key = Attribute('Other Key', 'Value')
        not_equal_value = Attribute('Key', 'Other Value')
        not_equal = Attribute('Other Key', 'Other Value')

        self.assertEqual(self.attribute, equal)
        self.assertNotEqual(self.attribute, not_equal_key)
        self.assertNotEqual(self.attribute, not_equal_value)
        self.assertNotEqual(self.attribute, not_equal)
