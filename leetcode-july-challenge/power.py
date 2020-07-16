"""
Implement pow(x, n), which calculates x raised to the power n (xn)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        else:
            ans: float = 1.0
            if n < 0:
                x = 1 / x
                n = -n
            
            while n:
                if n % 2 == 1:
                    ans *= x
                x *= x
                n //= 2
                
            return ans
        
