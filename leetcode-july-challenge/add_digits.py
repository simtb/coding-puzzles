"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return num
        
        else:
            return ((num - 1) % 9) + 1

class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return num
        
        total: int = 0
        
        while num:
            total += (num % 10)
            num //= 10
        
        if total < 10:
            return total
        
        else:
            return self.addDigits(total)
