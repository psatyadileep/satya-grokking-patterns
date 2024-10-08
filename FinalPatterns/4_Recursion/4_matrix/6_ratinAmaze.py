"""
Consider a rat placed at (0, 0) in a square matrix mat of order n* n. It has to reach the destination at (n - 1, n - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell. In case of no path, return an empty list. The driver will output "-1" automatically.

Examples:

Input: mat[][] = [[1, 0, 0, 0],
                [1, 1, 0, 1],
                [1, 1, 0, 0],
                [0, 1, 1, 1]]
Output: DDRDRR DRDDRR
Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.
Input: mat[][] = [[1, 0],
                [1, 0]]
Output: -1
Explanation: No path exists and destination cell is blocked."""

"""


"""

from typing import List

from typing import List


class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        res = []
        rows = len(m)
        cols = len(m[0]) if rows > 0 else 0

        # Check if the maze is empty or the starting point is blocked
        if rows == 0 or cols == 0 or m[0][0] == 0:
            return res

        def isMove(r, c):
            return 0 <= r < rows and 0 <= c < cols and m[r][c] == 1

        def dfs(r, c, curr):
            # If we can't move to this cell, return
            if not isMove(r, c):
                return

            # If we reach the bottom-right corner, append the path to result
            if r == rows - 1 and c == cols - 1:
                res.append("".join(curr))
                return

            # Mark this cell as visited by temporarily setting it to 0
            m[r][c] = 0

            # Directions: down ('D'), right ('R'), up ('U'), left ('L')
            directions = [(1, 0, "D"), (0, 1, "R"), (-1, 0, "U"), (0, -1, "L")]

            # Explore all directions
            for dr, dc, di in directions:
                new_row, new_col = r + dr, c + dc
                dfs(new_row, new_col, curr + di)

            # Unmark this cell (backtracking)
            m[r][c] = 1

        # Start DFS from the top-left corner
        dfs(0, 0, "")

        return res


# Example usage:
solution = Solution()
maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
        [0, 1, 1, 1]]
print(solution.findPath(maze))  # Output will be paths such as ['DDRR', 'DRDR']