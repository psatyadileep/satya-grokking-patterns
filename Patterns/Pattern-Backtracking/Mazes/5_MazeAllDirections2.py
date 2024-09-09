def mazeObstacles(maze):
    res = []

    def path(p, r, c, pathm, step):
        if r == len(maze) - 1 and c == len(maze[0]) - 1:
            pathm[r][c] = step
            res.append(p)
            print(pathm)
            return

        if not maze[r][c]:
            return

        # Considering this block in my path
        maze[r][c] = False
        pathm[r][c] = step

        directions = [(1, 0, "D"), (0, 1, "R"), (-1, 0, "U"), (0, -1, "L")]
        for dr, dc, move in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
                path(p + move, nr, nc, pathm , step+1)

        # This is where the function will be over
        # So before the function gets removed, revert the changes made by the function
        maze[r][c] = True
        pathm[r][c] = 0

    pathm = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    path("", 0, 0,pathm, 1)
    return res

matrix = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]

print(mazeObstacles(matrix))
