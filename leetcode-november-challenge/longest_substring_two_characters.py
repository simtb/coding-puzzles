"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n: int = len(s)
        
        if n < 3:
            return n
        
        window_size: int = 2
        window: dict = dict()
        
        left: int = 0
        right: int = 0
        
        while right < n:
            window[s[right]] = right
            right += 1
            
            if len(window) == 3:
                last_index = min(window.values())
                del window[s[last_index]]
                left = last_index + 1
            window_size = max(window_size, right - left)
            
        return window_size
