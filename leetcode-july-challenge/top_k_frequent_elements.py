"""
Given a non-empty array of integers, return the k most frequent elements.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        counts: Counter = Counter(nums)
        
        return heapq.nlargest(k, counts.keys(), key=counts.get)
