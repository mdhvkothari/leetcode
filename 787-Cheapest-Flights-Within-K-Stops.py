import heapq
from typing import List

"""
We gives priority to stop in min head because we can not go feather than the k
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for i in range(n)]
        for u, v, cost in flights:
            adj[u].append((v, cost))
        distance = [float('inf')] * n
        distance[src] = 0
        q = []
        heapq.heappush(q, (0, src, 0)) # stops, node, cost
        
        while q:
            stops, node, cost = heapq.heappop(q)
            for neighbor, n_cost in adj[node]:
                new_stops = stops + 1
                new_cost = cost + n_cost
                if new_stops <= k+1 and new_cost < distance[neighbor]:
                    distance[neighbor] = new_cost
                    heapq.heappush(q, (new_stops, neighbor, new_cost))
        return -1 if distance[dst] == float('inf') else distance[dst]
