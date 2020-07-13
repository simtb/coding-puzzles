"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

iteratively
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        q1 = [p]
        q2 = [q]
        
        while q1 and q2:
            a = q1.pop(0)
            b = q2.pop(0)
            
            if not a and b:
                return False
            if a and not b:
                return False
            if a and b:
                if a.val != b.val:
                    return False
            
                q1.append(a.left)
                q1.append(a.right)
                q2.append(b.left)
                q2.append(b.right)
        
        if not q1 and not q2:
            return True
        return False


recursively

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and q:
            return False
        if p and not q:
            return False
        if not p and not q:
            return True
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
