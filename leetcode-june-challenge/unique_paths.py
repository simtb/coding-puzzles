"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

#Solution 1 dynamic programming

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp: int = [[0 for x in range(m)] for y in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    
        return dp[n - 1][m - 1]

#Solution 2 combinations 

class Solution:
    def factorial(self, n: int) -> int:
        if (n == 0 or n == 1):
            return 1
        
        dp: List[int] = [1 for x in range(n + 1)]
        
        for i in range(2, n + 1):
            dp[i] = i * dp[i - 1]
        
        return dp[n]
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        a: int = n + m - 2
        b: int = n - 1
        
        return self.factorial(a) // (self.factorial(b) * self.factorial(a - b))
