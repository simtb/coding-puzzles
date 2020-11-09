"""
Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: TreeNode, current_max, current_min) -> int:
        if not root:
            return abs(current_max - current_min)
        else:
            current_max = max(current_max, root.val)
            current_min = min(current_min, root.val)
            left: int = self.helper(root.left, current_max, current_min)
            right: int = self.helper(root.right, current_max, current_min)
            
            return max(left, right)
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.helper(root, root.val, root.val)
