"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        tmp: dict = {}
        
        for num in nums:
            tmp[num] = tmp.get(num, 0) + 1
        
        res: List[int] = []
        
        for key in tmp:
            if tmp[key] == 1:
                res.append(key)
        
        return res
