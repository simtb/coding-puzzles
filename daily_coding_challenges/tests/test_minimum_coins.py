import unittest
from challenges.minimum_coins import minimum_coins

class TestMinimumCoins(unittest.TestCase):
    
    def test_amount_is_zero(self):
        test_amount: int = 0
        expected_outcome: int = None
        actual_outcome: int = minimum_coins(test_amount)
        self.assertEqual(actual_outcome, expected_outcome)
    
    def test_amount_is_negative(self):
        test_amount: int = -10
        expected_outcome: int = None
        actual_outcome: int = minimum_coins(test_amount)
        self.assertEqual(actual_outcome, expected_outcome)
    
    def test_amount_is_one(self):
        test_amount: int = 1
        expected_outcome: int = 1
        actual_outcome: int = minimum_coins(test_amount)
        self.assertEqual(actual_outcome, expected_outcome)
    
    def test_amount_is_fifty(self):
        test_amount: int = 50
        expected_outcome: int = 2
        actual_outcome: int = minimum_coins(test_amount)
        self.assertEqual(actual_outcome, expected_outcome)

    def test_amount_is_sixteen(self):
        test_amount: int = 16
        expected_outcome: int = 3
        actual_outcome: int = minimum_coins(test_amount)
        self.assertEqual(actual_outcome, expected_outcome)
    
    def test_amount_is_thirty_six(self):
        test_amount: int = 3
        expected_outcome: int = 3
        actual_outcome: int = minimum_coins(test_amount)
        self.assertEqual(actual_outcome, expected_outcome)

if __name__ == "__main__":
    unittest.main()