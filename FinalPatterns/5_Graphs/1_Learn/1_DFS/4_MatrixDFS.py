def dfs(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def move(r, c):
        # Check if the cell is within bounds and is not a blocked cell (1).
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0

    def helper(r, c):
        nonlocal count

        # Check if we have reached the bottom-right corner of the grid.
        if r == rows - 1 and c == cols - 1:
            count += 1
            return

        if not move(r, c):
            return

        # Mark the cell as visited by setting it to 1 (blocked).
        grid[r][c] = 1

        # Possible directions: right, down, up, left.
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for dr, dc in directions:
            new_row = r + dr
            new_col = c + dc
            helper(new_row, new_col)

        # Unmark the cell to allow other paths to use it.
        grid[r][c] = 0

    if grid[0][0] == 0:  # Check if the starting cell is not blocked.
        helper(r, c)

    return count


# Example usage:
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(dfs(grid, 0, 0))  # Output depends on the grid; this case returns the number of paths.
