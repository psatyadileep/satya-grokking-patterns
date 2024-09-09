def NumberPrint(n):

    if n<1:
        return

    print(n)

    return NumberPrint(n-1)


def NumberPrint2(n):

    if n<1:
        return


    NumberPrint2(n-1)
    print(n)



# NumberPrint(6)


NumberPrint2(6)


