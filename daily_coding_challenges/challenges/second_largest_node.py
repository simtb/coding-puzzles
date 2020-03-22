"""
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
"""

class BinarySearchTreeNode:
    def __init__(self, value):
        self.value: int = value 
        self.left: BinarySearchTreeNode = None
        self.right: BinarySearchTreeNode = None


def solution(root: BinarySearchTreeNode) -> BinarySearchTreeNode:
    if root == None:
        return None
    
    queue: list = [root]
    values: dict = {}

    while queue:
        current_node: BinarySearchTreeNode = queue.pop(0)
        values[current_node.value]: BinarySearchTreeNode = current_node
        if current_node.left != None:
            queue.append(current_node.left)
        if current_node.right != None:
            queue.append(current_node.right)
    
    largest_key: int = None
    second_largest_key: int = None

    for key in values:
        if largest_key == None and second_largest_key == None:
            largest_key: int = key
        elif (largest_key != None and second_largest_key == None) and key > largest_key:
            tmp: int = largest_key
            largest_key: int = key
            second_largest_key: int = tmp 
        elif (largest_key != None and second_largest_key == None) and key < largest_key:
            second_largest_key: int = key
        elif(largest_key != None and second_largest_key != None) and key > largest_key:
            tmp: int = largest_key
            largest_key: int = key
            second_largest_key: int = tmp 
        elif(largest_key != None and second_largest_key != None) and second_largest_key < key < largest_key:
            second_largest_key: int = key

    return values[second_largest_key]

def pre_order_traversal(root: BinarySearchTreeNode, tmp: dict) -> BinarySearchTreeNode:
    if root == None: 
        pass
    if root != None:
        tmp[root.value] = root
        pre_order_traversal(root.left, tmp)
        pre_order_traversal(root.right, tmp)
    return tmp

def solution_2(values: dict) -> BinarySearchTreeNode:
    if values == {}:
        return None

    tmp: list = []
    for value in values:
        tmp.append(value)
    key: int = sorted(tmp)[-2]

    return values[key]
