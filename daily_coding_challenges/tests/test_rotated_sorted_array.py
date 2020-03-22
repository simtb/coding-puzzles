import unittest

from typing import List
from challenges.rotated_sorted_array import rotated_search


class TestRotatedSearch(unittest.TestCase):
    def test_empty_array(self):
        test_array: List[int] = []
        actual_output: int = rotated_search(test_array, 10)
        expected_output: int = None
        self.assertIs(actual_output, expected_output)
        self.assertEqual(actual_output, expected_output)
    
    def test_one_element_array_exist(self):
        test_array: List[int] = [10]
        actual_output: int = rotated_search(test_array, 10)
        expected_output: int = 0
        self.assertEqual(actual_output, expected_output)
    
    def test_one_element_array_does_not_exist(self):
        test_array: List[int] = [0]
        actual_output: int = rotated_search(test_array, 10)
        expected_output: int = None
        self.assertEqual(actual_output, expected_output)
    
    def test_sorted_example(self):
        test_array: List[int] = [2, 8, 10, 13, 18, 25]

        actual_output_0: int = rotated_search(test_array, 2)
        expected_output_0: int = 0
        self.assertEqual(actual_output_0, expected_output_0)

        actual_output_1: int = rotated_search(test_array, 8)
        expected_output_1: int = 1
        self.assertEqual(actual_output_1, expected_output_1)

        actual_output_2: int = rotated_search(test_array, 10)
        expected_output_2: int = 2
        self.assertEqual(actual_output_2, expected_output_2)

        actual_output_3: int = rotated_search(test_array, 13)
        expected_output_3: int = 3
        self.assertEqual(actual_output_3, expected_output_3)

        actual_output_4: int = rotated_search(test_array, 18)
        expected_output_4: int = 4
        self.assertEqual(actual_output_4, expected_output_4)

        actual_output_5: int = rotated_search(test_array, 25)
        expected_output_5: int = 5
        self.assertEqual(actual_output_5, expected_output_5)

        actual_output_6: int = rotated_search(test_array, 100)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 1)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 14)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)
    
    def test_sorted_example_rotation_1(self):
        test_array: List[int] = [25, 2, 8, 10, 13, 18]

        actual_output_0: int = rotated_search(test_array, 25)
        expected_output_0: int = 0
        self.assertEqual(actual_output_0, expected_output_0)

        actual_output_1: int = rotated_search(test_array, 2)
        expected_output_1: int = 1
        self.assertEqual(actual_output_1, expected_output_1)

        actual_output_2: int = rotated_search(test_array, 8)
        expected_output_2: int = 2
        self.assertEqual(actual_output_2, expected_output_2)

        actual_output_3: int = rotated_search(test_array, 10)
        expected_output_3: int = 3
        self.assertEqual(actual_output_3, expected_output_3)

        actual_output_4: int = rotated_search(test_array, 13)
        expected_output_4: int = 4
        self.assertEqual(actual_output_4, expected_output_4)

        actual_output_5: int = rotated_search(test_array, 18)
        expected_output_5: int = 5
        self.assertEqual(actual_output_5, expected_output_5)

        actual_output_6: int = rotated_search(test_array, 100)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 1)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 14)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)
    
    def test_sorted_example_rotation_2(self):
        test_array: List[int] = [18, 25, 2, 8, 10, 13]

        actual_output_0: int = rotated_search(test_array, 18)
        expected_output_0: int = 0
        self.assertEqual(actual_output_0, expected_output_0)

        actual_output_1: int = rotated_search(test_array, 25)
        expected_output_1: int = 1
        self.assertEqual(actual_output_1, expected_output_1)

        actual_output_2: int = rotated_search(test_array, 2)
        expected_output_2: int = 2
        self.assertEqual(actual_output_2, expected_output_2)

        actual_output_3: int = rotated_search(test_array, 8)
        expected_output_3: int = 3
        self.assertEqual(actual_output_3, expected_output_3)

        actual_output_4: int = rotated_search(test_array, 10)
        expected_output_4: int = 4
        self.assertEqual(actual_output_4, expected_output_4)

        actual_output_5: int = rotated_search(test_array, 13)
        expected_output_5: int = 5
        self.assertEqual(actual_output_5, expected_output_5)

        actual_output_6: int = rotated_search(test_array, 100)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 1)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 14)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)
    
    def test_sorted_example_rotation_3(self):
        test_array: List[int] = [13, 18, 25, 2, 8, 10]

        actual_output_0: int = rotated_search(test_array, 13)
        expected_output_0: int = 0
        self.assertEqual(actual_output_0, expected_output_0)

        actual_output_1: int = rotated_search(test_array, 18)
        expected_output_1: int = 1
        self.assertEqual(actual_output_1, expected_output_1)

        actual_output_2: int = rotated_search(test_array, 25)
        expected_output_2: int = 2
        self.assertEqual(actual_output_2, expected_output_2)

        actual_output_3: int = rotated_search(test_array, 2)
        expected_output_3: int = 3
        self.assertEqual(actual_output_3, expected_output_3)

        actual_output_4: int = rotated_search(test_array, 8)
        expected_output_4: int = 4
        self.assertEqual(actual_output_4, expected_output_4)

        actual_output_5: int = rotated_search(test_array, 10)
        expected_output_5: int = 5
        self.assertEqual(actual_output_5, expected_output_5)

        actual_output_6: int = rotated_search(test_array, 100)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 1)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 14)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)
    
    def test_sorted_example_rotation_4(self):
        test_array: List[int] = [10, 13, 18, 25, 2, 8]

        actual_output_0: int = rotated_search(test_array, 10)
        expected_output_0: int = 0
        self.assertEqual(actual_output_0, expected_output_0)

        actual_output_1: int = rotated_search(test_array, 13)
        expected_output_1: int = 1
        self.assertEqual(actual_output_1, expected_output_1)

        actual_output_2: int = rotated_search(test_array, 18)
        expected_output_2: int = 2
        self.assertEqual(actual_output_2, expected_output_2)

        actual_output_3: int = rotated_search(test_array, 25)
        expected_output_3: int = 3
        self.assertEqual(actual_output_3, expected_output_3)

        actual_output_4: int = rotated_search(test_array, 2)
        expected_output_4: int = 4
        self.assertEqual(actual_output_4, expected_output_4)

        actual_output_5: int = rotated_search(test_array, 8)
        expected_output_5: int = 5
        self.assertEqual(actual_output_5, expected_output_5)

        actual_output_6: int = rotated_search(test_array, 100)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 1)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 14)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)
    
    def test_sorted_example_rotation_5(self):
        test_array: List[int] = [8, 10, 13, 18, 25, 2]

        actual_output_0: int = rotated_search(test_array, 8)
        expected_output_0: int = 0
        self.assertEqual(actual_output_0, expected_output_0)

        actual_output_1: int = rotated_search(test_array, 10)
        expected_output_1: int = 1
        self.assertEqual(actual_output_1, expected_output_1)

        actual_output_2: int = rotated_search(test_array, 13)
        expected_output_2: int = 2
        self.assertEqual(actual_output_2, expected_output_2)

        actual_output_3: int = rotated_search(test_array, 18)
        expected_output_3: int = 3
        self.assertEqual(actual_output_3, expected_output_3)

        actual_output_4: int = rotated_search(test_array, 25)
        expected_output_4: int = 4
        self.assertEqual(actual_output_4, expected_output_4)

        actual_output_5: int = rotated_search(test_array, 2)
        expected_output_5: int = 5
        self.assertEqual(actual_output_5, expected_output_5)

        actual_output_6: int = rotated_search(test_array, 100)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 1)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)

        actual_output_6: int = rotated_search(test_array, 14)
        expected_output_6: int = None
        self.assertEqual(actual_output_6, expected_output_6)
    
    def test_sorted_example_10(self):
        test_array: List[int] = [8,9,10,1,2,3,4,5,6,7]

        actual_output_0: int = rotated_search(test_array, 5)
        expected_output_0: int = 7
        self.assertEqual(actual_output_0, expected_output_0)


if __name__ == "__main__":
    unittest.main()