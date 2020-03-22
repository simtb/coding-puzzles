import unittest
from challenges.invert_binary_tree import BinaryTreeNode, invert_tree

class TestInvertTree(unittest.TestCase):
    test_root_1: BinaryTreeNode = None

    test_root_2: BinaryTreeNode = BinaryTreeNode("a")
    test_root_2.left = BinaryTreeNode("b")
    test_root_2.right = BinaryTreeNode("c")
    test_root_2.left.left = BinaryTreeNode("d")
    test_root_2.left.right = BinaryTreeNode("e")
    test_root_2.right.left = BinaryTreeNode("f")

    def test_empty_tree(self):
        expected_result: BinaryTreeNode = None
        actual_result: BinaryTreeNode = invert_tree(self.test_root_1)
        self.assertEqual(actual_result, expected_result)
    
    def test_invert(self):
        inverted_tree: BinaryTreeNode = invert_tree(self.test_root_2)
        
        self.assertEqual(self.test_root_2, "a") 
        self.assertEqual(self.test_root_2.left, "c") 
        self.assertEqual(self.test_root_2.right, "b") 
        self.assertEqual(self.test_root_2.left.left, None) 
        self.assertEqual(self.test_root_2.left.right, "f") 
        self.assertEqual(self.test_root_2.right.left, "e") 
        self.assertEqual(self.test_root_2.right.right, "d") 


if __name__ == "__main__":
    unittest.main()