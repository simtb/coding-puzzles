"""Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements."""

from typing import List

def move_zeros(arr: List[int]) -> List[int]:
    n: int = len(arr)
    
    for i in range(n):
        changes: int = 0
        for j in range(n - 1 - i):
            if arr[j] == 0 and arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                changes: int = changes + 1 
        if not changes:
            break
    return arr


def moveZeros(arr: List[int]) -> List[int]:
    n: int = len(arr)
    nxt: int = 0
    
    for x in arr:
        if x != 0:
            arr[nxt]: int = x
            nxt: int = nxt + 1
    
    for i in range(nxt, n):
        arr[i]: int = 0
    
    return arr





