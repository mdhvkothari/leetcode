from typing import List

class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj, indegree, q, topo = [[] for _ in range(numCourses)], [0] * numCourses, [], []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1
    
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.pop(0)
            topo.append(node)
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        
        return [] if len(topo) != numCourses else topo
