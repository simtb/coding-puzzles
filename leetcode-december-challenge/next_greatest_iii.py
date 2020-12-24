class Solution:
    def getDigits(self, n: int) -> List[str]:
        a: List[str] = []
        
        while (n):
            a.append(n % 10)
            n //= 10
            
        return a[::-1]
    
    def nextGreaterElement(self, n: int) -> int:
        if n >= (2147483647 + 1) // 2:
            return -1
        digits: List[int] = self.getDigits(n)
        digits_sorted: List[int] = sorted(digits)[::-1]
            
        if digits == digits_sorted:
            return -1
        
        a: int = len(digits)
            
        for i in range(1, a):
            current: int = digits[a - 1 - i]
            tmp: List[str] = digits[a - i:]
            tmp.sort()
            print(digits[:a -i - 1], current, tmp)
            b: int = len(tmp)
            for j in range(b):
                if tmp[j] > current:
                    tmp[j], current = current, tmp[j]
                    z: List[str] = []
                    for x in digits[:a - i - 1]:
                        z.append(str(x))
                    z.append(str(current))
                    for y in tmp:
                        z.append(str(y))
                    return int(''.join(z))
                    