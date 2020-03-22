"""
This problem was asked by Twitter.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
"""

from typing import List

class BinaryTreeNode:

    def __init__(self, value: int):
        self.value: int = value 
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other) -> bool:
        return self.value == other.value


def is_leaf(node: BinaryTreeNode) -> bool:
    return not node.left and not node.right

def path_to_node(root: BinaryTreeNode, node: BinaryTreeNode, stack: List[BinaryTreeNode]) -> List[BinaryTreeNode]:
    if root:
        if root != stack[0]:
            stack.append(root)
        path_to_node(root.left, node, stack)
        if root == node:
            return stack
        else:
            stack.pop()
        path_to_node(root.right, node, stack)

def lowest_common_ancestor(root: BinaryTreeNode, node_a: BinaryTreeNode, node_b: BinaryTreeNode) -> BinaryTreeNode:
    if not root:
        return None

    stack: List[BinaryTreeNode] = []
    stack.append(root)

    route_to_node_a: List[BinaryTreeNode] = path_to_node(root, node_a, stack)


a = BinaryTreeNode(1)

a.left = BinaryTreeNode(2)
a.right = BinaryTreeNode(3)

a.left.left = BinaryTreeNode(4)
a.left.right = BinaryTreeNode(5)

a.right.left = BinaryTreeNode(6)
a.right.right = BinaryTreeNode(7)

print(path_to_node(a, BinaryTreeNode(2), stack=[a]))