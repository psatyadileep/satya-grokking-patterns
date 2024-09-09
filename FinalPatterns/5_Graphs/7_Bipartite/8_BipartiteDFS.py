from collections import defaultdict


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        adjl = defaultdict(list)
        for i in range(len(graph)):
            adjl[i] = graph[i]

        colors = [-1] * len(graph)

        def dfs(node, color):

            colors[node] = color

            for neighbor in adjl[node]:

                if colors[neighbor] == -1:
                    if not dfs(neighbor, 1 - color):
                        return False

                elif colors[neighbor] == color:
                    return False
            return True

        for i in range(len(graph)):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False

        return True






