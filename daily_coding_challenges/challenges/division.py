"""
This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
"""

def division(p: int, q: int) -> int:
    if q == 0:
        return 
    if q >= p:
        return 0

    answer: int = 0
    current_value: int = p

    while True:
        current_value: int = current_value - q
        if current_value < 0:
            return answer
        else:
            answer: int = answer + 1
    
    return answer

print(division(10, 5))
print(division(1000, 5))
print(division(5, 5))
print(division(3, 5))
print(division(5, 0))
print(division(103, 5))