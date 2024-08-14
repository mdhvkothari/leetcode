from typing import List
from collections import deque


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        q = deque([(sr, sc)])
        image[sr][sc] = color
        
        while q:
            r, c = q.popleft()
            for dr, dc in DIRECTIONS:
                row, col = r + dr, c + dc
                if 0 <= row < m and 0 <= col < n and image[row][col] == original_color:
                    image[row][col] = color
                    q.append((row, col))
        
        return image