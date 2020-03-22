"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

def solution_1(query_string: str, dictionary: list) -> list:
    length_of_query_string: int = len(query_string)
    tmp: list = []
    for word in dictionary:
        if length_of_query_string > len(word):
            continue
        elif length_of_query_string < len(word) and word[:length_of_query_string] == query_string:
            tmp.append(word)
        else:
            continue
    return tmp 

print(solution_1("de", ["dog", "deer", "deal"]))