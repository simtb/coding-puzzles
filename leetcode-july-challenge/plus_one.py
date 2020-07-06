"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = [str(x) for x in digits]
        return list(str(int(''.join(tmp)) + 1))

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n: int = len(digits)
        i: int = 0
        
        if n == 1:
            digits[n - 1] += 1
        
        while True:
            if i == n - 1:
                break
            
            if digits[n - 1 - i] == 9 and i == 0:
                digits[n - 1 - i] = 0
                digits[n - 1 - i - 1] += 1
            
            elif digits[n - 1 - i] == 10:
                digits[n - 1 - i] = 0
                digits[n - 1 - i - 1] += 1
            
            elif digits[n - 1 - i] != 9 and i == 0:
                digits[n - 1 - i] += 1
                
                break
            elif digits[n - 1 - i] != 9 and i != 0:
                break
                
            i += 1
        
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
            
            
        return digits
