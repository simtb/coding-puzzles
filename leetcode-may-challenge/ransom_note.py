"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter: dict = {}
        
        for character in magazine:
            magazine_counter[character]: int = magazine_counter.get(character, 0) + 1
        
        for character in ransomNote:
            count_of_characters: int = magazine_counter.get(character, 0)
            if not count_of_characters:
                return False
            else:
                new_count_of_characters: int = count_of_characters - 1
                magazine_counter[character]: int = new_count_of_characters
        
        return True
