from typing import List

def max_subarray(nums: List[int]) -> int:
        
        ans: int = float("-inf")
        a: int = 0
            
        for num in nums:
            a += num
            ans: int = max(ans, a)
            a: int = max(a, 0)
                
        return ans
