"""This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

class SinglyLinkedListNode:
    def __init__(self, value):
        self.value: int = value 
        self.next: None = None 
    
    def __str__(self) -> str:
        return str(self.value)
    
def solution_1(head_a: SinglyLinkedListNode, head_b: SinglyLinkedListNode) -> SinglyLinkedListNode:
    visited: dict = {}
    current_node_a: SinglyLinkedListNode = head_a

    while current_node_a:
        visited[current_node_a.value]: bool = True
        current_node_a: SinglyLinkedListNode = current_node_a.next
    
    current_node_b: SinglyLinkedListNode = head_b

    while current_node_b:
        if visited.get(current_node_b.value):
            break
        current_node_b: SinglyLinkedListNode = current_node_b.next
    
    return current_node_b

"""
complexity: space = O(n)
            time = O(n + m)
"""

def solution_2(head_a: SinglyLinkedListNode, head_b: SinglyLinkedListNode) -> SinglyLinkedListNode:
    if head_a == None or head_b == None:
        return None
    
    pointer_a: SinglyLinkedListNode = head_a
    pointer_b: SinglyLinkedListNode = head_b

    while pointer_a.value != pointer_b.value:
        if pointer_a == None:
            pointer_a = head_b
        else:
            pointer_a = pointer_a.next
        
        if pointer_b == None:
            pointer_b = head_a
        else:
            pointer_b = pointer_b.next

    return pointer_a

"""
complexity: space = O(1)
            time = O(n + m)
"""

head_a: SinglyLinkedListNode = SinglyLinkedListNode(3)
head_a.next: SinglyLinkedListNode = SinglyLinkedListNode(7)
head_a.next.next: SinglyLinkedListNode = SinglyLinkedListNode(8)
head_a.next.next.next: SinglyLinkedListNode = SinglyLinkedListNode(10)

head_b: SinglyLinkedListNode = SinglyLinkedListNode(99)
head_b.next: SinglyLinkedListNode = SinglyLinkedListNode(1)
head_b.next.next: SinglyLinkedListNode = SinglyLinkedListNode(8)
head_b.next.next.next: SinglyLinkedListNode = SinglyLinkedListNode(10)

print(solution_1(head_a, head_b))
print(solution_2(head_a, head_b))