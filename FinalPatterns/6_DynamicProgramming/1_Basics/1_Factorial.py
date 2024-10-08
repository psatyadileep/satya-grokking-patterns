def fact(n):

    if n<=1:
        return n


    left = fact(n-1)
    right = fact(n-2)

    return left + right



def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = memoization(n - 1) + memoization(n - 2)
    return cache[n]


print(memoization(5))