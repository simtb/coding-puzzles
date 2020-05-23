"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        output: str = ""
        frequency: dict = {}
        
        for char in s:
            frequency[char]: int = frequency.get(char, 0) + 1
        
        tmp: List[str] = sorted(frequency, key=lambda x: frequency[x], reverse=True)
        
        for char in tmp:
            output += (char * frequency.get(char))
        
        return output
        
