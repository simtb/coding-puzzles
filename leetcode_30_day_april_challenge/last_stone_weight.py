""We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
"""

from typing import List

def maxElement(arr: List[int]) -> int:
        if not arr:
            return 0
        
        max_element: int = arr[0]
        max_element_index: int = 0
        
        for i in range(len(arr)):
            if arr[i] > max_element:
                max_element: int = arr[i]
                max_element_index: int = i
        
        del arr[max_element_index]
        
        return max_element
    
    def lastStoneWeight(stones: List[int]) -> int:
        if not stones:
            return 0
        
        while True:
            if not stones:
                return 0
            if len(stones) == 1:
                return stones[0]
            
            heaviest_stone: int = self.maxElement(stones)
            second_heaviest_stone: int = self.maxElement(stones)
            
            weight: int = heaviest_stone - second_heaviest_stone
            
            if weight:
                stones.append(weight)
