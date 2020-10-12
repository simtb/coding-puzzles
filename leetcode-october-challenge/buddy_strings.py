"""
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        n: int = len(A)
        m: int = len(B)
        
        if n < 2:
            return False
        if m < 2:
            return False
        
        if n != m:
            return False
        
        first_character_info: int = None
        second_character_info: int = None
        number_of_changes = 0
        tmp_1: dict = dict()
        tmp_2: dict = dict()
        
        for i in range(n):
            a: str = A[i]
            b: str = B[i]
            
            tmp_1[a]: int = tmp_1.get(a, 0) + 1
            tmp_2[b]: int = tmp_2.get(b, 0) + 1
            if a != b:
                if first_character_info is None:
                    first_character_info = i
                    number_of_changes += 1
                else:
                    second_character_info = i
                    number_of_changes += 1
            
            if number_of_changes > 2:
                return False
            elif number_of_changes == 2:
                if A[first_character_info] == B[second_character_info] and A[second_character_info] == B[first_character_info]:
                    if A[second_character_info + 1:] == B[second_character_info + 1:]:
                        return True
                    else:
                        return False
                else:
                    return False
        
        has_duplicates: bool = False
        
        for key in tmp_1:
            if key not in tmp_2:
                return False
            if tmp_1[key] != tmp_2[key]:
                return False
            if tmp_1[key] > 1 and not has_duplicates:
                has_duplicates = True
        
        if has_duplicates:
            return True
        return False
