import unittest
from challenges.run_length_encoding import solution 

class TestSolution(unittest.TestCase):

    def test_empty_string(self):
        test_string: str = ""
        output: str = solution(test_string)
        self.assertEqual(output, "")
    
    def test_one_letter(self):
        test_string: str = "A"
        output: str = solution(test_string)
        self.assertEqual(output, "1A")

    def test_same_letters(self):
        test_string: str = "AAAAAAAAAA"
        output = solution(test_string)
        self.assertEqual(output, "10A")
    
    def test_five_double_letters(self):
        test_string: str = "AABBCCDDEE"
        output: str = solution(test_string)
        self.assertEqual(output, "2A2B2C2D2E")
    
    def test_mixed_case(self):
        test_string: str = "AAAABBBCCDAA"
        output: str = solution(test_string)
        self.assertEqual(output, "4A3B2C1D2A")


if __name__ == "__main__":
    unittest.main()