""""
https://leetcode.com/problems/find-if-path-exists-in-graph/description/
1971. Find if Path Exists in Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2


Explore:
1. The graph is bidirectional :
2.


Approach :
1. Store  input in graph : Adjacency List

"""
import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()

        #store in graph
        graph = collections.defaultdict(list)

        for a , b in edges:

            graph[a].append(b)
            graph[b].append(a)


        q =  collections.deque()
        q.append(source,-1)
        visited.add(source)


        while q:

            curr = q.popleft()

            if curr == destination:
                return True

            neighbors = graph.get(curr)


            for neighbor in neighbors:
                if neighbor in visited:
                    continue

                q.append(neighbor)
                visited.add(neighbor)


        return False


# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2

print(Solution().validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))