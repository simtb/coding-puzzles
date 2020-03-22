"""
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""

from typing import List, Tuple

def top_left_to_bottom_right(N: int, M: int) -> int:
    matrix: List[List[int]] = [[0 for n in range(M)] for m in range(N)]
    
    if N == 0 or M == 0:
        return 0
    
    start: Tuple[int] = (0, 0)
    end: Tuple[int] = (N - 1, M - 1)
    queue: List[Tuple[int]] = [start]
    visited: dict = {}

    while queue:
        current_position: Tuple[int] = queue.pop(0)
        if not visited.get(current_position):
            visited[current_position]: bool = True
            right_of_current_position: Tuple[int] = (current_position[0], current_position[1] + 1)
            down_of_current_position: Tuple[int] = (current_position[0] + 1, current_position[1])
            if check_in_matrix(right_of_current_position, N, M):
                if matrix[current_position[0]][current_position[1]] == 0 and matrix[right_of_current_position[0]][right_of_current_position[1]] == 0:
                    matrix[right_of_current_position[0]][right_of_current_position[1]]: int = 1
                else:
                    matrix[right_of_current_position[0]][right_of_current_position[1]]: int =  matrix[right_of_current_position[0]][right_of_current_position[1]] + matrix[current_position[0]][current_position[1]]
                queue.append(right_of_current_position)

            if check_in_matrix(down_of_current_position, N, M):
                if matrix[current_position[0]][current_position[1]] == 0 and matrix[down_of_current_position[0]][down_of_current_position[1]] == 0:
                    matrix[down_of_current_position[0]][down_of_current_position[1]]: int = 1
                else:
                    matrix[down_of_current_position[0]][down_of_current_position[1]]: int = matrix[down_of_current_position[0]][down_of_current_position[1]] + matrix[current_position[0]][current_position[1]]
                queue.append(down_of_current_position)

    return matrix[end[0]][end[1]]
    

def check_in_matrix(position: Tuple[int], N: int, M: int) -> bool:
    horizontal_position: int = position[1]
    vertical_position: int = position[0]

    if horizontal_position < M and vertical_position < N:
        return True
    else: 
        return False
