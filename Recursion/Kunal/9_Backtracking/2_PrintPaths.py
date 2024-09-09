"""
Give a matrix , sorice and destination .
Find the number of ways a person can reach the detination if he can only move either to the left or right
"""



def maze(r, c):

    res =[]

    def count_helper(p,r,c):


        if r ==1  and c==1:
            res.append(p)
            return

        if r>1:
            left = count_helper(p+"D",r-1,c)
        if c>1:
            right = count_helper(p+"R",r , c-1)

    count_helper("",r,c)
    return res


print(maze(3,3))
