"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans: List[List[int]] = []
        queue: List[TreeNode] = [root] 
        
        while (queue):
            level: List[int] = []
            n: int = len(queue)
            
            for i in range(n):
                current: TreeNode = queue.pop(0)
                if current:
                    level.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
            if level:
                ans.insert(0, level)
                
        return ans
