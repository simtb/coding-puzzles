import unittest
from challenges.fib import fib

class TestFib(unittest.TestCase):
    def test_case_1(self):
        test_n: int = 1
        expected_value: int = 0
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_2(self):
        test_n: int = 2
        expected_value: int = 1
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_3(self):
        test_n: int = 3
        expected_value: int = 1
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_4(self):
        test_n: int = 4
        expected_value: int = 2
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_5(self):
        test_n: int = 5
        expected_value: int = 3
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_6(self):
        test_n: int = 6
        expected_value: int = 5
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_7(self):
        test_n: int = 7
        expected_value: int = 8
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_8(self):
        test_n: int = 8
        expected_value: int = 13
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)

    def test_case_9(self):
        test_n: int = 9
        expected_value: int = 21
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)

    def test_case_10(self):
        test_n: int = 10
        expected_value: int = 34
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)

    def test_case_100(self):
        test_n: int = 100
        expected_value: int = 218922995834555169026
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_1000(self):
        test_n: int = 1000
        expected_value: int = 26863810024485359386146727202142923967616609318986952340123175997617981700247881689338369654483356564191827856161443356312976673642210350324634850410377680367334151172899169723197082763985615764450078474174626
        actual_value: int = fib(test_n)
        self.assertEqual(expected_value, actual_value)
    


if __name__ == '__main__':
    unittest.main()