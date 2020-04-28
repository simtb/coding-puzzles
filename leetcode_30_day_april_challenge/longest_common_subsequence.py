"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.
"""


class Solution:
    def _longestCommonSubsequence(self, text1: str, text2: str, length1: str, length2: str, tmp: dict = None) -> int:
        if not length1 or not length2:
            return 0
        
        key: tuple = (length1, length2)
        if tmp is None:
            tmp: dict = {}
        
        if text1[length1 - 1] == text2[length2 - 1]:
            tmp[key]: int = self._longestCommonSubsequence(text1, text2, length1 - 1, length2 - 1, tmp) + 1
            
        else:
            value1: int = tmp.get((length1 - 1, length2))
            if not value1:
                value1: int = self._longestCommonSubsequence(text1, text2, length1 - 1, length2, tmp)
            value2: int = tmp.get((length1, length2 - 1))
            if not value2:
                value2: int = self._longestCommonSubsequence(text1, text2, length1, length2 - 1, tmp)
            tmp[key]: int = max(value1, value2)
        return tmp[key]
    
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1: int = len(text1)
        length2: int = len(text2)
        
        return self._longestCommonSubsequence(text1, text2, length1, length2)
