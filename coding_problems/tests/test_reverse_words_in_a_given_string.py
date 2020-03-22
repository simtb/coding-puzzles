import unittest
from problems.reverse_words_in_a_given_string import reverse_string

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        test_string: str = ""
        output: str = reverse_string(test_string)
        self.assertEqual(output, "")

    def test_example_1(self):
        test_string: str = "geeks quiz practice code"
        output: str = reverse_string(test_string)
        self.assertEqual(output, "code practice quiz geeks")
    
    def test_example_2(self):
        test_string: str = "getting good at coding needs a lot of practice"
        output: str = reverse_string(test_string)
        self.assertEqual(output, "practice of lot a needs coding at good getting")

if __name__ == "__main__":
    unittest.main()