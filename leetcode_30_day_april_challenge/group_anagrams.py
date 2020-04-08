"""Given an array of strings, group anagrams together."""

from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
        
        canonical_form: dict = {}
        temp: List[List[str]] = []
            
        for word in strs:
            word_: List[str] = sorted(word)
            new_word: str = ''
            for char in word_:
                new_word += char
                    
            if new_word in canonical_form:
                canonical_form[new_word].append(word)
            else:
                canonical_form[new_word]: List[str] = [word]
        
        for x in canonical_form:
            temp.append(canonical_form[x])
        return temp
            

def is_anagram(word_1: str, word_2: str) -> bool:
        return sorted(word_1) == sorted(word_2)
    
    
    def group_anagrams(strs: List[str]) -> List[List[str]]:
        group_of_anagrams: List[List[str]] = []
        index_already_used: dict = {}
        n: int = len(strs)
        
        for i in range(n):
            if index_already_used.get(i) == True:
                pass
            else:
                index_already_used[i]: bool = True
                group_of_anagram: List[str] = [strs[i]]
                for j in range(i + 1, n):
                    if is_anagram(strs[i], strs[j]):
                        index_already_used[j]: bool = True
                        group_of_anagram.append(strs[j])
                group_of_anagrams.append(group_of_anagram)
                
        return group_of_anagrams	
