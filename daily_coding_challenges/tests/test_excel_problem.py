import unittest
from challenges.excel_problem import get_column_id

class TestExcelProblem(unittest.TestCase):

    def test_case_1(self):
        value: int = 1
        expected_value: str = "A"
        actual_value: str = get_column_id(value)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_2(self):
        value: int = 2
        expected_value: str = "B"
        actual_value: str = get_column_id(value)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_3(self):
        value: int = 3
        expected_value: str = "C"
        actual_value: str = get_column_id(value)
        self.assertEqual(expected_value, actual_value)

    def test_case_4(self):
        value: int = 25
        expected_value: str = "Y"
        actual_value: str = get_column_id(value)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_5(self):
        value: int = 26
        expected_value: str = "Z"
        actual_value: str = get_column_id(value)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_6(self):
        value: int = 27
        expected_value: str = "AA"
        actual_value: str = get_column_id(value)
        self.assertEqual(expected_value, actual_value)

    def test_case_7(self):
        value: int = 103
        expected_value: str = "CY"
        actual_value: str = get_column_id(value)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_8(self):
        value: int = 104
        expected_value: str = "CZ"
        actual_value: str = get_column_id(value)
        self.assertEqual(expected_value, actual_value)
    
    def test_case_9(self):
        value: int = 105
        expected_value: str = "DA"
        actual_value: str = get_column_id(value)
        self.assertEqual(expected_value, actual_value)

    def test_case_10(self):
        value: int = 1000
        expected_value: str = "ALL"
        actual_value: str = get_column_id(value)
        self.assertEqual(expected_value, actual_value)

if __name__ == "__main__":
    unittest.main()