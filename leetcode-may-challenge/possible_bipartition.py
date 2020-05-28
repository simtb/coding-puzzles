"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.
"""

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        tmp: dict = {}
            
        for dislike in dislikes:
            a: int = dislike[0]
            b: int = dislike[1]
            
            if a not in tmp:
                tmp[a]: set = {b}
            else:
                tmp[a].add(b)
            
            if b not in tmp:
                tmp[b]: set = {a}
            else:
                tmp[b].add(a)
            
        seen: dict = {}
        for i in range(1, N + 1):
            if i not in seen:
                seen[i]: int = 0
                stack: list = [i]
                while stack:
                    a = stack.pop()
                    if a in tmp:
                        for b in tmp[a]:
                            if b in seen:
                                if seen[a] == seen[b]:
                                    return False
                            else:
                                seen[b] = (seen[a] + 1) % 2
                                stack.append(b)
        return True
