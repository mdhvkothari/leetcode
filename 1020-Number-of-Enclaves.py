from typing import List


"""
Same logic as 130 - Surrounded Regionss
"""


class Solution:

    def dfs(self, DIRECTIONS, visited_matrix, grid, r, c, n, m):
        visited_matrix[r][c] = True
        for rd, cd in DIRECTIONS:
            row, col = r + rd, c + cd
            if 0 <= row < n and 0 <= col < m and not visited_matrix[row][col] and grid[row][col] == 1:
                self.dfs(DIRECTIONS, visited_matrix, grid, row, col, n, m)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited_matrix = [[False] * m for _ in range(n)]
        
        # DFS from all boundary land cells
        for i in range(m):
            if grid[0][i] == 1 and not visited_matrix[0][i]:
                self.dfs(DIRECTIONS, visited_matrix, grid, 0, i, n, m)
            if grid[n-1][i] == 1 and not visited_matrix[n-1][i]:
                self.dfs(DIRECTIONS, visited_matrix, grid, n-1, i, n, m)
        
        for j in range(n):
            if grid[j][0] == 1 and not visited_matrix[j][0]:
                self.dfs(DIRECTIONS, visited_matrix, grid, j, 0, n, m)
            if grid[j][m-1] == 1 and not visited_matrix[j][m-1]:
                self.dfs(DIRECTIONS, visited_matrix, grid, j, m-1, n, m)
                
        # Count all non-visited land cells
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited_matrix[i][j]:
                    count += 1
        return count
