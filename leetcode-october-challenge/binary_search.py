"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums)
        index: int = -1
            
        while left < right:
            mid: int = (left + right) // 2
            
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return index 
