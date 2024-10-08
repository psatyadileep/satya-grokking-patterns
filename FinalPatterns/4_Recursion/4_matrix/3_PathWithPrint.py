class Solution:
    def maze(self, n):
        rows = n
        cols = n

        def isSafe(r, c):
            return 0 <= r < rows and 0 <= c < cols

        # Helper function to print the path in matrix form
        def print_matrix_path(path):
            # Create an empty matrix with '0's
            matrix = [["0" for _ in range(cols)] for _ in range(rows)]

            # Mark the cells in the path as 'P'
            for r, c in path:
                matrix[r][c] = "P"

            # Print the matrix
            for row in matrix:
                print(" ".join(row))
            print()  # Add an empty line between different solutions

        def dfs(r, c, path):
            # Add the current cell to the path
            path.append((r, c))

            # If we've reached the bottom-right corner, print the path as a matrix
            if r == rows - 1 and c == cols - 1:
                print_matrix_path(path)
                path.pop()  # Backtrack
                return

            # Directions: move down (1, 0) or right (0, 1)
            directions = [(1, 0), (0, 1)]

            # Explore each direction
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if isSafe(new_row, new_col):
                    dfs(new_row, new_col, path)

            # Backtrack by removing the current cell from the path
            path.pop()

        # Start the DFS from the top-left corner (0, 0)
        dfs(0, 0, [])


# Test the solution
Solution().maze(3)
