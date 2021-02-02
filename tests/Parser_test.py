import unittest

from KSPModule.Parser import Parser


class ParserTestCase(unittest.TestCase):

    def setUp(self):
        self.commented = Parser("//This is an example\n" +
                                "MODULE //This is the module type\n" +
                                "{\n" +
                                "  name = somename //This is the module name\n" +
                                "}")

    def test_deleteComments(self):
        uncommented = Parser("MODULE\n" +
                             "{\n" +
                             "  name = somename\n" +
                             "}")
        self.assertEqual(self.commented.raw, uncommented.raw)
