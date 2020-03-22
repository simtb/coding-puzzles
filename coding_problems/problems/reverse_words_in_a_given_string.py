
def reverse_string(string: str) -> str:
    words_in_string: list = string.split(" ")
    reversed_string: str = " ".join(words_in_string[::-1])
    return reversed_string