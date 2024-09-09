"""
Given a string skip a character given in the input
"""



def skipchar(str,ch):


    def helper(index, res):


        if index>=len(str):
            return  res

        if  str[index] == ch:
            return helper(index+1,res)

        return helper(index+1, str[index]+res)

    ans = helper(0,"")
    return ans


print(skipchar("abcdefggaataa","a"))

