"""
Given a Linked List of size N, where every node represents a linked list and contains two pointers of its type:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.

You have to flatten the linked list to a single linked list which is sorted.
"""
from typing import List

class Node:
    def __init__(self, value):
        self.value: int = value 
        self.next: None = None
        self.bottom: None = None


def solution_1(head: Node) -> Node:

    if head == None:
        return None

    queue: List[Node] = [head]
    values: List[int] = []

    while queue:
        current_node: Node = queue.pop(0)
        value: int = current_node.value
        values.append(value)
        if current_node.bottom != None:
            queue.append(current_node.bottom)
        if current_node.next != None:
            queue.append(current_node.next)
    
    sorted_values: List[int] = sorted(values)
    flattened_head: Node = Node(sorted_values[0])
    current_flattened_node: Node = flattened_head

    for i in range(1, len(sorted_values)):
        new_node: Node = Node(sorted_values[i])
        current_flattened_node.next: Node = new_node
        current_flattened_node: node = new_node
    
    return flattened_head
    
