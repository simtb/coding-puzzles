"""
Given an input string, reverse the string word by word.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        
        tmp: List[str] = s.split(" ")
        tmp: List[str] = list(filter(lambda x: x != "", tmp))
        
        l: int = 0
        r: int = len(tmp) - 1

        while (l < r):
            tmp[l], tmp[r] = tmp[r], tmp[l]
            l += 1
            r -= 1
        
        return " ".join(tmp)
