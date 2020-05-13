"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
""""

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        single: int = 0
        for num in nums:
            single ^= num
        return single 
        

#binary search
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1
        
        while left < right:
            mid: int = (left + right) // 2
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid
        return nums[left]
