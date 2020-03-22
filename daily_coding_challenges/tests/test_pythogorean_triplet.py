import unittest
from challenges.pythogorean_triplet import pythagorean_triple


class TestPythagoreanTriplet(unittest.TestCase):
    def test_case_1(self):
        test_arr = []
        expected_outcome = False
        actual_outcome = pythagorean_triple(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_2(self):
        test_arr = [1]
        expected_outcome = False
        actual_outcome = pythagorean_triple(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_3(self):
        test_arr = [1, 2]
        expected_outcome = False
        actual_outcome = pythagorean_triple(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_3(self):
        test_arr = [1, 2, 3, 4, 5]
        expected_outcome = True
        actual_outcome = pythagorean_triple(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_4(self):
        test_arr = [2, 2, 2, 2, 2]
        expected_outcome = False
        actual_outcome = pythagorean_triple(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)

if __name__ == '__main__':
    unittest.main()