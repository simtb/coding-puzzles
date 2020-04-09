"""
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.
"""

from typing import List

def countElements(arr: List[int]) -> int:
        temp: set = set()
        for x in arr:
            temp.add(x)
        
        count: int = 0
        
        for y in arr:
            if y + 1 in temp:
                count: int = count + 1
        
        return count
                
