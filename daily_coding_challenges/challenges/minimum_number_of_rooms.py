"""
This problem was asked by Snapchat.
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

from typing import List
from itertools import combinations

def solution(time_intervals: List[tuple]) -> int:
    overlaps:List[tuple] = list(combinations(time_intervals, 2))
    number_of_overlaps: int = 0
    
    for overlap in overlaps:
        if overlap[0][0] in range(overlap[1][0], overlap[1][1] + 1) or overlap[0][1] in range(overlap[1][0], overlap[1][1] + 1):
            number_of_overlaps += 1

    if not number_of_overlaps:
        number_of_classrooms: int = 1
    else:
        number_of_classrooms: int = number_of_overlaps
    
    return number_of_classrooms

