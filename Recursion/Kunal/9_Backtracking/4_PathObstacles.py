
def mazeObstacles(maze):

    res =[]

    def count_helper(p,maze,r,c):

        if r ==len(maze)-1 and c==len(maze[0])-1:
            return 1


        if not maze[r][c]:
            return

        if r>1:
            left = count_helper(p+"D",maze,r-1,c)
        if c>1:
            right = count_helper(p+"R",maze,r , c-1)

    def path(p, r, c):
        if r == len(maze) - 1 and c == len(maze[0]) - 1:
            res.append(p)
            return

        if not maze[r][c]:
            return

        if r < len(maze) - 1:
            path(p + "D", r + 1, c)
        if c < len(maze[0]) - 1:
            path(p + "R", r, c + 1)

    path("", 0, 0)
    return res


matrix=[[True,True,True],
         [True,False,True],
         [True,True,True]]
print(mazeObstacles(matrix))
