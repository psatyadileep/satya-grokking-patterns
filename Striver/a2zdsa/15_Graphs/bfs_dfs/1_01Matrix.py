import collections
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        response = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        q = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    q.append(((i, j), 0))
                    response[i][j] = 0

        if not q:
            return response

        if not mat:
            return response
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            for i in range(len(q)):
                source, distance = q.popleft()
                r, c = source
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row < 0 or col < 0 or row == rows or col == cols or
                            (row, col) in visited):
                        continue
                    response[row][col] = min(response[row][col], distance + 1)
                    visited.add((row, col))
                    q.append(((row, col), distance + 1))
        return response
