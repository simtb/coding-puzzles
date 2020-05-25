"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.
"""

class Solution:
    def _maxUncrossedLines(self, A: List[int], B: List[int], indexA: int, indexB: int, tmp: dict = None) -> int:
        if tmp is None:
            tmp: dict = {}
        
        if indexA < 0:
            tmp[(indexA, indexB)]: int = 0
            return 0
        if indexB < 0:
            tmp[indexA, indexB]: int = 0
            return 0 
        
        if A[indexA] == B[indexB]:
            if tmp.get((indexA - 1, indexB - 1)) is None:
                tmp[(indexA - 1, indexB - 1)]: int = self._maxUncrossedLines(A, B, indexA - 1, indexB - 1, tmp)
            a: int = tmp.get((indexA - 1, indexB - 1))
            tmp[(indexA, indexB)]: int = a + 1
        else:
            if tmp.get((indexA - 1, indexB)) is None:
                tmp[(indexA - 1, indexB)]: int = self._maxUncrossedLines(A, B, indexA - 1, indexB, tmp)
            if tmp.get((indexA, indexB - 1)) is None:
                tmp[(indexA, indexB - 1)]: int = self._maxUncrossedLines(A, B, indexA, indexB - 1, tmp)
            
            b: int = tmp.get((indexA - 1, indexB))
            c: int = tmp.get((indexA, indexB - 1))
            tmp[(indexA, indexB)]: int = max(b, c)      
        return tmp[indexA, indexB]
    
                    
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n: int = len(A) - 1
        m: int = len(B) - 1
        
        ans: int = self._maxUncrossedLines(A, B, n, m)
        return ans
