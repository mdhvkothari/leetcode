from collections import deque
from typing import List


"""
First calculate the visited set if grid orange is already rotten
then put it into visited set as initial step to enter
then using DIRECTIONS we can only go left, right, up and down to check or make fresh 
oranges as rotten and also maintain fresh count
"""


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: None 
    
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited, queue = set(), deque()
        minutes, fresh_oranges = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in DIRECTIONS:
                    row, col = r + dr, c + dc
                    if (row < 0 or row >= ROWS or 
                        col < 0 or col >= COLS or
                        (row, col) in visited or
                        grid[row][col] != 1):
                        continue

                    visited.add((row, col))
                    queue.append((row, col))
                    fresh_oranges -= 1

            minutes += 1

        return minutes if fresh_oranges == 0 else -1
