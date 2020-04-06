from typing import List

def single_number(nums: List[int]) -> int:
        x: int = 0
        for i in range(len(nums)):
            x ^= nums[i]
        return x
