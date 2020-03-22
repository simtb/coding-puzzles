"find the first non-repeating character in a string"

"simeon"
from collections import OrderedDict

def find_first_non_repeating_character(string: str) -> str:
    if string == "":
        return ""
    
    tmp: OrderedDict = OrderedDict()
    length_of_string: int = len(string)

    for i in range(0, length_of_string):
        letter: str = string[i]
        if tmp.get(letter) == None:
            tmp[letter]: int = 1
        else:
            tmp[letter] += 1
    if not tmp:
        return None
    for key in tmp:
        if tmp[key] == 1:
            return key
