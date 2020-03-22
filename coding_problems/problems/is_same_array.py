"are two arrays the same"

def is_same_array(array_1: list, array_2: list) -> bool:
    counter: dict = {}
    length_of_array: int = len(array_1)

    if length_of_array == 0:
        return True

    for i in range(0 , length_of_array):
        element: int = array_1[i]
        if element in counter:
            counter[element] += 1
        else:
            counter[element]: int = 1
    
    for j in range(0, length_of_array):
        element: int = array_2[j]
        if counter.get(element) != None and counter.get(element) > 0:
            counter[element] -= 1
    
    all_zeros: bool = True

    for key in counter:
        if counter[key] != 0:
            all_zeros: bool = False
            break
    
    is_same_array: bool = all_zeros
    return is_same_array