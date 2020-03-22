"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""
from typing import List

class BinaryTreeNode:
    def __init__(self, value: object):
        self.value: object = value
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None
    
    def __str__(self) -> None:
        return str(self.value)
    
    def __eq__(self, value: object):
        return self.value == value

def invert_tree(root: BinaryTreeNode) -> BinaryTreeNode:

    if root is None:
        return None
    
    queue: List[BinaryTreeNode] = [root]

    while True:
        if queue == []: 
            break

        current_node: BinaryTreeNode = queue.pop()

        if current_node != None:
            current_node.left, current_node.right = current_node.right, current_node.left
            queue.append(current_node.left)
            queue.append(current_node.right)
    
    return root