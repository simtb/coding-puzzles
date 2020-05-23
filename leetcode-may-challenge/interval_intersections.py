"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
"""

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a: int = 0
        b: int = 0
        intervals: List[List[ints]] = []
        
        while a < len(A) and b < len(B):
            interval_starting, interval_ending = max(A[a][0], B[b][0]), min(A[a][1], B[b][1])
            
            if interval_starting <= interval_ending:
                intervals.append([interval_starting, interval_ending])
            
            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1
                
        return intervals
            
