"""
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.
"""

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort(key=lambda x:x[0])
        greatest: int = float('-inf')
        n: int = len(arrays)
        
        for i in range(1, n):
            greatest = max(greatest, arrays[i][-1])
        
        a: int = abs(greatest - arrays[0][0])
            
        arrays.sort(key=lambda x: -x[-1])
        smallest: int = float('+inf')
        
        for j in range(1, n):
            smallest = min(smallest, arrays[j][0])
        
        b: int = abs(arrays[0][-1] - smallest)
        
        return max(a, b)
