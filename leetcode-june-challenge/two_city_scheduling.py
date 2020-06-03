"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
"""

class Solution:
    def opportunityCost(self, item: List[int]) -> List[List[int]]:
        return item[0] - item[1]
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sortedCosts: List[List[int]] = sorted(costs, key=self.opportunityCost)
        n: int = len(costs)
        i: int = 0
        total: int = 0
        
        while i < n:
            if i < n // 2:
                total += sortedCosts[i][0]
            else:
                total += sortedCosts[i][1]
            i += 1
            
        return total
