import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        # primeiro teste de assertEqual
        self.assertEqual('teste'.upper(), 'TESTE')

    def test_lower(self):
        # primeiro teste de assertNotEqual
        self.assertNotEqual('teste'.lower(), 'TESTE')

    def test_isupper(self):
        # teste de assertTrue e assertFalse
        self.assertTrue('TESTE'.isupper())
        self.assertFalse('Teste'.isupper())

    def test_is(self):
        a = "a"
        b = "abc"
        self.assertIs(a, a)
        self.assertIsNot(a, b)
        self.assertIn(a, b)


if __name__ == '__main__':
    unittest.main()