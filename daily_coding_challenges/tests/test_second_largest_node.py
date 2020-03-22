import unittest
from challenges.second_largest_node import solution, BinarySearchTreeNode, pre_order_traversal, solution_2

class TestSolution(unittest.TestCase):
    root = BinarySearchTreeNode(8)
    
    root.left = BinarySearchTreeNode(3)
    root.right = BinarySearchTreeNode(10)

    root.left.left = BinarySearchTreeNode(1)
    root.left.right = BinarySearchTreeNode(6)

    root.right.right = BinarySearchTreeNode(14)

    root.left.right.left = BinarySearchTreeNode(4)
    root.left.right.right = BinarySearchTreeNode(7)

    root.right.right.left = BinarySearchTreeNode(13)

    def test_empty_bst(self):
        test_root = None
        output = solution(test_root)
        self.assertEqual(output, None)
    
    def test_example(self):
        test_root = self.root
        output = solution(test_root)
        self.assertEqual(output.value, 13)

class TestSolution2(unittest.TestCase):
    root = BinarySearchTreeNode(8)
    
    root.left = BinarySearchTreeNode(3)
    root.right = BinarySearchTreeNode(10)

    root.left.left = BinarySearchTreeNode(1)
    root.left.right = BinarySearchTreeNode(6)

    root.right.right = BinarySearchTreeNode(14)

    root.left.right.left = BinarySearchTreeNode(4)
    root.left.right.right = BinarySearchTreeNode(7)

    root.right.right.left = BinarySearchTreeNode(13)

    def test_empty_bst(self):
        test_root = None
        values = pre_order_traversal(test_root, {})
        output = solution_2(values)
        self.assertEqual(output, None)
    
    def test_example(self):
        test_root = self.root
        values = pre_order_traversal(test_root, {})
        output = solution_2(values)
        self.assertEqual(output.value, 13)


if __name__ == "__main__":
    unittest.main()

