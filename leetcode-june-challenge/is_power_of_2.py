"""
Given an integer, write a function to determine if it is a power of two.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while(n):
            if n == 1:
                return True
            if n % 2 == 1:
                return False
            n //= 2
        return False

	def isPowerOfTwo(self, n: int) -> bool:
        return (n and not (n & (n - 1)))
