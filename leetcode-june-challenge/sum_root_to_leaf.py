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
    tmp: List[int] = None
        
    def preOrder(self, root: TreeNode, current: str) -> None:
        if root:
            if self.isLeaf(root):
                current += str(root.val)
                self.tmp.append(int(current))
            else:
                current += str(root.val)
                self.preOrder(root.left, current)
                self.preOrder(root.right, current)
                
                
    def isLeaf(self, root: TreeNode) -> bool:
        return not root.left and not root.right
    
    
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if self.tmp is None:
            self.tmp: List[int] = []
        
        self.preOrder(root, "")
        return sum(self.tmp)
        
