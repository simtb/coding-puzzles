"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        return ((1 << num.bit_length()) - 1) ^ num
