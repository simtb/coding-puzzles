import unittest
from challenges.boustrophedon_order import BinaryTreeNode, boustrophedon_order

class TestBoustrophedonoOrder(unittest.TestCase):

    node_1 = BinaryTreeNode(1)
    node_2 = BinaryTreeNode(2)
    node_3 = BinaryTreeNode(3)
    node_4 = BinaryTreeNode(4)
    node_5 = BinaryTreeNode(5)
    node_6 = BinaryTreeNode(6)
    node_7 = BinaryTreeNode(7)
    node_8 = BinaryTreeNode(8)
    node_9 = BinaryTreeNode(9)
    node_10 = BinaryTreeNode(10)
    node_11 = BinaryTreeNode(11)
    node_12 = BinaryTreeNode(12)
    node_13 = BinaryTreeNode(13)
    node_14 = BinaryTreeNode(14)
    node_15 = BinaryTreeNode(15)


    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    node_4.left = node_8
    node_4.right = node_9

    node_5.left = node_10
    node_5.right = node_11

    node_6.left = node_12
    node_6.right = node_13

    node_7.left = node_14
    node_7.right = node_15

    def test_case_0(self):
        expected_result = [1, 3, 2, 4, 5, 6, 7, 15, 14, 13, 12, 11, 10, 9, 8]
        actual_result = boustrophedon_order(self.node_1)
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
