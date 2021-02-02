import unittest

from KSPModule.Parser import Parser


class ParserTestCase(unittest.TestCase):

    def loadCFG(self, file: str):
        with open('tests/input/{0}.cfg'.format(file), 'r', errors='ignore') as cfgFile:
            return Parser(''.join(cfgFile.readlines()))

    def test_deleteComments(self):
        commented = self.loadCFG('simple')
        uncommented = self.loadCFG('simple_commented')
        self.assertEqual(commented.raw, uncommented.raw)
