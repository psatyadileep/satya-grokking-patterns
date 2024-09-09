"""
Imagine you're coordinating a voting station, and there are multiple lines of people waiting. However, not everyone is in the proper place in line (some have cut in front others, naturally).

You're given a grid/matrix representing people as integer values. The lower the number, the higher the priority in line (eg: 1 should be first in line).

The grid has diagonal (voting) **lines **of cells starting from some cell in either the top row or leftmost column - leading to the bottom right/grid's end.

Given an m x n grid grid of integers, sort each grid diagonal in ascending order and return the resulting grid. Values will all end up on the same diagonal they started on. Notice that the top right and bottom left corner values won't move.

You may safely assume your grid is rectangular/valid.'
"""


def sort_diagonal(matrix):
    from collections import defaultdict

    # Get matrix dimensions
    rows, cols = len(matrix), len(matrix[0])

    # Dictionary to store diagonals
    diagonals = defaultdict(list)

    # Populate the diagonals dictionary
    for r in range(rows):
        for c in range(cols):
            diagonals[r - c].append(matrix[r][c])

    # Sort each diagonal
    for key in diagonals:
        diagonals[key].sort()

    # Write the sorted diagonals back to the matrix
    for r in range(rows):
        for c in range(cols):
            print(f'Popping from diagonal {r - c}: {diagonals[r - c][0]}')
            matrix[r][c] = diagonals[r - c].pop(0)

    return matrix


# Example usage:
grid = [
    [3, 3, 1, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2]
]

sorted_grid = sort_diagonal(grid)
for row in sorted_grid:
    print(row)
