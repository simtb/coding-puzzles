"""
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total_tilt: int = 0
    def tilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_sum: int = self.tilt(root.left)
        right_sum: int = self.tilt(root.right)
        tmp: int = abs(left_sum - right_sum)
        self.total_tilt += tmp
        return left_sum + right_sum + root.val
    
    def findTilt(self, root: TreeNode) -> int:
        self.tilt(root)
        return self.total_tilt
        
