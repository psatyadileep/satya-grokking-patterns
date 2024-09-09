# Function to return a list containing
# the BFS traversal of the graph
def bfsOfGraph(self, V, adj):
    # Visited array
    vis = [0] * V

    # To store the result
    ans = []

    # Traverse all the nodes
    for i in range(V):
        # If the node is unvisited
        if vis[i]  == 0:
            # Mark the node as visited
            vis[i] = 1

            # Call BFS from that node
            self.bfs(i, adj, vis, ans)

    return ans