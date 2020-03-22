"""
This problem was asked by Google.

UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:

For a single-byte character, the first bit must be zero.
For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.
Visually, this can be represented as follows.

 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Write a program that takes in an array of integers representing byte values, and returns whether it is a valid UTF-8 encoding.
"""

from typing import List


def is_utf_8_encoding(arr: List[str]) -> bool:
    byte_size: int = len(arr)

    if byte_size > 4:
        return False

    if byte_size == 1:
        a = arr[0]
        if a[0] == '0' and len(a) == 8:
            return True
        else: 
            False
    elif byte_size == 2:
        a = arr[0]
        b = arr[1]

        if a[0] == '1' and a[1] == '1' and a[2] == '0' and b[0] == '1' and b[1] == '0' and len(a) == 8 and len(b) == 8:
            return True
        return False

    elif byte_size == 3:
        a = arr[0]
        b = arr[1]
        c = arr[2]

        if a[0] == '1' and a[1] == '1' and a[2] == '1' and a[3] == '0' and b[0] == '1' and b[1] == '0' and c[0] == '1' and c[1] == '0' and len(a) == 8 and len(b) == 8 and len(c) == 8:
            return True
        return False
    
    elif byte_size == 4:
        a = arr[0]
        b = arr[1]
        c = arr[2]
        d = arr[3]

        if a[0] == '1' and a[1] == '1' and a[2] == '1' and a[3] == '1' and a[4] == '0' and b[0] == '1' and b[1] == '0' and c[0] == '1' and c[1] == '0' and d[0] == '1' and d[1] == '0' and len(a) == 8 and len(b) == 8 and len(c) == 8 and len(d) == 8:
            return True
        return False
    
    else:
        return False
        