from collections import defaultdict

class Solution:
    def topoSort(self, edges, num_nodes):
        # Initialize adjacency list using defaultdict
        adj_list = defaultdict(list)

        # Create the adjacency list from the list of edges
        for src, dst in edges:
            adj_list[src].append(dst)

        # Set to keep track of visited nodes
        visited = set()
        result = []  # This will store the topological sort order

        # Depth First Search (DFS) function for topological sorting
        def dfs(node):
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    dfs(neighbour)
            result.append(node)  # Append the node after exploring all its neighbors

        # Iterate through all nodes
        for i in range(num_nodes):
            if i not in visited:
                dfs(i)  # Start a DFS from this node

        return result[::-1]  # Reverse the result to get the correct topological order

# Example usage
edges = [(0, 1), (1, 2), (2, 3)]
num_nodes = 4
sol = Solution()
print(sol.topoSort(edges, num_nodes))  # Output: [0, 1, 2, 3]
