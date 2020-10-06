"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _helper(self, root: TreeNode, val: int) -> None:
        if root:
            if val < root.val:
                if root.left:
                    self._helper(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    self._helper(root.right, val)
                else:
                    root.right = TreeNode(val)
        
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        self._helper(root, val)
        return root
