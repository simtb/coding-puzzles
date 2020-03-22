"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""

from typing import List

class BinaryTreeNode:
    def __init__(self, value: int):
        self.value: int = value
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None
    
    def __str__(self):
        return str(self.value)


def tree_level_print(root: BinaryTreeNode) -> None:
    if root == None:
        return None

    queue: List[BinaryTreeNode] = [root]

    while True:
        if queue == []:
            break
        
        current_node: BinaryTreeNode = queue.pop(0)
        print(current_node)

        if current_node.left != None:
            queue.append(current_node.left)
        if current_node.right != None:
            queue.append(current_node.right)



a: BinaryTreeNode = BinaryTreeNode(1)

a.left: BinaryTreeNode= BinaryTreeNode(2)
a.right: BinaryTreeNode = BinaryTreeNode(3)

a.left.left: BinaryTreeNode = BinaryTreeNode(4)
a.left.right: BinaryTreeNode = BinaryTreeNode(5)
a.right.left: BinaryTreeNode = BinaryTreeNode(6)
a.right.right: BinaryTreeNode = BinaryTreeNode(7)


tree_level_print(a)
    