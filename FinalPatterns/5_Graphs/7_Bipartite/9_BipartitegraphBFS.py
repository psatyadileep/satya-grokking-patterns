from typing import List
import collections
from collections import defaultdict


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adjl = defaultdict(list)

        # Create adjacency list from the input graph
        for i in range(len(graph)):
            adjl[i] = graph[i]

        # Colors array to store color of each node (-1: not colored, 0: color 0, 1: color 1)
        colors = [-1] * len(graph)

        # Use a queue for BFS
        q = collections.deque()

        # Check each component of the graph
        for i in range(len(graph)):
            if colors[i] == -1:  # Node i hasn't been colored yet
                q.append((i, 0))  # Start coloring node i with color 0

                while q:
                    node, color = q.popleft()

                    # Color the node with the current color
                    if colors[node] == -1:
                        colors[node] = color
                    elif colors[node] != color:
                        return False

                    # Check the neighbors
                    for neighbor in adjl[node]:
                        if colors[neighbor] == -1:
                            q.append((neighbor, 1 - color))
                        elif colors[neighbor] == color:
                            return False

        return True
