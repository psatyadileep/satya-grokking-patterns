from collections import defaultdict
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        graph = defaultdict(list)

        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j]==1:
                    graph[i].append(j)
                    graph[j].append(j)


        def dfs(curr):

            visited.add(curr)

            neighbors = graph.get(curr)

            if not neighbors or len(neighbors)==0:
                return


            for node in neighbors:

                if node in visited:
                    continue
                dfs(node)

        provinces = 0
        for val in graph.keys():
            if val not in visited:
                dfs(val)
                provinces+=1


        return provinces