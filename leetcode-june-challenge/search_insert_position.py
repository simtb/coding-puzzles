"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        ans: int = -1
        left: int = 0
        right: int = len(nums) - 1
        
        while (left <= right):
            mid: int = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                ans: int = mid
                left: int = mid + 1
            
            else:
                right: int = mid - 1
                    
        return ans + 1
        
