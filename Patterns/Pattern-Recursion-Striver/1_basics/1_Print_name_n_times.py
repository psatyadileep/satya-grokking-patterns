"""
Print Name n time using recursio
"""



def print_name():
    n = int(input("Enter how many time you eant the name"))


    def helper(i):

        if i>n:
            return


        print("Dileep")

        return helper(i+1)

    helper(1)


print_name()
