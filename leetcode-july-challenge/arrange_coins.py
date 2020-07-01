"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
"""

import math

class Solution:
    def quadraticSolver(self, c: int) -> int:
        discriminant: float = math.sqrt(1 + 8 * c)
        return int((-1 + discriminant) / 2)
    
    def arrangeCoins(self, n: int) -> int:
        return self.quadraticSolver(n)


