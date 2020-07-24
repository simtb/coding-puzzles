"""
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.
"""

class Solution:
    ans: List[List[int]] = None
    
    def backtrack(self, tmp: List[int], graph: List[List[int]], destination: int) -> None:
        n: int = len(tmp)
        current: int = tmp[n - 1]
        
        if current == destination:
            self.ans.append(tmp[:])
            
        for i in range(len(graph[current])):
            tmp.append(graph[current][i])
            self.backtrack(tmp, graph, destination)
            tmp.pop()
        
        
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if self.ans is None:
            self.ans = []
            
        N: int = len(graph) - 1
            
        self.backtrack([0], graph, N)
        
        return self.ans
        
