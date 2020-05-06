"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter: dict = {}
        majority: int = (len(nums) // 2) + 1
        
        for num in nums:
            counter[num]: int = counter.get(num, 0) + 1
            if counter.get(num) == majority:
                return num
        
