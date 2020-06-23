"""
Given a complete binary tree, count the number of nodes.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    count: int = None
        
    def _helper(self, root: TreeNode) -> None:
        if root:
            self.count += 1
            self._helper(root.left)
            self._helper(root.right)
            
            
    def countNodes(self, root: TreeNode) -> int:
        if self.count is None:
            self.count = 0
        
        self._helper(root)
        
        return self.count
        
