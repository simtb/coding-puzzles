import unittest
from challenges.fixed_point import fixed_point


class TestFixedPoint(unittest.TestCase):

    def test_case_1(self):
        test_array = [0, 1, 2, 3, 4]
        expected_outcome = True
        actual_outcome = fixed_point(test_array)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_2(self):
        test_array = [1, 2, 3, 4, 5]
        expected_outcome = False
        actual_outcome = fixed_point(test_array)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_3(self):
        test_array = []
        expected_outcome = False
        actual_outcome = fixed_point(test_array)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_4(self):
        test_array = [10, 8, 6, 5, 4]
        expected_outcome = True
        actual_outcome = fixed_point(test_array)
        self.assertEqual(expected_outcome, actual_outcome)

if __name__ == '__main__':
    unittest.main()