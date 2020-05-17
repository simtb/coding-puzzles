"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""


from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        n: int = len(s)
        m: int = len(p)
        tmp: dict = {}
        p_counter: dict = {}
        start_indicies: List[int] = []
        
        if m > n:
            return start_indicies
        
        for i in range(n):
            if i < m - 1:
                tmp[s[i]]: int = tmp.get(s[i], 0) + 1
                p_counter[p[i]]: int = p_counter.get(p[i], 0) + 1
            
            elif i == m - 1:
                tmp[s[i]]: int = tmp.get(s[i], 0) + 1
                p_counter[p[i]]: int = p_counter.get(p[i], 0) + 1
                    
                if tmp == p_counter:
                    start_indicies.append(i - m + 1)
            else:
                tmp[s[i]]: int = tmp.get(s[i], 0) + 1
                
                j: int = i - m
                letter: str = s[j]
                    
                if letter in tmp:
                    tmp[letter] -= 1
                    if tmp[letter] <= 0:
                        del tmp[letter]
                    
                if tmp == p_counter:
                    start_indicies.append(j + 1)
        
        return start_indicies
