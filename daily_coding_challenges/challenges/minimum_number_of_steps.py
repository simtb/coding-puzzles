"""
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

from typing import List

def inbound(matrix: List[list], coordinates: List[int]) -> bool:
    lower_x_bound: int = 0
    upper_x_bound: int = len(matrix[0])
    lower_y_bound: int = 0
    upper_y_bound: int = len(matrix)

    y_coordinate: int = coordinates[0]
    x_coordinate: int = coordinates[1]

    if x_coordinate in range(lower_x_bound, upper_x_bound) and y_coordinate in range(lower_y_bound, upper_y_bound):
        return True
    return False 

def solution(matrix: List[list], start: tuple, end: tuple) -> int:

    if start == end:
        return 0
    if not matrix: 
        return None
    
    matrix[start[0]][start[1]] = 0
    coordinates_queue: List[tuple] = [start]
    
    while coordinates_queue:
        current_position: tuple = coordinates_queue.pop(0)
        distance_from_start: int = matrix[current_position[0]][current_position[1]]
        directions: List[tuple] = [(0, 1), (0, -1), (1, 0), (-1,0)]

        for direction in directions:
            new_coordinates: tuple = (current_position[0] + direction[0], current_position[1] + direction[1])
            if inbound(matrix, new_coordinates) and matrix[new_coordinates[0]][new_coordinates[1]] != True:
                new_distance_from_start: int = distance_from_start + 1

                if matrix[new_coordinates[0]][new_coordinates[1]] == False:
                    matrix[new_coordinates[0]][new_coordinates[1]]: int = new_distance_from_start
                elif isinstance(matrix[new_coordinates[0]][new_coordinates[1]], int) and new_distance_from_start < matrix[new_coordinates[0]][new_coordinates[1]]:
                    matrix[new_coordinates[0]][new_coordinates[1]]: int = new_distance_from_start
                else:
                    continue
                
                coordinates_queue.append(new_coordinates)
    if matrix[end[0]][end[1]] != True and matrix[end[0]][end[1]] != False:
        return matrix[end[0]][end[1]]
    else:
        return None









