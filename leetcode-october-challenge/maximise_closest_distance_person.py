"""
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n: int = len(seats)
        
        greatestDistance = 0
        last_occupied_seat: int = None
        
        for i in range(n):
            occupied: int = seats[i]
            
            if occupied and last_occupied_seat is None:
                last_occupied_seat = i
                greatestDistance = i
            elif occupied and last_occupied_seat is not None:
                distance_between_two_seats = i - last_occupied_seat
                mid_point = distance_between_two_seats // 2
                greatestDistance = max(greatestDistance, mid_point)
                last_occupied_seat = i
            elif not occupied:
                pass
        if last_occupied_seat != n - 1:
            greatestDistance = max(greatestDistance, n - 1 - last_occupied_seat)
            
        return greatestDistance


