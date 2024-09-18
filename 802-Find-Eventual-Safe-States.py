from collections import deque
from typing import List



"""

Put the node in the opposite direction and maintain In degree array

[[1,2],[2,3],[5],[0],[5],[],[]]

0 -> 1, 2
1 -> 2, 3
2 -> 5
3 ->
4 -> 5
5 ->
6 ->

"""


class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj, in_degree, result, V = [[] for _ in range(len(graph))], [0] * len(graph), [], len(graph)

         # reverse the direction and calculate in degree
        for i in range(V):
            for j in graph[i]:
                adj[j].append(i)
                in_degree[i] += 1
    
        q = deque()
        for i in range(V):
            if in_degree[i] == 0:
                q.append(i)
        
        # apply Kahn's algorithm and store the element in the list
        # basically we are detecting the cycle in the directed graph

        while q:
            node = q.popleft()
            result.append(node)
            for i in adj[node]:
                if in_degree[i] != 0:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        q.append(i)

        return sorted(result)
