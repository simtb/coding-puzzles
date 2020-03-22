import unittest
from challenges.is_palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_case_0(self):
        test_number: int = 0
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_1(self):
        test_number: int = 1
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_2(self):
        test_number: int = 2
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_3(self):
        test_number: int = 3
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_4(self):
        test_number: int = 4
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_5(self):
        test_number: int = 5
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_6(self):
        test_number: int = 6
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_7(self):
        test_number: int = 7
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_8(self):
        test_number: int = 8
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_9(self):
        test_number: int = 9
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_10(self):
        test_number: int = 10
        expected_outcome: bool = False
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_11(self):
        test_number: int = 11
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_12(self):
        test_number: int = 12
        expected_outcome: bool = False
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_13(self):
        test_number: int = 1234567890123456789
        expected_outcome: bool = False
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_14(self):
        test_number: int = 1234567890987654321
        expected_outcome: bool = True
        actual_outcome: bool = is_palindrome(test_number)
        self.assertEqual(expected_outcome, actual_outcome)

if __name__ == "__main__":
    unittest.main()

