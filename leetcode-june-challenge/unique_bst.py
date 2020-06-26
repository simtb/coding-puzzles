"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"""

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        
        ans: int = 0
        for i in range(n):
            ans += (self.numTrees(i) * self.numTrees(n - i - 1))
        
        return ans
