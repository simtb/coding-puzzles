"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parents: dict = {root.val: None}
        parent_heights: dict = {None: -1}
        queue: List[TreeNode] = [root]
        
        while queue:
            if parents.get(x) and parents.get(y):
                break
            
            current_node: TreeNode = queue.pop(0)
            parent_value: int = parents.get(current_node.val)
            parent_height: int = parent_heights.get(parent_value)
            current_height: int = parent_height + 1
            parent_heights[current_node.val]: int = current_height
            
            if current_node.left:
                parents[current_node.left.val]: int = current_node.val
                queue.append(current_node.left)
            if current_node.right:
                parents[current_node.right.val]: int = current_node.val
                queue.append(current_node.right)
                
        
        if x != y and parents.get(x) != parents.get(y) and parent_heights.get(parents.get(x)) == parent_heights.get(parents.get(y)):
            return True
        return False
