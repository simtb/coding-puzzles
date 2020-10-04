Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n: int = len(intervals)
            
        if not n:
            return 0
        
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        covered: int = 0
        current: int = intervals[0][1]
        
        for i in range(1, n):
            if intervals[i][1] <= current:
                covered += 1
            else:
                current = intervals[i][1]
                
        return n - covered
