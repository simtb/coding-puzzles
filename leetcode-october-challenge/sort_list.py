"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        tmp: List[int] = []
        
        current: ListNode = head
            
        while (current):
            tmp.append(current.val)
            current = current.next
        
        tmp.sort()
        
        current: int = head
        i: int = 0
            
        while (current):
            current.val = tmp[i]
            i += 1
            current = current.next
        
        return head
