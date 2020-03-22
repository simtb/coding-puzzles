import unittest
from challenges.stock_prices import solution
from typing import List

class TestSolution(unittest.TestCase):

    def test_no_stocks(self):
        test_stocks: List[int] = []
        actual_output: int = solution(test_stocks)
        expected_output: None = None
        self.assertEqual(actual_output, expected_output)
    
    def test_one_stock(self):
        test_stocks: List[int] = [10]
        actual_output: int = solution(test_stocks)
        expected_output: int = 10
        self.assertEqual(actual_output, expected_output)
    
    def test_strictly_increasing(self):
        test_stocks: List[int] = [1, 2, 3, 4, 5]
        actual_output: int = solution(test_stocks)
        expected_output: int = 4
        self.assertEqual(actual_output, expected_output)
    
    def test_strictly_decreasing(self):
        test_stocks: List[int] = [5, 4, 3, 2, 1]
        actual_output: int = solution(test_stocks)
        expected_output: int = 0
        self.assertEqual(actual_output, expected_output)

    def test_all_same(self):
        test_stocks: List[int] = [10, 10, 10, 10, 10]
        actual_output: int = solution(test_stocks)
        expected_output: int = 0
        self.assertEqual(actual_output, expected_output)
    
    def test_example_1(self):
        test_stocks: List[int] = [10, 10, 11, 10, 10]
        actual_output: int = solution(test_stocks)
        expected_output: int = 1
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        test_stocks: List[int] = [10, 10, 11, 10, 12]
        actual_output: int = solution(test_stocks)
        expected_output: int = 2
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        test_stocks: List[int] = [9, 11, 8, 5, 7, 10]
        actual_output: int = solution(test_stocks)
        expected_output: int = 5
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()