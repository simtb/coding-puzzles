"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 
"""

from typing import List

class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next: int = None
        self.previous: int = None
            
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
    

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums
        self.head: Node = Node(float('-inf'))
        self.tail: Node = Node(float('+inf'))
        self.head.next: Node = self.tail
        self.tail.previous: Node = self.head
        self.duplicates: dict = {}
        
        self.pointers: dict = {}
        #for loop
        for i in range(len(self.nums)):
            self.add(self.nums[i])
    

    def showFirstUnique(self) -> int:
        first_unique: Node = self.tail.previous
        if first_unique.value == float('-inf'):
            return -1
        return first_unique.value
        

    def add(self, value: int) -> None:
        #if pointer exists remove, else add
        pointer: Node = self.pointers.get(value, Node(-1))
        duplicate: bool = self.duplicates.get(value, False)
        if pointer.value == -1 and not duplicate:
            #add because it doesn't exist, add to dl queue and hashmap
            new_node: Node = Node(value)
            old_last_node: Node = self.head.next

            self.head.next: Node = new_node
            new_node.previous: Node = self.head

            new_node.next: Node = old_last_node
            old_last_node.previous: Node = new_node

            self.pointers[value]: Node = new_node
            self.duplicates[value]: bool = True

                
        elif pointer.value != -1 and duplicate:
            #it does exists so remove delete from DL queue and pointers hashmap
            next_node: Node = pointer.next
            previous_node: Node = pointer.previous
            
            previous_node.next: Node = next_node
            next_node.previous: Node = previous_node
            
            del self.pointers[pointer.value]


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
