from typing import List


class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat),len(mat[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited_mat, distance_mat = [[False]*n for _ in range(m)], [[0]*n for _ in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited_mat[i][j] = True
        
        while q:
            r, c, distance = q.pop(0)
            distance_mat[r][c] = distance
            for dr, dc in DIRECTIONS:
                row, col = r + dr, c + dc
                if 0 <= row < m and 0 <= col < n and not visited_mat[row][col]:
                    q.append((row, col, distance+1))
                    visited_mat[row][col] = True

        return distance_mat
