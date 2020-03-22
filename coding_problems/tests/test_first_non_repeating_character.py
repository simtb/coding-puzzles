import unittest
from problems.first_non_repeating_character import find_first_non_repeating_character as f

class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_empty_string(self):
        test_string: str = ""
        output: str = f(test_string)
        self.assertEqual(output, "")
    
    def test_all_single_char(self):
        test_string: str = "abcde"
        output: str = f(test_string)
        self.assertEqual(output, "a")
    
    def test_all_doubles(self):
        test_string: str = "aabbccddee"
        output: str = f(test_string)
        self.assertEqual(output, None)

    def test_final_char(self):
        test_string: str = "aaaaaaaaaaaab"
        output: str = f(test_string)
        self.assertEqual(output,"b")



if __name__ == "__main__":
    unittest.main()