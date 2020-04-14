"""
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.
"""

from typing import List

def shift(s: str, direction: int, amount: int) -> str:
        n: int = len(s)
        s_: List[str] = [None] * n
            
        if not direction:
            for i in range(n):
                i_: int = i - amount
                s_[i_]: str = s[i]
        else:
            for j in range(n):
                j_: int = (j + amount) % n
                s_[j_]: str = s[j]
            
        return "".join(s_)
            
        
    def stringShift(s: str, shifts: List[List[int]]) -> str:
        new_string: str = s
        
        for shift in shifts:
            direction: int = shift[0]
            amount: int = shift[1]
            new_string: str = shift(new_string, direction, amount)

        return new_string
