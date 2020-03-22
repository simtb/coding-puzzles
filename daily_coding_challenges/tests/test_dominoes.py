import unittest
from challenges.dominoes import is_valid_index, dominoes

class TestDominoes(unittest.TestCase):
    def test_1(self):
        test_arr = ['.']
        expected_outcome = ['.']
        actual_outcome = dominoes(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_2(self):
        test_arr = ['R']
        expected_outcome = ['R']
        actual_outcome = dominoes(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_3(self):
        test_arr = ['L']
        expected_outcome = ['L']
        actual_outcome = dominoes(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_4(self):
        test_arr = ['.', 'L', '.', 'R', '.', '.', '.', '.', 'L']
        expected_outcome = ['L', 'L', '.', 'R', 'R', 'R', 'L', 'L', 'L']
        actual_outcome = dominoes(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_5(self):
        test_arr = ['.', '.', 'R', '.', '.', '.', 'L', '.', 'L']
        expected_outcome = ['.', '.', 'R', 'R', '.', 'L', 'L', 'L', 'L']
        actual_outcome = dominoes(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_6(self):
        test_arr = ['.', 'R', '.', 'L', '.', 'L', '.', 'R', '.']
        expected_outcome = ['.', 'R', '.', 'L', 'L', 'L', '.', 'R', 'R']
        actual_outcome = dominoes(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_7(self):
        test_arr = ['.', 'R', '.', '.', '.', '.', '.', '.', '.']
        expected_outcome = ['.', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
        actual_outcome = dominoes(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_8(self):
        test_arr = ['.', 'L', '.', '.', '.', '.', '.', '.', '.']
        expected_outcome = ['L', 'L', '.', '.', '.', '.', '.', '.', '.']
        actual_outcome = dominoes(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_9(self):
        test_arr = ['R', '.', '.', '.', '.', '.', '.', '.', 'L']
        expected_outcome = ['R', 'R', 'R', 'R', '.', 'L', 'L', 'L', 'L']
        actual_outcome = dominoes(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_10(self):
        test_arr = ['L', '.', '.', '.', '.', '.', '.', '.', 'R']
        expected_outcome = ['L', '.', '.', '.', '.', '.', '.', '.', 'R']
        actual_outcome = dominoes(test_arr)
        self.assertEqual(expected_outcome, actual_outcome)


if __name__ == '__main__':
    unittest.main()