"""
Reverse bits of a given 32 bits unsigned integer.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        # int cast with second argument as 2 for binary
        # {:032d} = 32 leading zeroes format specifier
        # format function for the 032 specifier - has to be done on an integer
        # bin(n)[2:] = convert to binary without the leading "0b"
        # [::-1] reverses the string
        return int("{:032d}".format(int(bin(n)[2:]))[::-1], 2)
