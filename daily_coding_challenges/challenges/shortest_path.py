"""
This problem was asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""

from typing import List

def shortest_path(points: List[List[int]]) -> int:

    length_of_path = 0
    starting_point: List[int] = points.pop(0)

    while True:

        if points == []:
            break
        
        current_point: List[int] = starting_point
        next_point: List[int] = points[0]
        
        while True:
            if current_point == next_point:
                break
            
            if next_point[0] > current_point[0] and next_point[1] == current_point[1]:
                current_point[0]: int = current_point[0] + 1

            elif next_point[0] < current_point[0] and next_point[1] == current_point[1]:
                current_point[0]: int = current_point[0] - 1

            elif next_point[0] == current_point[0] and next_point[1] > current_point[1]:
                current_point[1]: int = current_point[1] + 1

            elif next_point[0] == current_point[0] and next_point[1] < current_point[1]:
                current_point[1]: int = current_point[1] - 1
            
            elif next_point[0] < current_point[0] and next_point[1] < current_point[1]:
                current_point[0]: int = current_point[0] - 1
                current_point[1]: int = current_point[1] - 1

            elif next_point[0] > current_point[0] and next_point[1] > current_point[1]:
                current_point[0]: int = current_point[0] + 1
                current_point[1]: int = current_point[1] + 1
            
            elif next_point[0] < current_point[0] and next_point[1] > current_point[1]:
                current_point[0]: int = current_point[0] - 1
                current_point[1]: int = current_point[1] + 1
            
            elif next_point[0] > current_point[0] and next_point[1] < current_point[1]:
                current_point[0]: int = current_point[0] + 1
                current_point[1]: int = current_point[1] - 1
            
            length_of_path: int = length_of_path + 1

        current_point: List[int] = points.pop(0)
    
    return length_of_path
