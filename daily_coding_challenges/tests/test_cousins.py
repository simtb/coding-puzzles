import unittest
from challenges.cousins import cousins, BinaryTreeNode

class TestCousins(unittest.TestCase):
    def test_case_1(self):
        test_root = BinaryTreeNode(1)
        test_node = BinaryTreeNode(1)
        expected_outcome = []
        actual_outcome = cousins(test_root, test_node)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_2(self):
        test_root = BinaryTreeNode(1)
        test_node_2 = BinaryTreeNode(2)
        test_node_3 = BinaryTreeNode(3)
        test_node_4 = BinaryTreeNode(4)
        test_node_5 = BinaryTreeNode(5)
        test_node_6 = BinaryTreeNode(6)

        test_root.left = test_node_2
        test_root.right = test_node_3

        test_node_2.left = test_node_4
        test_node_2.right = test_node_5

        test_node_3.right = test_node_6

        expected_outcome = [6]
        actual_outcome = cousins(test_root, test_node_4)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_case_3(self):
        test_root = BinaryTreeNode(1)
        test_node_2 = BinaryTreeNode(2)
        test_node_3 = BinaryTreeNode(3)
        test_node_4 = BinaryTreeNode(4)
        test_node_5 = BinaryTreeNode(5)
        test_node_6 = BinaryTreeNode(6)
        test_node_7 = BinaryTreeNode(7)
        test_node_8 = BinaryTreeNode(8)
        test_node_9 = BinaryTreeNode(9)
        test_node_10 = BinaryTreeNode(10)
        test_node_11 = BinaryTreeNode(11)
        test_node_12 = BinaryTreeNode(12)
        test_node_13 = BinaryTreeNode(13)
        test_node_14 = BinaryTreeNode(14)
        test_node_15 = BinaryTreeNode(15)


        test_root.left = test_node_2
        test_root.right = test_node_3
        
        test_node_2.left = test_node_4
        test_node_2.right = test_node_5
        test_node_3.left = test_node_6
        test_node_3.right = test_node_7

        test_node_4.left = test_node_8
        test_node_4.right = test_node_9
        test_node_5.left = test_node_10
        test_node_5.right = test_node_11
        test_node_6.left = test_node_12
        test_node_6.right = test_node_13
        test_node_7.left = test_node_14
        test_node_7.right = test_node_15

        expected_outcome = [8, 9, 10, 11, 14, 15]
        actual_outcome = cousins(test_root, test_node_12)
        self.assertEqual(expected_outcome, actual_outcome)

if __name__ == '__main__':
    unittest.main()