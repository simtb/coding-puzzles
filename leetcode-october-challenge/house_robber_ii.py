"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n: int = len(nums)
        
        if n == 1 or n == 2 or n == 3:
            return max(nums)
        
        tmp_1: List[int] = [0 for x in range(n)]
        max_a: int = 0
        i: int = 0
        
        while (i < n - 1):
            if i - 2 >= 0 and i - 3 >= 0:
                tmp_1[i] = nums[i] + max(tmp_1[i - 2], tmp_1[i - 3])
            elif i - 2 >= 0:
                tmp_1[i] = nums[i] + tmp_1[i - 2]
            else:
                tmp_1[i] = nums[i]
                
            max_a = max(max_a, tmp_1[i])
            i += 1
            
        tmp_2: List[int] = [0 for x in range(n)] 
        max_b: int = 0
        j: int = 1
        
        while (j < n):
            if j - 2 >= 0 and j - 3 >= 0:
                tmp_2[j] = nums[j] + max(tmp_2[j - 2], tmp_2[j - 3])
            elif i - 2 >= 0:
                tmp_2[j] = nums[j] + tmp_2[j - 2]
            else:
                tmp_2[j] = nums[j]
                
            max_b = max(max_b, tmp_2[i])
            j += 1
        
        return max(max_a, max_b)
