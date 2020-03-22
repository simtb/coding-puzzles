import unittest
from typing import List
from challenges.reconstruct_tree import BinaryTreeNode, preorder_traversal, inorder_traversal, reconstruct_tree

class TestReconstructTree(unittest.TestCase):
    
    def test_empty_tree(self):
        test_preorder_list: List[BinaryTreeNode] = []
        test_inorder_list: List[BinaryTreeNode] = []
        actual_output: BinaryTreeNode = reconstruct_tree(test_preorder_list, test_inorder_list)
        expected_output: BinaryTreeNode = None
        self.assertEqual(actual_output, expected_output)
    
    def test_one_node(self):
        test_preorder_list: List[BinaryTreeNode] = ["a"]
        test_inorder_list: List[BinaryTreeNode] = ["a"]
        actual_output: BinaryTreeNode = reconstruct_tree(test_preorder_list, test_inorder_list)
        expected_output: BinaryTreeNode = BinaryTreeNode("a")
        self.assertEqual(actual_output, expected_output)
    
    def test_example_1(self):
        test_preorder_list: List[BinaryTreeNode] = ["a", "b", "d", "e", "c", "f", "g"]
        test_inorder_list: List[BinaryTreeNode] = ["d", "b", "e", "a", "f", "c", "g"]
        resultant_root: BinaryTreeNode = reconstruct_tree(test_preorder_list, test_inorder_list)
        actual_preorder_list: List[BinaryTreeNode] = preorder_traversal(resultant_root, store=[])
        expected_preorder_list: List[BinaryTreeNode] = ["a", "b", "d", "e", "c", "f", "g"]
        actual_inorder_list: List[BinaryTreeNode] = inorder_traversal(resultant_root, store=[])
        expected_inorder_list: List[BinaryTreeNode] = ["d", "b", "e", "a", "f", "c", "g"]
        self.assertEqual(actual_preorder_list, expected_preorder_list)
        self.assertEqual(actual_inorder_list, expected_inorder_list)
    
    def test_example_2(self):
        test_preorder_list: List[BinaryTreeNode] = [8, 3, 1, 6, 4, 7, 10, 14, 13]
        test_inorder_list: List[BinaryTreeNode] = [1, 3, 4, 6, 7, 8, 10, 13, 14]
        resultant_root: BinaryTreeNode = reconstruct_tree(test_preorder_list, test_inorder_list)
        actual_preorder_list: List[BinaryTreeNode] = preorder_traversal(resultant_root, store=[])
        expected_preorder_list: List[BinaryTreeNode] = [8, 3, 1, 6, 4, 7, 10, 14, 13]
        actual_inorder_list: List[BinaryTreeNode] = inorder_traversal(resultant_root, store=[])
        expected_inorder_list: List[BinaryTreeNode] = [1, 3, 4, 6, 7, 8, 10, 13, 14]
        self.assertEqual(actual_preorder_list, expected_preorder_list)
        self.assertEqual(actual_inorder_list, expected_inorder_list)
    
    # def test_example_3(self):
    #     test_preorder_list: List[BinaryTreeNode] = [8, 5, 9, 7, 1, 12, 2, 4, 11, 3]
    #     test_inorder_list: List[BinaryTreeNode] = [9, 5, 1, 7, 2, 12, 8, 4, 3, 11]
    #     resultant_root: BinaryTreeNode = reconstruct_tree(test_preorder_list, test_inorder_list)
    #     actual_preorder_list: List[BinaryTreeNode] = preorder_traversal(resultant_root, store=[])
    #     expected_preorder_list: List[BinaryTreeNode] = [8, 5, 9, 7, 1, 12, 2, 4, 11, 3]
    #     actual_inorder_list: List[BinaryTreeNode] = inorder_traversal(resultant_root, store=[])
    #     expected_inorder_list: List[BinaryTreeNode] = [9, 5, 1, 7, 2, 12, 8, 4, 3, 11]
    #     self.assertEqual(actual_preorder_list, expected_preorder_list)
    #     self.assertEqual(actual_inorder_list, expected_inorder_list)
    
    # def test_example_4(self):
    #     test_preorder_list: List[BinaryTreeNode] = [60, 41, 16, 25, 53, 46, 42, 55, 74, 65, 63, 62, 64, 70]
    #     test_inorder_list: List[BinaryTreeNode] = [16, 25, 41, 42, 46, 53, 55, 60, 62, 63, 64, 65, 70, 74]
    #     resultant_root: BinaryTreeNode = reconstruct_tree(test_preorder_list, test_inorder_list)
    #     actual_preorder_list: List[BinaryTreeNode] = preorder_traversal(resultant_root, store=[])
    #     expected_preorder_list: List[BinaryTreeNode] = [60, 41, 16, 25, 53, 46, 42, 55, 74, 65, 63, 62, 64, 70]
    #     actual_inorder_list: List[BinaryTreeNode] = inorder_traversal(resultant_root, store=[])
    #     expected_inorder_list: List[BinaryTreeNode] = [16, 25, 41, 42, 46, 53, 55, 60, 62, 63, 64, 65, 70, 74]
    #     self.assertEqual(actual_preorder_list, expected_preorder_list)
    #     self.assertEqual(actual_inorder_list, expected_inorder_list)
    
    def test_example_5(self):
        test_preorder_list: List[BinaryTreeNode] = [5, 3, 7, 6, 9]
        test_inorder_list: List[BinaryTreeNode] = [3, 5, 6, 7, 9]
        resultant_root: BinaryTreeNode = reconstruct_tree(test_preorder_list, test_inorder_list)
        actual_preorder_list: List[BinaryTreeNode] = preorder_traversal(resultant_root, store=[])
        expected_preorder_list: List[BinaryTreeNode] = [5, 3, 7, 6, 9]
        actual_inorder_list: List[BinaryTreeNode] = inorder_traversal(resultant_root, store=[])
        expected_inorder_list: List[BinaryTreeNode] = [3, 5, 6, 7, 9]
        self.assertEqual(actual_preorder_list, expected_preorder_list)
        self.assertEqual(actual_inorder_list, expected_inorder_list)
    
    
    

if __name__ == "__main__":
    unittest.main()