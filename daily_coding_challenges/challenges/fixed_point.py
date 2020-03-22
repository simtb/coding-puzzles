"""
This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
"""

from typing import List

def fixed_point(arr: List[int]) -> bool:
    length: int = len(arr)

    if length == 0:
        return False

    for i in range(length):
        element: int = arr[i]
        if element == i:
            return True

    return False
