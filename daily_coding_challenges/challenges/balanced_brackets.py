"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

"""

def balanced_brackets(brackets: str) -> bool:

    open_brackets_stack: list = []
    brackets_mapping: dict = {")": "(", "]": "[", "}": "{"}

    for bracket in brackets:
        if bracket in "([{":
            open_brackets_stack.append(bracket)
        else:
            if open_brackets_stack:
                last_bracket: str = open_brackets_stack.pop()
                if brackets_mapping.get(bracket) == last_bracket:
                    continue
                else:
                    return False
            else:
                return False

    if open_brackets_stack:
        return False
    return True

def balanced_brackets_1(brackets: str) -> bool:
    length: int = len(brackets)
    if length % 2 == 1:
        return False 
    
    lookup: dict = {")": "(", "]": "[", "}": "{"}
    
    left_pointer: int = 0
    right_pointer: int = length - 1

    balanced: int = True

    while left_pointer < right_pointer and balanced:
        if brackets[left_pointer] != lookup[brackets[right_pointer]]:
            balanced: bool = False
            break

        left_pointer += 1
        right_pointer -= 1
    
    return balanced


print(balanced_brackets_1("(([]))"))