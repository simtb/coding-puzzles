"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts: dict = {0: -1}
        max_length: int = 0
        count: int = 0
            
        for i in range(len(nums)):
            if not nums[i]:
                count -= 1
            else:
                count += 1
            
            if count in counts:
                max_length: int = max(max_length, i - counts.get(count))
            else:
                counts[count]: int = i
        
        return max_length
