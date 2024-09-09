"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.


"""
import collections
from typing import List

mport
collections
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        rows = len(isConnected)
        cols = len(isConnected[0])

        graph = {city: [] for city in range(rows)}
        visited = set()

        for i in range(rows):
            for j in range(cols):

                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)

        provinces = 0

        def bfs(start):
            q = collections.deque([start])
            visited.add(start)
            while q:
                for _ in range(len(q)):
                    city = q.popleft()

                    neighbors = graph.get(city)

                    for neighbor in neighbors:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)

        for city in graph.keys():
            if city not in visited:
                bfs(city)
                provinces += 1

        return provinces

# # Test the function with the provided example
# isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
# print(Solution().findCircleNum(isConnected))  # Output should be 1
