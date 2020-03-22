import unittest
from problems.longest_common_subsequence import solution, solution_2

class TestSolution(unittest.TestCase):

    def test_empty_string(self):
        test_string_1: str = ""
        test_string_2: str = ""
        length_string_1: int = 0
        length_string_2: int = 0
        output: int = solution(test_string_1, test_string_2, length_string_1, length_string_2)
        self.assertEqual(output, 0)
    
    def test_example_test_string(self):
        test_string_1: str = "ABCBDAB"
        test_string_2: str = "BDCABA"
        length_string_1: int = 7
        length_string_2: int = 6
        output: int = solution(test_string_1, test_string_2, length_string_1, length_string_2)
        self.assertEqual(output, 4)
    
    def test_same_test_strings(self):
        test_string_1: str = "FOO"
        test_string_2: str = "FOO"
        length_string_1: int = 3
        length_string_2: int = 3
        output: int = solution(test_string_1, test_string_2, length_string_1, length_string_2)
        self.assertEqual(output, 3)
    
    def test_different_test_strings(self):
        test_string_1: str = "BAR"
        test_string_2: str = "FOO"
        length_string_1: int = 3
        length_string_2: int = 3
        output: int = solution(test_string_1, test_string_2, length_string_1, length_string_2)
        self.assertEqual(output, 0)

class TestSolution2(unittest.TestCase):

    def test_empty_string(self):
        test_string_1: str = ""
        test_string_2: str = ""
        length_string_1: int = 0
        length_string_2: int = 0
        output: int = solution_2(test_string_1, test_string_2, length_string_1, length_string_2, {})
        self.assertEqual(output, 0)
    
    def test_example_test_string(self):
        test_string_1: str = "ABCBDAB"
        test_string_2: str = "BDCABA"
        length_string_1: int = 7
        length_string_2: int = 6
        output: int = solution_2(test_string_1, test_string_2, length_string_1, length_string_2, {})
        self.assertEqual(output, 4)
    
    def test_same_test_strings(self):
        test_string_1: str = "FOO"
        test_string_2: str = "FOO"
        length_string_1: int = 3
        length_string_2: int = 3
        output: int = solution_2(test_string_1, test_string_2, length_string_1, length_string_2, {})
        self.assertEqual(output, 3)
    
    def test_different_test_strings(self):
        test_string_1: str = "BAR"
        test_string_2: str = "FOO"
        length_string_1: int = 3
        length_string_2: int = 3
        output: int = solution_2(test_string_1, test_string_2, length_string_1, length_string_2, {})
        self.assertEqual(output, 0)


if __name__ == "__main__":
    unittest.main()