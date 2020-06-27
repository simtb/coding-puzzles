"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp: List[int] = [0 for x in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[i]: int = float('+inf')
            j: int = 1
            while (j * j <= i):
                dp[i] = min(dp[i], 1 + dp[i - j * j])
                j += 1
                
                
        return dp[n]
