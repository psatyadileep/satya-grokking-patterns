"""
Give a matrix , sorice and destination .
Find the number of ways a person can reach the detination if he can only move either to the left or right
"""



def maze(n):

    count = 0
    res = []
    def count_helper(r,c,path):
        nonlocal count



        if r ==n-1 and  c==n-1 :
            res.append(path)
            count+=1
            return


        if r<n:
            left = count_helper(r+1,c,path+"D")
        if c<n:
            right = count_helper(r, c+1, path+"R")



    count_helper(0,0,"")
    return res


print(maze(3))
