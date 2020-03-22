"""
This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

import itertools
from typing import List, Tuple

def solution(number: List[int]) -> List[List[int]]:
    
    length_of_number: int = len(number)
    perms: List[Tuple[int]] = list(itertools.permutations(number, length_of_number))
    return perms

print(solution([1,2,3]))