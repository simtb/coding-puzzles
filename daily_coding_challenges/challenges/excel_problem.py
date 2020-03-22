'''This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA"'''

def get_column_id(value: int) -> str:
    alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #assume only integer values of 1 or more can be entertedger
    
    column: str = ""

    while value:
        temp_value: int = value % 26
        if temp_value == 0:
            column: str = "Z" + column
            value: int = (value // 26) - 1 
        else:
            column: str = alphabet[temp_value - 1] + column
            value: int = value // 26
        

    return column
