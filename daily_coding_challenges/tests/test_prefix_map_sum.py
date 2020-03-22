import unittest
from challenges.prefix_map_sum import PrefixMapSum  


class TestPrefixMaxSum(unittest.TestCase):
    def test_case_1(self):
        mapsum: PrefixMapSum = PrefixMapSum()
        mapsum.insert('columnar', 3)
        expected_sum: int = 3 
        actual_sum: int = mapsum.sum()
        self.assertTrue(expected_sum, actual_sum)
        mapsum.insert('column', 2)
        expected_sum: int = 5 
        actual_sum: int = mapsum.sum()
        self.assertTrue(expected_sum, actual_sum)

    def test_case_2(self):
        mapsum: PrefixMapSum = PrefixMapSum()
        mapsum.insert('columnar', 3)
        expected_sum: int = 3 
        actual_sum: int = mapsum.sum()
        self.assertTrue(expected_sum, actual_sum)

        mapsum.insert('column', 2)
        expected_sum: int = 5 
        actual_sum: int = mapsum.sum()
        self.assertTrue(expected_sum, actual_sum)

        mapsum.insert('column', 4)
        expected_sum: int = 7
        actual_sum: int = mapsum.sum()
        self.assertTrue(expected_sum, actual_sum)
        
        mapsum.insert('col', 10)
        expected_sum: int = 17
        actual_sum: int = mapsum.sum()
        self.assertTrue(expected_sum, actual_sum)

        mapsum.insert('column', 10)
        expected_sum: int = 23
        actual_sum: int = mapsum.sum()
        self.assertTrue(expected_sum, actual_sum)




if __name__ == '__main__':
    unittest.main()