"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tmp: set = set()
        n: int = len(nums)
        
        if n < 3:
            return []
        
        nums.sort()
        
        for i in range(n - 2):
            x: int = i + 1
            y: int = n - 1
            
            while (x < y):
                if (nums[i] == 0 and nums[x] == 0 and nums[y] == 0):
                    if (nums[i], nums[x], nums[y]) in tmp:
                        break
                    else:
                        tmp.add((nums[i], nums[x], nums[y]))
                        
                if nums[i] + nums[x] + nums[y] == 0:
                    tmp.add((nums[i], nums[x], nums[y]))
                    x += 1
                
                elif nums[i] + nums[x] + nums[y] > 0:
                    y -= 1
                
                else:
                    x += 1
                    
        ans: List[List[int]] = []
        
        for triplet in tmp:
            ans.append(triplet)
        
        return ans
