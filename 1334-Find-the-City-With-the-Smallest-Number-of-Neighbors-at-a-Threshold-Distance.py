from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]

        # Set the distance from a city to itself to 0
        for i in range(n):
            dist[i][i] = 0

        # Populate initial distances from the edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Apply the Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], (dist[i][k]+dist[k][j]))
		
        no_of_city, result_city = n, -1

        for city in range(n):
            counter = 0
            for adj_city in range(n):
                if dist[city][adj_city] <= distanceThreshold:
                    counter += 1
            if no_of_city >= counter:
                no_of_city = counter
                result_city = city
        
        return result_city
