"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""

def solution(decoded_string: str) -> str:
    if not decoded_string:
        return ""
    
    length_of_decoded_string: int = len(decoded_string)
    encoded_string: str = ""
    current_letter: str = ""
    frequency: int = 1

    for i in range(length_of_decoded_string):
        letter: str = decoded_string[i]
        if i == 0:
            current_letter: str = letter
        elif i != 0 and letter == current_letter:
            frequency += 1
        elif i != 0 and letter != current_letter:
            encoded_string += str(frequency)
            encoded_string += current_letter
            current_letter: str = letter
            frequency: int = 1

    encoded_string += str(frequency)
    encoded_string += current_letter

    return encoded_string


