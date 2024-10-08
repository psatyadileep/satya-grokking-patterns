"""
Find the path from 0,0 to the end cell o fthe matrix


Algo :
-> you can move left or to the right
-> have an helrper function

"""

class Solution:
    def maze(self, n):
        rows = n
        cols = n

        def isSafe(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            # If we've reached the bottom-right corner, there's exactly 1 valid path (we're done)
            if r == rows - 1 and c == cols - 1:
                return 1

            # Directions: move down (1, 0) or right (0, 1)
            directions = [(1, 0), (0, 1)]
            path_count = 0

            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc

                # If the next cell is within bounds, continue the DFS
                if isSafe(new_row, new_col):
                    path_count += dfs(new_row, new_col)

            return path_count

        # Start the DFS from the top-left corner (0, 0)
        return dfs(0, 0)

# Test the solution
print(Solution().maze(3))  # Expected output: 6 (for a 3x3 grid)
