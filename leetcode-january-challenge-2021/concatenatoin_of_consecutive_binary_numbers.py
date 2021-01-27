class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary_string: str = ""
        MOD: int = (10 ** 9)  + 7
        
        for i in range(1, n + 1):
            binary_string += bin(i)[2:]
        
        return int(binary_string, 2) % MOD