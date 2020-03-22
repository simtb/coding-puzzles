"""
This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
"""

from typing import List 

class BinarySearchTreeNode:
    def __init__(self, value: int):
        self.value: int = value
        self.left: BinarySearchTreeNode = None
        self.right: BinarySearchTreeNode = None

def valid_bst(root: BinarySearchTreeNode) -> bool:
    if root == None:
        return True
    
    queue: List[BinarySearchTreeNode] = [root]

    while True:
        if queue == []:
            return True

        current_node: BinarySearchTreeNode = queue.pop(0)
        parent_value: int = current_node.value

        if current_node.left != None:
            left_value: int = current_node.left.value
            if left_value > parent_value:
                return False
            else:
                queue.append(current_node.left)
        
        if current_node.right != None:
            right_value: int = current_node.right.value
            if right_value < parent_value:
                return False
            else:
                queue.append(current_node.right)


root = BinarySearchTreeNode(5)

root.left = BinarySearchTreeNode(3)
root.right = BinarySearchTreeNode(8)

root.left.left = BinarySearchTreeNode(2)
root.left.right = BinarySearchTreeNode(4)

root.right.right = BinarySearchTreeNode(10)

print(valid_bst(root))