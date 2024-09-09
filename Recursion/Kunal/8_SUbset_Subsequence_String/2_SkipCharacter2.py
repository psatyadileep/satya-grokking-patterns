"""
Given a  string , remove all the a from it
"""

def SkipChar(arr):


    def skip_chars(ind):

        nonlocal  arr
        if ind >= len(arr):
            return ''
        if arr[ind] != 'a' and arr[ind] != 'A':
            return arr[ind] + skip_chars(ind + 1)
        return skip_chars(ind + 1)
    return skip_chars(0)

result = SkipChar(list("baaccad"))  # Pass a list instead of a string
print(result)

