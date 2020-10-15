"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n: int = len(nums)
        
        start: int = 0
        count: int = 0
        
        while count < n:
            current = start
            prev = nums[start]
            
            while True:
                next_index: int = (current + k) % n
                nums[next_index], prev = prev, nums[next_index]
                current = next_index
                count += 1
                
                if start == current:
                    break
            start += 1


#Solution 2
]class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n: int = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
