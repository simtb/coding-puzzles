"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return -1
        
        slow: int = nums[0]
        fast: int = nums[nums[0]]
        
        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        
        while (slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
