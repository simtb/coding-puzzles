"""This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
"""

def is_palindrome(number: int) -> bool:
    original_number: int = number
    new_number: int = 0

    while number: 
        new_number: int = new_number * 10
        unit: int = number % 10
        new_number: int = new_number + unit
        
        number: int = number // 10

    return original_number == new_number
