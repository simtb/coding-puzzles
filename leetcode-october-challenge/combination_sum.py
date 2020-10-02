"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
"""

class Solution:
    ans: List[List[int]] = None
        
    def backtrack(self, candidates: List[int], tmp: List[int], target: int, start: int) -> None:
        if sum(tmp) == target:
            self.ans.append(tmp[:])
        for i in range(start, len(candidates)):
            if sum(tmp[:]) < target:
                tmp.append(candidates[i])
                self.backtrack(candidates, tmp, target, i)
                tmp.pop()
                
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if self.ans is None:
            self.ans = []
            
        self.backtrack(candidates, [], target, 0)
        return self.ans
