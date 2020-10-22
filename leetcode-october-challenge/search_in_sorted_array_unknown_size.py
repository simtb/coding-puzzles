"""
Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.
"""

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        
        left: int = 0
        right: int = 1
        
        while reader.get(right) < target:
            left = right
            right <<= 1
            
        while (left <= right):
            mid: int = (left + right) >> 1
            
            if reader.get(mid) == target:
                return mid
            
            elif reader.get(mid) > target:
                right = mid - 1
            
            else:
                left = mid + 1
