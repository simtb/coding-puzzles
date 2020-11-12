"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""

class Solution:
    permutations: List[int] = None
    seen: set = None
    
    def backtrack(self, leftover: List[int], tmp: List[int], size: int) -> None:
        n: int = len(leftover)
        m: int = len(tmp)
            
        if size == m:
            a: List[str] = [str(x) for x in tmp[:]]
            b: str = "".join(a)
            if b not in self.seen:
                self.seen.add(b)
                self.permutations.append(tmp[:])
        
        for i in range(n):
            tmp.append(leftover[i])
            self.backtrack(leftover[: i] + leftover[i + 1: ], tmp, size)
            tmp.pop()
    
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if self.permutations is None:
            self.permutations = []
        
        if self.seen is None:
            self.seen = set()
        
        length: int = len(nums)
        self.backtrack(nums, [], length)
        
	return self.permutations  
