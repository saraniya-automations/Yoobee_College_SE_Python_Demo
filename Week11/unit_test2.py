import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    

    def test_addition(self):
        """Test addition method of Calculator - two positive integers"""
        self.assertEqual(self.calc.add(2, 3), 5)
        """Test addition method of Calculator - two negetive integers"""
        self.assertEqual(self.calc.add(-1, -1), -2)
        """Test addition method of Calculator - one positive and one negative integers"""
        self.assertAlmostEqual(self.calc.add(2, -1), 1)
        """Test addition method of Calculator - two floating point numbers"""
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)
    
    def test_subtraction(self):
        """Test subtraction method of Calculator - two positive integers"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        """Test subtraction method of Calculator - two negetive integers"""
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        """Test subtraction method of Calculator - one positive and one negative integers"""
        self.assertAlmostEqual(self.calc.subtract(2, -1), 3)
        """Test subtraction method of Calculator - two floating point numbers"""
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_multiplication(self):
        """Test multiplication method of Calculator - two positive integers"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        """Test multiplication method of Calculator - two negetive integers"""
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        """Test multiplication method of Calculator - one positive and one negative integers"""
        self.assertEqual(self.calc.multiply(2, -3), -6)
        """Test multiplication method of Calculator - two floating point numbers"""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)

    def test_division(self):
        """Test division method of Calculator - two positive integers"""
        self.assertEqual(self.calc.divide(6, 3), 2)
        """Test division method of Calculator - two negetive integers"""
        self.assertEqual(self.calc.divide(-6, -3), 2)
        """Test division method of Calculator - one positive and one negative integers"""
        self.assertEqual(self.calc.divide(6, -3), -2)
        """Test division method of Calculator - two floating point numbers"""
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        """Test division by zero raises ValueError"""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        """Test power method of Calculator - positive base and exponent"""
        self.assertAlmostEqual(self.calc.power(2, 3), 8)
        """Test power method of Calculator - negative base and even exponent"""
        self.assertAlmostEqual(self.calc.power(-2, 2), 4)
        """Test power method of Calculator - negative base and odd exponent"""
        self.assertAlmostEqual(self.calc.power(-2, 3), -8)
        """Test power method of Calculator - floating point base and exponent"""
        self.assertAlmostEqual(self.calc.power(2.5, 2), 6.25)

    def test_root(self):
        """Test root method of Calculator - square root of positive number"""
        self.assertAlmostEqual(self.calc.root(4), 2)
        """Test root method of Calculator - cube root of positive number"""
        self.assertAlmostEqual(self.calc.root(8, 3), 2)
        """Test root method of Calculator - square root of negative number raises ValueError"""
        with self.assertRaises(ValueError):
            self.calc.root(-4)
        """Test root method of Calculator - nth root of negative number with odd n"""
        self.assertAlmostEqual(self.calc.root(-27, 3), -3)

    def test_sine(self):
        """Test sine method of Calculator - sine of 0 degrees"""
        self.assertAlmostEqual(self.calc.sin(0), 0)
        """Test sine method of Calculator - sine of 90 degrees"""
        self.assertAlmostEqual(self.calc.sin(90), 1)
        """Test sine method of Calculator - sine of 180 degrees"""
        self.assertAlmostEqual(self.calc.sin(180), 0)
        """Test sine method of Calculator - sine of 270 degrees"""
        self.assertAlmostEqual(self.calc.sin(270), -1)

    def test_cosine(self):
        """Test cosine method of Calculator - cosine of 0 degrees"""
        self.assertAlmostEqual(self.calc.cos(0), 1)
        """Test cosine method of Calculator - cosine of 90 degrees"""
        self.assertAlmostEqual(self.calc.cos(90), 0)
        """Test cosine method of Calculator - cosine of 180 degrees"""
        self.assertAlmostEqual(self.calc.cos(180), -1)
        """Test cosine method of Calculator - cosine of 270 degrees"""
        self.assertAlmostEqual(self.calc.cos(270), 0)

    def test_tangent(self):
        """Test tangent method of Calculator - tangent of 0 degrees"""
        self.assertAlmostEqual(self.calc.tan(0), 0)
        """Test tangent method of Calculator - tangent of 45 degrees"""
        self.assertAlmostEqual(self.calc.tan(45), 1)
        """Test tangent method of Calculator - tangent of 90 degrees raises ValueError"""
        with self.assertRaises(ValueError):
            self.calc.tan(90)
        """Test tangent method of Calculator - tangent of 180 degrees"""
        self.assertAlmostEqual(self.calc.tan(180), 0)

    def test_tangent_undefined(self):
        """Test tangent method of Calculator - tangent of 90 degrees raises ValueError"""
        with self.assertRaises(ValueError):
            self.calc.tan(90)
        """Test tangent method of Calculator - tangent of 270 degrees raises ValueError"""
        with self.assertRaises(ValueError):
            self.calc.tan(270)

    

if __name__ == '__main__':
    unittest.main()