"""
In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].
"""

from typing import List


class BinaryTreeNode:
    def __init__(self, value: int):
        self.value: int = value
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None
    
    def __str__(self):
        return str(self.value)


def get_all_nodes(root: BinaryTreeNode) -> List[BinaryTreeNode]:
    nodes: List[BinaryTreeNode] = []
    queue: List[BinaryTreeNode] = [root]

    while queue:
        current_node: BinaryTreeNode = queue.pop(0)
        nodes.append(current_node)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    
    return nodes

def height(root: BinaryTreeNode, node: BinaryTreeNode) -> int:
    if root == None:
        return -1

    distance: int = -1
    if root.value == node.value:
        return distance + 1
    else:
        distance: int = height(root.left, node)
        if distance >= 0:
            return distance + 1
        else:
            distance = height(root.right, node)
            if distance >= 0:
                return distance + 1

    return distance

def boustrophedon_order(root: BinaryTreeNode) -> List[int]:
    nodes: List[BinaryTreeNode] = get_all_nodes(root)
    levels: dict = {}

    for node in nodes:
        level: int = height(root, node)

        if level in levels:
            levels[level].append(node.value)
        else:
            levels[level]: int = [node.value]
    
    temp: List[int] = []

    for level in levels:
        if level % 2 == 0:
            temp += levels[level]
        else:
            temp += levels[level][::-1]
    
    return temp


