"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
"""

from typing import List, Tuple

def word_search(matrix: List[List[str]], word: str) -> bool:
    length_of_column: int = len(matrix)
    length_of_row: int = len(matrix[0])
    length_of_word: int = len(word)
    first_letter: str = word[0]

    for ith_column in range(length_of_column):
        for jth_row in range(length_of_row):
            letter: str = matrix[ith_column][jth_row]
            if letter == first_letter:
                if length_of_word > length_of_row - jth_row:
                    pass
                else:
                    result: bool = search_horizontally(matrix=matrix, word=word, position=(ith_column, jth_row))
                    if result == True:
                        return True
                if length_of_word > length_of_column - ith_column:
                    pass
                else:
                    result: bool = search_vertically(matrix=matrix, word=word, position=(ith_column, jth_row))
                    if result == True:
                        return True
    return False

def search_horizontally(matrix: List[List[str]], word: str, position: Tuple[int]) -> bool:
    length_of_word: int = len(word)

    for i in range(length_of_word):
        found = True
        if word[i] != matrix[position[0]][position[1] + i]:
            found = False
            break
    return found

def search_vertically(matrix: List[List[str]], word: str, position: Tuple[int]) -> bool:
    length_of_word: int = len(word)

    for i in range(length_of_word):
        found = True
        if word[i] != matrix[position[0] + i][position[1]]:
            found = False
            break
    return found
