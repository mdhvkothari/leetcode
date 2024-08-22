from typing import List


"""
A Graph is bipartite that can be coloured with two colors such that
no two adjacent nodes have the same color.
"""


class Solution:

    def dfs(self, visited_arr, graph, node, color):
        visited_arr[node] = color
        for i in graph[node]:
            if visited_arr[i] == -1 and not self.dfs(visited_arr, graph, i, color^1):
                return False
            elif visited_arr[i] == color:
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        visited_arr = [-1] * V

        for i in range(V):
            if visited_arr[i] == -1 and not self.dfs(visited_arr, graph, i, 0):
                return False
        return True
