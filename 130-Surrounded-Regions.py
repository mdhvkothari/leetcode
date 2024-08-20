from typing import List

"""
Start from the boundary 0's and mark them they will not convert.
and convert rest of the 0's
"""


class Solution:

    def dfs(self, row, col, vis, mat, delrow, delcol):
        vis[row][col] = 1
        n = len(mat)
        m = len(mat[0])
        
        # Check for top, right, bottom, left 
        for i in range(4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]
            # Check for valid coordinates and unvisited 'O's
            if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0 and mat[nrow][ncol] == 'O':
                self.dfs(nrow, ncol, vis, mat, delrow, delcol)

    def solve(self, board: List[List[str]]) -> None:
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        n, m = len(board), len(board[0])
        vis = [[0] * m for _ in range(n)]
        
        # Traverse first row and last row 
        for j in range(m):
            # Check for unvisited 'O's in the boundary rows
            # First row
            if vis[0][j] == 0 and board[0][j] == 'O':
                self.dfs(0, j, vis, board, delrow, delcol)
            
            # Last row
            if vis[n-1][j] == 0 and board[n-1][j] == 'O':
                self.dfs(n-1, j, vis, board, delrow, delcol)
        
        # Traverse first column and last column
        for i in range(n):
            # Check for unvisited 'O's in the boundary columns
            # First column
            if vis[i][0] == 0 and board[i][0] == 'O':
                self.dfs(i, 0, vis, board, delrow, delcol)
            
            # Last column
            if vis[i][m-1] == 0 and board[i][m-1] == 'O':
                self.dfs(i, m-1, vis, board, delrow, delcol)
        
        # If unvisited 'O' then convert to 'X'
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'
