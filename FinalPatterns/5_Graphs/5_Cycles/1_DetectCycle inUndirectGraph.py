from collections import defaultdict, deque

class Solution:
    def isCycle(self, V, adj):
        # Create an adjacency list from the given edges
        adjlist = defaultdict(list)
        for u in range(V):

            adjlist[u] = adj[u]

        visited = set()
        q = deque()

        # Loop through each vertex to ensure all components are checked
        for i in range(V):
            if i not in visited:
                q.append((i, -1))  # Start BFS from this vertex

                while q:
                    vertex, src = q.popleft()
                    visited.add(vertex)

                    # Explore neighbors
                    for neighbor in adjlist[vertex]:
                        if neighbor not in visited:
                            q.append((neighbor, vertex))  # Enqueue neighbor with current vertex as source
                        elif neighbor != src:
                            # If the neighbor is visited and is not the parent, a cycle is detected
                            return True

        # If no cycles were detected
        return False