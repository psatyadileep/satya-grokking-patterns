from collections import defaultdict


class Solution:
    def numProvinces(self, adj):
        # Initialize adjacency list using defaultdict
        adj_list = defaultdict(list)

        # Create the adjacency list from the adjacency matrix
        nodes = len(adj)
        for i in range(nodes):
            for j in range(nodes):
                if adj[i][j] == 1 and i != j:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        # Set to keep track of visited nodes
        visited = set()
        provinces = 0

        # Depth First Search (DFS) function
        def dfs(node):
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        # Iterate through all nodes
        for i in range(nodes):
            if i not in visited:
                dfs(i)  # Start a DFS from this node
                provinces += 1  # Increment province count

        return provinces