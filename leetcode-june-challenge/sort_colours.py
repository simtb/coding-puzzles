"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        frequency: dict = {0: 0, 1: 0, 2: 0}
        
        for num in nums:
            frequency[num]: int = frequency.get(num, 0) + 1
        
        i: int = 0
        
        while (i < len(nums)):
            if frequency.get(0) > 0:
                nums[i]: int = 0
                frequency[0] -= 1
            elif frequency.get(1) > 0:
                nums[i]: int = 1
                frequency[1] -= 1
            else:
                nums[i]: int = 2
                frequency[2] -= 1
            
            i += 1
