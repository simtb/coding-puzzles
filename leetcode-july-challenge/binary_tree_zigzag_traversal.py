"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        ans: List[List[int]] = []
        queue: List[TreeNode] = [root]
        i: int = 0
        
        while queue:
            level: List[int] = []
            n: int = len(queue)
            
            for j in range(n):
                if i % 2 == 0:
                    node: TreeNode = queue.pop(0)
                    if node:
                        queue.append(node.left)
                        queue.append(node.right)
                else:
                    node: TreeNode = queue.pop()
                    if node:
                        queue.insert(0, node.right)
                        queue.insert(0, node.left)
                if node:
                    level.append(node.val)
            
            if level:
                ans.append(level)
            
            i += 1
                
        return ans
