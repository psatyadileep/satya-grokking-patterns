"""
https://leetcode.com/problems/find-eventual-safe-states/description/
802. Find Eventual Safe States
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.



Example 1:
"""
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        path = set()
        safe = set()
        response = []

        def dfs(node):
            if node in safe:
                return True  # Node is already determined to be safe

            if node in path:
                return False  # Cycle detected, so node is not safe

            path.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False  # If any neighbor is unsafe, this node is unsafe

            path.remove(node)
            safe.add(node)  # Mark the node as safe
            return True

        # Check each node in the graph
        for i in range(len(graph)):
            if dfs(i):
                response.append(i)  # Add safe nodes to the response list

        return sorted(response)  # Return sorted list of safe nodes
