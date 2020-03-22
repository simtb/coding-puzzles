
def solution(string: str, start_index: int, end_index: int) -> int:
    if string == "":
        return 0
    if start_index > end_index:
        return 0

    if string[start_index] == string[end_index]:
        if start_index == end_index:
            return solution(string, start_index + 1, end_index - 1) + 1
        else:
            return solution(string, start_index + 1, end_index - 1) + 2
    else:
        return max(solution(string, start_index + 1, end_index), solution(string, start_index, end_index - 1))

print(solution("ABBDCACB", 0, 7))