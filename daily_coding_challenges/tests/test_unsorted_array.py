import unittest
from challenges.unsorted_array import unsorted_array

class TestUnsortedArray(unittest.TestCase):
    def test_case_0(self):
        test_array = [1, 2, 3, 4, 5]
        expected_result = ()
        actual_result = unsorted_array(test_array)
        self.assertEqual(expected_result, actual_result)

    def test_case_1(self):
        test_array = [5, 4, 3, 2, 1]
        expected_result = (0, 4)
        actual_result = unsorted_array(test_array)
        self.assertEqual(expected_result, actual_result)

    def test_case_2(self):
        test_array = [1, 2, 4, 5, 3]
        expected_result = (2, 4)
        actual_result = unsorted_array(test_array)
        self.assertEqual(expected_result, actual_result)



if __name__ == '__main__':
    unittest.main()