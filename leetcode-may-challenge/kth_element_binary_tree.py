"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    tmp: List[TreeNode] = None
    def _f(self, root: TreeNode) -> List[int]:
        if root:
            self._f(root.left)
            if self.tmp is None:
                self.tmp: List[TreeNode] = []
            self.tmp.append(root.val)
            self._f(root.right) 
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self._f(root)
        return self.tmp[k - 1]
        
        
