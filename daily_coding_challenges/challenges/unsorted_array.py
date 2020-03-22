"""Given an array of integers out of order, 
determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted. 
For example, given [3, 7, 5, 6, 9], you should return (1, 3).
"""

from typing import List, Tuple

# def bubble_sort(array: List[int]) -> List[int]:
#     size: int = len(array)

#     for i in range(size):
#         for j in range(size - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]

#     return array

def unsorted_array(array: List[int]) -> Tuple[int]:
    inital_array: List[int] = array
    sorted_array: List[int] = sorted(array)

    temp: List[int] = []
    for i in range(len(inital_array)):
        if inital_array[i] != sorted_array[i]:
            temp.append(i)

    if temp:
        return (temp[0], temp[-1])
    else:
        return ()
        

print(unsorted_array([5,4,3,2,1]))