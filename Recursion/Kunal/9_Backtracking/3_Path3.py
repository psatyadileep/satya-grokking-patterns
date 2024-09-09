"""
Give a matrix , sorice and destination .
Find the number of ways a person can reach the
detination if he can only move either to the left or right or diagnolaly

"""


def maze(r, c):



    def count_helper(r,c):

        if r ==1 or c==1:
            return 1

        left = count_helper(r-1,c)
        right = count_helper(r , c-1)
        diagonal = count_helper(r-1 , c-1)

        return left + right + diagonal


    return count_helper(r,c)


print(maze(2,2))
