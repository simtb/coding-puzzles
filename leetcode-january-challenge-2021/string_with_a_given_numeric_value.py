class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        alphabet: List[str] =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v','w','x','y', 'z']
        ans: str = ""
        
        while (k - 26 >= n):
            n -= 1
            k -= 26
            ans = 'z' + ans
        
        needed: int = k - n
        ans = alphabet[needed] + ans
        n -= 1
        
        for i in range(n):
            ans = 'a' + ans
            
        return ans