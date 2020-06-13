"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
"""

class Solution:
    def largestDivisibleSubset(self, nums) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        ans: List[List[int]] = [[num] for num  in nums]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(ans[i]) < len(ans[j]) + 1:
                    ans[i] = ans[j] + [nums[i]]
                    
        return max(ans, key=len)
