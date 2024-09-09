def revStr(str):
    res = ""
    def helper(ind):
        nonlocal res
        if ind>=len(str):
            return

        helper(ind+1)
        res+=str[ind]

    helper(0)


    return res

print(revStr("dileep"))




def revStr2(str):
    res = ""
    def helper(ind):
        nonlocal res
        if ind<0:
            return
        res += str[ind]

        helper(ind-1)

    helper(len(str)-1)


    return res

print(revStr2("satya"))