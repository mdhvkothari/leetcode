import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        q = []
        heapq.heappush(q, (0, 0, 0))  # (effort difference, x, y)
        distance = [[1e9] * m for _ in range(n)]
        distance[0][0] = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            diff, x, y = heapq.heappop(q)
            if x == n - 1 and y == m - 1:
                return diff

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < m:
                    new_effort = max(abs(heights[x][y] - heights[new_x][new_y]), diff)
                    
                    if new_effort < distance[new_x][new_y]:
                        distance[new_x][new_y] = new_effort
                        heapq.heappush(q, (new_effort, new_x, new_y))
        
        return -1
