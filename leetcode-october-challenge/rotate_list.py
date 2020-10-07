"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        q = collections.deque()
        current: ListNode = head
        
        while(current):
            q.append(current.val)
            current = current.next
        
        q.rotate(k)
        n: int = len(q)
        current: ListNode = head
            
        for i in range(n): 
            tmp: int = q.popleft()
            current.val = tmp
            current = current.next
        
        return head
