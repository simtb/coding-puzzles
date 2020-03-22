"""This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

from itertools import combinations

def power_set(input_set: set) -> set:
    length_of_set: int = len(input_set)
    power_list: list = list()
    for i in range(length_of_set + 1):
        subsets: list = list(combinations(input_set, i))
        for subset in subsets:
            power_list.append(set(subset))
    return power_list
