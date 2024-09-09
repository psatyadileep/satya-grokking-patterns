class Solution:
    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        response = []
        visited = set()

        def dfs_helper(curr_node):
            if curr_node in visited:  # Early exit if node already visited
                return
            response.append(curr_node)
            visited.add(curr_node)

            for neighbor in adj[curr_node]:
                dfs_helper(neighbor)

        # Assuming DFS starts from the first vertex
        # Adjust the starting index as per the problem statement

        for i in range(len(adj)):
            if i not in visited:
                dfs_helper(i)  # Adjust if nodes start from 1 or any specific node

        return response

V = 5
adj = [[2,3,1] , [0], [0,4], [0], [2]]
print(Solution().dfsOfGraph(V,adj))