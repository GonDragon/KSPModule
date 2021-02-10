import unittest

from KSPModule.Token import Tokenizer, Token


class TokenizerTestCase(unittest.TestCase):

    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_tokenIsPair(self):
        testString1 = 'foo = bar'
        testString2 = 'foo = 123'
        testString3 = 'foo = 1.0'
        testString4 = 'foo = 1, 1.0, 3'
        self.tokenizer.analize(testString1)
        self.tokenizer.analize(testString2)
        self.tokenizer.analize(testString3)
        self.tokenizer.analize(testString4)
        tokens = self.tokenizer.getTokens()
        for token in tokens:
            self.assertIs(token.type, Token.PAIR)

    def test_tokenRecoverPair(self):
        testString = 'foo = bar'
        self.tokenizer.analize(testString)
        tokens = self.tokenizer.getTokens()
        self.assertIs(tokens[0].type, Token.PAIR)
        k, v = tokens[0].value
        self.assertEqual(k, 'foo')
        self.assertEqual(v, 'bar')

    def test_tokenIsName(self):
        testString = 'FOOBAR'
        self.tokenizer.analize(testString)
        tokens = self.tokenizer.getTokens()
        self.assertIs(tokens[0].type, Token.NAME)

    def test_tokenIsOpener(self):
        testString = '{'
        self.tokenizer.analize(testString)
        tokens = self.tokenizer.getTokens()
        self.assertIs(tokens[0].type, Token.OPENER)

    def test_tokenIsCloser(self):
        testString = '}'
        self.tokenizer.analize(testString)
        tokens = self.tokenizer.getTokens()
        self.assertIs(tokens[0].type, Token.CLOSER)
