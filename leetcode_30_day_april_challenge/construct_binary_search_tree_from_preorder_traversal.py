"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List

class Solution:
    def firstGreater(self, arr: List[int], index: int) -> int:
        n: int = len(arr)
        value: int = arr[index]
        if index + 1 < n:
            for i in range(index + 1, n):
                if arr[i] > value:
                    return i
        return -1
    
        
    def firstSmaller(self, arr: List[int], index: int) -> int:
        n: int = len(arr)
        value: int = arr[index]
        if index + 1 < n:
            for i in range(index + 1, n):
                if arr[i] < value:
                    return i
        return -1
    
                
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None 
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        n: int = len(preorder)
        i: int = 0
            
        root: TreeNode = TreeNode(preorder[0])
        queue: List[TreeNode] = [root]
        seen: dict = {root.val: 0}
            
        while queue:
            current_node: TreeNode = queue.pop(0)
            if not current_node:
                pass
            else:
                index: int = seen.get(current_node.val)
                if index is None:
                    pass
                else:
                    first_smaller_index: int = self.firstSmaller(preorder, index)
                    first_greater_index: int = self.firstGreater(preorder, index)
                    
                    if first_smaller_index != -1:
                        if first_greater_index == -1 or first_smaller_index < first_greater_index:
                            smaller_value: int = preorder[first_smaller_index]
                            if not seen.get(smaller_value):
                                seen[smaller_value]: int = first_smaller_index
                                new_left_child: TreeNode = TreeNode(smaller_value)
                                current_node.left: TreeNode = new_left_child
                                queue.append(new_left_child)
                    
                    if first_greater_index != -1:
                        greater_value: int = preorder[first_greater_index]
                        if not seen.get(greater_value):
                            seen[greater_value]: int = first_greater_index
                            new_right_child: TreeNode = TreeNode(greater_value)
                            current_node.right: TreeNode = new_right_child
                            queue.append(new_right_child)
                
        return root
