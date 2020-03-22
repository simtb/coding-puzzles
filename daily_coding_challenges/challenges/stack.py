"""
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""

class Stack:
    def __init__(self):
        self.stack: list = []
        self.__max_values: list = []

    @property
    def is_empty(self) -> bool:
        return not bool(self.stack)
    
    def push(self, val: int) -> None:
        if self.is_empty and not self.__max_values: 
            self.__max_values.append(val)
        elif not self.is_empty and self.__max_values and val >= self.__max_values[-1]:
            self.__max_values.append(val)
        else:
            pass
        self.stack.append(val)
    
    def pop(self) -> int:
        if self.is_empty and not self.__max_values: 
            return None

        value: int = self.stack.pop()

        if value == self.__max_values[-1]:
            self.__max_values.pop()
        
        return value 

    def max(self) -> int:
        if self.is_empty and not self.__max_values:
            return None
        else:
            return self.__max_values[-1]
    
    def __contains__(self, test_value: int) -> bool:
        for value in self.stack:
            if test_value == value:
                return True
        return False 
            