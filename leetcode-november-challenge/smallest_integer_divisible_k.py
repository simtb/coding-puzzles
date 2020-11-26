'''
Given a positive integer K, you need to find the length of the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N. If there is no such N, return -1.

Note: N may not fit in a 64-bit signed integer.
'''

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if (K % 2 == 0) or (K % 5 == 0):
            return -1
        
        remainders: set = set()
        x: int = 1
        ans: int = 1
        
        while True:
            remainder = x % K
            if remainder == 0:
                return ans
            if remainder in remainders:
                break
            else:
                remainders.add(remainder)
            
            ans += 1
            x *= 10
            x += 1
        
        return -1
