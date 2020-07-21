"""
Remove all elements form a linked list of integers that have the value val.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        fake_head: ListNode = ListNode(-1)
        fake_head.next = head
        current = fake_head
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return fake_head.next
