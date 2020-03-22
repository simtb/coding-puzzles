import unittest
from typing import List
from challenges.shortest_path import shortest_path

class TestShortestPath(unittest.TestCase):
    
    def test_same_points(self):
        test_points: List[List[int]] = [[0, 0], [0, 0], [0, 0]]
        expected_result: int = 0
        actual_result: int = shortest_path(test_points)
        self.assertEqual(actual_result, expected_result)
    
    def test_back_to_start(self):
        test_points: List[List[int]] = [[0, 0], [10, 0], [0, 0]]
        expected_result: int = 20
        actual_result: int = shortest_path(test_points)
        self.assertEqual(actual_result, expected_result)
    
    def test_square(self):
        test_points: List[List[int]] = [[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]
        expected_result: int = 40
        actual_result: int = shortest_path(test_points)
        self.assertEqual(actual_result, expected_result)
    
    def test_sample(self):
        test_points: List[List[int]] = [[0, 0], [1, 1], [1, 2]]
        expected_result: int = 2
        actual_result: int = shortest_path(test_points)
        self.assertEqual(actual_result, expected_result)
    
    def test_sample_2(self):
        test_points: List[List[int]] = [[0, 0], [-10, -5], [10, 20]]
        expected_result: int = 35
        actual_result: int = shortest_path(test_points)
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()