"""
This problem was asked by Pivotal.

A step word is formed by taking a given word, adding a letter, and anagramming the result. For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns all valid step words.
"""

from typing import List
import string

def is_anagram(word_1: str, word_2: str) -> bool:
    word_1_counter: dict = {}

    for letter in word_1:
        if letter in word_1_counter:
           word_1_counter[letter] += 1
        else:
            word_1_counter[letter]: int = 1

    for letter in word_2:
        if letter not in word_1_counter:
            return False
        else:
            if word_1_counter[letter] == 0:
                return False
            else:
                word_1_counter[letter] -= 1
    
    for letter in word_1_counter:
        if word_1_counter[letter] != 0:
            return False
    return True

def step_word(word: str, dictionary: List[str]) -> List[str]:
    alphabet: str = string.ascii_lowercase
    step_words: List[str] = []

    for letter in alphabet:
        word_: str = word + letter
        for entry in dictionary:
            if is_anagram(entry.lower(), word_.lower()):
                step_words.append(entry.lower())
    
    return step_words
    

    
