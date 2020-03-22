import unittest
from challenges.balanced_brackets import balanced_brackets

class TestBalancedBrackets(unittest.TestCase):
    def test_empty_string_case(self):
        test_string: str = ""
        output: bool = balanced_brackets(test_string)
        self.assertEqual(output, True)
    
    def test_simple_round_brackets(self):
        test_string: str = "()"
        output: bool = balanced_brackets(test_string)
        self.assertEqual(output, True)

    def test_simple_squre_brackets(self):
        test_string: str = "[]"
        output: bool = balanced_brackets(test_string)
        self.assertEqual(output, True)
    
    def test_simple_curly_brackets(self):
        test_string: str = "{}"
        output: bool = balanced_brackets(test_string)
        self.assertEqual(output, True)
    
    def test_simple_unbalanced_round_brackets(self):
        test_string: str = ")("
        output: bool = balanced_brackets(test_string)
        self.assertEqual(output, False)
    
    def test_balanced_brackets(self):
        test_string: str = "([])[]({})"
        output: bool = balanced_brackets(test_string)
        self.assertEqual(output, True)
    
    def test_unbalanced_brackets(self):
        test_string: str = "((()"
        output: bool = balanced_brackets(test_string)
        self.assertEqual(output, False)
    
    def test_unbalanced_brackets_2(self):
        test_string: str = "([)]"
        output: bool = balanced_brackets(test_string)
        self.assertEqual(output, False)
    
    def test_unbalanced_brackets_3(self):
        test_string: str = "([])[]({}))"
        output: bool = balanced_brackets(test_string)
        self.assertEqual(output, False)
    
    def test_unbalanced_brackets_4(self):
        test_string: str = "([])[]({})("
        output: bool = balanced_brackets(test_string)
        self.assertEqual(output, False)


if __name__ == "__main__":
    unittest.main()