"""
490. The Maze
Medium
Topics
Companies
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).
"""
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:


        rows = len(maze)
        cols = len(maze[0])

        start_row = start[0]
        start_col = start[1]
        def path(r, c):
            if r == destination[0] and c == destination[1]:
                return True

            if r>=rows or c>=cols:
                return False

            if not maze[r][c]!=0:
                return





            # Up
            if r>=0:
                up = path(r+1,c)
            # Down
            if r<=rows-1:
                down  = path(r-1,c)

            # left
            if c>=0:
                left = path(r,c-1)

            # right
            if c<=cols-1:
                right = path(r,c+1)


        ans = path(start_row,start_col)
        return ans

print(Solution().hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]))