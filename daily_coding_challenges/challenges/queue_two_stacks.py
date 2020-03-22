"""
This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out)
data structure with the following methods: 
enqueue, which inserts an element into the queue, 
dequeue, which removes it.
"""


class Queue:
    def __init__(self):
        self.__enqueue_stack: list = []
        self.__dequeue_stack: list = []
    
    @property
    def size(self) -> int:
        length_of_enqueue_stack: int = len(self.__enqueue_stack)
        length_of_dequeue_stack: int = len(self.__dequeue_stack)
        return max(length_of_enqueue_stack, length_of_dequeue_stack)

    def enqueue(self, item: object) -> None:
        while self.__dequeue_stack != []:
            tmp: object = self.__dequeue_stack.pop()
            self.__enqueue_stack.append(tmp)
        self.__enqueue_stack.append(item)
    
    def dequeue(self) -> object:
        while self.__enqueue_stack != []:
            tmp: object = self.__enqueue_stack.pop()
            self.__dequeue_stack.append(tmp)
        if self.__dequeue_stack == []:
            return None
        else:
            item: object = self.__dequeue_stack.pop()
            return item 