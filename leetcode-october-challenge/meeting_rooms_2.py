"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n: int = len(intervals)
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        intervals.sort(key=lambda x: x[0])
        
        meeting_rooms: List[int] = [None] * n
        needed: int = 0
        
        for i in range(n):
            for j in range(n):
                if meeting_rooms[j] == None:
                    meeting_rooms[j] = i
                    needed += 1
                    break
                else:
                    if intervals[i][0] >= intervals[meeting_rooms[j]][1]:
                        meeting_rooms[j] = i
                        break
        
        return needed
