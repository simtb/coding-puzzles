"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n: int = len(nums)
        current_number: int = None
        
        for i in range(n - 1):
            if i % 3 == 0:
                current_number: int = nums[i]
            else:
                current_value: int = nums[i]
                if current_value != current_number:
                    if current_value > current_number:
                        return current_number
        
        return nums[n - 1]
        
