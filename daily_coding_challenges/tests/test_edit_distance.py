import unittest
from challenges.edit_distance import solution

class TestSolution(unittest.TestCase):
    def test_two_empty_strings(self):
        test_string_1: str = ""
        test_string_2: str = ""
        output: int = solution(test_string_1, test_string_2)
        self.assertEqual(output, 0)
    
    def test_one_empty_string(self):
        test_string_1: str = ""
        test_string_2: str = "foo"
        output: int = solution(test_string_1, test_string_2)
        self.assertEqual(output, 3)
    
    def test_one_empty_string_2(self):
        test_string_1: str = "bar"
        test_string_2: str = ""
        output: int = solution(test_string_1, test_string_2)
        self.assertEqual(output, 3)
    
    def test_same_strings(self):
        test_string_1: str = "bar"
        test_string_2: str = "bar"
        output: int = solution(test_string_1, test_string_2)
        self.assertEqual(output, 0)
    
    def test_anagram(self):
        test_string_1: str = "earth"
        test_string_2: str = "heart"
        output: int = solution(test_string_1, test_string_2)
        self.assertEqual(output, 0)
    
    def test_plural(self):
        test_string_1: str = "foos"
        test_string_2: str = "foo"
        output: int = solution(test_string_1, test_string_2)
        self.assertEqual(output, 1)


if __name__ == "__main__":
    unittest.main()