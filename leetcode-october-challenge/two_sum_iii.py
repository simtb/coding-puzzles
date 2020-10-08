"""
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

"""

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums: List[int] = []
        self.found: set = set()
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if value in self.found:
            return True
        
        tmp: dict = dict()
        
        for num in self.nums:
            if value - num in tmp:
                return True
            else:
                tmp[num] = True
                
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
