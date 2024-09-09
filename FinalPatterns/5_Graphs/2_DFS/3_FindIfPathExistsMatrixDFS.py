"""
https://leetcode.com/problems/find-if-path-exists-in-graph/description/
LC1971
here is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.



Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:

"""
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # Create an adjacency matrix
        adj_matrix = [[0] * n for _ in range(n)]

        # Populate the adjacency matrix
        for u, v in edges:
            adj_matrix[u][v] = 1
            adj_matrix[v][u] = 1

        # To keep track of visited nodes
        visited = [False] * n

        # DFS Function
        def dfs(node: int) -> bool:
            # If we reach the destination, return True
            if node == destination:
                return True

            # Mark the current node as visited
            visited[node] = True

            # Traverse all the neighbors of the current node
            for neighbor in range(n):
                if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                    if dfs(neighbor):
                        return True

            return False

        # Start DFS from the source node
        return dfs(source)

