"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        max_width: int = 0
        queue: List[TreeNode] = [(root, 1)]
            
        while queue:
            level: List[TreeNode] = []
            n: int = len(queue)
            
            for i in range(n):
                element: tuple = queue.pop(0)
                level.append(element)
            
            if level:
                m: int = len(level)
                max_width = max(max_width, level[n - 1][1] - level[0][1] + 1)
            
            for element in level:
                parent: TreeNode = element[0]
                if parent.left:
                    queue.append((parent.left, 2 * element[1]))
                if parent.right:
                    queue.append((parent.right, (2 * element[1]) + 1))
        
        return max_width
