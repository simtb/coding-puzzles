"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""

class Solution:
    def createGraph(self, edges: List[List[int]]) -> dict:
        graph: dict = {}
        
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]]: set = set([edge[1]])
            else:
                graph[edge[0]].add(edge[1])
                
        return graph
    
    def isCyclic(self, graph: dict, N: int) -> bool:
        for i in range(N):
            start: int = i
            
            if graph.get(start) is not None:
                
                queue: set = list(graph.get(start))
                j: int = 0
                while queue:
                    current: int = queue.pop()
                    if current == start:
                        return True
                    if j > N + 1:
                        break
                    if graph.get(current) is not None:
                        for x in graph.get(current):
                            queue.insert(0, x)
                    j += 1
        return False
                    
                
        
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return not self.isCyclic(self.createGraph(prerequisites), numCourses)
        
