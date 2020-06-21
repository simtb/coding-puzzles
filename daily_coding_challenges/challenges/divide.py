"""
This problem was asked by Nextdoor.

Implement integer division without using the division operator. Your function should return a tuple of (dividend, remainder) and it should take two numbers, the product and divisor.

For example, calling divide(10, 3) should return (3, 1) since the divisor is 3 and the remainder is 1.

Bonus: Can you do it in O(log n) time?
"""


def divide(n: int, m: int) -> tuple:
    if m == 0:
        return (float('+inf'), 0)
    if m > n:
        return (0, n)

    left: int  = 0
    right: int = n

    closest: int = 0

    while (left <= right):
        mid: int = (left + right) // 2
        value: int = mid * m
        
        if value == n:
            return (mid, 0)
        elif value > n:
            right: int = mid - 1
        
        else:
            closest: int = max(closest, mid)
            left: int = mid + 1
    
    remainder: int = n - (closest * m)
    
    return (closest, remainder)

print(divide(10, 3))