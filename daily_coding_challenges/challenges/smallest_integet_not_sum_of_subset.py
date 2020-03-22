"""This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time."""

from typing import List

def solution(array: List[int]) -> int:
    
    smallest_integer_not_sum_of_subset: int = 0
    running_total: int = 0 

    for i in range(len(array)):
        smallest_integer_not_sum_of_subset: int = smallest_integer_not_sum_of_subset + 1
        current_value: int = array[i]
        running_total: int = running_total + current_value 

        if smallest_integer_not_sum_of_subset != current_value and smallest_integer_not_sum_of_subset != running_total:
            return smallest_integer_not_sum_of_subset

    return smallest_integer_not_sum_of_subset + 1


print(solution([1, 2, 3, 10]))
print()
print(solution([1, 2, 3, 4]))
