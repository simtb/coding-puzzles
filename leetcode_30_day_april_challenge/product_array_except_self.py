"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
        product_arr: List[int] = [1] * len(nums)
        left: int = 1
        right: int = 1
        
        for i in range(len(nums)):
            product_arr[i]: int = product_arr[i] * left
            product_arr[-(i + 1)]: int = product_arr[-(i + 1)] * right
            left: int = left * nums[i]
            right: int = right * nums[-(i + 1)]
        
        return product_arr
