"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
"""

class Solution:
    def decodeString(self, s: str) -> str:
        n: int = len(s)
        decoded_string: str = []
        
        multiplier: List[str] = []
        multiplier_stack: List[int] = []
        character_stack: List[List[str]] = []
        
        i: int = 0
        
        while (i < n):
            current: str = s[i]
            if not multiplier_stack:
                if current.isalpha():
                    decoded_string.append(current)
                elif current.isdigit():
                    multiplier.append(current)
                else:
                    character_stack.append([])
                    multiplier_stack.append(int("".join(multiplier)))
                    multiplier = []
            else:
                if current == "[":
                    multiplier_stack.append(int("".join(multiplier)))
                    character_stack.append([])
                    multiplier = []
                elif current == "]":
                    k: int = multiplier_stack.pop()
                    a: List[str] = character_stack.pop()
                    characters: str = "".join(a)
                    tmp: str = k * characters
                    if not multiplier_stack:
                        decoded_string.append(tmp)
                        temp_string = []
                    else:
                        character_stack[-1].append(tmp)
                elif current.isalpha():
                    character_stack[-1].append(current)
                elif current.isdigit():
                    multiplier.append(current)
            i += 1
            
        return "".join(decoded_string)


