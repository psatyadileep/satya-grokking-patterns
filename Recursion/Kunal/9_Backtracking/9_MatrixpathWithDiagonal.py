"""
If  queens can move down adn to the right find the , the number of steps in a n *n matrix to reach the corner
"""


def maze(r, c):

    res = []
    def count_helper(row, col,path):
        if row == r - 1 and col == c - 1:
            res.append(path)
            return

        if row < r - 1:
            down = count_helper(row + 1, col,path+"D")
        if col < c - 1:
            right = count_helper(row, col + 1,path+"R")

        if row<r-1 and col<c-1:
            diagonal = count_helper(row, col + 1,path+"D")

    count_helper(0, 0,"")
    return  res



print(maze(3, 3))
