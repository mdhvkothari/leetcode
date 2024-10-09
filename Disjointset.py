class DisjointSet:
    def __init__(self, n):
        # Initialize rank and parent lists
        self.rank = [0] * (n + 1)  # Rank for each node
        self.parent = [i for i in range(n + 1)]  # Parent for each node (initially each node is its own parent)

    def findUPar(self, node):
        # Find the ultimate parent (path compression is used)
        if node == self.parent[node]:
            return node
        # Path compression: make the parent of the node point directly to the ultimate parent
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        # Find ultimate parents of both nodes
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return  # They are already in the same set

        # Union by rank: attach the smaller ranked tree under the larger ranked tree
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v  # Attach tree with root `ulp_u` under root `ulp_v`
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u  # Attach tree with root `ulp_v` under root `ulp_u`
        else:
            # If ranks are the same, attach one under the other and increment the rank of the new root
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1  # Increment rank of new root
    
    def unionBySize(self, u, v):
        # Find ultimate parents of both nodes
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return  # They are already in the same set

        # Union by size: attach the smaller tree under the larger tree
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v  # Attach tree with root `ulp_u` under root `ulp_v`
            self.size[ulp_v] += self.size[ulp_u]  # Increase the size of the root `ulp_v`
        else:
            self.parent[ulp_v] = ulp_u  # Attach tree with root `ulp_v` under root `ulp_u`
            self.size[ulp_u] += self.size[ulp_v]  # Increase the size of the root `ulp_u`


if __name__ == "__main__":
    ds = DisjointSet(7)
    ds.unionByRank(1, 2)
    ds.unionByRank(2, 3)
    ds.unionByRank(4, 5)
    ds.unionByRank(6, 7)
    ds.unionByRank(5, 6)

    # Check if 3 and 7 are in the same set
    if ds.findUPar(3) == ds.findUPar(7):
        print("Same")
    else:
        print("Not Same")

    ds.unionByRank(3, 7)
    if ds.findUPar(3) == ds.findUPar(7):
        print("Same")
    else:
        print("Not Same")
