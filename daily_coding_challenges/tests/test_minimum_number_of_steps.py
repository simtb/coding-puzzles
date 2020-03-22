import unittest
from challenges.minimum_number_of_steps import solution
from typing import List

class TestSolution(unittest.TestCase):
    
    def test_example_matrix(self):

        test_matrix: List[list] = [
            [False, False, False, False],
            [True, True, False, True],
            [True, False, False, False],
            [False, False, False, False]
            ]
        
        start: tuple = (3, 0)
        end: tuple = (0, 0)

        output: int = solution(test_matrix, start, end)
        self.assertEqual(output, 7)
    
    def test_start_is_end(self):

        test_matrix: List[list] = [
            [False, False, False, False],
            [True, True, False, True],
            [True, False, False, False],
            [False, False, False, False]
            ]
        
        start: tuple = (3, 0)
        end: tuple = (3, 0)

        output: int = solution(test_matrix, start, end)
        self.assertEqual(output, 0)

    def test_empty_matrix(self):

        test_matrix: List[list] = [[]]
        
        start: tuple = (0, 0)
        end: tuple = (0, 0)

        output: int = solution(test_matrix, start, end)
        self.assertEqual(output, 0)
    
    def test_all_true(self):
        test_matrix: List[list] =[
            [True, True],
            [True, True]
        ]

        start: tuple = (1, 0)
        end: tuple = (0, 1)

        output: int = solution(test_matrix, start, end)
        self.assertEqual(output, None)
    
    def test_no_path(self):
        test_matrix: List[list] =[
            [True, False],
            [False, True]
        ]

        start: tuple = (1, 0)
        end: tuple = (0, 1)

        output: int = solution(test_matrix, start, end)
        self.assertEqual(output, None)
    
    def test_path(self):
        test_matrix: List[list] =[
            [False, False],
            [False, True]
        ]
        
        start: tuple = (1, 0)
        end: tuple = (0, 1)

        output: int = solution(test_matrix, start, end)
        self.assertEqual(output, 2)
    
    def test_four_by_four_matrix(self):
        test_matrix: List[list] =[
            [True, False, False, False],
            [True, False, False, True],
            [True, False, False, True],
            [False, False, False, True],
        ]
        
        start: tuple = (0, 3)
        end: tuple = (3, 0)

        output: int = solution(test_matrix, start, end)
        self.assertEqual(output, 6)

if __name__ == "__main__":
    unittest.main()