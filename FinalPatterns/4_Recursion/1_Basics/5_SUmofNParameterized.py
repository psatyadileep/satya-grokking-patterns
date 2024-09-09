def SumofN(n):

    sum = 0

    def helper(i):
        nonlocal sum

        if i>n:
            return
        sum+=i

        helper(i+1)

    helper(1)

    return sum

print(SumofN(3))