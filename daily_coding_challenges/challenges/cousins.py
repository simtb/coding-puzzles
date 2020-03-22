"""
This problem was asked by Yext.

Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents. For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \   \
4   5   6
Given a binary tree and a particular node, find all cousins of that node.

"""

from typing import Dict, List

class BinaryTreeNode:
    def __init__(self, value):
        self.value: int = value
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None
    
    def __eq__(self, other) -> bool:
        return self.value == other.value
    
    def __str__(self) -> None:
        return str(self.value)


def level_and_parent(root:BinaryTreeNode, node: BinaryTreeNode) -> dict:
    if not root:
        return -1
    
    levels: Dict[BinaryTreeNode, int] = {root.value: 0}
    parent: Dict[BinaryTreeNode, int] = {}
    queue: List[BinaryTreeNode] = [root]

    while queue:
        current_node: BinaryTreeNode = queue.pop(0)
        child_level: int = levels[current_node.value] + 1
        if current_node == node:
            return {'level': levels[current_node.value], 'parent': parent[current_node.value]}
        if current_node.left:
            parent[current_node.left.value]: BinaryTreeNode = current_node.value
            levels[current_node.left.value]: int = child_level
            queue.append(current_node.left)
        if current_node.right:
            parent[current_node.right.value]: BinaryTreeNode = current_node.value
            levels[current_node.right.value]: int = child_level
            queue.append(current_node.right)

def cousins(root: BinaryTreeNode, node: BinaryTreeNode) -> List[BinaryTreeNode]:
    if root == node:
        return []

    node_info: dict = level_and_parent(root, node)
    level: int = node_info['level']
    parent: int = node_info['parent']
    cousins: List[BinaryTreeNode] = []
    queue: List[BinaryTreeNode] = [root]

    while queue:
        current_node: BinaryTreeNode = queue.pop(0)
        if not current_node == root:
            current_node_info: dict = level_and_parent(root, current_node)
            current_node_level: int = current_node_info['level']
            current_node_parent: it = current_node_info['parent']
            if current_node_level > level:
                break
            if current_node_level == level and current_node_parent != parent:
                cousins.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return cousins


            


