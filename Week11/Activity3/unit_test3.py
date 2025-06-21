import  unittest

class TestStringMethods(unittest.TestCase):

    # checks if upper() method converts lowercase string 'foo' to uppercase 'FOO'.
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_isupper(self):
        # checks if all characters are uppercase then returns true.
        self.assertTrue('FOO'.isupper())
        # if characters are in mixed case then returns false.
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        # splits the string 'hello world' into a list of words.
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            # this will raise a TypeError because the separator is an integer
            s.split(2)

    def test_isdigit(self):
        self.assertTrue('123'.isdigit())  # Checks if '123' is a digit
        self.assertFalse('abc'.isdigit()) # Checks if 'abc' is not a digit


if __name__ == '__main__':
    unittest.main()