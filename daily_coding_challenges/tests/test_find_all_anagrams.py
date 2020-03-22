import unittest
from typing import List
from challenges.find_all_anagrams import find_all_anagrams

class TestFindAllAnagrams(unittest.TestCase):
    def test_string_longer_than_word(self):
        test_word: str = "abc"
        test_string: str = "abcde"
        actual_outcome: List[int] = find_all_anagrams(test_word, test_string)
        expected_outcome: List[int] = []
        self.assertEqual(actual_outcome, expected_outcome)
    
    def test_same_word_and_string(self):
        test_word: str = "abc"
        test_string: str = "abc"
        actual_outcome: List[int] = find_all_anagrams(test_word, test_string)
        expected_outcome: List[int] = [0]
        self.assertEqual(actual_outcome, expected_outcome)
    
    def test_exmaple(self):
        test_word: str = "abxaba"
        test_string: str = "ab"
        actual_outcome: List[int] = find_all_anagrams(test_word, test_string)
        expected_outcome: List[int] = [0, 3, 4]
        self.assertEqual(actual_outcome, expected_outcome)
    
    def test_no_anagram(self):
        test_word: str = "abxaba"
        test_string: str = "cd"
        actual_outcome: List[int] = find_all_anagrams(test_word, test_string)
        expected_outcome: List[int] = []
        self.assertEqual(actual_outcome, expected_outcome)
    
    def test_same_letter(self):
        test_word: str = "aaaaa"
        test_string: str = "a"
        actual_outcome: List[int] = find_all_anagrams(test_word, test_string)
        expected_outcome: List[int] = [0, 1, 2, 3, 4, ]
        self.assertEqual(actual_outcome, expected_outcome)

if __name__ == "__main__":
    unittest.main()