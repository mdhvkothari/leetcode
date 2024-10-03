import heapq
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        ways = [0] * n
        distance = [float('inf')] * n
        distance[0] = 0
        ways[0] = 1
        
        q = []
        heapq.heappush(q, (0, 0))  # (distance, node)
        
        MOD = 10**9 + 7
        
        while q:
            weight, node = heapq.heappop(q)
            if weight > distance[node]:
                continue
            for neighbor, n_weight in adj[node]:
                new_weight = weight + n_weight
                if new_weight < distance[neighbor]:
                    distance[neighbor] = new_weight
                    ways[neighbor] = ways[node]
                    heapq.heappush(q, (new_weight, neighbor))
                elif new_weight == distance[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n-1] % MOD
