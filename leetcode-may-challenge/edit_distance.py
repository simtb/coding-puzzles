"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""
class Solution:
    def _minDistance(self, word1: str, word2: str, n: int,  m: int, tmp: dict = None) -> int:
        if n == 0:
            return m
        if m == 0:
            return n
        if tmp is None:
            tmp: dict = {}
        
        if word1[n - 1] == word2[m - 1]:
            tmp[(n, m)]: int = tmp.get((n, m), self._minDistance(word1, word2, n - 1, m - 1, tmp))
            return tmp[(n, m)]
        
        else:
            if (n - 1, m) not in tmp:
                tmp[(n - 1, m)]: int = self._minDistance(word1, word2, n - 1, m, tmp)
            if (n, m - 1) not in tmp:
                tmp[(n, m - 1)]: int = self._minDistance(word1, word2, n, m - 1, tmp)
            if (n - 1, m - 1) not in tmp:
                tmp[(n - 1, m - 1)]: int = self._minDistance(word1, word2, n - 1, m - 1, tmp)
            return 1 + min(tmp[(n - 1, m)], tmp[(n, m - 1)], tmp[(n - 1, m - 1)])
        
    def minDistance(self, word1: str, word2: str) -> int:
        return self._minDistance(word1, word2, len(word1), len(word2))
