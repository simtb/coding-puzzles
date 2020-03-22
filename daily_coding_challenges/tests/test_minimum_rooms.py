import unittest
from typing import List
from challenges.minimum_number_of_rooms import solution

class TestSolution(unittest.TestCase):
    def test_two_rooms_need(self):
        intervals: List[tuple] = [(30, 75), (0, 50), (60, 150)]
        output: int = solution(intervals)
        self.assertEqual(output, 2)
        
    def test_three_rooms_need(self):
        intervals: List[tuple] = [(30, 75), (0, 50), (40, 150)]
        output: int = solution(intervals)
        self.assertEqual(output, 3)

    def test_one_rooms_need(self):
        intervals: List[tuple] = [(0, 10), (20, 30), (40, 50)]
        output: int = solution(intervals)
        self.assertEqual(output, 1)

    def test_one_interval_only(self):
        intervals: List[tuple] = [(0, 10)]
        output: int = solution(intervals)
        self.assertEqual(output, 1)

if __name__ == "__main__":
    unittest.main()

