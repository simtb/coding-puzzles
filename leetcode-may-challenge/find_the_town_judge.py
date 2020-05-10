"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
"""

from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N
        
        potential_judge: set = set()
        has_trusted: dict = dict()
            
        for pair in trust:
            if pair[0] not in potential_judge:
                if pair[1] not in has_trusted:
                    potential_judge.add(pair[1])
            else:
                potential_judge.remove(pair[0])
            has_trusted[pair[0]]: bool = True
        
        
        if len(potential_judge) == 1:
            return potential_judge.pop()
        return -1
        
