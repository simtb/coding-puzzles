"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
"""

def rangeBitwiseAnd(m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while(m < n):
            n -= (n & -n)
        if m == n: return m
        return n
