"""Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node."""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#efficient two pointer solution
def middleNode_1(head: ListNode) -> ListNode:
        pointer_a: ListNode = head
        pointer_b: ListNode = head
        
        while True:
            if pointer_b == None:
                break
                
            if pointer_b.next == None:
                break
            
            next_node_a: ListNode = pointer_a.next
            pointer_a: ListNode = next_node_a
            
            next_node_b: ListNode = pointer_b.next.next
            pointer_b: ListNode = next_node_b
            
                
        return pointer_a


#conceptually easier solution but not as efficient as solution above 
def middleNode_2(head: ListNode) -> ListNode: 
        size: int = 0
        current_node: ListNode = head
        
        while current_node:
            size += 1
            next_node: ListNode = current_node.next
            current_node: ListNode = next_node
        
        middle_index: int = size // 2
        current_node: ListNode = head
        i: int = 0
        
        while True:
            if i == middle_index:
                break
            next_node: ListNode = current_node.next
            current_node: ListNode = next_node
            i += 1
            
        return current_node
