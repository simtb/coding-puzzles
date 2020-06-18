"""
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n: int = len(citations)
        h: int = 0
        left: int = 0
        right: int = n - 1
        
        while (left <= right):
            mid: int = (left + right) // 2
            max_possible_h: int = n - mid
            num: int = citations[mid]
            
            if num >= max_possible_h:
                h: int = max(h, max_possible_h)
                right: int = mid - 1
            else:
                left: int = mid + 1
                    
        return h

