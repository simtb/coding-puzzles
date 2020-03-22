"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

def solution(string_1: str, string_2: str) -> int:
    if string_1 == "":
        return len(string_2)
    if string_2 == "":
        return len(string_1)
    
    if string_1 == string_2:
        return 0

    number_changes: int = 0
    difference_in_length: int = abs(len(string_1) - len(string_2))
    string_1_counter: dict = {}

    for char in string_1:
        if string_1_counter.get(char) == None:
            string_1_counter[char]: int = 1
        else:
            string_1_counter[char] += 1
    
    for char in string_2:
        if string_1_counter.get(char) == None:
            number_changes += 1
        elif string_1_counter.get(char) != None or string_1_counter.get(char) > 0:
            string_1_counter[char] -= 1
        else:
            number_changes += 1
    
    return number_changes + difference_in_length

    
