from collections import deque
from typing import List

"""
Here we are using q instead of priority queue because we know that all the distance will be one
and they will be store in q in increasing order so there is now need to sort them.
"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid)
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        q = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        q.append((1, 0, 0))   #  distance, x, y
        distance = [[1e9]*n for _ in range(m)]
        distance[0][0] = 0

        while q:
            dist, x, y = q.popleft()
            if x == m-1 and y == n-1:
                return dist
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (0<= new_x < m and 0<=new_y < n and grid[new_x][new_y] == 0 and dist + 1 < distance[new_x][new_y]):
                    distance[new_x][new_y] = dist + 1
                    q.append((dist + 1, new_x, new_y))

        return -1

