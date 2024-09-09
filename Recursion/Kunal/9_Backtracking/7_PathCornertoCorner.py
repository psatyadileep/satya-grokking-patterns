"""
If  queens can move down adn to the right find the , the number of steps in a n *n matrix to reach the corner
"""



def maze(r, c):
    def count_helper(row, col):
        if row == r - 1 or col == c - 1:
            return 1

        
        if row < r - 1:
            down = count_helper(row + 1, col)
        if col < c - 1:
            right = count_helper(row, col + 1)

        return down + right

    return count_helper(0, 0)

print(maze(3, 3))
