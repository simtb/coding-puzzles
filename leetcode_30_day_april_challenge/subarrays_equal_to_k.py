"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
"""

from typing import List

def subarraySum(nums: List[int], k: int) -> int:

        array_sums: dict = {0: 1}
        total: int = 0
        number_of_subarrays: int = 0
            
        for num in nums:
            total += num
            
            if array_sums.get(total - k):
                number_of_subarrays += array_sums.get(total - k)
            
            array_sums[total]: int = array_sums.get(total, 0) + 1
        
        return number_of_subarrays
