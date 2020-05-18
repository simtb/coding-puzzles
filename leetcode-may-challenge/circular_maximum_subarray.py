"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
"""

from typing import List

class Solution:     
    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]
        
        n: int = len(A)
        total: int = 0
        max_sum: int = float('-inf')
        current_sum: int = 0
        
        for i in range(n):
            x: int = A[i]
            total += x
            current_sum += x
            max_sum: int = max(max_sum, current_sum)
            current_sum: int = max(current_sum, 0)
            
            A[i]: int = x * -1
                
                
        max_inverse: int = float("-inf")
        current_sum: int = 0
            
        for j in range(n):
            y: int = A[j]
            current_sum += y
            max_inverse: int = max(max_inverse, current_sum)
            current_sum: int = max(current_sum, 0)
        
        if max_inverse + total > max_sum and max_inverse + total != 0:
            return max_inverse + total
        else:
            return max_sum
