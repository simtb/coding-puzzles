import unittest
from challenges.stack import Stack

class TestStack(unittest.TestCase):

    def test_is_empty(self):
        test_stack = Stack()
        output: bool = test_stack.is_empty
        self.assertEqual(output, True)
        self.assertIsInstance(test_stack, Stack)
        self.assertNotIsInstance(test_stack, list)
    
    def test_push(self):
        empty_stack: Stack = Stack()

        test_stack: Stack = empty_stack
        test_stack.push(3)
        test_stack.push(2)
        test_stack.push(1)

        self.assertIn(3, test_stack)
        self.assertIn(2, test_stack)
        self.assertIn(1, test_stack)
    
    def test_pop(self):
        empty_stack: Stack = Stack()

        test_stack: Stack = empty_stack
        test_stack.push(3)
        test_stack.push(2)
        test_stack.push(1)

        value_1: int = test_stack.pop()
        value_2: int = test_stack.pop()
        value_3: int = test_stack.pop()
        value_4: int = test_stack.pop()
        value_5: int = test_stack.pop()
        self.assertEqual(value_1, 1)
        self.assertEqual(value_2, 2)
        self.assertEqual(value_3, 3)
        self.assertEqual(value_4, None)
        self.assertEqual(value_5, None)
    
    def test_max(self):
        empty_stack: Stack = Stack()

        test_stack: Stack = empty_stack
        test_stack.push(3)
        test_stack.push(2)
        test_stack.push(1)

        self.assertEqual(3, test_stack.max())
        test_stack.pop()
        self.assertEqual(3, test_stack.max())
        test_stack.pop()
        self.assertEqual(3, test_stack.max())
        test_stack.pop()
        self.assertEqual(None, test_stack.max())
        test_stack.push(100)
        self.assertEqual(100, test_stack.max())


if __name__ == "__main__":
    unittest.main()