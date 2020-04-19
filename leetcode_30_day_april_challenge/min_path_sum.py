"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
"""

from typing import List

class Solution:
    def validPosition(self, grid: List[List[int]], y: int, x: int) -> bool:
        y_max: int = len(grid) - 1
        x_max: int = len(grid[0]) - 1
        if 0 <= x <= x_max and 0 <= y <= y_max:
            return True
        return False
        
    def _minPathSum(self, grid: List[List[int]], endpoint: tuple, seen: dict=None) -> int:
        
        #base case
        if endpoint[0] == 0 and endpoint[1] == 0:
            return grid[0][0]
        
        else:
            y: int = endpoint[0]
            x: int = endpoint[1]
            if self.validPosition(grid, y, x):
                value: int = grid[y][x]
                new_point_1: tuple = (y - 1, x)
                new_point_2: tuple = (y, x - 1)
                if seen is None:
                    seen: dict = {}
                if not seen.get(new_point_1):
                    seen[new_point_1]: int = self._minPathSum(grid, new_point_1, seen)
                if not seen.get(new_point_2):
                    seen[new_point_2]: int = self._minPathSum(grid, new_point_2, seen)
                
                value_1: int = seen[new_point_1]
                value_2: int = seen[new_point_2]
        
                return min(value + value_1, value + value_2)
            else:
                return float('+inf')
            
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        y_max: int = len(grid) - 1
        x_max: int = len(grid[0]) - 1
        endpoint: tuple = (y_max, x_max)
        min_path_sum: int = self._minPathSum(grid, endpoint)
        
        return min_path_sum
