"""Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character."""

def resolve_string(string: str) -> str:
    new_string: str = ""
    length_of_string: int = len(string)
    i: int = 0
    number_of_hashtags: int = 0
    
    while True:
        if i  > length_of_string - 1:
            break
        
        current_character: str = string[length_of_string - i - 1]
            
        if current_character == '#':
            number_of_hashtags: int = number_of_hashtags + 1
        else:
            if number_of_hashtags == 0:
                new_string: str = new_string + current_character
            else:
                number_of_hashtags: int = number_of_hashtags - 1
        i: int = i + 1

    return new_string
    
    
#solution using stacks
def resolve_string(string: str) -> str:
        stack: list = []
        
        for character in string:
            if character != '#':
                stack.append(character)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)
    
def backspaceCompare(S: str, T: str) -> bool:
    return resolve_string(S) == resolve_string(T)

### both resolve mehtods work 