"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
"""

class Solution:
    ans: List[List[int]] = None
    
    def backtrack(self, leftover: List[int], tmp: List[int], index: int) -> None:
        self.ans.append(tmp[:])
        
        n: int = len(leftover)
        
        for i in range(index, n):
            tmp.append(leftover[i])
            self.backtrack(leftover, tmp, i + 1)
            tmp.pop()
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if self.ans is None:
            self.ans = []
        
        self.backtrack(nums, [], 0)
        
        return self.ans
        
