from collections import defaultdict, deque


class Solution:
    def topoSortBFS(self, edges, n):
        # Initialize the adjacency list and in-degree array
        adj_list = defaultdict(list)
        in_degree = [0] * n

        # Build the adjacency list and in-degree array
        for src, dst in edges:
            adj_list[src].append(dst)
            in_degree[dst] += 1

        # Queue to hold nodes with in-degree of 0
        queue = deque()

        # Enqueue nodes with in-degree 0 (i.e., no dependencies)
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        # List to store the topological order
        topo_order = []

        # BFS traversal
        while queue:
            node = queue.popleft()
            topo_order.append(node)

            # Decrease in-degree of all its neighbors
            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if there was a cycle (i.e., not all nodes are included)
        if len(topo_order) != n:
            return []  # Cycle detected or graph is not a DAG

        return topo_order
