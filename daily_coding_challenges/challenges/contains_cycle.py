"""
This problem was asked by Pandora.

Given an undirected graph, determine if it contains a cycle.
"""

from typing import Dict, List

def contains_cycle(graph: Dict[int, List[int]]) -> bool:
    if graph == {}:
        return False
    
    has_cycle: bool = False
    visited: Dict[int, bool] = {}
    paths: List[List[int]] = []

    for node in graph:
        visited: dict = {node: True}
        queue: List[int] = []
        for x in graph[node]:
            queue.append(x)
        temp: List[int] = [node]
        while queue:
            current_node: int = queue.pop(0)
            if visited.get(current_node) != True:
                visited[current_node]: bool = True
                temp.append(current_node)
                for x in graph[current_node]:
                    queue.append(x)
        if not paths:
            paths.append(sorted(temp))
            stop_loop: bool = False
        else:
            tmp: List[int] = sorted(temp)
            stop_loop: bool = False
            for path in paths:
                if tmp == path:
                    has_cycle: bool = True
                    stop_loop: bool = True
                    break
            paths.append(tmp)
        if stop_loop:
            break

    return has_cycle


    

