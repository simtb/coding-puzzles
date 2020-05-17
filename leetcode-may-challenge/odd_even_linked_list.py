"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        odd: ListNode = head
        
        if head.next:
            even: ListNode = head.next
        else:
            return head
        
        current_odd: ListNode = odd
        current_even: ListNode = even
        
        while True:
            
            if current_odd.next.next == None:
                break
            
            if current_even.next.next == None:
                current_odd.next: ListNode = current_odd.next.next
                current_odd: ListNode = current_odd.next
                current_even.next: ListNode = None
                break
                
            current_odd.next: ListNode = current_odd.next.next
            current_even.next: ListNode = current_odd.next.next
            
            current_odd: ListNode = current_odd.next
            current_even: ListNode = current_even.next

        current_odd.next: ListNode = even
        return head
        
        
