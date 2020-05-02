"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left: int = 0
        right: int = n + 1
        first_bad: int = n + 1
            
        while left < right:
            mid: int = (left + right) // 2
            
            if isBadVersion(mid):
                first_bad: int = mid
                right: int = mid
            else:
                left: int = mid + 1
                    
        return first_bad
