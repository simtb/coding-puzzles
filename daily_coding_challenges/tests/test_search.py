import unittest
from challenges.search import binary_search, binary_search_recursively

class TestBinarySearch(unittest.TestCase):
    test_array = []
    for i in range(1, 11):
        for j in range(i):
            test_array.append(i)

    def test_case_0(self):
        value = 0
        expected_outcome = False
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_1(self):
        value = 1
        expected_outcome = True
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_2(self):
        value = 2
        expected_outcome = True
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_3(self):
        value = 3
        expected_outcome = True
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_4(self):
        value = 4
        expected_outcome = True
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_5(self):
        value = 5
        expected_outcome = True
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_6(self):
        value = 6
        expected_outcome = True
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_7(self):
        value = 7
        expected_outcome = True
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_8(self):
        value = 8
        expected_outcome = True
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_9(self):
        value = 9
        expected_outcome = True
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_10(self):
        value = 10
        expected_outcome = True
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_11(self):
        value = 11
        expected_outcome = False
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)


class TestBinarySearchRecursively(unittest.TestCase):
    test_array = []
    for i in range(1, 11):
        for j in range(i):
            test_array.append(i)

    def test_case_0(self):
        value = 0
        expected_outcome = False
        actual_outcome = binary_search_recursively(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_1(self):
        value = 1
        expected_outcome = True
        actual_outcome = binary_search_recursively(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_2(self):
        value = 2
        expected_outcome = True
        actual_outcome = binary_search_recursively(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_3(self):
        value = 3
        expected_outcome = True
        actual_outcome = binary_search_recursively(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_4(self):
        value = 4
        expected_outcome = True
        actual_outcome = binary_search_recursively(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_5(self):
        value = 5
        expected_outcome = True
        actual_outcome = binary_search_recursively(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_6(self):
        value = 6
        expected_outcome = True
        actual_outcome = binary_search_recursively(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_7(self):
        value = 7
        expected_outcome = True
        actual_outcome = binary_search_recursively(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_8(self):
        value = 8
        expected_outcome = True
        actual_outcome = binary_search(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_9(self):
        value = 9
        expected_outcome = True
        actual_outcome = binary_search_recursively(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_10(self):
        value = 10
        expected_outcome = True
        actual_outcome = binary_search_recursively(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_11(self):
        value = 11
        expected_outcome = False
        actual_outcome = binary_search_recursively(self.test_array, value)
        self.assertEqual(expected_outcome, actual_outcome)


if __name__ == '__main__':
    unittest.main()

    