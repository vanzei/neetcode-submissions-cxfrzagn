class UnionFind:
    def __init__(self, n):
        # Initialize parent array and rank array
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        # Find the root of the node, with path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        # Find the roots of the nodes
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
                
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        # Union nodes that are connected by an edge
        for edge in edges:
            uf.union(edge[0], edge[1])
        
        # Count the number of unique roots, which correspond to connected components
        unique_roots = len(set(uf.find(i) for i in range(n)))
        return unique_roots