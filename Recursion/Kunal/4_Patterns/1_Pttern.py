""""
Print the follwoing aptrteen

*
* *
* * *
* * *  *
"""

def PrintPattern1():


    def helper(n):


        for row in range(n):
            #for every row run teh col,
            for col in range(row+1):
                print("*",end="")
            #after every roow pirn a new line
            print()
 

    helper(5)

PrintPattern1()
