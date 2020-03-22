"""
This problem was asked by Netflix.

Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.
"""

from typing import List

def pythagorean_triple(arr: List[int]) -> bool:
    if len(arr) < 3:
        return False
    
    seen: dict = {}

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            a: int = arr[i]
            b: int = arr[j]
            pair: tuple = (a, b)
            if seen.get(pair) == None:
                seen[pair]: bool = True
                c_squared: int = (a * a) + (b * b)
                for element in arr:
                    if element == c_squared:
                        return True
    return False




