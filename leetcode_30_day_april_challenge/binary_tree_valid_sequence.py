"""
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
"""

from typing import List 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    outcome: bool = False
        
    def isLeaf(self, root: TreeNode) -> bool:
        return not root.left and not root.right
    
    def _isValidSequence(self, root: TreeNode, arr: List[int], index) -> bool:
        if index < len(arr):
            if root:
                if root.val == arr[index]:
                    if self.isLeaf(root) and index == len(arr) - 1:
                        self.outcome: bool = True
                    else:
                        new_index: int = index + 1
                        self._isValidSequence(root.left, arr, new_index)
                        self._isValidSequence(root.right, arr, new_index)

    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        outcome: bool = self._isValidSequence(root, arr, 0)
        return self.outcome
