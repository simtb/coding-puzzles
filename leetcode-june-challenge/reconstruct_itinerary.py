"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
"""

class Solution:
    route: List[str] = None
    graph: dict = None
        
    def buildGraph(self, arr: List[List[str]]) -> dict:
        graph: dict = dict()
        
        for element in arr:
            if element[0] in graph:
                graph[element[0]].append(element[1])
            else:
                graph[element[0]]: List[str] = [element[1]]
        
        for key in graph:
            graph[key] = sorted(graph[key], reverse=True)
        
        return graph
    
    def dfs(self, airport: str):
        while (self.graph.get(airport, [])):
            potential: str = self.graph[airport].pop()
            self.dfs(potential)
        
        self.route.append(airport)
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if self.route is None:
            self.route: List[str] = []
                
        self.graph: dict = self.buildGraph(tickets)
        self.dfs('JFK')
        
        return self.route[::-1]
