import unittest
from challenges.divide import divide

class TestDivide(unittest.TestCase):
    def test_1(self):
        n: int = 10
        m: int = 3
        expected: tuple = (3, 1)
        actual: tuple = divide(n, m)
        self.assertEqual(expected, actual)
    
    def test_2(self):
        n: int = 100
        m: int = 6
        expected: tuple = (16, 4)
        actual: tuple = divide(n, m)
        self.assertEqual(expected, actual)
    
    def test_3(self):
        n: int = 100
        m: int = 20
        expected: tuple = (5, 0)
        actual: tuple = divide(n, m)
        self.assertEqual(expected, actual)
    
    def test_4(self):
        n: int = 100
        m: int = 0
        expected: tuple = (float('+inf'), 0)
        actual: tuple = divide(n, m)
        self.assertEqual(expected, actual)
    
    def test_4(self):
        n: int = 1
        m: int = 5
        expected: tuple = (0, 1)
        actual: tuple = divide(n, m)
        self.assertEqual(expected, actual)





if __name__ == '__main__':
    unittest.main()