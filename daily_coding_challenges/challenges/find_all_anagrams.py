"""
This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

"""

from typing import List

def is_anagram(word_1: str, word_2: str) -> bool:

    length_of_word_1: int = len(word_1)
    length_of_word_2: int = len(word_2)

    if length_of_word_1 != length_of_word_2:
        return False
    
    word_1_counter: dict = {}

    for letter in word_1:
        if letter in word_1_counter:
            word_1_counter[letter] += 1
        else:
            word_1_counter[letter] = 1
    
    for letter in word_2:
        if word_1_counter.get(letter) == None or word_1_counter.get(letter) < 0:
            return False
        else:
            word_1_counter[letter] -= 1

    for letter in word_1_counter:
        if word_1_counter[letter] != 0:
            return False
    return True


def find_all_anagrams(word: str, string: str) -> List[int]:

    indicies: List[int] = []
    length_of_word: int = len(word)
    length_of_string: int = len(string)
    stop_index: int = length_of_word + length_of_string + 1

    if length_of_string > length_of_word:
        return []
    
    for i in range(stop_index):
        temp_word: str = word[i: i + length_of_string]
        if is_anagram(string, temp_word):
            indicies.append(i)
    return indicies
