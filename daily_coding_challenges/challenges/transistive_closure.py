"""
This problem was asked by Microsoft.

The transitive closure of a graph is a measure of which vertices are reachable from other vertices. It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
The transitive closure of this graph would be:

[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Given a graph, find its transitive closure.
"""

from typing import List

def transitive_closure(adjacency_graph: List[List[int]])-> List[List[int]]:
    size_of_transistive_closure: int = len(adjacency_graph)
    transistive_closure: List[List[int]] = [[0 for i in range(size_of_transistive_closure)] for j in range(size_of_transistive_closure)]

    for i in range(len(graph)):
        for j in graph[i]:
            for k in graph[j]:
                if transistive_closure[i][k] == 0:
                    transistive_closure[i][k]: int = 1
    
    return transistive_closure

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]

print(transitive_closure(graph))

