"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
"""


class Solution:
    def factorial(self, n: int) -> int:
        dp: List[int] = [1 for x in range(n + 1)]
            
        for i in range(1, n + 1):
            dp[i]: int = i * dp[i - 1]
        
        return dp[n]
    
    def getPermutation(self, n: int, k: int) -> str:
        tmp: List[str] = []
        digits: List[str] = [str(x) for x in range(1, n + 1)]
        m: int = k
        
        while (digits):
            a: int = len(digits)
                
            for i in range(a):
                check: int = (i + 1) * self.factorial(a - 1)
                if check >= m:
                    tmp.append(digits[i])
                    digits: List[str] = digits[ :i] + digits[i + 1: ]
                    break
                    
            m: int = m - (i * self.factorial(a - 1))

        
        
        return "".join(tmp)
            
