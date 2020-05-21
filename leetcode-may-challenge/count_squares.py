"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        n: int = len(matrix)
        m: int = len(matrix[0])
        squares: int = 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    if i and j:
                        matrix[i][j]: int = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
                    squares += matrix[i][j]
                
        return squares        
