"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer: int = float('-inf')
    def _maxPathSum(self, root: TreeNode, answer: int = float('-inf')) -> int:
        if not root:
            return 0
        
        x: int = self._maxPathSum(root.left)
        y: int = self._maxPathSum(root.right)
        
        self.answer: int = max(self.answer, x + y + root.val)
        return max(0, root.val + max(x, y))
    
    def maxPathSum(self, root: TreeNode) -> int:
        self._maxPathSum(root)
        return self.answer
        
