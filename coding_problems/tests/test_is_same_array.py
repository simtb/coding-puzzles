import unittest
from problems.is_same_array import is_same_array

class TestIsSameArray(unittest.TestCase):
    def test_empty_array(self):
        test_array_1: list = []
        test_array_2: list = []
        output: bool = is_same_array(test_array_1, test_array_2)
        self.assertEqual(output, True)
    
    def test_example_1(self):
        test_array_1: list = [1, 2, 5, 4, 0]
        test_array_2: list = [2, 4, 5, 0, 1]
        output: bool = is_same_array(test_array_1, test_array_2)
        self.assertEqual(output, True)
    
    def test_example_2(self):
        test_array_1: list = [1, 2, 5, 4, 0, 2, 1]
        test_array_2: list = [2, 4, 5, 0, 1, 1, 2]
        output: bool = is_same_array(test_array_1, test_array_2)
        self.assertEqual(output, True)
    
    def test_example_3(self):
        test_array_1: list = [1, 7, 1]
        test_array_2: list = [7, 7, 1]
        output: bool = is_same_array(test_array_1, test_array_2)
        self.assertEqual(output, False)



if __name__ == "__main__":
    unittest.main()