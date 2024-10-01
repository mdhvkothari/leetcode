import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in times:
            adj[u-1].append((v-1, w))
        q = []
        distance = [1e9] * n
        distance[k-1] = 0
        heapq.heappush(q, (0, k-1))  # (time, node)

        while q:
            time, node = heapq.heappop(q)
            for neighbor, n_time in adj[node]:
                new_time = n_time + time
                if new_time < distance[neighbor]:
                    distance[neighbor] = new_time
                    heapq.heappush(q, (new_time, neighbor))
        
        max_time = max(distance)
        return max_time if max_time != 1e9 else -1
