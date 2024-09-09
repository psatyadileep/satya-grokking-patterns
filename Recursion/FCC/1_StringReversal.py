def reverstring(str):


    if not str:
        return ""

    return reverstring(str[1::]) + str[0]


print(reverstring("dileep"))

