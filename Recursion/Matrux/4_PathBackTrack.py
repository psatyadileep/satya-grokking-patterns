
def mazeObstacles(maze):

    res =[]

    def path(p, r, c):
        if r == len(maze) - 1 and c == len(maze[0]) - 1:
            res.append(p)
            return

        if not maze[r][c]:
            return

        # cindering this block  in my path
        maze[r][c] = False

        if r < len(maze) - 1:
            path(p + "D", r + 1, c)
        if c < len(maze[0]) - 1:
            path(p + "R", r, c + 1)

        if r>0:
            path(p+"U",r-1,c)

        if c>0:
            path(p+"L",r,c-1)

        # this is where the function will be over
        # so before the function gets removed : rever the changes made by the function
        maze[r][c] = True
    path("", 0, 0)
    return res

matrix=[[True,True,True],
         [True,True,True],
         [True,True,True]]
print(mazeObstacles(matrix))
