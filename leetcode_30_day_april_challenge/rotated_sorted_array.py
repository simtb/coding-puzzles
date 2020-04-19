"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""

from typing import List

def search(array: List[int], target: int) -> int:
        if array == []:
            return -1

        left: int = 0
        right: int = len(array) - 1

        if left == 0 and right == 0 and array[0] == target:
            return 0

        while left != right:
            if array[left] == target:
                return left

            elif array[right] == target:
                return right

            mid: int = left + ((right - left) // 2)

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

        return -1
