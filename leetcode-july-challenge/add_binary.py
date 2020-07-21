"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        tmp: int = int(a, 2) + int(b, 2)
        return bin(tmp)[2:]

