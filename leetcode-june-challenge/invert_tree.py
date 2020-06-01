"""
Invert a binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _invertTree(self, root:TreeNode) -> None:
        if root:
            tmp1: TreeNode = root.left
            tmp2: TreeNode = root.right
            root.left: TreeNode = tmp2
            root.right: TreeNode = tmp1
            self._invertTree(root.left)
            self._invertTree(root.right)
            
    def invertTree(self, root: TreeNode) -> TreeNode:
        self._invertTree(root)
        return root
        
