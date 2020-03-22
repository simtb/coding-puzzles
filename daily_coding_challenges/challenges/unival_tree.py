"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""

class BinaryTreeNode:
    def __init__(self, value):
        self.value: int = value
        self.left_child: None = None 
        self.right_child: None = None

children = []
count = 0

def is_unival(node: BinaryTreeNode) -> bool:
    global children
    if node:
        if node.left_child:
            children.append(node.left_child.value)
        else:
            children.append(None)
        if node.right_child:
            children.append(node.right_child.value)
        else:
            children.append(None)
        is_unival(node.left_child)
        is_unival(node.right_child)
    
    for i in range(0, len(children), 2):
        if children[i] != children[i + 1]:
            return False
    return True

def solution(root: BinaryTreeNode) -> None:
    global children
    global count
    if root:
        if is_unival(root):
            count += 1
        children = []
        solution(root.left_child)
        solution(root.right_child)


root = BinaryTreeNode(0)
root.left_child = BinaryTreeNode(1)
root.right_child = BinaryTreeNode(0)

root.right_child.left_child = BinaryTreeNode(1)
root.right_child.right_child = BinaryTreeNode(0)

root.right_child.left_child.left_child = BinaryTreeNode(1)
root.right_child.left_child.right_child = BinaryTreeNode(1)

solution(root)
print(count)







