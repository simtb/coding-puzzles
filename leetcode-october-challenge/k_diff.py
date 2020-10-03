"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
a <= b
b - a == k
"""

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans: int = 0
        if k == 0:
            counter: dict = dict()
            for num in nums:
                counter[num] = counter.get(num, 0) + 1
            for value in counter:
                if counter[value] > 1:
                    ans += 1
        else:
            nums_set = set(nums)
            for num in nums_set:
                if num + k in nums_set:
                    ans += 1
        return ans
