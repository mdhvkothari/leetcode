import collections

from typing import List


"""
Idea is to create a adjacency matrix from the input matrix apply 
dfs or bfs for the traversal and maintain the count 
"""


class Solution:

    def make_adjacency_matrix(self, matrix:  List[List[int]], v: int) -> List[List[int]]:
        aj_matrix = collections.defaultdict(list)
        for i in range(v):
            for j in range(i+1, v):
                if matrix[i][j] == 1:
                    aj_matrix[i].append(j)
                    aj_matrix[j].append(i)
        return aj_matrix

    def dfs(self, aj_matrix: List[List[int]], node: int, visited_arr: List[bool]) -> None:
        for i in aj_matrix[node]:
            if not visited_arr[i]:
                visited_arr[i] = True
                self.dfs(aj_matrix, i, visited_arr)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        v, count = len(isConnected), 0
        aj_matrix = self.make_adjacency_matrix(isConnected, v)
        visited_arr = [False] * v
        for i in range(v):
            if not visited_arr[i]:
                count += 1
                visited_arr[i] = True 
                self.dfs(aj_matrix, i, visited_arr)
        return count
