'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
'''

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n: int = len(A)
        
        counter_top: dict = dict()
        counter_bottom: dict = dict()
            
        for i in range(n):
            a: int = A[i]
            if a in counter_top:
                counter_top[a][i] = True
            else:
                counter_top[a] = {i: True}
        
        for j in range(n):
            b: int = B[j]
            if b in counter_bottom:
                counter_bottom[b][j] = True
            else:
                counter_bottom[b] = {j: True}
                
        minimum_rotations: int = float('+inf')
        
        for value in counter_top:
            m: int = n - len(counter_top[value])
            if counter_bottom.get(value) != None:
                if len(counter_bottom[value]) >= m:
                    c: int = 0
                    for temp in counter_bottom[value]:
                        if temp not in counter_top[value]:
                            c += 1
                    if c >= m:
                        minimum_rotations = min(minimum_rotations, c)
        
        for value in counter_bottom:
            m: int = n - len(counter_bottom[value])
            if counter_top.get(value) != None:
                if len(counter_top[value]) >= m:
                    d: int = 0
                    for temp in counter_top[value]:
                        if temp not in counter_bottom[value]:
                            d += 1
                    if d >= m:
                        minimum_rotations = min(minimum_rotations, d)
                            
        
        if minimum_rotations == float('+inf'):
            return -1
        return minimum_rotations
