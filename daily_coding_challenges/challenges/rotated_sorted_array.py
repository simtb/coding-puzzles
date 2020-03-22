"""
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""

from typing import List 

def rotated_search(array: List[int], target: int) -> int:
    if array == []:
        return None

    left: int = 0
    right: int = len(array) - 1

    if left == 0 and right == 0 and array[0] == target:
        return 0
 
    while left != right:
        if array[left] == target:
            return left

        elif array[right] == target:
            return right

        mid: int = (left + right) // 2
       
        if array[mid] == target:
            return mid
 
        elif array[left] < target < array[mid]:
            right: int = mid - 1
        
        elif target < array[mid] < array[left]:
            right: int = mid - 1
        
        elif target < array[right] < array[mid]:
            left: int = mid + 1
        
        elif array[mid] < target < array[right]:
            left: int = mid + 1
        
        elif array[left] > array[mid]:
            right: int = mid - 1

        elif array[mid] > array[right]:
            left: int = mid + 1 
        
        else:
            break

    return None