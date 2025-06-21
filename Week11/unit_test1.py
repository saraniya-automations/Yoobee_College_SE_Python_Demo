import unittest

# Unit testing is a way to test individual components of a program to ensure they work as expected. 
# It helps to detect bugs early in the development process and ensures that changes to the code do 
# not break existing functionality.

def add(x,y):
    return x+y

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()


