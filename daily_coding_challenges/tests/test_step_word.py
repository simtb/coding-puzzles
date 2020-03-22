import unittest
from challenges.step_word import step_word

class TestStepWord(unittest.TestCase):
    def test_case_1(self):
        dictionary = ['APPEAL', 'CAPPLE', 'PALPED', 'LAPPED', 'DAPPLE', 'ALEPPO', 'LAPPER', 'RAPPEL', 'LAPPET', 'PAPULE', 'UPLEAP', 'CAT', 'DOG', 'FISH', 'LONDON']
        expected_outcome = ['appeal', 'capple', 'palped', 'lapped', 'dapple', 'aleppo', 'lapper', 'rappel', 'lappet', 'papule', 'upleap']
        actual_outcome = step_word('apple', dictionary)
        self.assertEqual(expected_outcome, actual_outcome)


if __name__ == '__main__':
    unittest.main()


