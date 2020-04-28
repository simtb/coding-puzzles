"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.
"""

class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next = None
        self.previous = None
    
    def __str__(self):
        return str(self.value)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.current_size: int = 0
        self.cache: dict = {}
        self.head: Node = Node(float('+inf'))
        self.tail: Node = Node(float('-inf'))
        self.head.next: Node = self.tail
        self.tail.previous: Node = self.head

    def get(self, key: int) -> int:
        value: int = self.cache.get(key, -1)
        
        if value == -1:
            return -1
        
        else:
            current_node: Node = self.head
            while current_node.value != key:
                current_node: Node = current_node.next
            current_node.previous.next: Node = current_node.next
            current_node.next.previous: Node = current_node.previous
            
            old_front: Node = self.head.next
            self.head.next: Node = current_node
            current_node.previous: Node = self.head
                
            current_node.next: Node = old_front
            old_front.previous: Node = current_node
            
            return value
        

    def put(self, key: int, value: int) -> None:
        #create node
        new_node: Node = Node(key)
        check: int = self.cache.get(key, -1)
        #check if doesn't already exists
        if check == -1:
            #Put the new node in cache and LinkedList
            old_front: Node = self.head.next

            self.head.next: Node = new_node
            new_node.previous: Node = self.head

            new_node.next: Node = old_front
            old_front.previous: Node = new_node

            self.current_size: int = self.current_size + 1
        else:
            #else update cache and move to front
            #get old key and move to front of list 
            current_node: Node = self.head
            while current_node.value != key:
                current_node: Node = current_node.next
            current_node.previous.next: Node = current_node.next
            current_node.next.previous: Node = current_node.previous
                
            old_front: Node = self.head.next
            self.head.next: Node = current_node
            current_node.previous = self.head
            
            current_node.next: Node = old_front
            old_front.previous: Node = current_node
        self.cache[key]: int = value

        
        if self.current_size > self.capacity:
            lru_node: Node = self.tail.previous
            #turning off the evicted node
            self.cache[lru_node.value]: int = -1
            lru_node.previous.next: Node = self.tail
            self.tail.previous: Node = lru_node.previous
            self.current_size: int = self.current_size - 1
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
