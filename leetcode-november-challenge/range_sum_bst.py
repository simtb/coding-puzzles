"""
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans: int = None
    
    def helper(self, root: TreeNode, low: int, high: int) -> None:
        if root:
            x: int = root.val
            
            if low <= x <= high:
                self.ans += x
            
            self.helper(root.left, low, high)
            self.helper(root.right, low, high)
    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if self.ans is None:
            self.ans = 0
        self.helper(root, low, high)
        
        return self.ans
        
