"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        
        n: int = len(num)
        i: int = 0
        stack: list = []
        
        while i < n:
            
            while k > 0 and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
                
            stack.append(num[i])
            i += 1
        
        while k > 0:
            stack.pop()
            k -= 1
        
        return str(int("".join(stack)))
