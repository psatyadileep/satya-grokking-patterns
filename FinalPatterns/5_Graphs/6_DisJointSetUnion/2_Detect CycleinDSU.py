class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))  # Initially, each element is its own parent
        self.rank = [0] * n           # Rank is initially 0 for all elements

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1  # Increment rank if both are same
        else:
            return False  # Indicates that a cycle is detected
        return True

def detect_cycle(n, edges):
    dsu = DisjointSetUnion(n)

    for u, v in edges:
        if not dsu.union(u, v):  # If union returns False, a cycle is detected
            return True

    return False

# Example Usage
n = 5  # Number of vertices
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 1)  # Adding this edge will form a cycle
]

if detect_cycle(n, edges):
    print("Cycle detected in the graph.")
else:
    print("No cycle detected in the graph.")
