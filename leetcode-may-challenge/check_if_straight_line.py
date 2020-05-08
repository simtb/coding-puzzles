"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""
from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinate_1: List[int] = coordinates[0]
        coordinate_2: List[int] = coordinates[1]
        if coordinate_1[0] != coordinate_2[0]:
            m: int = (coordinate_2[1] - coordinate_1[1]) // (coordinate_2[0] - coordinate_1[0])
            c: int = coordinate_1[1] - (m * coordinate_1[0])
            for coordinate in coordinates:
                if coordinate[1] != (m * coordinate[0]) + c:
                    return False
            return True
        
        else:
            x: int = coordinates[0][0]
            for coordinate in coordinates:
                if coordinate[0] != x:
                    return False
            return True
