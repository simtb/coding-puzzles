"""This problem was asked by Apple.

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space."""

def fib(n: int) -> int:
    
    a: int = 0
    b: int = 1
    m: int = n - 1

    while m:
        c: int = a + b
        a: int = b
        b: int = c
        m: int = m - 1

    return a



