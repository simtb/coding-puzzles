
def solution(string_1: str, string_2: str, length_of_string_1: int, length_of_string_2: int) -> int:
    if length_of_string_1 == 0 or length_of_string_2 == 0:
        return 0
    if string_1[length_of_string_1 - 1] == string_2[length_of_string_2 - 1]:
        return solution(string_1, string_2, length_of_string_1 - 1, length_of_string_2 - 1) + 1
    else:
        return max(solution(string_1, string_2, length_of_string_1 - 1, length_of_string_2), solution(string_1, string_2, length_of_string_1, length_of_string_2 - 1))

def solution_2(string_1: str, string_2: str, length_of_string_1: int, length_of_string_2: int, tmp: dict) -> int:
    if length_of_string_1 == 0 or length_of_string_2 == 0:
        return 0
    
    key: tuple = (length_of_string_1, length_of_string_2)

    if string_1[length_of_string_1 - 1] == string_2[length_of_string_2 - 1]:
        tmp[key]: int = solution_2(string_1, string_2, length_of_string_1 - 1, length_of_string_2 - 1, tmp) + 1
    else:
       tmp[key]: int = max(solution_2(string_1, string_2, length_of_string_1 - 1, length_of_string_2, tmp), solution_2(string_1, string_2, length_of_string_1, length_of_string_2 - 1, tmp))

    return tmp[key]