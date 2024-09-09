from collections import defaultdict


class Solution:
    def isCyclic(self, N, adj):
        visited = set()  # To track visited nodes

        def dfs(node, path):

            # Mark the node as visited and add it to the current path
            visited.add(node)
            path.add(node)

            # Explore all neighbors of the current node
            for neighbor in adj[node]:

                if neighbor in path:
                    return True

                else:
                    if dfs(neighbor, path):  # If a cycle is detected in the DFS
                        return True

            # Remove the node from the current path before backtracking
            path.remove(node)
            return False

        # Iterate through all nodes in the graph
        for i in range(N):
            if i not in visited:  # If the node has not been visited yet
                if dfs(i, set()):  # Start DFS from this node
                    return True  # Cycle detected

        return False  # No cycles detected
