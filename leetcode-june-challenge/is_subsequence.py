"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        
        n: int = len(t)
        m: int = len(s)
        firstChar: str = s[0]
        
        for i in range(n):
            currentChar: str = t[i]
            if currentChar == firstChar:
                j: int = i
                k: int = 0
                while j < n:
                    if k == m:
                        break
                    check: str = s[k]
                    tmp: str = t[j]
                    if check == tmp:
                        k += 1
                    j += 1
                print(k)
                if k == m:
                    return True
        return False
