# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
"""

class Solution:
    diameter = 0
    
    def maxDepth(self, root):
        if root is None:
            return 0   
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        self.diameter = max(self.diameter, leftDepth + rightDepth)
        
        return max(leftDepth, rightDepth) + 1
            
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxDepth(root)
        return self.diameter


#### brute force
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List

class Solution:
    def inOrder(self, root: TreeNode, inorder: List[int]=[]) -> List[TreeNode]:
        if root:
            self.inOrder(root.left, inorder)
            inorder.append(root.val)
            self.inOrder(root.right, inorder)
        return inorder
    
    def distanceFromRoot(self, root: TreeNode, value: int) -> int:
        if not root:
            return 0
        
        queue: List[TreeNode] = [root]
        parent_heights: dict = {None: -1}
        child_to_parent: dict = {root.val: None}
            
        while queue:
            current_node: TreeNode = queue.pop(0)
            parent: int = child_to_parent[current_node.val]
            parent_height: int = parent_heights[parent]
            current_height: int = parent_height + 1
            parent_heights[current_node.val]: int = current_height
            
            if current_node.val == value:
                break
                    
            left_child: TreeNode = current_node.left
            right_child: TreeNode = current_node.right 
            
            if left_child:
                queue.append(left_child)
                child_to_parent[left_child.val]: int = current_node.val
            if right_child:
                queue.append(right_child)
                child_to_parent[right_child.val]: int = current_node.val
        
        return current_height
    
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        inorder: List[int] = self.inOrder(root)
        size: int = len(inorder)
        index_of_root_node: int = 0
        
        for i in range(size):
            if inorder[i] == root.val:
                index_of_root_node: int = i
                break
                
        max_left: int = 0
        max_right: int = 0
            
        if index_of_root_node == 0:
            pass
        else:
            left_nodes: List[int] = inorder[: index_of_root_node]
            for value in left_nodes:
                height_left: int = self.distanceFromRoot(root, value)
                if height_left > max_left:
                    max_left: int = height_left
        if index_of_root_node == size - 1:
            pass
        else:
            right_nodes: List[int] = inorder[index_of_root_node + 1:]
            for value in right_nodes:
                height_right: int = self.distanceFromRoot(root, value)
                if height_right > max_right:
                    max_right: int = height_right
        
        diameter: int = max_left + max_right
         
        return diameter
