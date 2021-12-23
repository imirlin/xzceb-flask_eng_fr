import unittest

from translator import englishToFrench, frenchToEnglish


class TestE2F(unittest.TestCase):
    # Test for null input
    def testNoneE2F(self):
        self.assertIsNotNone(englishToFrench(None))

    # Test for the translation of the world 'Hello' and 'Bonjour'.
    def testHello(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')


class TestF2E(unittest.TestCase):
    # Test for null input
    def testNoneF2E(self):
        self.assertIsNotNone(frenchToEnglish(None))

    # Test for the translation of the world 'Bonjour' and 'Hello'.
    def testBonjour(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')


unittest.main()
