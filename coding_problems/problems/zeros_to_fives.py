"""
Given a integer as a input and replace all the ‘0’ with ‘5’ in the integer.
Examples:

    102 - 152
    1020 - 1525 
Use of array to store all digits is not allowed.
"""

def solution(number: int) -> int:
    if number == 0:
        return 5

    tmp: int = number
    power: int = 0

    while tmp:
        digit: int = tmp % 10
        if digit == 0:
            number_to_add: int = 5 * (10 ** power)
            number += number_to_add
        tmp //= 10
        power += 1

    return number