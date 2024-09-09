def reverseNum(n):
    res = ""

    def helper(n):
        nonlocal res  # Specify that res is from the outer function
        if not n or n < 0:
            return

        remainder = n % 10  # Use modulo (%) instead of integer division (//)

        res = res * 10 + remainder

        helper(n // 10)

    helper(n)
    return res

print(reverseNum(1824))  # Call the function to see the reversed number
