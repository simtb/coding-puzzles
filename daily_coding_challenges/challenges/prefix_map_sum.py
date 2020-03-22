"""
This problem was asked by Google.

Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:

"""

class PrefixMapSum:
    
    def __init__(self):
        self.map = {}
    
    def insert(self, key: str, value: int) -> None:
        self.map[key]: int = value

    def sum(self) -> int:
        total: int = 0

        for key in self.map:
            total: int = total + self.map[key]
        
        return total 

