"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self._helper(root, 0)
    
    def _helper(self, root: TreeNode, current_sum: int) -> int:
        if (not root):
            return 0
        
        new_sum: int = (current_sum * 10) + root.val
            
        if (not root.left and not root.right):
            return new_sum
        
        return self._helper(root.left, new_sum) + self._helper(root.right, new_sum)
