"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""


class Solution:        
    def inRange(self, matrix: List[List[str]], position: tuple) -> bool:
        y: int = position[0]
        x: int = position[1]
        y_max: int = len(matrix)
        x_max: int = len(matrix[0])
        
        if 0 <= x < x_max and 0 <= y < y_max:
            return True
        return False
        
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        maximum_area: int = 0
        
        length: int = len(matrix)
        width: int = len(matrix[0])
            
        for i in range(length):
            for j in range(width):
                value: str = matrix[i][j]
                if value == "1":
                    width_max: int = len(matrix[0]) - j
                    if (width_max * width_max) > maximum_area:
                        k: int = 1
                        while k <= width_max:
                            all_ones: bool = True

                            for m in range(k):
                                for n in range(k):
                                    current_position: tuple = (i + m, j + n)
                                    if not self.inRange(matrix, current_position):
                                        all_ones: bool = False
                                        break
                                    else:
                                        current_value: str = matrix[i + m][j + n]
                                        if current_value == "0":
                                            all_ones: bool = False
                                            break
                            if all_ones:
                                current_area: int = k * k 
                                maximum_area: int = max(maximum_area, current_area)
                                k: int = k + 1
                            else:
                                break
        return maximum_area
