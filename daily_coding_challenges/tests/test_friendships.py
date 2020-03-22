import unittest
from challenges.friendships import friendships


class TestFrienships(unittest.TestCase):
    def test_case_1(self):
        test_classroom = test = {
                    0: [1, 2],
                    1: [0, 5],
                    2: [0],
                    3: [6],
                    4: [],
                    5: [1],
                    6: [3]
                }
        expected_outcome = 3
        actual_outcome = friendships(test_classroom)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_2(self):
        test_classroom = test = {
                    0: [],
                    1: [],
                    2: [],
                    3: [],
                    4: [],
                    5: [],
                    6: []
                }
        expected_outcome = 7
        actual_outcome = friendships(test_classroom)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_3(self):
        test_classroom = test = {
                    0: [1, 2, 3, 4, 5, 6],
                    1: [0, 2, 3, 4, 5, 6],
                    2: [0, 1, 3, 4, 5, 6],
                    3: [0, 1, 2, 4, 5, 6],
                    4: [0, 1, 2, 3, 4, 6],
                    5: [0, 1, 2, 3, 4, 6],
                    6: [0, 1, 2, 3, 4, 5]
                }
        expected_outcome = 1
        actual_outcome = friendships(test_classroom)
        self.assertEqual(expected_outcome, actual_outcome)

    
    def test_case_4(self):
        test_classroom = test = {
                    0: [1],
                    1: [0, 2],
                    2: [1, 3],
                    3: [2, 4],
                    4: [3, 5],
                    5: [4, 6],
                    6: [5]
                }
        expected_outcome = 1
        actual_outcome = friendships(test_classroom)
        self.assertEqual(expected_outcome, actual_outcome)
        
        


if __name__ == '__main__':
    unittest.main()