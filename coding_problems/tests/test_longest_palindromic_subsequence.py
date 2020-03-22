import unittest
from problems.longest_palindromic_subsequence import solution

class TestSolution(unittest.TestCase):
    def test_empty_string(self):
        test_string: str = ""
        start_index: int = 0
        end_index: int = 0
        output: int = solution(test_string, start_index, end_index)
        self.assertEqual(output, 0)
    
    def test_example(self):
        test_string: str = "ABBDCACB"
        start_index: int = 0
        end_index: int = 7
        output: int = solution(test_string, start_index, end_index)
        self.assertEqual(output, 5)
    
    def test_palindrome(self):
        test_string: str = "RADAR"
        start_index: int = 0
        end_index: int = 4
        output: int = solution(test_string, start_index, end_index)
        self.assertEqual(output, 5)

    def test_all_different(self):
        test_string: str = "ABCDE"
        start_index: int = 0
        end_index: int = 4
        output: int = solution(test_string, start_index, end_index)
        self.assertEqual(output, 1)
    
    def test_example_1(self):
        test_string: str = "AECFA"
        start_index: int = 0
        end_index: int = 4
        output: int = solution(test_string, start_index, end_index)
        self.assertEqual(output, 3)


if __name__ == "__main__":
    unittest.main()


