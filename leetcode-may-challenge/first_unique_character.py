"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""

#The solution below is only valid if you are running python 3.7 or later. otherwise you'll need to import an OrderedDict for frequency and initialise it

class Solution:
    def firstUniqChar(self, s: str) -> int:
        n: int = len(s)
        frequency: dict = dict()
        first_seen: dict = {}
        
        for i in range(n):
            if first_seen.get(s[i], None) == None:
                first_seen[s[i]]: int = i
                frequency[s[i]]: int = 1
            else:
                frequency[s[i]] += 1
        for key in frequency:
            if frequency[key] == 1:
                return first_seen[key]
        return -1
