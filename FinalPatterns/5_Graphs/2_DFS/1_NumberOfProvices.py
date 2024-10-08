
"""
https://leetcode.com/problems/number-of-provinces/
547. Number of Provinces
Solved
Medium
Topics
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""

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