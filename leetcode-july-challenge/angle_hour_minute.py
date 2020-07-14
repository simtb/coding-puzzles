"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        tmp: float = abs(0.5 * (60 * hour - (11 * minutes)))
        return min(tmp, 360 - tmp)
        


