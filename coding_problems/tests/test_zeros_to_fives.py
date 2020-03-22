import unittest
from problems.zeros_to_fives import solution 

class TestSolution(unittest.TestCase):
    def test_single_zero(self):
        test_number: int = 0
        output: int = solution(test_number)
        self.assertEqual(output, 5)
    
    def test_example_1(self):
        test_number: int = 102
        output: int = solution(test_number)
        self.assertEqual(output, 152)
    
    def test_example_2(self):
        test_number: int = 1020
        output: int = solution(test_number)
        self.assertEqual(output, 1525)


if __name__ == "__main__":
    unittest.main()