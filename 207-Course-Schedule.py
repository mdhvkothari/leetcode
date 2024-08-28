from typing import List


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj, in_degree, q, topo_sort = [[] for _ in range(numCourses)], [0] * numCourses, [], []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            in_degree[course] += 1
    
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        while q:
            node = q.pop(0)
            topo_sort.append(node)
            for i in adj[node]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append(i)
        
        return len(topo_sort) == numCourses
        