"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        ans: List[int] = [0] * (num + 1)
        ans[1]: int = 1
        pow_of_2: int = 1
        
        for i in range(2, num + 1):
            if i == pow_of_2 * 2:
                ans[i]: int = 1
                pow_of_2 *= 2
            else:
                m: int = i - pow_of_2
                ans[i]: int = 1 + ans[m]
                    
        return ans
