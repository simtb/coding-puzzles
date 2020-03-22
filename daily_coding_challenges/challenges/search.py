"""This problem was asked by Netflix.

Given a sorted list of integers of length N, determine if an element x is in the list without performing any multiplication, division, or bit-shift operations.

Do this in O(log N) time.
"""

from typing import List

def binary_search(arr: List[int], x: int) -> bool:
    if len(arr) == 0:
        return False

    left: int = 0
    right: int = len(arr) - 1

    while left != right:
        middle = left + (right - left) // 2

        if arr[middle] < x:
            left: int = middle + 1
        else:
            right: int = middle 

    if arr[left] == x:
        return True
    else:
        return False


def binary_search_recursively(arr: List[int], x: int) -> bool:
    if len(arr) == 0:
        return False

    left: int = 0
    right: int = len(arr) - 1
    middle: int = left + (right - left) // 2

    if arr[middle] == x:
        return True
    elif arr[middle] < x:
        new_arr: List[int] = arr[middle + 1:]
    else:
        new_arr: List[int] = arr[left: middle + 1]
    
    return binary_search(new_arr, x)


