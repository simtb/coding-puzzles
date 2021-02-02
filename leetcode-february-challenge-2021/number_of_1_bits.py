class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)
        ans: int = 0
        
        for _ in x:
            if _ == '1':
                ans += 1
        
        return ans