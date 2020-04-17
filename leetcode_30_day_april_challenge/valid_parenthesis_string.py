"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
"""

from typing import List

def checkValidString(s: str) -> bool:
        if not s:
            return True
        
        n: int = len(s)
        positions_of_open_braces: List[int] = []
        positions_of_wildcards: List[int] = []
        
        for i in range(n):
            char: str = s[i]
            if char == "(":
                positions_of_open_braces.append(i)
            elif char == '*':
                positions_of_wildcards.append(i)
            else:
                if positions_of_open_braces:
                    positions_of_open_braces.pop()
                else:
                    if positions_of_wildcards:
                        positions_of_wildcards.pop()
                    else:
                        return False
                    
        while positions_of_open_braces:
            if not positions_of_wildcards:
                return False
            else:
                if positions_of_open_braces.pop() > positions_of_wildcards.pop():
                    return False
        return True
