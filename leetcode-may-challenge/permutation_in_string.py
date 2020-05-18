"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s2 == "":
            return False
        
        n: int = len(s2)
        m: int = len(s1)
        
        counterA: dict = {}
        counterB: dict = {}
            
        for i in range(n):
            if i < m - 1:
                counterA[s2[i]]: int = counterA.get(s2[i], 0) + 1
                counterB[s1[i]]: int = counterB.get(s1[i], 0) + 1
                    
            elif i == m - 1:
                counterA[s2[i]]: int = counterA.get(s2[i], 0) + 1
                counterB[s1[i]]: int = counterB.get(s1[i], 0) + 1
                
                if counterA == counterB:
                    return True
            else:
                counterA[s2[i]]: int = counterA.get(s2[i], 0) + 1
                
                j: int = i - m
                letter: str = s2[j]
                
                if letter in counterA:
                    counterA[letter] -= 1
                    if counterA[letter] <= 0:
                        del counterA[letter]
                
                if counterA == counterB:
                    return True
                
        return False
