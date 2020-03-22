import unittest
from problems.flattening_a_linked_list import Node, solution_1

class TestSolution1(unittest.TestCase):
    head = Node(5)

    head.bottom = Node(7)
    head.bottom.bottom = Node(8)
    head.bottom.bottom.bottom = Node(30)

    head.next = Node(10)
    head.next.bottom = Node(20)

    head.next.next = Node(19)
    head.next.next.bottom = Node(22)
    head.next.next.bottom.bottom = Node(50)

    head.next.next.next = Node(28)
    head.next.next.next.bottom = Node(35)
    head.next.next.next.bottom.bottom = Node(40)
    head.next.next.next.bottom.bottom.bottom = Node(45)

    def test_empty_string(self):
        test_head = None
        output = solution_1(test_head)
        self.assertEqual(output, None)
    
    def test_example(self):
        test_head = self.head
        output = solution_1(test_head)
        self.assertEqual(output.value, 5)
        self.assertEqual(output.next.value, 7)
        self.assertEqual(output.next.next.value, 8)
        self.assertEqual(output.next.next.next.value, 10)
        self.assertEqual(output.next.next.next.next.value, 19)
        self.assertEqual(output.next.next.next.next.next.value, 20)
        self.assertEqual(output.next.next.next.next.next.next.value, 22)
        self.assertEqual(output.next.next.next.next.next.next.next.value, 28)
        self.assertEqual(output.next.next.next.next.next.next.next.next.value, 30)
        self.assertEqual(output.next.next.next.next.next.next.next.next.next.value, 35)
        self.assertEqual(output.next.next.next.next.next.next.next.next.next.next.value, 40)
        self.assertEqual(output.next.next.next.next.next.next.next.next.next.next.next.value, 45)
        self.assertEqual(output.next.next.next.next.next.next.next.next.next.next.next.next.value, 50)
        self.assertEqual(output.next.next.next.next.next.next.next.next.next.next.next.next.next, None)




if __name__ == "__main__":
    unittest.main()