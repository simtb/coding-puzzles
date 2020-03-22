import unittest
from challenges.contains_cycle import contains_cycle


class TestContainsCycle(unittest.TestCase):
    def test_case_1(self):
        test_graph = {}
        expected_outcome = False
        actual_outcome = contains_cycle(test_graph)
        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_case_2(self):
        test_graph = {
            1: [2],
            2: [3],
            3: [4],
            4: [1],
        }

        expected_outcome = True
        actual_outcome = contains_cycle(test_graph)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_3(self):
        test_graph = {
            1: [2],
            2: [3],
            3: [4],
            4: [],
        }

        expected_outcome = False
        actual_outcome = contains_cycle(test_graph)
        self.assertEqual(expected_outcome, actual_outcome)

if __name__ == '__main__':
    unittest.main()