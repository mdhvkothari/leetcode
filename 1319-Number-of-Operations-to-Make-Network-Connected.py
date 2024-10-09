from typing import List


class Solution:
    def find_ultimate_parent(self, node: int, parent: List[int]) -> int:
        if parent[node] == node:
            return node
        ultimate_parent = self.find_ultimate_parent(parent[node], parent)
        parent[node] = ultimate_parent  # Path compression
        return ultimate_parent
    
    def union_by_size(self, a: int, b: int, parent: List[int], size: List[int]) -> None:
        ulp_a = self.find_ultimate_parent(a, parent)
        ulp_b = self.find_ultimate_parent(b, parent)
        if ulp_a == ulp_b:
            return  # Already in the same component
        # Union by size
        if size[ulp_a] > size[ulp_b]:
            parent[ulp_b] = ulp_a
            size[ulp_a] += size[ulp_b]
        else:
            parent[ulp_a] = ulp_b
            size[ulp_b] += size[ulp_a]

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # If there are less connections than required to connect all nodes, return -1
        if len(connections) < n - 1:
            return -1
        
        count_extra_edges = 0
        parent = [i for i in range(n)]
        size = [1] * n

        # Process all connections
        for u, v in connections:
            if self.find_ultimate_parent(u, parent) == self.find_ultimate_parent(v, parent):
                count_extra_edges += 1  # This is an extra edge
            else:
                self.union_by_size(u, v, parent, size)

        # Count the number of components
        count_components = 0
        for i in range(n):
            if self.find_ultimate_parent(i, parent) == i:  # Find the ultimate parent
                count_components += 1

        # If we have enough extra edges to connect all components, return the number of edges needed
        return count_components - 1 if count_extra_edges >= count_components - 1 else -1
