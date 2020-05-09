"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        left: int = 1
        right: int = num // 2
        
        while left <= right:
            mid: int = (left + right) // 2
            
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left: int = mid + 1
            else:
                right: int = mid - 1
        return False
