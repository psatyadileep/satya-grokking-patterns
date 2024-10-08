class Solution:
    def numProvinces(self, adj, V):

        visited = set()
        self.count = 0

        def dfs(node):

            visited.add(node)

            for neighbour in range(V):

                if adj[node][neighbour] == 1 and neighbour not in visited:
                    dfs(neighbour)

        for node in range(V):
            if node not in visited:
                dfs(node)
                self.count += 1

        return self.count