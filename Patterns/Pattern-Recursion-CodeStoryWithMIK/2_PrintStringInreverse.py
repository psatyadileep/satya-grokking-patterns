def rev(str):

    def helper(index):

        if index>=len(str):
            return

        helper(index+1)
        print(str[index],end="")

    helper(0)

rev("dileep")
