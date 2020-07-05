"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        ugly_numbers: List[int] = [0] * n
        ugly_numbers[0]: int = 1
        
        two: int = 0
        three: int = 0
        five: int = 0
        
        for i in range(1, n):
            ugly_numbers[i]: int = min(ugly_numbers[two] * 2, ugly_numbers[three]* 3, ugly_numbers[five] * 5)
            if ugly_numbers[i] == ugly_numbers[two] * 2:
                two += 1
            
            if ugly_numbers[i] == ugly_numbers[three] * 3:
                three += 1
            
            if ugly_numbers[i] == ugly_numbers[five] * 5:
                five += 1
            
        return ugly_numbers[n - 1]
        
