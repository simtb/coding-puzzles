"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        tmp: List[int] = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
        n: int = len(matrix)
        m: int = len(matrix[0])
        squares: int = 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    a: int = 0
                    b: int = 0
                    c: int = 0
                    
                    if 0 <= i - 1 < n and 0 <= j - 1 < m:
                        a: int = tmp[i - 1][j - 1]
                    if 0 <= i - 1 < n and 0 <= j < m:
                        b: int = tmp[i - 1][j]
                    if 0 <= i < n and 0 <= j - 1 < m:
                        c: int = tmp[i][j - 1]
                    
                    tmp[i][j]: int = min(a, b, c) + 1
                    squares += tmp[i][j]
                
        return squares
        
