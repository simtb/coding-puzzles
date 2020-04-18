"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

from typing import List 


def validPosition(position: tuple, x_max: int, y_max: int) -> bool:
        current_x: int = position[1]
        current_y: int = position[0]
        if (0 <= current_x <= x_max) and (0 <= current_y <= y_max):
            return True
        return False 
    
    def numIslands(grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        number_of_islands: int = 0
        land_visited: dict = {}
        x_max: int = len(grid[0]) - 1
        y_max: int = len(grid) - 1

        for i in range(y_max + 1):
            for j in range(x_max + 1):
                if grid[i][j] == '1':
                    if not land_visited.get((i, j)):
                        queue: List[int] = [(i, j)]
                        current_island_size: int = 0
                        while queue:
                            current_position: tuple = queue.pop(0)
                            if validPosition(current_position, x_max, y_max):
                                if grid[current_position[0]][current_position[1]] == '1':
                                    if not land_visited.get((current_position[0], current_position[1])):
                                        land_visited[(current_position[0], current_position[1])]: bool = True
                                        queue.append((current_position[0], current_position[1] + 1))
                                        queue.append((current_position[0] + 1, current_position[1]))
                                        queue.append((current_position[0], current_position[1] - 1))
                                        queue.append((current_position[0] - 1, current_position[1]))
                                        current_island_size += 1
    
                        if current_island_size:
                            number_of_islands: int = number_of_islands + 1
                                    
        return number_of_islands
