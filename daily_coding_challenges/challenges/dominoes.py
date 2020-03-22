"""
You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
"""

from typing import List


def is_valid_index(index: int, arr: List[str]) -> bool:
    largest_index: int = len(arr) - 1

    return 0 <= index <= largest_index


def dominoes(arr: List[str]) -> List[str]:
    n: int = len(arr)
    new_arr: List[str] = arr

    for i in range(n):
        temp: dict = {}
        for j in range(n):
            element: str = new_arr[j]
            if element == '.':
                pass

            elif element == 'R':
                test_index: int = j + 1
                if is_valid_index(test_index, new_arr):
                    new_element: str = new_arr[test_index]
                    test_index_2: int = test_index + 1
                    if is_valid_index(test_index_2, new_arr):
                        new_element_2: str = new_arr[test_index_2]
                        if new_element == '.' and (new_element_2 == '.' or new_element_2 == 'R'):
                            temp[test_index]: str = 'R'
                    else:
                        if new_element == '.':
                            temp[test_index]: str = 'R'
                else:
                    pass

            elif element == 'L':
                test_index: int = j - 1
                if is_valid_index(test_index, new_arr):
                    new_element: str = new_arr[test_index]
                    test_index_2: int = test_index - 1
                    if is_valid_index(test_index_2, new_arr):
                        new_element_2: str = new_arr[test_index_2]
                        if new_element == '.' and (new_element_2 == '.' or new_element_2 == 'L'):
                            temp[test_index]: str = 'L'
                    else:
                        if new_element == '.':
                            temp[test_index]: str = 'L'
                else:
                    pass
            
        if temp:
            for key in temp:
                new_arr[key]: str = temp[key]
    return new_arr






