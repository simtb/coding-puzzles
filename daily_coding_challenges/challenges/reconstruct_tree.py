"""
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
"""
from typing import List

class BinaryTreeNode:
    def __init__(self, value: object):
        self.value: object = value 
        self.left: object = None
        self.right: object = None
    
    def __eq__(self, other):
        if other != None:
            return self.value == other.value
    
    def __str__(self) -> None:
        return str(self.value)

def preorder_traversal(root: BinaryTreeNode, store: List[BinaryTreeNode]) -> List[BinaryTreeNode]:
    if root != None:
        store.append(root.value)
        preorder_traversal(root.left, store)
        preorder_traversal(root.right, store)
    return store 

def inorder_traversal(root: BinaryTreeNode, store: List[BinaryTreeNode]) -> List[BinaryTreeNode]:
    if root != None:
        inorder_traversal(root.left, store)
        store.append(root.value)
        inorder_traversal(root.right, store)
    return store 

def reconstruct_tree(preorder_list: List[object], inorder_list: List[object]) -> BinaryTreeNode:
    length_of_preorder_list: int = len(preorder_list)
    length_of_inorder_list: int = len(inorder_list)
    
    if length_of_preorder_list != length_of_inorder_list:
        raise Exception("Reconstruction not possible")
    
    if length_of_preorder_list == 0 and length_of_inorder_list == 0:
        return None

    if length_of_preorder_list == 1: 
        root_value: object = preorder_list[0]
        root: BinaryTreeNode = BinaryTreeNode(root_value)
        return root
    
    root_value: object = preorder_list[0]
    root: BinaryTreeNode = BinaryTreeNode(root_value)
    current_node: BinaryTreeNode = root
    position_of_root_value: int = inorder_list.index(root_value)
    position_of_current_node: int = position_of_root_value

    node_stack: list = []

    for i in range(1, length_of_preorder_list):
        value: object = preorder_list[i]
        position: int = inorder_list.index(value)
        new_node: BinaryTreeNode = BinaryTreeNode(value)

        if position < position_of_current_node:
            current_node.left: BinaryTreeNode = new_node
            node_stack.append(current_node)
            current_node: BinaryTreeNode = new_node
            position_of_current_node: int = position
        
        elif position > position_of_current_node:
            if not node_stack:
                node_stack.append(current_node)
            current_node: BinaryTreeNode = node_stack.pop()
            current_node.right: BinaryTreeNode =  new_node
            current_node: BinaryTreeNode = new_node
            position_of_current_node: int = position

    return root 


